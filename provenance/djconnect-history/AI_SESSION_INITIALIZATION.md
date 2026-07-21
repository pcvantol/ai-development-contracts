# AI Session Initialization

**Status:** Canonical operational contract

Every engineering prompt follows this exact `PRE-FLIGHT` sequence:

```text
Repository Synchronization
  -> Current Main Verification
  -> Development Machine Qualification
  -> Previous Pull Request Verification
  -> Post-Merge State Classification
  -> Rolling State Reconciliation
  -> Canonical Repository Read
  -> Implementation Reality Check
  -> GO / NO-GO Decision
```

Repository Synchronization means `git switch main` followed by
`git pull --ff-only`. Do not continue if either command fails.

Current Main Verification confirms the checked-out branch, `HEAD`, upstream
tracking branch, fast-forward status, working-tree cleanliness and repository
cleanliness. A failure stops the prompt.

## Development Machine Qualification

Before accepting or performing a contentful tracked-repository mutation, obtain
the current-session local desired-state verification summary from the machine
that will do the work. Continue with mutations only when it records
`READY FOR DJCONNECT DEVELOPMENT` and a zero exit code. Do not infer this from
conversation history, another host, a prior session or partial copied output.

When the gate is not satisfied, limit the prompt to read-only inspection and
report the required verification evidence. The exact verification command,
evidence format and the only narrow exceptions are defined in
`BOOTSTRAP_CODEX_SESSION.md`; those exceptions bypass this gate only, never any
other initialization or engineering requirement.

Previous Pull Request Verification uses objective GitHub and Git evidence for
the predecessor merge state and commit, current-main containment and archived
Prompt History. Classify the state under `ENGINEERING_METHOD.md`. For
`MERGED_UNRECONCILED`, only the dedicated Finalization increment may reconcile
`ENGINEERING_STATUS.md`, `REPOSITORY_STATUS.md`, `MANAGEMENT_SUMMARY.md` and
`PROMPT_INDEX.md`; never rewrite Prompt History. Unknown merge candidates,
missing history, divergence and stale main remain terminal.

Only after successful synchronization, verification and reconciliation where
required, read and verify:

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

Confirm the requested capability remains pending, has no equivalent merged
implementation and is not superseded by an architecture amendment. Verify the
required validation baseline and current roadmap, architecture and maturity
records. End Pre-Flight with `GO` only from `MERGED_RECONCILED`; otherwise issue
`NO-GO` and do not make production changes.

If any observed repository fact differs from the expected state, stop. Correct
the repository state or planning records before work proceeds. Historical
prompts and conversation history are context only and never override current
main.

Use `BOOTSTRAP.md` as the reading-order entry point and
`REPOSITORY_HYGIENE.md` for branch cleanup rules.
