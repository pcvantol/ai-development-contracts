# AI Session Initialization

**Status:** Canonical operational contract

Every engineering prompt follows this exact initialization sequence:

```text
Repository Synchronization
  -> Current Main Verification
  -> Canonical Repository Read
  -> Implementation Reality Check
  -> Engineering Planning
```

Repository Synchronization means `git switch main` followed by
`git pull --ff-only`. Do not continue if either command fails.

Current Main Verification confirms the checked-out branch, `HEAD`, upstream
tracking branch, fast-forward status, working-tree cleanliness and repository
cleanliness. A failure stops the prompt.

Only after successful synchronization and current-main verification, read and
verify:

1. current branch, current `main`, repository status and implementation reality;
2. `ENGINEERING_STATUS.md`, `REPOSITORY_STATUS.md` and `MANAGEMENT_SUMMARY.md`;
3. the active roadmap and active backlog selected through `ROADMAP_INDEX.md`;
4. `PROMPT_INDEX.md` and relevant Prompt History only when historical context
   is actually needed; and
5. whether the requested result already exists, has been validated or has been
   qualified.

Then perform the implementation-reality check: inspect requested functionality,
validation, qualification, documentation and existing implementation. If the
outcome already exists, do not reimplement it; close only remaining evidenced
gaps.

If any observed repository fact differs from the expected state, stop. Correct
the repository state or planning records before work proceeds. Historical
prompts and conversation history are context only and never override current
main.

Use `BOOTSTRAP.md` as the reading-order entry point and
`REPOSITORY_HYGIENE.md` for branch cleanup rules.
