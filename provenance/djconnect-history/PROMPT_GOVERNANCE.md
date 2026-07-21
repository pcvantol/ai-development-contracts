# Prompt Governance

**Status:** Canonical operational contract

## Ownership and format

One prompt owns one engineering objective, one engineering increment and one
reviewable pull request. Prompts must not overlap or compete for implementation
scope.

Every engineering prompt produces exactly one complete, copy-pasteable prompt
inside exactly one code block. Required implementation must be inside that
prompt, not scattered around it.

Prompts must begin with the canonical initialization sequence in
`PROMPT_INITIALIZATION.md`. They must instruct Codex to determine the latest
merged increment, current repository truth and current engineering status from
synchronized current main. They must not assert those facts from conversation
context, examples or historical planning.

## Lifecycle

`PROMPT_INDEX.md` is the lifecycle authority. A canonical prompt progresses:

```text
Draft -> Active -> Completed -> Deprecated -> Archived
```

Only one prompt may be Active. A Completed prompt is never reactivated; new
scope becomes a new Draft after the predecessor has a reviewable pull request.

## Post-merge engineering state

Prompt lifecycle is distinct from engineering lifecycle. The latter is
`REVIEWABLE_FROZEN`, `MERGED_UNRECONCILED` or `MERGED_RECONCILED`, as defined
by `ENGINEERING_METHOD.md`. A merged implementation enters
`MERGED_UNRECONCILED`; only its dedicated Finalization may proceed from that
state. After Finalization merges, its mandatory Workspace Cleanup establishes
the independent `WORKSPACE_READY` state. The next production capability begins
only with `MERGED_RECONCILED` and `WORKSPACE_READY`, without altering Prompt
History.

## Freeze and deferred work

The freeze point is the existence of the reviewable pull request; its state is
`REVIEWABLE_FROZEN`. After it,
implementation is frozen. PR review may add only work necessary to complete
the original objective. Any new objective is recorded, prioritized and
recommended as deferred work for a subsequent increment; it is never silently
included.

The reusable prompt form is `docs/governance/PROMPT_TEMPLATE.md`. Every
implementation prompt uses its mandatory `PRE-FLIGHT`, `IMPLEMENTATION`,
`VALIDATION` and `FINALIZATION` structure.
