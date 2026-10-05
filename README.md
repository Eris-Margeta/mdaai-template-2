# MDAAI 2 template

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/logo-white.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/brand/logo-black.svg">
  <img alt="MDAAI coiled guardian emblem" src="assets/brand/logo-black.svg" width="112" height="112">
</picture>

## How to use this template

1. **Choose one template, not both.** This separate, independently versioned repository is a concrete governance layer **over the MDAAI protocol**, intended to apply that protocol to your project. It is not the protocol monorepo or a coding harness. Do not overlay MDAAI 1.0 and MDAAI 2.0 on the same project.
2. **Read the protocol alongside the template.** The public monorepo is [Eris-Margeta/mdaai](https://github.com/Eris-Margeta/mdaai). If cloned as `mdaai/`, its `README.md` is the entry point, `website/content.json` holds the published protocol guidance, and `docs/publication/` explains publication/provenance; `website/` and `tests/` are documentation-site tooling, not files to install in your application. Use the [protocol website](https://www.mdaai.internet.technology/) and [how files work together](https://www.mdaai.internet.technology/how-files-work-together/) as references. Keep the monorepo checkout separate from your project; **do not copy the whole monorepo**.
3. **Copy the governance payload below into your project root after review.** For a new project, add the listed files to its own repository. For an existing project, review a diff and merge applicable instructions and scaffolds; never overwrite its `AGENTS.md`, governance, task history, `README.md`, version or license. Retain the template revision you adopted in your project documentation.

| Action | Files at this template root | Purpose |
| --- | --- | --- |
| Copy (core); merge existing authority | `AGENTS.md`; `PROJECT-INTERNAL/GOVERNANCE/AUTHORITY.md`, `ENGINEERING.md`, `EVIDENCE.md`, `REASONING.md`, `RECORDS.md` (all five in that directory) | Entry contract plus authority, engineering, evidence, coordination and record rules. No runtime scripts are needed for this portable core. |
| Copy and initialize; preserve existing history | `PROJECT-INTERNAL/MANAGEMENT/PROJECT-ELABORATION.md`, `PROJECT-INTERNAL/MANAGEMENT/TASKS.json` | Your project's scope/sequence and single task-state registry. Both are required, not sample execution history. |
| Retain notices with copied material | `LICENSE`, `NOTICE`, `licenses/legacy-MIT.txt` | Preserve these terms/notices for template-derived files; keep an existing project's root license and store template terms separately if needed. |
| Skip as project payload | `README.md`, `CONTRIBUTING.md`, `.gitignore`, `.python-version`, `VERSION`, `TEMPLATE-IDENTITY.json`, `export-manifest.json`, `assets/brand/`, `scripts/`, `tests/`, `.github/workflows/template.yml` | Template packaging, branding and package validation—not application governance dependencies. Keep your own project README, license, tooling, CI and version. |

4. **Initialize before activation.** Define your scope and delivery sequence in `PROJECT-INTERNAL/MANAGEMENT/PROJECT-ELABORATION.md`. Set your stable task prefix in `PROJECT-INTERNAL/MANAGEMENT/TASKS.json` and start a fresh registry for a new project; for an existing project, reconcile its active tasks without erasing history or creating a second state source. Add project-specific build/test commands and evidence locations to your own guidance. Review [known source-link gaps](tests/known-source-link-gaps.json); private laboratory tooling and completed history are not part of this export.
5. **Use it with your agent or manually.** Point agent entry instructions to the nearest `AGENTS.md`; applicable parent and scoped instructions are cumulative. Read that contract, the assigned task and its relevant governance references. Elaboration owns scope/order; `TASKS.json` alone owns state, evidence and next action. Implement bounded authorized work, run project-relevant checks and record real acceptance evidence before completion. Routine edits need no separate WO; durable records are conditional. Preserve terminal results and link later corrections.
6. **Adopt future changes explicitly.** Review this repository's changes and merge only approved updates; publication or listing does not update downstream authority. Browse alternatives in the [template catalog](https://github.com/Eris-Margeta/mdaai-templates) or [template directory](https://www.mdaai.internet.technology/templates/).


Canonical public template by Eris Margeta Kurdali. Apache-2.0; inherited MIT notices are retained in `licenses/legacy-MIT.txt`. Owner-authorized licensing revision, not a literal original source license.

Read `AGENTS.md` before adoption. Review-before-adoption: uninitialized scaffolds and known source cross-reference gaps are deliberately retained. Copy only selected payloads and reconcile existing project authority. No installer or automatic rollout is provided. Inherited scripts are not run by our checks.

Portable v2 core; laboratory-specific operations and private execution history excluded. Canonical scaffold transitions to this exported v2 authority profile at instantiation.

Development and CI pin: Python **3.13.14**, read from `.python-version`. Catalog validators retain Python 3.11+ compatibility; protocol historical language examples are provenance, not active packaging pins. No global Python replacement is required.

Validate: `python scripts/validate_template.py`; `python -m unittest discover -s tests -v`.

Propose changes here first. Catalog registration is a separately reviewed PR to https://github.com/Eris-Margeta/mdaai-templates with immutable commit and hashes. Website: https://www.mdaai.internet.technology/templates/ . Original per-file provenance and adaptations: `export-manifest.json`.

## Independent portable release identity

Named template **MDAAI 2.0**, portable release **2.0.1** (RELEASE). `TEMPLATE-IDENTITY.json` owns this independently chosen identity; it is not inherited automatically from original source VERSION 2.0.0 or the standalone protocol. The earlier portable export had no VERSION file and used an upstream-derived catalog label. This metadata-only correction does not export private runtime/history or change governance semantics. The public package commit identifies this release; catalog admission and downstream adoption remain separate.
