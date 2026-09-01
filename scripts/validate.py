#!/usr/bin/env python3
"""Hermetic qualification for the canonical contract repository."""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "materialize.py"
PROFILES = json.loads((ROOT / "profiles" / "profiles.json").read_text())["profiles"]
EXPECTED = {
    "AI_BOOTSTRAP_CONTRACT", "HANDOFF_CONTRACT", "PROMPT_INITIALIZATION_CONTRACT",
    "BRANCH_WORKTREE_CONTRACT", "VALIDATION_EVIDENCE_CONTRACT", "TDE_INTEGRATION_CONTRACT",
    "REPOSITORY_GOVERNANCE_CONTRACT", "PROJECTION_CONTRACT",
}

def run(*args, ok=True):
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if (result.returncode == 0) != ok:
        raise SystemExit(result.stdout + result.stderr or f"unexpected result: {args}")

contracts = json.loads((ROOT / "contracts" / "contracts.json").read_text())["contracts"]
if set(contracts) != EXPECTED or len(contracts) != 8:
    raise SystemExit("contract identity registry is not the canonical eight")

with tempfile.TemporaryDirectory(prefix="contracts-qualification-") as temporary:
    temp = Path(temporary)
    for profile in PROFILES:
        first, second = temp / f"{profile}-first", temp / f"{profile}-second"
        run(sys.executable, str(TOOL), "materialize", "--repository", profile, "--output", str(first), "--source-commit", "qualification-sha")
        run(sys.executable, str(TOOL), "materialize", "--repository", profile, "--output", str(second), "--source-commit", "qualification-sha")
        for filename in ("GENERATED_PROJECTION.md", "projection-manifest.json"):
            a = (first / "docs" / "ai-development" / filename).read_bytes()
            b = (second / "docs" / "ai-development" / filename).read_bytes()
            if a != b:
                raise SystemExit(f"nondeterministic {profile} {filename}")
        run(sys.executable, str(TOOL), "check", "--repository", profile, "--output", str(first), "--source-commit", "qualification-sha")

        projection = first / "docs" / "ai-development" / "GENERATED_PROJECTION.md"
        projection.write_text(projection.read_text() + "manual change\n")
        run(sys.executable, str(TOOL), "check", "--repository", profile, "--output", str(first), ok=False)
        run(sys.executable, str(TOOL), "check", "--repository", profile, "--output", str(second), "--source-commit", "wrong-sha", ok=False)
        wrong_profile = next(item for item in PROFILES if item != profile)
        run(sys.executable, str(TOOL), "check", "--repository", wrong_profile, "--output", str(second), ok=False)

# The committed self projection is the real offline bootstrap artifact.
run(sys.executable, str(TOOL), "check", "--repository", "ai-development-contracts")
for required in ("README.md", "contracts/contracts.json", "profiles/profiles.json", "docs/ai-development/AI_DEVELOPMENT_CONTRACTS_EXTENSION.md", "provenance/PROMOTION_RECEIPT.md"):
    if not (ROOT / required).is_file():
        raise SystemExit(f"offline bootstrap entrypoint missing: {required}")
print("central contract qualification: PASS")
