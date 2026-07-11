# DJConnect Codex Session Bootstrap

This is the official platform-wide onboarding procedure for starting a clean
Codex or AI-agent session in any DJConnect repository.

It replaces the old pattern of reading a large local chat bootstrap first.
Clean sessions should use this procedure, then repository-local instructions,
then the current Epic or Phase context.

## Purpose

DJConnect is a multi-repository platform with one canonical foundation. This
document defines how AI agents start work without mixing temporary handoff
notes, recent release state and durable architecture guidance.

The intended startup order is:

1. platform bootstrap;
2. repository-local `AGENTS.md`;
3. Platform Strategy;
4. Meta Engineering guidance;
5. canonical references;
6. repository status and prompt index;
7. current Epic or Phase context;
8. implementation prompt.

For Verification Program work, continue from this general bootstrap to:

- `BOOTSTRAP_CODEX_VERIFICATION.md`
- `PROMPT_INDEX.md`

## Required Startup Flow

A new Codex session must:

1. Read this document.
2. Read the local repository `AGENTS.md`.
3. Read `PLATFORM_STRATEGY.md`.
4. Read `docs/meta/README.md`.
5. Read `CANONICAL_REFERENCES.md`.
6. Identify the current repository role.
7. Identify what the repository owns and does not own.
8. Read `REPOSITORY_STATUS.md`.
9. Read `PROMPT_INDEX.md` when the work is phase-driven.
10. Read the canonical DJConnect Foundation in `pcvantol/djconnect` only as
   needed for the current task, following `CANONICAL_REFERENCES.md`.
11. Identify the current Epic or Phase if applicable.
12. Read relevant local docs.
13. Return a readiness summary.
14. Wait for the next implementation prompt.

## Meta Engineering

Read `docs/meta/README.md`, then continue with repository-specific guidance.

The Meta Engineering Foundation defines how humans and AI agents collaborate,
where durable engineering knowledge belongs and how AI agents should operate.

## Canonical Foundation Files

Read these files from the canonical Home Assistant repository,
`pcvantol/djconnect`, when platform context is required:

- `PLATFORM_STRATEGY.md`
- `FOUNDATION_INDEX.md`
- `DJCONNECT_CONSTITUTION.md`
- `PRODUCT_VISION.md`
- `DESIGN_FOUNDATION_VERSION.md`
- `DESIGN_PRINCIPLES.md`
- `ARCHITECTURE_PRINCIPLES.md`
- `DOMAIN_MODEL.md`
- `PLATFORM_PRINCIPLES.md`
- `CLIENT_CAPABILITY_MATRIX.md`
- `PRODUCT_LANGUAGE.md`
- `PLATFORM_GOVERNANCE.md`
- `PLATFORM_QUALITY_STANDARD.md`
- `PLATFORM_BACKLOG.md`
- `REPOSITORY_OWNERSHIP.md`
- `PLATFORM_DISCOVERY_REPORT.md`
- `ADR_INDEX.md`

When runtime evolution or long-term platform shape is relevant, also read:

- `docs/research/R0_RUNTIME_INDEPENDENCE.md`

`CANONICAL_REFERENCES.md` is the durable repository-local map for these
references and for the ownership boundary between canonical platform guidance
and repository-local implementation guidance.

## Repository-Local Instructions

`AGENTS.md` remains authoritative for repository-specific implementation
details.

Local `README`, `HANDOFF`, release, architecture, test and platform-specific
docs may also be required depending on the repository and task.

Repository-local instructions extend the DJConnect Platform Foundation. They do
not redefine it. If local instructions appear to conflict with the foundation,
resolve the conflict through the foundation, accepted ADRs and maintainer
direction.

## Current Epic / Phase

Repository phase state starts in `REPOSITORY_STATUS.md`. Platform verification
phase navigation starts in `PROMPT_INDEX.md`. Implementation work should
reference `docs/implementation/` in the canonical Home Assistant repository.

For Epic work, read the current epic context or
`docs/implementation/epic-template/00-context.md` when creating one, plus the
active phase prompt supplied by the user. Do not jump phases. Do not implement
until the user gives an explicit phase or implementation prompt.

For future epics, read the current epic context, any phase template or phase
prompt, and relevant completion/review notes before making changes.

For Verification Program phases, read `BOOTSTRAP_CODEX_VERIFICATION.md` and
follow the active phase in `PROMPT_INDEX.md`. The verification bootstrap is the
durable replacement for large chat-only verification prompts.

## Repository Status

`REPOSITORY_STATUS.md` records the repository role, current phase, blocking
dependencies, current prompt, completion report, last qualification and current
SHA for this repository only. It must not duplicate the platform roadmap.

## Deprecated Chat Bootstrap

`CHAT_BOOTSTRAP.md` is deprecated and must not be used as a clean-session
entrypoint. If historical references still mention it, they should treat it as
a pointer back to this bootstrap.

## Readiness Summary Template

After bootstrap, Codex should return a readiness summary in this shape:

- Repository:
- Repo role:
- Canonical foundation read:
- Local docs read:
- Current Epic/Phase:
- What this repo owns:
- What this repo must not own:
- Relevant risks:
- Recommended next prompt:

## Strict Rule

A clean Codex session must not start implementation immediately after
bootstrap.

It must first return the readiness summary and wait for the next user prompt.
