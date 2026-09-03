# Existing Repository Integration Plan

## Purpose

This plan connects earlier work to the central portfolio without deleting, renaming, copying, changing visibility, or rewriting repository history. Assessment is deliberately split into confirmed facts and provisional signals.

## Evidence available

The five repository names and owner were supplied by the portfolio owner. During the 2026-09-03 review, GitHub CLI authentication was invalid and the environment could not resolve `github.com`; public search returned no repository content. Code, branches, languages, licences, READMEs, deployments, and test results therefore remain unverified.

## Provisional portfolio value

| Repository | Provisional signal from name only | Candidate role | Priority after inspection |
|---|---|---|---|
| `aston-fitness-project` | A domain-focused application | Strong candidate case study showing product scope and application delivery | High |
| `BasicPHP1` | Early PHP/backend learning | Supporting evidence of language breadth and progression | Medium |
| `assignment2` | Coursework or assessed implementation | Include only if the README establishes original contribution, problem, and outcome | Conditional |
| `my-first-website` | Foundational front-end work | Learning-journey evidence; choose the stronger website as the primary example | Conditional |
| `my-first-website1` | A second or duplicated website iteration | Use for before/after progression only if differences are meaningful | Conditional |

These rankings are hypotheses, not content-based findings. `aston-fitness-project` is the most promising integration candidate because its name communicates a concrete user domain; its actual quality must still be validated.

## Read-only review checklist

For each repository, inspect:

1. Default branch, visibility, activity, topics, licence, and repository description.
2. README clarity: problem, user, features, screenshots, setup, architecture, and limitations.
3. Source ownership and attribution, especially for coursework, templates, or team projects.
4. Secret exposure, generated artifacts, dependency health, and ignored local files.
5. Reproducible install, build, test, lint, and deployment commands.
6. Responsive behavior and accessibility for websites; input handling and database safety for PHP.
7. Commit history and evidence that distinguishes personal contribution from supplied starter code.

## Integration sequence

### 1. Validate and classify

Clone each public repository into a temporary review directory once GitHub access works. Run non-mutating checks first. Classify it as featured, supporting, learning-history, or excluded-from-promotion. Exclusion from promotion does not mean deletion.

### 2. Strengthen independently

Use small reviewable commits in the repository itself. Add or improve README, licence clarity, ignore rules, safe configuration, tests, and CI where appropriate. Preserve names, visibility, and history.

### 3. Connect the narrative

- Feature at most one of the two “first website” repositories; describe the other only when it proves iteration.
- Present `BasicPHP1` as progression into server-side work if its code supports that claim.
- Present `aston-fitness-project` as a domain case study if it has a coherent runnable flow.
- Include `assignment2` only with explicit coursework context and contribution boundaries.
- Link validated projects from the central README with concise outcomes and technology labels.

### 4. Presentation gate

A repository should be promoted as featured only when setup succeeds, principal behavior is demonstrated, ownership is clear, no secrets are found, links work, and limitations are stated. Record commands and results in `PORTFOLIO_AUDIT.md`.

## Safe GitHub metadata recommendations

After validation, add accurate one-sentence descriptions and a small set of relevant topics, then pin the strongest repositories on the profile. These are future recommendations only; no metadata or visibility changes were made during this review.

