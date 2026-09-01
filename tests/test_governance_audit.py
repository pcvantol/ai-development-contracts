import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "tools/governance_audit.py"
SPEC = importlib.util.spec_from_file_location("governance_audit", MODULE)
AUDIT = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(AUDIT)

BASE = {"repository":"sample","governance_class":"LIGHTWEIGHT_COMPONENT_MANAGED","license_state":"LICENSE_DEFINED","expected_profile":"sample","release_classes":[]}

class GovernanceAuditTests(unittest.TestCase):
    def fixture(self):
        temp = tempfile.TemporaryDirectory(); root = Path(temp.name); repo = root / "sample"
        (repo / ".github/workflows").mkdir(parents=True); (repo / "docs/ai-development").mkdir(parents=True)
        for file in ("README.md", "LICENSE", "SECURITY.md", "BOOTSTRAP.md"): (repo / file).write_text("x")
        for file in ("GENERATED_PROJECTION.md", "SAMPLE_DEVELOPMENT_EXTENSION.md", "AI_DEVELOPMENT_ADOPTION_RECEIPT.md"): (repo / "docs/ai-development" / file).write_text("x")
        projection = repo / "docs/ai-development/GENERATED_PROJECTION.md"
        (repo / "docs/ai-development/projection-manifest.json").write_text(json.dumps({"extension_identity": "SAMPLE_DEVELOPMENT_EXTENSION", "projection_file_digest": __import__("hashlib").sha256(projection.read_bytes()).hexdigest()}))
        (repo / ".github/workflows/ci.yml").write_text("uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1\n")
        return temp, root
    def statuses(self, root, record=BASE): return {f["check_id"]: f["status"] for f in AUDIT.audit_offline(record, root)}
    def test_lightweight_fixture_passes(self):
        temp, root = self.fixture()
        with temp: self.assertEqual(self.statuses(root)["ai_development.projection"], "PASS")
    def test_mutable_action_is_drift(self):
        temp, root = self.fixture()
        with temp:
            (root / "sample/.github/workflows/ci.yml").write_text("uses: actions/checkout@v5\n")
            self.assertEqual(self.statuses(root)["actions.pinning"], "DRIFT")
    def test_missing_projection_is_detected(self):
        temp, root = self.fixture()
        with temp:
            (root / "sample/docs/ai-development/GENERATED_PROJECTION.md").unlink()
            self.assertEqual(self.statuses(root)["ai_development.projection"], "MISSING")
    def test_modified_generated_projection_is_drift(self):
        temp, root = self.fixture()
        with temp:
            (root / "sample/docs/ai-development/GENERATED_PROJECTION.md").write_text("modified")
            self.assertEqual(self.statuses(root)["ai_development.projection_digest"], "DRIFT")
    def test_missing_security_is_detected(self):
        temp, root = self.fixture()
        with temp:
            (root / "sample/SECURITY.md").unlink()
            self.assertEqual(self.statuses(root)["security.policy"], "MISSING")
    def test_parent_governed_projection_is_intentional(self):
        temp = tempfile.TemporaryDirectory(); root = Path(temp.name); repo = root / "dist"; repo.mkdir(); (repo / "README.md").write_text("x"); (repo / "SECURITY.md").write_text("x")
        record = {"repository":"dist","governance_class":"PARENT_GOVERNED_SUPPORT","license_state":"INTENTIONALLY_NO_LICENSE","release_classes":[]}
        with temp: self.assertEqual({f["check_id"]:f["status"] for f in AUDIT.audit_offline(record, root)}["ai_development.projection"], "INTENTIONAL_DIFFERENCE")
    def test_deferred_exception_is_not_drift(self):
        record = {"repository":"ep","governance_class":"DEFERRED_MIGRATION","exception":{"reason":"review gate"}}
        self.assertEqual(AUDIT.audit_offline(record, Path("."))[0]["status"], "DEFERRED")
    def test_expired_deferred_exception_is_drift(self):
        record = {"repository":"ep","governance_class":"DEFERRED_MIGRATION","exception":{"reason":"review gate","expires_on":"2000-01-01"}}
        self.assertEqual(AUDIT.audit_offline(record, Path("."))[0]["status"], "DRIFT")
    def test_invalid_deferred_exception_is_unresolved(self):
        record = {"repository":"ep","governance_class":"DEFERRED_MIGRATION","exception":{"reason":"review gate","expires_on":"not-a-date"}}
        self.assertEqual(AUDIT.audit_offline(record, Path("."))[0]["status"], "UNRESOLVED")
    def test_distribution_requires_source_authority(self):
        temp = tempfile.TemporaryDirectory(); root = Path(temp.name); repo = root / "dist"; repo.mkdir(); (repo / "README.md").write_text("x"); (repo / "SECURITY.md").write_text("x")
        record = {"repository":"dist","governance_class":"PARENT_GOVERNED_SUPPORT","license_state":"INTENTIONALLY_NO_LICENSE","release_classes":[]}
        with temp: self.assertEqual({f["check_id"]:f["status"] for f in AUDIT.audit_offline(record, root)}["distribution.source_authority"], "DRIFT")
    def test_missing_required_check_producer_is_detected(self):
        temp, root = self.fixture()
        with temp:
            record = dict(BASE, required_check_producers=[".github/workflows/required.yml"])
            self.assertEqual({f["check_id"]:f["status"] for f in AUDIT.audit_offline(record, root)}["required_check.producer"], "DRIFT")
    def test_missing_firmware_source_provenance_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); repo = root / "djconnect-esp32"; (repo / ".github/workflows").mkdir(parents=True)
            for file in ("README.md", "LICENSE", "SECURITY.md"): (repo / file).write_text("x")
            (repo / ".github/workflows/release-firmware.yml").write_text("uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1\n")
            record = {"repository":"djconnect-esp32","governance_class":"LIGHTWEIGHT_COMPONENT_MANAGED","license_state":"LICENSE_DEFINED","expected_profile":"djconnect-esp32","release_classes":[],"artifact_provenance_required":True}
            self.assertEqual({f["check_id"]:f["status"] for f in AUDIT.audit_offline(record, root)}["release.source_provenance"], "DRIFT")
    def test_artifact_manifest_requires_source_and_digest(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = Path(temp) / "artifact.json"
            manifest.write_text(json.dumps({"source_repository":"pcvantol/example","source_sha":"a" * 40}))
            self.assertEqual(AUDIT.artifact_manifest_finding("sample", manifest)["status"], "DRIFT")
    def test_registry_rejects_duplicate_names(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "registry.json"; path.write_text(json.dumps({"schema_version":1,"repositories":[{"repository":"x"},{"repository":"x"}]}))
            with self.assertRaises(ValueError): AUDIT.load_registry(path)
