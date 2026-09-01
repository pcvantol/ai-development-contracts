# AI Development Contracts

The sole authoring authority for generic AI-development contracts. Product
repositories consume committed offline projections and keep their own local
extensions. Product architecture, TDE semantics, Engineering Platform runtime,
Forge planning, Workspace behavior, and Knowledge Base lifecycle are excluded.

## Estate governance baseline

`governance/estate.json` records the expected pcvantol repository classes and
the bounded Engineering Platform migration exception. Run the read-only local
auditor from a directory containing repository checkouts:

```sh
python3 tools/governance_audit.py check --registry governance/estate.json --root <checkout-parent> --json-output governance-audit.json
```

`--online` adds GitHub metadata checks through the authenticated `gh` CLI. The
auditor reports drift only; it never changes repositories or GitHub settings.
