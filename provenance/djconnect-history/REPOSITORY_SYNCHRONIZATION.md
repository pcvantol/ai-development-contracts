# Repository Synchronization

**Status:** Canonical operational contract

Repository synchronization is the first step of every engineering prompt.
From the intended repository, run:

```sh
git switch main
git pull --ff-only
```

Do not continue if either command fails.

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

For `MERGED_UNRECONCILED`, reconcile `ENGINEERING_STATUS.md`,
`REPOSITORY_STATUS.md`, `MANAGEMENT_SUMMARY.md` and `PROMPT_INDEX.md` before
substantive engineering. Prompt History remains immutable. Then follow
`BOOTSTRAP.md`, perform the implementation-reality check in
`PROMPT_INITIALIZATION.md`, and only then plan work. Current synchronized main
always overrides conversation history, historical prompts, assumptions and prior
planning.
