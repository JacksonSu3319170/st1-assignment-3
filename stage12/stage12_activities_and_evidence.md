# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial:
Group 5
Wednesday 4:30 - 6:30

Members and UG/PG applicability: 
Jackson S (u3319170) UG
Jonathan V (u3319279) UG
Ayaz M (u3320654) UG

## A Release scope and starting SHA

Release label/version and requirements baseline: v1.0-UG (Overview Rev 2: Common UG scope, FR-01–FR-09, QRY-01–04, FP-01–03, in-memory storage only)
Common starting SHA / branch / applicable members: c5a6dbd1b0e24482bbab9923560bff11b9ac7f0a / main / Jackson, Ayaz, Jonathan
PG starting SHA / branch / applicable members or not applicable:
Working-state review and approved integration: Clean status verified with zero untracked runtime artifacts. Stage 9 pure query functions (select_appointments, appointment_sort_key), practitioner listing, and interactive console menu were reviewed, approved via pull request, and integrated into the primary branch with full test suite passing.
Protected common candidate and PG differences: Single common candidate at SHA c5a6dbd1b0e24482bbab9923560bff11b9ac7f0a. No PG extension differences or secondary branches required.
Feature freeze / owner / verifier: Strict feature freeze executed, no optional or new feature development permitted. Owner: Jackson / Verifier: Jonathan


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: Do not release (or Release with some exceptions), Passing tests show the code works, but that alone does not mean the software is ready to release. Without clear setup instructions in the README, others cannot run the project on a clean computer. An unreviewed dependency could introduce security, licensing, or stability issues, and missing documentation hides known limitations from reviewers. Before signing off, the team needs to test the setup steps on a fresh machine, audit the dependency, and clearly document all known limitations in the release files.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope                   | Evidence                                                                                                                                | Location/link and SHA                                                      | Reviewer     | Sufficient? | Gap/action                                    |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|--------------|-------------|-----------------------------------------------|
| Cancellation history works                            | Tests verify cancelled appointments keep their ID, set status to CANCELLED, remain findable, and block double cancellation.             | tests/test_appointment*.py (SHA: 71bd3e69bc7db6629b6efbc99080896e6ce46f01) | [Teammate 1] | Yes         | None; verified in test suite                  |
| Architecture responsibilities are appropriate         | Entities manage invariants, SmartCareDataStore holds in-memory data, services coordinate tasks, queries stay pure, and console runs UI. | project/ (SHA: [Insert SHA])                                               | [Teammate 2] | Yes         | None; clean separation confirmed              |
| Rescheduling is safe — PG only                        | Not applicable for Undergraduate pathway (Common UG scope only).                                                                        | N/A — UG Scope                                                             | N/A          | Yes         | None; retained template as-is for UG          |
| AI use is responsible — common recheck / PG assurance | Copilot suggestions were human-reviewed, tested, free of secrets/keys, and tested with synthetic data only.                             | Section E/N (SHA: [Insert SHA])                                            | [Teammate 1] | Yes         | None; verified during code audit              |
| System is maintainable                                | Clean PEP 8 styling, type hints, docstrings, focused methods, and zero dead code.                                                       | project/ (SHA: [Insert SHA])                                               | [Teammate 2] | Yes         | None; code review complete                    |
| FR-01–03 register/find and validation                 | Tests and console show registration, input validation, and clean recovery on invalid searches.                                          | tests/test_patient*.py, tests/test_practitioner*.py (SHA: [Insert SHA])    | [Teammate 1] | Yes         | None; passing                                 |
| FR-04–05 booking/conflict rules                       | Tests verify valid bookings, reject practitioner double-booking, allow different practitioners at same time, and ensure atomic failure. | tests/test_booking*.py (SHA: [Insert SHA])                                 | [Teammate 2] | Yes         | None; all conflict rules pass                 |
| FR-06–08 cancellation/history/find                    | Tests and demo verify successful cancellation, history lookup by ID, and error handling on bad cancellations.                           | tests/test_appointment*.py (SHA: [Insert SHA])                             | [Teammate 1] | Yes         | None; verified                                |
| FR-09 and QRY/FP listing/filter/order/purity          | Pure functions (select_appointments, appointment_sort_key) provide ascending order and status filters without altering data.            | project/queries/, tests/test_queries*.py (SHA: [Insert SHA])               | [Teammate 2] | Yes         | None; Stage 9 integrated and tested           |
| UI full console sequence and error recovery           | Interactive menu handles full user workflow, bad dates, and invalid choices without crashing, cleanly returning to menu.                | project/main.py (SHA: [Insert SHA])                                        | [Teammate 1] | Yes         | None; interactive demo verified               |
| Session-only scope / FR-10 retired                    | In-memory storage with synthetic data only; no database or external files; FR-10 retired.                                               | project/ (SHA: [Insert SHA])                                               | [Teammate 2] | Yes         | None; session data loss on exit is documented |
| PG RES and assurance integration                      | Not applicable to UG cohort.                                                                                                            | N/A — UG Scope                                                             | N/A          | Yes         | None                                          |

## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [response] | [response] | [response] | [response] | [response] |
| Complete PG if applicable | [response] | [response] | [response] | [response] | [response] |
| Affected focused checks after correction | [response] | [response] | [response] | [response] | [response] |
| Full integrated recheck | [response] | [response] | [response] | [response] | [response] |
Prior assertions preserved / reviewed test diff: [response]
Remaining failure / limitation: [response]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [response] | [response] | [response] | [response] |
| Register and find Patient and two Practitioners | [response] | [response] | [response] | [response] |
| Valid booking | [response] | [response] | [response] | [response] |
| Same practitioner exact-time conflict rejected | [response] | [response] | [response] | [response] |
| Different practitioner same time allowed | [response] | [response] | [response] | [response] |
| Cancel SCHEDULED and retain/find CANCELLED object | [response] | [response] | [response] | [response] |
| Invalid/repeated cancellation rejected | [response] | [response] | [response] | [response] |
| Default all-status listing | [response] | [response] | [response] | [response] |
| Explicit filtering / empty vs unknown / deterministic order | [response] | [response] | [response] | [response] |
| Invalid date/status/menu/lookup recovery and continued operation | [response] | [response] | [response] | [response] |
| Session-only limitation and normal exit | [response] | [response] | [response] | [response] |
| One meaningful requirement-linked pytest test explained | [response] | [response] | [response] | [response] |
| Architecture and one actual AI decision / known limitation | [response] | [response] | [response] | [response] |
| PG reschedule identity/participants/time and no-op | [response] | [response] | [response] | [response] |
| PG conflict/invalid status/failure non-mutation | [response] | [response] | [response] | [response] |
| PG old slot / current lookup/list ordering / assurance risks | [response] | [response] | [response] | [response] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [response] | [response] | [response] |
| PascalCase and snake_case naming | [response] | [response] | [response] |
| Useful type hints and meaningful docstrings | [response] | [response] | [response] |
| Four-space indentation and imports/layout | [response] | [response] | [response] |
| Focused methods / duplication / dead or commented code | [response] | [response] | [response] |
| Globals / leakage / unnecessary inheritance or frameworks | [response] | [response] | [response] |
| No SQLite/persistence/repository ABCs/speculative features | [response] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands | [response] | [response] | [response] |
| Repository structure and architecture responsibilities | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? A release candidate (RC) is a nearly finished version of the software that has all features built and is considered stable. It is treated as the final product unless testing reveals a major, game-breaking bug.

2. What is feature freeze and why is it used? A feature freeze is the point in development where the team stops adding new features. It is used to lock down the scope so the team can focus entirely on fixing bugs, testing, and writing documentation without creating new issues.

3. What is regression testing in a release context? Regression testing means re-running your full test suite against the latest build. Its purpose is to prove that recent code changes, refactors, or bug fixes haven't accidentally broken existing features.

4. What is a known limitation? A known limitation is an acknowledged boundary or missing capability that the team deliberately chose not to support (such as data only saving in-memory for the current session). It is documented openly so users and evaluators know what the system cannot do.

5. What is technical debt? Technical debt is the future rework you create when you take a shortcut or choose a quick fix today instead of the best long-term solution. It represents compromises you intentionally accept to hit a deadline, knowing you will need to clean them up later.

6. What are release notes? Release notes are a brief document that comes with a software version. They tell users and reviewers what was built, what bugs were fixed, any architectural changes made, and what limitations still exist.

7. What is software maintenance? Software maintenance is the ongoing work that starts right after a release is deployed. It covers fixing newly found bugs, updating libraries, improving performance, and adapting the program as requirements change over time.

8. What is the purpose of the individual demonstration/viva? The purpose of the individual viva is to prove personal understanding and genuine contribution. It confirms that you understand the architecture, can explain why design decisions were made, can walk through tests, and can speak to the code you actually worked on.

9. What should the final responsible-AI check establish before release? The final check confirms that all AI-generated code was human-reviewed and tested, without introducing exposed secrets, unapproved dependencies, or real patient data.

10. What is the main course conclusion about AI and the role of the software engineer? While AI is great at drafting code and speeding up repetitive tasks, software engineers are still essential for critical thinking, architecture, and accountability. AI cannot take responsibility for system design, verify overall correctness, navigate ethical choices, or guarantee the safety of humans and their decisions.


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
