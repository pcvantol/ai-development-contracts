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

1. repository-state bootstrap (`BOOTSTRAP.md`);
2. platform bootstrap;
3. development-machine desired-state verification;
4. repository-local `AGENTS.md`;
5. Platform Strategy;
6. Meta Engineering guidance;
7. canonical references;
8. repository status and prompt index;
9. current Epic or Phase context;
10. implementation prompt.

For Verification Program work, continue from this general bootstrap to:

- `BOOTSTRAP_CODEX_VERIFICATION.md`
- `PROMPT_INDEX.md`

## Required Startup Flow

A new Codex session must:

1. Read `BOOTSTRAP.md` and verify its repository-state reading order.
2. Read this document.
3. Run the non-mutating development-machine desired-state verification from
   the canonical `pcvantol/djconnect` checkout:

   ```sh
   ./scripts/runner/bootstrap_djconnect_macos_host.sh --verify
   ```

   Capture its Markdown delta and exit code. Do not run recovery, force,
   skip, retry or any mutating bootstrap action during clean-session startup.
   If the canonical checkout or script is unavailable, record the machine as
   `UNVERIFIED`; do not infer readiness from conversation history.
   The check is valid only when it reports canonical developer-onboarding
   package version `4.1.0`. Bootstrap and recovery fail closed before invoking
   onboarding when that exact version is not present.
4. Read the local repository `AGENTS.md`.
5. Read `PLATFORM_STRATEGY.md`.
6. Read `docs/meta/README.md`.
7. Read `CANONICAL_REFERENCES.md`.
8. Identify the current repository role.
9. Identify what the repository owns and does not own.
10. Read `REPOSITORY_STATUS.md`.
11. Read `PROMPT_INDEX.md` when the work is phase-driven.
12. Read the canonical DJConnect Foundation in `pcvantol/djconnect` only as
   needed for the current task, following `CANONICAL_REFERENCES.md`.
13. Identify the current Epic or Phase if applicable.
14. Read relevant local docs.
15. Return a readiness summary.
16. Wait for the next implementation prompt.

## Development Machine Readiness

The clean-session readiness summary must include the result of the desired-state
verification:

- `READY FOR DJCONNECT DEVELOPMENT`: verify exits `0`; all required machine
  desired-state rows match.
- `NOT READY FOR DJCONNECT DEVELOPMENT`: verify exits non-zero because required
  drift exists. List every required `DRIFT` item from the Markdown delta and
  recommend the recovery command. After explicit user authorization, Codex may
  run exactly one prompt-free desired-state repair pass with
  `./scripts/runner/bootstrap_djconnect_macos_host.sh --repair`; it must report
  the post-repair verification delta and every remaining manual requirement.
  Do not run full recovery or unattended repair without explicit user
  authorization.
- `UNVERIFIED`: the verification command could not be run. State why and do
  not claim that the host is ready.

Host minimum qualification and full desired-state readiness are distinct. A
machine can satisfy Apple-Silicon, macOS, RAM and disk requirements while still
being `NOT READY` because tooling, runners or maintenance tasks drift from the
declared machine state.

## Qualified Development Machine Gate for Repository Mutation

Codex may accept and perform a contentful tracked-repository mutation only
from a qualified development machine. Before the developer gives such a prompt,
they must run the local `--verify` command above on the machine that will do the
work and provide Codex its resulting readiness summary.

The submitted evidence must identify the verification command and manifest,
its exit code, the resulting readiness verdict, and every required `DRIFT` item
when the exit code is non-zero. A machine is qualified only when the evidence
states `READY FOR DJCONNECT DEVELOPMENT` and the command exited `0`.

Codex must evaluate this gate in the current session. It must not infer a
qualified machine from conversation history, a result from another machine,
copied partial output, or a previous session. If the evidence is absent,
`NOT READY`, or `UNVERIFIED`, Codex must not make contentful repository
changes. It may perform read-only inspection and explain the exact local
verification command and evidence still required.

This gate applies to changes such as product code, tests, workflows, CI/CD,
deployment or release configuration, architecture documents, and operational
documentation. It is deliberately not a way to bypass the normal repository
bootstrap, engineering protocol, review, or authorization requirements.

The only exceptions are the following narrowly scoped changes:

- governance or backlog documentation: `docs/governance/**`,
  `BOOTSTRAP_CODEX_SESSION.md`, `PLATFORM_GOVERNANCE.md`, and
  `PLATFORM_BACKLOG.md`;
- the developer-onboarding package and its compatibility/test entry points:
  `onboarding/**`, `tools/dev_onboarding_macos.sh`,
  `tools/dev_onboarding_windows.ps1`, and `tests/test_onboarding_package.py`.

An exception bypasses only this qualified-machine gate. Codex must state that
the request is an exception and must still follow every applicable engineering
and security rule. A mixed change is not excepted: all non-excepted files remain
blocked until qualified-machine evidence is supplied.

## Repository Mutation Rule for Machine Recovery

The machine-recovery bootstrap may clone, fetch, fast-forward and validate
repositories, but it must not silently alter tracked product, workflow,
documentation or configuration source files as a side effect of host recovery.

If a verify or recovery result establishes that a tracked repository mutation
is required to reach the declared machine state, Codex must stop that recovery
subtask and treat the change as one dedicated engineering increment in the
owning repository. It must follow the applicable repository bootstrap,
engineering/phase protocol and completion protocol, then create exactly one
reviewable Pull Request for that increment. The readiness response must state
the owning repository, the objective mutation and the PR link once created.

Do not bundle unrelated remediation, generated files, local credentials or
changes from multiple repository owners into that PR. Do not auto-commit or
auto-open a PR merely because a local working tree is dirty; first establish
that the tracked mutation is necessary and belongs to the recovery objective.

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

Current platform lifecycle state:

```text
Platform Architecture
  -> Platform Qualification
  -> Platform Baseline
  -> Business-first Engineering
```

The platform is currently in Platform Qualification. Architecture is frozen
with decision `ARCHITECTURE_FROZEN`; Platform Baseline v1.0 is not yet
certified; Business-first Engineering has not yet started.

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
- Development machine readiness: `READY FOR DJCONNECT DEVELOPMENT` / `NOT READY FOR DJCONNECT DEVELOPMENT` / `UNVERIFIED`
- Machine verification evidence: manifest path, exit code and required drift (if any)
- Repository mutation gate: `SATISFIED` / `NOT SATISFIED` / `EXEMPT` (with the
  exact exception path scope, if applicable)
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
For any later contentful repository-mutation prompt, it must enforce the
Qualified Development Machine Gate before changing files, except for its
explicitly listed narrow exceptions.
