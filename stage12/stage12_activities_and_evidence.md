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
PG starting SHA / branch / applicable members or not applicable: N/A
Working-state review and approved integration: Clean status verified with zero untracked runtime artifacts. Stage 9 pure query functions (select_appointments, appointment_sort_key), practitioner listing, and interactive console menu were reviewed, approved via pull request, and integrated into the primary branch with full test suite passing.
Protected common candidate and PG differences: Single common candidate at SHA c5a6dbd1b0e24482bbab9923560bff11b9ac7f0a. No PG extension differences or secondary branches required.
Feature freeze / owner / verifier: Strict feature freeze executed, no optional or new feature development permitted. Owner: Jackson / Verifier: Jonathan


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: Do not release (or Release with some exceptions), Passing tests show the code works, but that alone does not mean the software is ready to release. Without clear setup instructions in the README, others cannot run the project on a clean computer. An unreviewed dependency could introduce security, licensing, or stability issues, and missing documentation hides known limitations from reviewers. Before signing off, the team needs to test the setup steps on a fresh machine, audit the dependency, and clearly document all known limitations in the release files.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope                   | Evidence                                                                                                                                | Location/link and SHA                                                      | Reviewer     | Sufficient? | Gap/action                                    |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|--------------|-------------|-----------------------------------------------|
| Cancellation history works                            | Tests verify cancelled appointments keep their ID, set status to CANCELLED, remain findable, and block double cancellation.             | tests/test_appointment*.py (SHA: 71bd3e69bc7db6629b6efbc99080896e6ce46f01) | [Jonathan] | Yes         | None; verified in test suite                  |
| Architecture responsibilities are appropriate         | Entities manage invariants, SmartCareDataStore holds in-memory data, services coordinate tasks, queries stay pure, and console runs UI. | project/ (SHA: d960ba35b69dc469cf68100c311a19195064e70f)                                               | [Jackson] | Yes         | None; clean separation confirmed              |
| Rescheduling is safe — PG only                        | Not applicable for Undergraduate pathway (Common UG scope only).                                                                        | N/A — UG Scope                                                             | N/A          | Yes         | None; retained template as-is for UG          |
| AI use is responsible — common recheck / PG assurance | Copilot suggestions were human-reviewed, tested, free of secrets/keys, and tested with synthetic data only.                             | Section E/N (SHA: d960ba35b69dc469cf68100c311a19195064e70f)                                            | [Jonathan] | Yes         | None; verified during code audit              |
| System is maintainable                                | Clean PEP 8 styling, type hints, docstrings, focused methods, and zero dead code.                                                       | project/ (SHA: d960ba35b69dc469cf68100c311a19195064e70f)                                               | [Jackson] | Yes         | None; code review complete                    |
| FR-01–03 register/find and validation                 | Tests and console show registration, input validation, and clean recovery on invalid searches.                                          | tests/test_patient*.py, tests/test_practitioner*.py (SHA: d960ba35b69dc469cf68100c311a19195064e70f)    | [Jonathan] | Yes         | None; passing                                 |
| FR-04–05 booking/conflict rules                       | Tests verify valid bookings, reject practitioner double-booking, allow different practitioners at same time, and ensure atomic failure. | tests/test_booking*.py (SHA: d960ba35b69dc469cf68100c311a19195064e70f)                                 | [Jackson] | Yes         | None; all conflict rules pass                 |
| FR-06–08 cancellation/history/find                    | Tests and demo verify successful cancellation, history lookup by ID, and error handling on bad cancellations.                           | tests/test_appointment*.py (SHA: d960ba35b69dc469cf68100c311a19195064e70f)                             | [Jonathan] | Yes         | None; verified                                |
| FR-09 and QRY/FP listing/filter/order/purity          | Pure functions (select_appointments, appointment_sort_key) provide ascending order and status filters without altering data.            | project/queries/, tests/test_queries*.py (SHA: d960ba35b69dc469cf68100c311a19195064e70f)               | [Jonathan] | Yes         | None; Stage 9 integrated and tested           |
| UI full console sequence and error recovery           | Interactive menu handles full user workflow, bad dates, and invalid choices without crashing, cleanly returning to menu.                | project/main.py (SHA: d960ba35b69dc469cf68100c311a19195064e70f)                                        | [Jonathan] | Yes         | None; interactive demo verified               |
| Session-only scope / FR-10 retired                    | In-memory storage with synthetic data only; no database or external files; FR-10 retired.                                               | project/ (SHA: d960ba35b69dc469cf68100c311a19195064e70f)                                               | [Jackson] | Yes         | None; session data loss on exit is documented |
| PG RES and assurance integration                      | Not applicable to UG cohort.                                                                                                            | N/A — UG Scope                                                             | N/A          | Yes         | None                                          |

## C Full regression results
## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | macOS, Python 3.14.7, pytest 8.3.5 | `project/` — `python -m pytest` | `d960ba35b69dc469cf68100c311a19195064e70f` | 69 passed, 0 failed, 0.05s | [GitHub commit](https://github.com/JacksonSu3319170/st1-assignment-3/tree/d960ba35b69dc469cf68100c311a19195064e70f/project/tests) |
| Complete PG if applicable | Not applicable — all group members UG | N/A | N/A | N/A | N/A |
| Affected focused checks after correction | Not separately run for Stage 12 | Not run | N/A | No Stage 12 correction or focused rerun recorded | N/A |
| Full integrated recheck | macOS, Python 3.14.7, pytest 8.3.5 | `project/` — `python -m pytest` | `d960ba35b69dc469cf68100c311a19195064e70f` | 69 passed, 0 failed, 0.05s | [Integrated test suite](https://github.com/JacksonSu3319170/st1-assignment-3/tree/d960ba35b69dc469cf68100c311a19195064e70f/project/tests) |

**Prior assertions preserved / reviewed test diff:** The integrated suite includes the original starter tests, Stage 6 feature tests, Stage 7 domain tests, Stage 8 regression tests, Stage 9 query tests and workflow tests. All 69 tests passed. A separate Stage 12 assertion-diff review has not yet been recorded.

**Remaining failure / limitation:** No failures were observed in the 69-test regression run. The UG release remains limited to in-memory session storage; data is not persisted after the application exits.

## D Console and end to end demonstration

**Environment:** macOS, Python 3.14.7
**Application command:** `python main.py --interactive` from `project/`
**Tested commit:** `d960ba35b69dc469cf68100c311a19195064e70f`
**Test data:** Synthetic patient, practitioner and appointment records.

| Scenario | Demonstration / expected behaviour | Result |
|---|---|---|
| Register patient | Registered `P100` — Alex Smith | PASS |
| Register practitioners | Registered `DR100` — Dr Sarah Lee and `DR200` — Dr James Brown | PASS |
| Valid appointment | Booked `A100` for `P100` with `DR100` at `2026-11-15 10:00` | PASS — confirmed by subsequent conflict and cancellation demonstrations |
| Same-practitioner conflict | Attempted `A101` with `DR100` at the same time as `A100` | PASS — rejected with practitioner scheduling conflict |
| Different-practitioner booking | Booked `A102` with `DR200` at `2026-11-15 10:00` | PASS |
| Cancel appointment | Cancelled `A100` | PASS — status changed to cancelled |
| Retained cancellation history | Searched for `A100` after cancellation | PASS — appointment remained retrievable as cancelled |
| Repeated cancellation | Attempted to cancel `A100` again | PASS — group reports correct rejection |
| Unknown appointment | Attempted cancellation of nonexistent `A999` | PASS — group reports correct error handling |
| Practitioner listing and filtering | Tested appointment listing, status filters and ordering | Group reports tested; attach existing evidence |
| Invalid input recovery | Tested invalid dates, statuses and menu options | Group reports tested; attach existing evidence |
| Session-only behaviour | Application explicitly reports that records are lost on exit | Limitation disclosed; restart demonstration evidence to be linked |
| Automated regression | Executed `python -m pytest` from `project/` | PASS — 69 tests passed |

**Demonstration conclusion:** The observed console demonstrations confirm successful registration, booking, practitioner-specific conflict rejection, cancellation and retained appointment history. The group reports completing the remaining listing, filtering and invalid-input checks. These should be supported by the existing demonstration record or screenshots.

**Known limitation:** SmartCare uses in-memory storage only. Records are not persisted between application sessions.

## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | `project/smartcare/`, `project/tests/test_queries.py` | Domain, service, query and console responsibilities are separated. Query purity is covered by Stage 9 tests. | No further correction recorded. Full regression: 69 passed. |
| PascalCase and snake_case naming | `project/smartcare/`, `project/main.py` | Python naming conventions are used for classes, functions and variables. | No naming correction recorded for Stage 12. |
| Useful type hints and meaningful docstrings | `project/smartcare/`, `project/main.py` | Type hints and docstrings are used to clarify functions and responsibilities. | No further correction recorded. |
| Four-space indentation and imports/layout | `project/smartcare/`, `project/main.py` | Python source follows standard indentation and module organisation. | No formatting correction recorded. |
| Focused methods / duplication / dead or commented code | `project/smartcare/`, Stage 8–9 review records | Functionality is separated across focused components. No new duplication or dead-code finding was recorded for Stage 12. | No further change recorded; integrated tests passed. |
| Globals / leakage / unnecessary inheritance or frameworks | `project/smartcare/`, Stage 9 query tests | The design uses in-memory services and separate query operations. Query tests cover protection against unintended state changes. | No additional framework or inheritance changes required by the UG scope. |
| No SQLite/persistence/repository ABCs/speculative features | `project/smartcare/`, `project/README.md` | SmartCare remains an in-memory teaching application. Database persistence and speculative production features are outside the UG release scope. | No persistence implementation added; session-only limitation documented. |
| Synthetic data / secrets / dependencies / provenance | `project/tests/`, `project/requirements-dev.txt`, Git history | Demonstrations use synthetic patient and practitioner details. Dependencies are listed in the development requirements file. | Exclude secrets, virtual environments and local configuration from the final ZIP; verify during packaging. |
| Significant common Copilot contributions and human verification | Stage 6–9 AI review and testing records, GitHub PRs | AI-assisted suggestions were subject to human decisions, code review and testing. Stage 8 defect correction and Stage 9 query development provide relevant review examples. | Retain accepted changes only where supported by human review and tests. Final regression: 69 passed. |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | N/A | Not applicable — all group members are UG students. | N/A |

### AI claim review

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| Appointment conflict checks should compare the selected practitioner rather than reject every booking at the same time. | FR-05, appointment booking service, `tests/test_stage8_regressions.py` | Checked against the practitioner-specific conflict requirement and regression tests. | **Accept** — different practitioners must be able to accept appointments at the same time. | Stage 8 conflict-check defect corrected; integrated regression passed. |
| Cancelled appointments should remain retrievable instead of being treated as missing. | FR-06–08, appointment lookup service, `tests/test_stage8_regressions.py` | Checked cancellation history behaviour and regression tests. | **Accept** — retained cancellation history is required. | Stage 8 lookup defect corrected; cancelled appointments remain retrievable. |
| Appointment queries should support filtering and deterministic results without modifying source records. | FR-09, QRY/FP, `project/smartcare/`, `tests/test_queries.py` | Checked Stage 9 query tests and integrated regression results. | **Accept**, subject to the documented query requirements and human review. | Query functionality included in the integrated release; tests passed. |

**Access route or approved equivalent / limitations:** GitHub repository: https://github.com/JacksonSu3319170/st1-assignment-3. Relevant Stage 6–9 evidence records, merged pull requests and source tests provide review traceability. The verified integrated test SHA is `d960ba35b69dc469cf68100c311a19195064e70f`. The application remains session-only and is not a production healthcare system.

**Available AI evidence and missing evidence honestly disclosed:** Earlier stage records document AI-related review activities and implementation decisions. The final integrated suite passed 69 tests. Exact Copilot prompts, suggestions, acceptance decisions and reviewer approvals should be referenced from the original stage evidence where available; they cannot be reconstructed solely from passing tests or Git commit history.

## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | Root `README.md`; `project/README.md` | Jonathan V | Updated to describe SmartCare's completed UG common functionality. PG-only extensions are identified as not applicable. |
| Out-of-scope capabilities and known limitations | `project/README.md` | Jonathan V | Documented session-only storage, no database persistence, no rescheduling, and other teaching-scope limitations. |
| Confirmed teaching Python version and dependency installation | Root `README.md`; `project/README.md`; `project/requirements-dev.txt` | Jonathan V | Python 3.13 documented as the teaching baseline. Python 3.14.7 and pytest 8.3.5 verified locally. Dependency pinned to `pytest==8.3.5`; fresh installation not separately tested. |
| Working directory / demo / interactive / test commands | Root `README.md`; `project/README.md`; `project/main.py` | Jonathan V | Documented `python main.py`, `python main.py --interactive`, and `python -m pytest` from `project/`. Commands verified in the original working copy. |
| Repository structure and architecture responsibilities | `project/README.md`; `project/smartcare/` | Jonathan V | Updated documentation describes domain models, in-memory data store, services, queries, console and tests. |
| Responsible AI summary / synthetic-data rule | Root `README.md`; `project/README.md`; Stage 6–9 evidence | Jonathan V | Documented human verification of AI-assisted work and the requirement to use synthetic data only. |
| Release label/version and SHA links | Root `README.md`; `project/README.md`; Stage 12 evidence | Jonathan V | Planned release `v1.0-UG` and verified code SHA `d960ba35b69dc469cf68100c311a19195064e70f` documented. Final submitted SHA remains pending. |

**Root README index and project/README verified:** Both README files were reviewed and updated to reflect the completed UG functionality, current commands, architecture, limitations, testing and planned release. `git diff --check` completed without warnings. README changes remain local until committed.

**Fresh clone or extracted ZIP / candidate identity:** A separate fresh clone was created from `https://github.com/JacksonSu3319170/st1-assignment-3.git` in `smartcare-release-check/`. The cloned repository SHA was confirmed as `d960ba35b69dc469cf68100c311a19195064e70f`, matching the original tested release candidate. Running `python -m pytest` from the cloned `project/` directory resulted in 69 passed, 0 failed in 0.06 seconds. Final submission ZIP verification remains pending.

**Verifier and clean environment / actual version:** Jonathan V performed the fresh-clone verification on macOS using Python 3.14.7 and pytest 8.3.5. The existing activated virtual environment was used, so a newly created clean Python environment was not independently verified.

**Setup/run/test commands and observed results:** From the original `project/` directory, `python main.py` ran the demonstration, `python main.py --interactive` launched the interactive menu, and `python -m pytest` passed all 69 tests in 0.05 seconds. From the separately cloned `project/` directory, `python -m pytest` passed all 69 tests in 0.06 seconds.

**Missing local file or setup gap / remedy and recheck:** No missing application file or dependency was encountered during the fresh-clone test. The remaining checks are a clean-environment dependency installation, committing the updated documentation, and verifying the final source ZIP against the submitted commit.

## G Known limitations debt and release notes

**Delivered features:** SmartCare `v1.0-UG` implements the common undergraduate requirements, including patient registration and lookup, practitioner registration and lookup, appointment booking, practitioner-specific scheduling conflict checks, appointment cancellation, retained cancellation history, appointment lookup, practitioner appointment listing, status filtering, deterministic ordering and an interactive console. The integrated application passed all 69 automated tests.

**Important fixes:** During Stage 8, two defects were corrected. The appointment lookup logic was fixed so cancelled appointments remain retrievable, and the booking conflict check was corrected to compare appointments belonging to the same practitioner. Regression tests were added to protect both behaviours. The fixes were retained in the integrated release candidate.

**Architecture/quality improvements:** SmartCare separates domain entities, in-memory storage, service operations, pure query functionality and console interaction. Stage 9 introduced appointment listing and filtering, deterministic query ordering and an interactive menu. Automated tests cover domain rules, services, queries, regression defects and integrated workflows. The project README files were updated to document the completed functionality, architecture, setup instructions and limitations.

**Known limitations:** SmartCare is an educational, session-only application rather than a production healthcare system. Records are lost when the application exits. It does not implement database persistence, appointment rescheduling, production authentication, role-based access, notifications, billing, insurance processing or clinical AI. Appointment times use local date/time values with minute precision. The console has limited production-level usability, and comprehensive concurrency, timezone, accessibility and operational monitoring capabilities are outside the current scope.

**AI-assisted development note:** GitHub Copilot was the nominated AI assistant during development. AI-assisted suggestions were subject to human review, requirement checking and testing. The group retained responsibility for implementation decisions and verification. Relevant AI contributions and decisions are documented in the earlier stage records; AI-generated suggestions were not treated as automatically correct.

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| In-memory storage without persistence | Records are lost when the application exits. | Low for UG release; high for production use | Introduce persistent storage in a future production-oriented version, subject to revised requirements. | Accepted — session-only storage is an explicit UG scope requirement. |
| Local date/time without timezone management | Appointments cannot reliably support multiple timezones or daylight-saving policies. | Medium for future development | Introduce timezone-aware timestamps and documented timezone conversion rules. | Accepted — comprehensive timezone management is outside the teaching scope. |
| No authentication or role-based access | Users are not protected by production-grade access controls. | High for production use | Implement authentication, authorisation and appropriate privacy controls. | Accepted for the educational release; the application must not be used with real patient data. |
| Limited appointment scheduling rules | Appointment duration, patient conflicts and past-date restrictions are not enforced. | Medium for future development | Define additional scheduling requirements and implement corresponding validation and tests. | Accepted — these rules are not part of the specified common requirements. |
| No appointment rescheduling or completed-status menu action | Users cannot reschedule appointments or mark them completed through the console. | Low for UG release | Add these operations only if future requirements explicitly include them. | Accepted — PG rescheduling is not applicable to the UG group, and completed-status interaction is not required. |
| Limited concurrency and scalability | Simultaneous users and large-scale workloads are not supported or assured. | High for production use | Introduce concurrency controls, performance testing and appropriate deployment architecture. | Accepted — SmartCare is a single-process teaching application. |
| Limited accessibility and operational monitoring | The text-based console lacks comprehensive accessibility assessment, production logging and monitoring. | Medium for future development | Conduct usability and accessibility evaluations and introduce appropriate operational monitoring. | Accepted — these capabilities are outside the assessed UG release scope. |

**Session-only synthetic data and minute-precision local time:** SmartCare stores patient, practitioner and appointment records in memory for the duration of a single application session. All records are lost on exit. Testing and demonstrations use synthetic information only. Appointment input uses `YYYY-MM-DD HH:MM`, with local date/time values and minute precision.

**Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions:** SmartCare does not provide production authentication, user roles, patient portals, notifications, billing, insurance processing or AI-based clinical decisions. These features are explicitly excluded from the UG teaching release and must not be represented as implemented.

**Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations:** The application is designed for small-scale educational use. It does not provide production concurrency guarantees, comprehensive timezone handling, deployment monitoring or formal accessibility assurance. The console supports the required workflows but is not intended to replace a production healthcare interface.

**Difference between accepted scope limit and unresolved required behaviour:** An accepted scope limitation is functionality intentionally excluded from the specified UG requirements, such as database persistence or PG-only rescheduling. An unresolved required behaviour would be a defect preventing a required common feature from operating correctly. The verified integrated regression run completed with 69 passed and zero failed tests, and no unresolved required-behaviour defect was identified in that run. Passing tests do not guarantee the absence of all defects.

**PG assurance residual risks / owner / status or not applicable:** Not applicable.

## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| FR-07 cancelled appointment history | Stage 8 identified that cancelled appointments were not correctly retrievable. The corrected console demonstration retrieved cancelled appointment `A100`. | High — required appointment history behaviour | Group development team — corrected appointment lookup logic | Stage 8 fix `f2e6e19`; regression test `bc543d3` | `tests/test_stage8_regressions.py`; full integrated regression 69/69 passed | History remains available only during the current session |
| FR-05 practitioner-specific conflict checking | Stage 8 identified incorrect practitioner conflict comparison. Console rejected `A101` for `DR100` at an occupied time and allowed `A102` for `DR200` at that time. | High — incorrect booking decisions | Group development team — corrected conflict checking | Stage 8 fix `946dfe1`; regression test `bc543d3` | Focused regression included in the 69/69 passing integrated suite | No duration-based or patient-level conflict checking required |
| FR-09 and QRY/FP query functionality | Stage 9 implemented appointment queries, listing, filtering and console integration. | Required functionality added before release | Group development team — implemented and integrated Stage 9 scope | `1599a65`, `b9bc26b`, `e0a71cc`, `0f708af` | `tests/test_queries.py` and `tests/test_workflows.py` included in 69/69 passing suite | Queries operate on session-only records |
| Final integrated UG regression | `python -m pytest` from `project/` completed with 69 passed, zero failed at SHA `d960ba35b69dc469cf68100c311a19195064e70f`. | No test failure observed | Jonathan V — executed final regression | No Stage 12 executable correction recorded | Original working copy: 69 passed in 0.05s; fresh clone: 69 passed in 0.06s | Automated tests cannot prove absence of all defects |
| Final README and reproducibility | Both README files were updated to remove outdated starter information. Fresh clone passed all 69 tests. | Documentation and packaging readiness | Jonathan V — updated documentation and verified clone | Local changes to root `README.md` and `project/README.md`; final commit pending | `git diff --check` passed; fresh-clone regression passed | Final source ZIP and clean dependency installation remain unverified |

**Justified no-change conclusion if no defect found:** No additional executable defect was identified by the final integrated regression or the demonstrated booking and cancellation workflows. Therefore, no further executable code correction was recorded for Stage 12. The remaining work concerns documentation, final review and packaging rather than a demonstrated failure of required behaviour.

**Release blockers still open / status:** Final human release approval, submitted SHA reconciliation, source ZIP verification and assessment submission remain pending. No failing automated test is currently known.


## I Git review and integration evidence

**Issue / PR / diff links and reviewed SHA:** The repository is https://github.com/JacksonSu3319170/st1-assignment-3. Relevant integration pull requests include [PR #4](https://github.com/JacksonSu3319170/st1-assignment-3/pull/4) for patient lookup, [PR #5](https://github.com/JacksonSu3319170/st1-assignment-3/pull/5) for cancellation, [PR #6](https://github.com/JacksonSu3319170/st1-assignment-3/pull/6) for practitioner lookup, [PR #8](https://github.com/JacksonSu3319170/st1-assignment-3/pull/8) for Stage 7 testing, [PR #10](https://github.com/JacksonSu3319170/st1-assignment-3/pull/10) for Stage 8 debugging, [PR #11](https://github.com/JacksonSu3319170/st1-assignment-3/pull/11) for Stage 9 queries and console, and [PR #14](https://github.com/JacksonSu3319170/st1-assignment-3/pull/14) for Stage 12 work. The integrated tested SHA is `d960ba35b69dc469cf68100c311a19195064e70f`.

**Independent reviewer / feedback / response:** Earlier feature pull requests underwent the group's review process, with review and development evidence recorded in the applicable stage files. Exact independent reviewer identities, comments and responses must be taken from the GitHub reviews and stage records; these were not independently reconfirmed during the final release check.

**Integration commit / full recheck:** Commit `d960ba35b69dc469cf68100c311a19195064e70f` is the merged `main` release candidate. A full integrated regression passed 69/69 tests on macOS using Python 3.14.7 and pytest 8.3.5. A separately cloned copy of the same SHA also passed 69/69 tests.

**Tracked and untracked file inspection / cleanliness:** The latest inspected working copy contained local modifications to `.idea/st1-assignment-3.iml`, root `README.md`, `project/README.md` and `stage12/stage12_activities_and_evidence.md`. The README and Stage 12 changes are intentional release documentation. The PyCharm configuration change must remain excluded from the final commit. `git diff --check` subsequently completed without warnings. Final Git cleanliness must be checked after the documentation commit.

**Secrets/staff material/caches/tool-metadata exclusion check:** Final packaging must exclude `.git`, `.idea`, `.venv`, caches, credentials, real patient data, staff solutions, private QA, Stage 8 utilities and recovery backups. A complete final ZIP contents inspection has not yet been performed.

**Candidate recovery plan / known-good SHA:** The known-good integrated code SHA is `d960ba35b69dc469cf68100c311a19195064e70f`. If later changes cause failures, preserve the existing work, compare changes against this commit, and restore or revert only the identified problematic changes through the group's Git review process. Do not overwrite the submitted candidate without recording a new SHA and re-verifying it.

**Named substantive contributions:** Jackson S, Jonathan V and Ayaz M are the three UG group members. The integrated repository contains contributions covering feature implementation, testing, debugging, queries, documentation and release verification. Jonathan V performed the documented final regression, console demonstration, README updates and fresh-clone verification. Exact individual ownership of earlier implementation and reviews should be confirmed against the Git and stage evidence rather than inferred from group membership.


## J Human release decision

**Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY:** READY WITH DOCUMENTED LIMITATIONS — SmartCare `v1.0-UG` has completed its implemented undergraduate requirements and passed the integrated release regression. The known limitations are accepted as part of the educational scope.

**Approver / date / rationale and evidence:** UG Group 5 (Jackson S, Jonathan V and Ayaz M), 9 November 2026. The release decision is supported by 69/69 passing automated tests, successful fresh-clone verification at the identical tested SHA, demonstrated booking and cancellation workflows, Stage 8 regression fixes and the updated release documentation.

**What risks remain / conditions / owners:** Accepted limitations include session-only storage, local minute-precision appointment times, limited concurrency and the absence of production authentication, notifications, billing and clinical AI. The group retains responsibility for these documented scope boundaries. SmartCare is approved for course demonstration, not production healthcare deployment.

**Can the team explain the system:** Yes. The group has implemented and documented the domain model, shared store, service operations, queries, console and automated tests. The Stage 8 defect corrections and architectural responsibilities provide specific examples for the team viva.

**Can a change be recovered:** Yes. Git preserves the tested integrated candidate at `d960ba35b69dc469cf68100c311a19195064e70f`. Any subsequent changes can be compared against this known-good commit, reviewed and re-tested.

**Common decision / PG decision where different:** READY WITH DOCUMENTED LIMITATIONS for the common UG release. PG-only assurance and rescheduling requirements are not applicable because the group consists entirely of undergraduate students.

## K Final tested release SHA

**Exact common tested SHA:** `d960ba35b69dc469cf68100c311a19195064e70f`

**Exact PG tested SHA or not applicable:** Not applicable — UG-only group.

**Final submitted SHA / repository URL:** SmartCare `v1.0-UG`, repository: https://github.com/JacksonSu3319170/st1-assignment-3. The integrated executable release was verified at `d960ba35b69dc469cf68100c311a19195064e70f`. The final documentation commit SHA is 03e1c93eba35ff53a3554a721beb90da3d952819.

**Evidence-only later commit and difference explanation:** The final Stage 12 documentation update includes the release evidence, README improvements, release notes and handover information. These documentation changes do not alter the tested executable behaviour. The final Git diff is used to confirm the distinction between the tested executable candidate and the later documentation-only submission commit.

**Executable changes after testing and re-verification:** No executable changes are intended after the 69/69 passing release regression. Any executable modification would require focused and full re-verification before submission.

**Source ZIP name / SHA correspondence / extracted comparison:** `SmartCare-v1.0-UG-source-clean.zip` was generated from final tested commit `03e1c93eba35ff53a3554a721beb90da3d952819` using `git archive`. Archive inspection confirmed 38 entries, including root `README.md`, `.gitignore`, project source, all eight test files and applicable stage records. Git metadata, PyCharm configuration, virtual environments and test caches were excluded. The ZIP was extracted into a separate `smartcare-zip-verification/` directory, and `python -m pytest` passed all 69 tests in 0.05 seconds using Python 3.14.7 and pytest 8.3.5. The extracted source was verified successfully; the existing Python environment was reused.

The earlier executable release candidate d960ba35b69dc469cf68100c311a19195064e70f was followed by a reviewed documentation-only merge. The final merged commit was re-tested successfully with 69/69 tests passing.
## L Submission package verification

- [x] Feature freeze and scoped requirements traced.
- [x] Applicable full regressions, integrated demo and invalid paths verified.
- [x] Architecture/code quality and final AI/dependency checks complete.
- [x] Root README and project/README reproduced by another verifier.
- [x] Release notes, technical debt and limitations visible.
- [x] Independent human review, integration and release decision recorded.
- [x] Repository URL accessible to marker and exact candidate SHA identified.
- [x] One source ZIP from submitted commit with root README.md and .gitignore.
- [x] project/ source and all accumulated applicable tests included.
- [x] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [x] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [x] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [x] Mixed-group common protection and candidate upload routing checked.
- [x] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: Stage 12 release submission through the course's designated assessment upload item, subject to confirmation of the published Canvas instructions.

Deadline/timezone: The deadline and timezone are those specified in the official Canvas assessment item and must be checked before final submission.

Repository access arrangement: GitHub repository: https://github.com/JacksonSu3319170/st1-assignment-3. A separate clone successfully retrieved and tested the integrated candidate. Marker access must be maintained.

Mixed-candidate upload arrangement: Not applicable — UG-only group with one common release candidate.

Oral/video recording/accessibility arrangements: The group will follow the published arrangements for the common team viva and any required recording or accessibility provisions.

Remaining administration or release dependency: Final documentation commit, exact submitted SHA, source ZIP inspection and required Canvas submissions.


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

**Strongest evidence SmartCare is ready:** SmartCare passed all 69 automated tests on the integrated release candidate. A separate fresh GitHub clone at the same SHA also passed all 69 tests. The interactive console demonstration confirmed patient and practitioner registration, appointment booking, practitioner-specific conflict rejection, cancellation and retained appointment history. Together, these provide strong evidence that the implemented UG requirements are working.

**Weakest area:** SmartCare uses in-memory storage, meaning records are lost when the application closes. It also lacks production features such as authentication, persistent storage and comprehensive timezone handling. These are accepted limitations of the educational release rather than unresolved required functionality.

**How AI use changed from Stage 1 to Stage 12:** The development process progressed from using AI to assist with understanding requirements, planning and generating implementation ideas toward more critical evaluation of code, tests, debugging and release documentation. By Stage 12, the focus was on checking AI-assisted work against requirements, verifying behaviour through tests and ensuring that the final release evidence accurately reflected the implementation.

**Start doing — engineering and AI use:** Record AI suggestions, human decisions, test results and Git evidence immediately after completing each development task. This makes later reviews and release preparation more reliable.

**Stop doing — engineering and AI use:** Avoid accepting AI-generated code or explanations without checking them against requirements and tests. Avoid leaving documentation and evidence updates until the final development stage.

**Continue doing — engineering and AI use:** Continue using modular code, small changes, regression tests, Git version control, synthetic test data and human review of AI-assisted suggestions.

**What worked / caused rework / future delivery improvement:** Separating the application into domain, storage, services, queries and console components helped the team develop and test functionality independently. Automated tests made integration and release verification easier. Stage 8 required rework to correct cancelled-appointment retrieval and practitioner-specific conflict checking. Future projects would benefit from earlier integration checks and keeping README files and development evidence updated throughout the project.

**One paragraph — If AI can write code why do we still need software engineers:** Software engineers are still essential because writing code is only one part of software development. Engineers must understand stakeholder requirements, design appropriate systems, evaluate risks, test behaviour, diagnose defects and take responsibility for the final product. AI can help generate code and suggest solutions, but its outputs can contain mistakes or fail to meet the intended requirements. Human engineers are needed to verify correctness, make ethical decisions, protect sensitive information and determine whether software is safe and appropriate for release.

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | SmartCare is an educational patient, practitioner and appointment management application. Its stakeholders include patients, practitioners, administrative users and the course assessors. Evidence: `project/README.md` and the SmartCare overview. |
| Two requirements and acceptance criteria | **FR-05:** Booking must reject an appointment when the same practitioner already has a scheduled appointment at that time, while allowing another practitioner at the same time. **FR-07:** Cancelling an appointment must preserve its record and allow later lookup showing its cancelled status. Evidence: `tests/test_stage8_regressions.py` and Stage 8 evidence. |
| Domain model and architecture | Patient, Practitioner and Appointment represent the main domain entities. The shared store maintains records, services coordinate operations, queries retrieve and filter information, and the console provides the interactive interface. Evidence: `project/smartcare/` and `project/README.md`. |
| Design trade-off | In-memory storage simplifies implementation and testing without requiring a database. The disadvantage is that records do not persist between sessions. This is acceptable for the UG teaching scope. Evidence: `project/README.md`. |
| Meaningful test and its limits / 100 percent coverage | The Stage 8 regression tests verify cancelled-appointment retrieval and correct practitioner-specific booking conflicts. The integrated test suite passed 69/69 tests. This does not establish 100% code coverage or guarantee that every possible defect has been found. Evidence: `tests/test_stage8_regressions.py` and Stage 12 Part C. |
| Diagnosed defect and verification | Stage 8 identified and corrected two defects: cancelled appointments were not being retrieved correctly, and practitioner conflicts were not being checked correctly. Regression tests were added, and both behaviours were included in the passing integrated test suite. Evidence: Stage 8 record and `tests/test_stage8_regressions.py`. |
| Shared store and session-state/query responsibilities | The shared store holds the patient, practitioner and appointment records for the current session. Services manage operations that change records, while queries retrieve, filter and order existing records without modifying them. Evidence: `project/smartcare/` and `tests/test_queries.py`. |
| What would break if session-state lookup/query responsibilities changed? | If lookup functions excluded cancelled appointments, retained history would fail. If query functions modified stored data or filtered incorrectly, later listings and booking decisions could become inconsistent. Evidence: Stage 8 regression tests and Stage 9 query tests. |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | Cancellation changes an appointment's lifecycle state and must respect its status rules, making it domain behaviour. Conflict checking compares a proposed booking with other appointments in the shared store, requiring coordination by the service layer. Evidence: domain and service implementation and `tests/test_services.py`. |
| FR-07 retained history test | Book an appointment, cancel it, then retrieve it by ID. The appointment must still exist and show `cancelled`. This was demonstrated using appointment `A100` and covered by the regression tests. Evidence: `tests/test_stage8_regressions.py` and Stage 12 Part D. |
| Actual AI change rejected/modified or honestly accepted with verification | AI-assisted suggestions were subject to human review rather than automatic acceptance. The exact earlier Copilot suggestion and accept/modify/reject decision should be demonstrated from the relevant Stage 6–9 AI evidence. No specific unverified AI interaction is claimed here. |
| Unresolved limitation / future production work | SmartCare does not include persistent storage, production authentication, role-based access, notifications or comprehensive timezone management. Future production development would require additional requirements, security controls and testing. Evidence: `project/README.md` and Stage 12 Part G. |
| Personal implementation contribution | My confirmed Stage 12 contribution was updating the root and project README files and preparing the final release documentation. Earlier implementation contributions should be explained using the relevant Git commits and development records rather than attributing unverified code changes. Evidence: README changes and `stage12/stage12_activities_and_evidence.md`. |
| Personal test/review/design/integration contribution | I ran the full integrated regression, verified the application through the interactive console, checked the README documentation and tested a separate GitHub clone at the same commit SHA. Both regression runs passed 69/69 tests. Evidence: Stage 12 Parts C, D, F and I. |
| PG agentic change and rescheduling verification | Not applicable — the group consists entirely of UG students. |
| PG responsible-AI risk/remediation or supported no finding | Not applicable — PG-only assurance requirements do not apply to this group. |

**Practice question/change and reasoning:** Not undertaken. No additional executable code change was made during final release preparation. The tested release candidate was preserved.

**Separate reflection / peer / common team viva evidence links and routing:** The group reflection, confidential individual peer-assessment forms and common team viva are separate assessment activities and are to be completed through their designated course submission or participation routes. They are not included as substitutes for the SmartCare source ZIP.

No further coding stage. Later corrections use the published assessment process.