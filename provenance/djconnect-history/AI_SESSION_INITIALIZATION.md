# AI Session Initialization

**Status:** Canonical operational contract

Every engineering prompt starts by assuming the preceding engineering pull
request is merged, current `main` is updated, `ENGINEERING_STATUS.md` is
current, the preceding Prompt History is archived and the repository is clean.
These are assumptions to verify, not facts to trust.

Before planning, verify:

1. current branch, current `main`, repository status and implementation reality;
2. `ENGINEERING_STATUS.md`, `REPOSITORY_STATUS.md` and `MANAGEMENT_SUMMARY.md`;
3. the active roadmap and active backlog selected through `ROADMAP_INDEX.md`;
4. `PROMPT_INDEX.md` and relevant Prompt History only when historical context
   is actually needed; and
5. whether the requested result already exists, has been validated or has been
   qualified.

If any observed repository fact differs from the expected state, stop. Correct
the planning records before work proceeds. Historical prompts and conversation
history are context only and never override current repository state.

Use `BOOTSTRAP.md` as the reading-order entry point and
`REPOSITORY_HYGIENE.md` for branch cleanup rules.
