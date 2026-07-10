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
3. current Epic or Phase context;
4. implementation prompt.

For Verification Program work, continue from this general bootstrap to:

- `BOOTSTRAP_CODEX_VERIFICATION.md`
- `PROMPT_INDEX.md`

## Required Startup Flow

A new Codex session must:

1. Read this document.
2. Read the local repository `AGENTS.md`.
3. Read the canonical DJConnect Foundation in `pcvantol/djconnect`.
4. Identify the current repository role.
5. Identify what the repository owns and does not own.
6. Identify the current Epic or Phase if applicable.
7. Read relevant local docs.
8. Return a readiness summary.
9. Wait for the next implementation prompt.

## Canonical Foundation Files

Read these files from the canonical Home Assistant repository,
`pcvantol/djconnect`, when platform context is required:

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

Implementation work should reference `docs/implementation/` in the canonical
Home Assistant repository.

For Epic 3, read `docs/implementation/epic3/00-context.md` when present and the
active phase prompt supplied by the user. Do not jump phases. Do not implement
until the user gives an explicit phase or implementation prompt.

For future epics, read the current epic context, any phase template or phase
prompt, and relevant completion/review notes before making changes.

For Verification Program phases, read `BOOTSTRAP_CODEX_VERIFICATION.md` and
follow the active phase in `PROMPT_INDEX.md`. The verification bootstrap is the
durable replacement for large chat-only verification prompts.

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
