# Capability Finalization

**Status:** Canonical operational contract

Finalization is the mandatory governance-only increment after a production
implementation has merged. It begins only after objective GitHub and current
main evidence classifies that implementation as `MERGED_UNRECONCILED`.
Production work must not begin from this temporary state.

Finalization must:

1. verify the merged implementation and retain objective validation evidence;
2. update `ENGINEERING_STATUS.md`, `REPOSITORY_STATUS.md`,
   `MANAGEMENT_SUMMARY.md` and `PROMPT_INDEX.md`;
3. archive the immutable Prompt History record for the merged implementation
   when it is not already recorded, using its README contract;
4. reconcile applicable roadmap and governance status, and record newly
   discovered deferred work with a recommended next prompt;
5. run applicable governance and repository-bootstrap validation; and
6. create, validate and merge exactly one Finalization pull request.

The Finalization pull request establishes its own `REVIEWABLE_FROZEN` freeze
point. Its merge restores Repository State `MERGED_RECONCILED`. Then execute
the mandatory Workspace Cleanup procedure in `ENGINEERING_METHOD.md`: check
out and synchronize canonical `main`, verify the completed implementation PR,
safely remove only its fully merged local implementation branch, prune obsolete
remote-tracking references and issue the deterministic cleanup report. Only
`MERGED_RECONCILED` plus `WORKSPACE_READY` permit the next capability to
start. Do not introduce production scope during Finalization.

The cleanup report must explicitly state the **stale local branch result**:
either `none` or every detected stale local branch with its retained/removed
disposition. Reporting is an audit only; it does not authorize deletion of an
unrelated branch.

After Workspace Cleanup, Codex must provide the Product & Platform Architect
(ChatGPT) with a concise **two-PR management feedback summary** in the
user-facing final response. It covers the two most recently merged pull
requests, newest first, using current repository and GitHub evidence only. For
each PR it states the product/governance outcome, material decisions and
boundaries, validation or qualification state, and remaining risk, deferred
work or next decision. It ends with the combined feedback that should guide the
next architecture or product-planning assessment.

This feedback is a reporting and decision-support artifact, not a substitute
for canonical records. It must not invent product scope, architecture,
ownership, priorities or implementation commitments; it must not expose
secrets, private user data or raw diagnostic material.

For a squash merge, apply the canonical Squash-Merge Cleanup Exception rather
than treating non-ancestry alone as a blocker.

For a stale Finalization branch, use the Finalization Branch Delta Exception
only when every branch-only commit passes its canonical reverse-apply check.

A reviewable pull request cannot truthfully record its own future merge. The
following prompt verifies the Finalization merge and confirms the restored
`MERGED_RECONCILED` state without rewriting immutable Prompt History.

The final management summary records the decision, branch, commit SHA, pull
request, validation, updated governance documents, repository-hygiene result,
stale local branch result and recommended next prompt.
