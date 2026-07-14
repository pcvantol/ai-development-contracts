# Prompt Governance

**Status:** Canonical operational contract

## Ownership and format

One prompt owns one engineering objective, one engineering increment and one
reviewable pull request. Prompts must not overlap or compete for implementation
scope.

Every engineering prompt produces exactly one complete, copy-pasteable prompt
inside exactly one code block. Required implementation must be inside that
prompt, not scattered around it.

## Lifecycle

`PROMPT_INDEX.md` is the lifecycle authority. A canonical prompt progresses:

```text
Draft -> Active -> Completed -> Deprecated -> Archived
```

Only one prompt may be Active. A Completed prompt is never reactivated; new
scope becomes a new Draft after the predecessor has a reviewable pull request.

## Freeze and deferred work

The freeze point is the existence of the reviewable pull request. After it,
implementation is frozen. PR review may add only work necessary to complete
the original objective. Any new objective is recorded, prioritized and
recommended as deferred work for a subsequent increment; it is never silently
included.

The reusable prompt form is `docs/governance/PROMPT_TEMPLATE.md`.
