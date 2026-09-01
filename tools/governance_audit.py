#!/usr/bin/env python3
"""Read-only governance baseline auditor.

The auditor reads a registry and repository trees.  ``--online`` additionally
queries GitHub through ``gh api``; it never invokes a mutating command.
"""
import argparse
import json
import re
import subprocess
import sys
import hashlib
from pathlib import Path

STATUSES = {"PASS", "INTENTIONAL_DIFFERENCE", "DEFERRED", "OWNER_DECISION_REQUIRED", "DRIFT", "MISSING", "UNRESOLVED", "ERROR"}
BLOCKING = {"DRIFT", "MISSING", "UNRESOLVED", "ERROR"}
SHA = re.compile(r"^[0-9a-f]{40}$")
USES = re.compile(r"^\s*(?:-\s*)?uses:\s*([^\s#]+)", re.M)

def finding(repo, check, expected, actual, status, severity="MEDIUM", hint=""):
    assert status in STATUSES
    return {"check_id": check, "repository": repo, "expected": expected, "actual": actual,
            "status": status, "severity": severity, "evidence": actual, "remediation_hint": hint}

def load_registry(path):
    data = json.loads(Path(path).read_text())
    if data.get("schema_version") != 1 or not isinstance(data.get("repositories"), list):
        raise ValueError("unsupported governance registry")
    names = [item.get("repository") for item in data["repositories"]]
    if len(names) != len(set(names)) or not all(names):
        raise ValueError("repository names must be unique")
    return data

def exists(path): return path.is_file()

def action_pins(repo, root):
    workflows = root / repo / ".github/workflows"
    if not workflows.is_dir(): return []
    mutable = []
    for workflow in sorted(workflows.glob("*.y*ml")):
        for value in USES.findall(workflow.read_text(encoding="utf-8")):
            if value.startswith("./"): continue
            ref = value.rsplit("@", 1)[-1] if "@" in value else ""
            if not re.fullmatch(r"[0-9a-f]{40}", ref): mutable.append(f"{workflow.name}:{value}")
    return mutable

def audit_offline(record, root):
    repo, cls = record["repository"], record["governance_class"]
    path = root / repo
    out = []
    if cls == "DEFERRED_MIGRATION":
        reason = record.get("exception", {}).get("reason")
        return [finding(repo, "exception.deferred_migration", "explicit bounded exception", reason or "missing", "DEFERRED" if reason else "UNRESOLVED", "INFORMATIONAL")]
    if not path.is_dir():
        return [finding(repo, "repository.checkout", "local checkout", "missing", "MISSING", "HIGH", "provide checkout for offline audit")]
    out.append(finding(repo, "discoverability.readme", "README", "present" if exists(path / "README.md") else "missing", "PASS" if exists(path / "README.md") else "MISSING", "HIGH"))
    license_state = record["license_state"]
    license = exists(path / "LICENSE") or exists(path / "LICENSE.md")
    status = "PASS" if license or license_state == "INTENTIONALLY_NO_LICENSE" else "OWNER_DECISION_REQUIRED" if license_state == "OWNER_DECISION_REQUIRED" else "DRIFT"
    out.append(finding(repo, "license.position", license_state, "defined" if license else "no license file", status, "LOW"))
    security_needed = cls != "EXPERIMENTAL_NOT_APPLICABLE"
    if security_needed:
        present = exists(path / "SECURITY.md")
        out.append(finding(repo, "security.policy", "SECURITY.md", "present" if present else "missing", "PASS" if present else "MISSING", "HIGH"))
    projection = path / "docs/ai-development/GENERATED_PROJECTION.md"
    if cls in {"FULL_MANAGED_FIRST_CLASS", "LIGHTWEIGHT_COMPONENT_MANAGED"}:
        manifest = path / "docs/ai-development/projection-manifest.json"
        extension_identity = ""
        if manifest.is_file():
            try:
                extension_identity = json.loads(manifest.read_text(encoding="utf-8")).get("extension_identity", "")
            except json.JSONDecodeError:
                extension_identity = ""
        extension_name = f"{extension_identity}.md"
        extensions = [path / "docs/ai-development" / extension_name, path / "docs/development" / extension_name]
        needed = projection.is_file() and manifest.is_file() and any(item.is_file() for item in extensions)
        out.append(finding(repo, "ai_development.projection", "projection, manifest and extension", "present" if needed else "missing artifact", "PASS" if needed else "MISSING", "HIGH"))
        if manifest.is_file() and projection.is_file():
            try:
                expected_digest = json.loads(manifest.read_text(encoding="utf-8")).get("projection_file_digest")
                actual_digest = hashlib.sha256(projection.read_bytes()).hexdigest()
                valid = expected_digest == actual_digest
                out.append(finding(repo, "ai_development.projection_digest", "manifest digest matches projection", actual_digest, "PASS" if valid else "DRIFT", "HIGH"))
            except json.JSONDecodeError:
                out.append(finding(repo, "ai_development.projection_digest", "valid manifest JSON", "invalid JSON", "UNRESOLVED", "HIGH"))
        if cls == "LIGHTWEIGHT_COMPONENT_MANAGED":
            receipt = path / "docs/ai-development/AI_DEVELOPMENT_ADOPTION_RECEIPT.md"
            bootstrap = path / "BOOTSTRAP.md"
            ok = receipt.is_file() and bootstrap.is_file()
            out.append(finding(repo, "ai_development.lightweight_adoption", "receipt and bootstrap", "present" if ok else "missing", "PASS" if ok else "MISSING", "HIGH"))
    else:
        out.append(finding(repo, "ai_development.projection", "not required", "absent" if not projection.exists() else "present", "INTENTIONAL_DIFFERENCE" if not projection.exists() else "DRIFT", "INFORMATIONAL"))
    if cls == "PARENT_GOVERNED_SUPPORT":
        parent = record.get("parent_authority")
        out.append(finding(repo, "distribution.source_authority", "declared parent/source authority", parent or "missing", "PASS" if parent else "DRIFT", "HIGH"))
    for producer in record.get("required_check_producers", []):
        present = (path / producer).is_file()
        out.append(finding(repo, "required_check.producer", producer, "present" if present else "missing", "PASS" if present else "DRIFT", "CRITICAL"))
    mutable = action_pins(repo, root)
    out.append(finding(repo, "actions.pinning", "immutable SHA pins", "; ".join(mutable) if mutable else "all external actions pinned", "DRIFT" if mutable else "PASS", "HIGH", "replace mutable tag or branch with immutable SHA"))
    if record.get("artifact_provenance_required") and repo == "djconnect-esp32":
        workflow = path / ".github/workflows/release-firmware.yml"
        text = workflow.read_text(encoding="utf-8") if workflow.is_file() else ""
        ok = '"source_repository": "${SOURCE_REPOSITORY}"' in text and '"source_sha": "${SOURCE_SHA}"' in text
        out.append(finding(repo, "release.source_provenance", "source repository and exact SHA in future manifest", "present" if ok else "missing", "PASS" if ok else "DRIFT", "HIGH"))
    return out

def audit_online(record, organization):
    repo = record["repository"]
    if record["governance_class"] == "DEFERRED_MIGRATION": return []
    try:
        data = json.loads(subprocess.check_output(["gh", "api", f"repos/{organization}/{repo}"], text=True))
        branch = data.get("default_branch")
        status = "PASS" if branch == "main" else "DRIFT"
        return [finding(repo, "github.default_branch", "main", branch or "missing", status, "HIGH")]
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        return [finding(repo, "github.metadata", "readable GitHub metadata", str(exc), "ERROR", "HIGH")]

def report(findings, output_json=None):
    blocking = [item for item in findings if item["status"] in BLOCKING]
    result = {"schema_version": 1, "summary": {"findings": len(findings), "blocking": len(blocking)}, "findings": findings}
    if output_json: Path(output_json).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"Governance audit: {len(findings)} findings; {len(blocking)} blocking")
    for item in findings:
        if item["status"] != "PASS": print(f"{item['status']}: {item['repository']} {item['check_id']} — {item['actual']}")
    return 1 if blocking else 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("check",))
    parser.add_argument("--registry", required=True, type=Path)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--repository")
    parser.add_argument("--online", action="store_true")
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()
    try:
        registry = load_registry(args.registry)
        records = [r for r in registry["repositories"] if not args.repository or r["repository"] == args.repository]
        if args.repository and not records: raise ValueError("unknown repository")
        results = [f for record in records for f in audit_offline(record, args.root)]
        if args.online: results += [f for record in records for f in audit_online(record, registry["organization"])]
        return report(results, args.json_output)
    except Exception as exc:
        print(f"auditor error: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__": sys.exit(main())
