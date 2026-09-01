# ADR: estate governance baseline and auditor

## Decision

`pcvantol/ai-development-contracts` owns the generic, machine-readable
repository-governance baseline and its read-only estate auditor. This is a
bounded extension of its existing generic repository-governance contract: it
describes expected repository state, not product behaviour or release runtime.

## Boundaries

The registry and auditor own generic classification, discoverability,
AI-development projection presence, workflow hygiene, and proportional
release-provenance expectations. They do not own DJConnect product architecture,
TDE product/release semantics, Forge Platform composition implementation, or
Engineering Platform migration decisions.

Consumers change the registry through normal governed pull requests. The
auditor is deliberately read-only; a finding is input to a separate repair PR.
