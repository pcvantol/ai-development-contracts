# VALIDATION_EVIDENCE_CONTRACT

Run applicable repository validation before review and record exact results.
Absent checks are reported as absent, never fabricated.

For a governed release lifecycle, durable evidence binds one immutable operation
identity to the owning component, selected version, policy revision, protected
source revision and exact artifact digests. Qualification, publication,
cleanup-pending recovery and release completion are distinct states. A resumed
operation reuses that identity and exact bytes; a conflicting concurrent
operation or an existing identity with different bytes fails closed.

Record qualification, publication receipt and registry readback separately.
Do not represent a normal build as a version change, a successful upload as
release completion, or a local installation as publication. Product
repositories retain their own release policy, artifact registry, installation
authority and runtime semantics.
