# Repository Synchronization

**Status:** Canonical operational contract

Repository synchronization is the first step of every engineering prompt.
From the intended repository, run:

```sh
git switch main
git fetch origin main
git merge --ff-only origin/main
```

For Managed execution, `origin/main` is the sole authoritative source ref.
The explicit fetch and fast-forward merge must not be replaced with `git pull`:
local upstream, `branch.main.merge`, `pull.rebase` and `pull.ff` configuration
must not select or change the synchronization source or strategy.

Do not continue if any command fails.

Immediately verify:

- the checked-out branch is `main`;
- the current `HEAD` is known;
- the tracking branch is correct;
- local `main` has zero ahead/behind divergence from its upstream;
- the working tree is clean; and
- the repository is clean.

Failure of any verification is terminal for the prompt. Resolve repository
state first; do not read history, plan engineering or start implementation.

After success, verify the previous pull request using objective GitHub and Git
evidence: merge state and commit, current-main containment, archived Prompt
History and no unknown merge candidate. Classify it under `ENGINEERING_METHOD.md`.

For `MERGED_UNRECONCILED`, only the dedicated Finalization increment may
reconcile `ENGINEERING_STATUS.md`, `REPOSITORY_STATUS.md`,
`MANAGEMENT_SUMMARY.md` and `PROMPT_INDEX.md`. Prompt History remains
immutable. Production implementation waits for its merged Finalization to
restore `MERGED_RECONCILED` and its mandatory Workspace Cleanup to establish
`WORKSPACE_READY`. Then follow `BOOTSTRAP.md`, perform the
implementation-reality check in `PROMPT_INITIALIZATION.md`, and only then plan
work. Current synchronized main always overrides conversation history,
historical prompts, assumptions and prior planning.
