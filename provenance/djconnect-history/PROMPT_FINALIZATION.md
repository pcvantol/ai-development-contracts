# Prompt Finalization

**Status:** Canonical operational contract

Before creating the one reviewable pull request for an increment:

1. validate the scoped change and retain objective evidence;
2. update `ENGINEERING_STATUS.md`, `REPOSITORY_STATUS.md`,
   `MANAGEMENT_SUMMARY.md` and `PROMPT_INDEX.md`;
3. archive one immutable record in `docs/history/prompts/` using its README
   contract; and
4. record newly discovered out-of-scope work as deferred work with a
   recommended next prompt.

The reviewable pull request is the freeze point. Do not introduce new scope
after that point. The branch must be clean after all scoped changes are
committed; merge remains a separate governance decision.

The final management summary records the decision, branch, commit SHA, pull
request, validation, updated governance documents, repository-hygiene result
and recommended next prompt.
