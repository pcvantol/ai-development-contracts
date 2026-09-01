#!/usr/bin/env python3
"""Offline deterministic projection materializer and drift checker."""
import argparse, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1"

def contract_names():
    document = json.loads((ROOT / "contracts/contracts.json").read_text())
    names = document["contracts"]
    if len(names) != 8 or len(set(names)) != len(names):
        raise SystemExit("contract registry must contain exactly eight unique identities")
    missing = [name for name in names if not (ROOT / "contracts" / f"{name}.md").is_file()]
    if missing:
        raise SystemExit("missing contract source: " + ", ".join(missing))
    return names

def profile_extension(profile):
    profiles = json.loads((ROOT / "profiles/profiles.json").read_text())["profiles"]
    if profile not in profiles:
        raise SystemExit(f"unknown profile: {profile}")
    return profiles[profile]

def source_commit():
    return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()

def render(profile, commit):
    extension = profile_extension(profile)
    files = [f"{name}.md" for name in contract_names()]
    source = {name: (ROOT / "contracts" / name).read_text() for name in files}
    digest = hashlib.sha256(json.dumps(source, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    manifest = {"schema_version":"1","source_repo":"pcvantol/ai-development-contracts","source_commit":commit,"profile":profile,"contracts":files,"extension_identity":extension,"projection_digest":digest,"materializer_version":VERSION}
    body = "# Generated AI-development projection\n\nDo not edit; update the local extension or canonical contracts.\n\n" + "\n".join(f"- {key}: `{value}`" for key, value in manifest.items() if key != "contracts") + "\n\n"
    for name in files: body += source[name] + "\n"
    manifest["projection_file_digest"] = hashlib.sha256(body.encode()).hexdigest()
    return body, manifest

def target(output): return output / "docs" / "ai-development"

def materialize(profile, output, commit):
    body, manifest = render(profile, commit)
    target(output).mkdir(parents=True, exist_ok=True)
    (target(output) / "GENERATED_PROJECTION.md").write_text(body)
    (target(output) / "projection-manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    (target(output) / "validate_projection.py").write_text((ROOT / "tools" / "projection_validator.py").read_text())

def check(profile, output, source_commit=None):
    manifest = json.loads((target(output) / "projection-manifest.json").read_text())
    if source_commit and manifest.get("source_commit") != source_commit:
        raise SystemExit("undeclared source revision")
    body, expected = render(profile, manifest["source_commit"])
    if manifest != expected or (target(output) / "GENERATED_PROJECTION.md").read_text() != body: raise SystemExit("projection drift")
    if (target(output) / "validate_projection.py").read_text() != (ROOT / "tools" / "projection_validator.py").read_text(): raise SystemExit("projection validator drift")

parser = argparse.ArgumentParser(); parser.add_argument("command", choices=("materialize", "check")); parser.add_argument("--repository", required=True); parser.add_argument("--output", type=Path, default=ROOT); parser.add_argument("--source-commit")
args = parser.parse_args()
if args.command == "materialize": materialize(args.repository, args.output, args.source_commit or source_commit())
else: check(args.repository, args.output, args.source_commit)
