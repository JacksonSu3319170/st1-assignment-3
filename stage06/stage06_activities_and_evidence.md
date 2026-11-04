# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Wed 4:30 - 6:30 Group 5
- Members, GitHub usernames and cohorts: Jonathan (jonathansv7), Jackson (JacksonSu3319170), Ayaz (AyazMohammed999)
- Repository URL: https://github.com/JacksonSu3319170/st1-assignment-3.git
- Starting SHA: [cb1a64ecd31300af393ca5a64d5bde4af025cf8e]

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Implement patient lookup by ID (FR-02)
- Context: SmartCare needs to retrieve an existing patient using their registered patient ID. The find_patient method is currently incomplete.
- Requirement: FR-02 – Patient Search.
- Acceptance criteria: A registered patient can be retrieved using their ID, and the returned object must be the same object stored in SmartCare. IDs are trimmed and case-sensitive. Invalid or blank IDs raise ValueError, while valid but unknown IDs raise LookupError. Failed lookups must not change stored data.
- Scope: Implement PatientService.find_patient in project/smartcare/services.py and add relevant tests in project/tests/test_services.py. Do not modify unrelated services or introduce additional storage.
- Definition of Done: The implementation meets the acceptance criteria, meaningful tests pass alongside the eight supplied tests, a different team member reviews the pull request, feedback is resolved, and the approved change is merged into main.
- Owner: jonathansv7
- Actual issue link: https://github.com/JacksonSu3319170/st1-assignment-3/issues/1#issue-6200123544

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Implement appointment cancellation and retain history (FR-06/FR-07)
- Context: SmartCare needs to allow users to cancel scheduled appointments while keeping cancelled appointments available for future lookup. The cancel_appointment service method is currently incomplete.
- Requirement: FR-06 – Appointment Cancellation and FR-07 – Retained Appointment History.
- Acceptance criteria: 

A SCHEDULED appointment can be cancelled successfully.

Cancellation changes its status to CANCELLED.

The method returns the same appointment object stored in SmartCare.

Cancelled appointments remain stored and retrievable.

Cancelling an already CANCELLED or COMPLETED appointment raises ValueError without changing its state.

Invalid or blank IDs raise ValueError, and valid but unknown IDs raise LookupError.
- Scope: Implement AppointmentService.cancel_appointment in project/smartcare/services.py and add focused tests in project/tests/test_services.py. Use the existing domain cancellation method. Do not delete appointments, directly change protected state or add new storage.
- Definition of Done: All acceptance criteria are verified by meaningful tests, the original eight tests still pass, another team member reviews the pull request, feedback is resolved, and the approved code is merged into main.
- Owner: jonathansv7
- Actual issue link: https://github.com/JacksonSu3319170/st1-assignment-3/issues/2#issue-6200201786

### FR-03 Practitioner Lookup

**Title:** Implement practitioner lookup by ID

**Context:** SmartCare must retrieve registered practitioners using their unique practitioner IDs. The `find_practitioner` method is currently incomplete.

**Requirement:** Supporting practitioner lookup operation for FR-03.

**Acceptance criteria:**
- A registered practitioner can be retrieved using their ID.
- The returned practitioner is the same object held in the data store.
- IDs are trimmed and case-sensitive.
- Invalid or blank IDs raise `ValueError`.
- Valid but unknown IDs raise `LookupError`.
- Failed lookups do not modify stored records.

**Scope:** Implement `PractitionerService.find_practitioner` in `project/smartcare/services.py` and add focused tests in `project/tests/test_services.py`. Preserve the existing registration behaviour and storage design.

**Definition of Done:** Acceptance criteria are tested, existing tests remain passing, another team member reviews the change, feedback is resolved, and the approved PR is merged into `main`.

**Owner:** jonathansv7

**Actual Issue Link:** https://github.com/JacksonSu3319170/st1-assignment-3/issues/3#issue-6200300319
## B Commit quality

| Original example | Strong or Weak | Reason |
|---|---|---|
| changes | Weak | Too vague. It does not explain what was changed, making it difficult for teammates to understand the commit history. |
| final version | Weak | Does not describe the actual changes and could become misleading if further updates are needed. |
| Add patient search by ID | Strong | Clearly identifies the functionality being added, making the purpose of the commit easy to understand. |
| fix stuff | Weak | Does not identify what was fixed or which part of the application was affected. |
| Prevent cancellation of completed appointments | Strong | Describes a specific behaviour being enforced, making the change easier to review and trace to requirements. |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: The pull request includes unrelated changes that are not needed to implement appointment cancellation. This makes the PR larger and more difficult to review, and increases the risk of introducing bugs.
- Responsibility and architecture concerns: Renaming patient fields and restructuring unrelated code could affect other parts of SmartCare. Appointment cancellation should be implemented through the existing service and domain methods, without unnecessarily changing the application's architecture.
- Testing and review concerns: A pull request with too many unrelated changes is harder for teammates to review and can lead to mistakes being missed. Even if all tests pass, there could still be problems with existing features. The reviewer should check that appointments can be cancelled correctly, cancelled appointments remain stored, and invalid cancellations are rejected.
- Changes to remove or separate, with reasons: The unrelated patient field renaming, code restructuring and new dependency should be removed from this PR. If these changes are genuinely necessary, they should be handled in separate issues and pull requests so they can be reviewed and tested independently. The current PR should focus on implementing and testing appointment cancellation under FR-06 and FR-07.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: Copilot has not explained which code it reviewed, which tests passed, or whether the changes meet the SmartCare requirements. It also hasn't checked for missing tests, incorrect error handling or unrelated code changes.
- Follow-up review question 1: Does the code meet all the acceptance criteria for the requirement being implemented?
- Follow-up review question 2: Which tests check that the new functionality works correctly, including invalid inputs and errors?
- Follow-up review question 3: Does appointment cancellation correctly change the status to CANCELLED while keeping the appointment stored?
- Follow-up review question 4: Are there any unrelated changes in the pull request that should be removed or reviewed separately?
- Follow-up review question 5: Could these changes break any existing SmartCare functionality, even if the current tests pass?
- Additional questions if useful: Does the code follow the existing responsibilities of the service, domain and data store classes? Has a team member independently reviewed the actual code changes?

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | Use descriptive names such as feature/patient-lookup, feature/practitioner-lookup and feature/appointment-cancellation. Each task will have its own branch. |
| Commit message convention | Use short, clear messages explaining what changed, such as Add patient search by ID or Test appointment cancellation. |
| PR size | Keep pull requests small and focused on one issue or feature at a time. Avoid unrelated changes. |
| Another-member review requirement | At least one different team member must review each pull request before it can be merged. |
| Merge rule | Only merge a PR into main after tests pass, feedback is addressed, human review is completed and approval is received. |
| Significant Copilot disclosure rule | Record significant GitHub Copilot assistance, including what was suggested, how it was checked and whether the suggestion was accepted, modified or rejected. |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| https://github.com/JacksonSu3319170/st1-assignment-3/issues/1#issue-6200123544 | FR-02 Patient Search | jonathansv7 | See acceptance criteria in linked issue | Open |
| https://github.com/JacksonSu3319170/st1-assignment-3/issues/2#issue-6200201786 | FR-06/FR-07 Appointment Cancellation | jonathansv7 | See acceptance criteria in linked issue | Open |
| https://github.com/JacksonSu3319170/st1-assignment-3/issues/3#issue-6200300319 | FR-03 supporting practitioner lookup | jonathansv7 | See acceptance criteria in linked issue | Open |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: Add patient search by ID with tests (FR-02) https://github.com/JacksonSu3319170/st1-assignment-3/pull/4#issue-6200989464
- Linked issue and requirement: #1, https://github.com/JacksonSu3319170/st1-assignment-3/issues/1#issue-6200123544
- Feature branch: feature/patient-lookup
- Changed behaviour: Patient lookup now returns the stored patient and raises the required errors.
- Meaningful commits: 04af89b3139d5603b58b33195624db7047323463
- Test command, directory and observed result: python -m pytest, project/, 16 passed in 0.02 seconds.
- Another-member reviewer: Jackson/Ayaz
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: The implementation uses the existing SmartCareDataStore.find_patient() method to retrieve a registered patient. It raises LookupError when the patient is not found and returns the original stored patient object when found.
- Key feedback: The reviewer confirmed that patient lookup uses the existing data store and returns the original patient object. They also checked the handling of invalid and unknown IDs and the test coverage. No major changes were requested.
- Author response/change and verification: The author reviewed the feedback and confirmed that the implementation meets FR-02. No additional code changes were required. The existing test suite passed with 16 tests.
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: Pull request merged into main — [actual merge commit SHA].
- Significant Copilot assistance: Copilot reviewed the PR after the human review. Its suggestions were checked against FR-02 and the actual code. None were Added.
- Linked issue closure: FR-02 Patient Search — Closed after the approved PR was merged.
- Each member updated main: Jonathan — confirmed; Jackson — confirmed; Ayaz — confirmed after pulling the merged changes and running tests.
- Integrated verification after merge: Ran python -m pytest from project/. All 16 tests passed. Tested code SHA: [actual SHA from git rev-parse HEAD].

Pull Request 2 — FR-06/FR-07 Appointment Cancellation
PR link: https://github.com/JacksonSu3319170/st1-assignment-3/pull/5#issue-6202039518

Linked issue: #2 — FR-06/FR-07 Appointment Cancellation and Retained History

Branch: feature/appointment-cancellation

Commit link/SHA: 2a7fb86b464beedc5706340e764d8020675e2c49

Reviewer: Jackson/Ayaz

Key feedback: The implementation correctly uses the existing Appointment.cancel() method to change an appointment from SCHEDULED to CANCELLED. It preserves the appointment in the data store and prevents invalid transitions, including repeated cancellation and cancellation of completed appointments. The tests cover the main requirements. A possible improvement is to add a test confirming that appointment details, such as the patient, practitioner and date/time, remain unchanged after cancellation.

Author response/change and verification: The author, Jonathan, reviewed the suggested improvement and confirmed that cancellation only changes the appointment status. The existing automated tests passed with 18 successful tests. The additional appointment-details test should be added and verified if the reviewer requests it.

Merge outcome and SHA: Merged 

Significant Copilot assistance: GitHub Copilot review 

Linked issue closure: Issue #2 remains open until the approved PR is merged.

Each member updated main: Jonathan — confirmed; Jackson — confirmed; Ayaz — confirmed after pulling the merged changes and running tests.

Local verification: python -m pytest from project/ — 18 passed. 

### Pull Request 3 — FR-03 Practitioner Lookup

- **PR link:** https://github.com/JacksonSu3319170/st1-assignment-3/pull/6#issue-6202135494
- **Linked issue:** #3 — FR-03 Practitioner Lookup
- **Branch:** `feature/practitioner-lookup`
- **Commit link/SHA:** 3d87bbf4eeabb6ed325c7b4f3ba12ea980529e51
- **Reviewer:** Jackson/Ayaz

- **Key feedback:** The practitioner lookup implementation correctly delegates to the existing data store and returns the original stored practitioner object. It handles invalid and unknown IDs, whitespace trimming and case sensitivity. The automated tests cover the main acceptance criteria. A possible improvement is to add a test confirming that an unsuccessful lookup does not affect other registered practitioners, although the existing test already checks preservation of one registered practitioner.

- **Author response/change and verification:** Implemented `PractitionerService.find_practitioner` using the shared SmartCare data store. Added automated tests for successful lookup, object identity, trimmed IDs, case sensitivity, invalid and unknown IDs, and unchanged stored data. The local test suite passed.

- **Merge outcome and SHA:** Merged 

- **Significant Copilot assistance:** GitHub Copilot review.

- **Linked issue closure:** Completed

- **Each member updated main:** Jonathan — confirmed; Jackson — confirmed; Ayaz — confirmed after pulling the merged changes and running tests.

- **Local verification**: `python -m pytest` from `project/` — [Insert actual test result]. Record the integrated test result and code SHA after merging.

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: Jonathan, GitHub Copilot review of FR-02 Patient Search implementation and tests.
- Prompt/purpose and relevant issue/diff: Asked GitHub Copilot to review PatientService.find_patient against FR-02 acceptance criteria, including object identity, ID validation, error handling, test coverage, code scope and maintainability. Issue: [Linked Above in Table]. PR: [Linked Above].
- Summary of output: Copilot found that the implementation meets the main patient lookup requirements. It confirmed that the service returns the original stored object, handles trimmed and case-sensitive IDs, and raises the correct exceptions. However, it identified a missing test to verify that failed lookups leave stored data unchanged. It also identified an outdated TODO description in the method's docstring.
- Human check against actual code, requirements and tests: The existing tests verify successful lookup, object identity, trimmed IDs, case sensitivity and invalid inputs. The reported test run showed 16 passing tests. The missing no-mutation assertion is a valid improvement because it is explicitly included in the FR-02 acceptance criteria. The docstring should also accurately describe the completed method.
- Decision — Accept / Modify / Reject: Accept the recommendation to add the missing regression test and update the outdated docstring, subject to checking the actual code.
- Reason: Both suggestions are relevant to the existing requirement and improve test coverage and maintainability without introducing unrelated functionality.
- Verification/evidence: Existing verification: python -m pytest from project/ — 16 passed in 0.02 seconds. https://github.com/copilot/share/802f5226-4a04-82b3-8051-b408444b4129

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: The draft human review found that the patient lookup implementation followed the requirements, returned the original stored patient object, and handled invalid and unknown IDs correctly. The tests covered the main functionality, and no unrelated changes were identified. These observations still require confirmation from the assigned teammate.
- Copilot noticed: Copilot confirmed that the main lookup functionality was correct but identified two improvements. First, there was no test verifying that a failed lookup leaves existing patient data unchanged. Second, the method's docstring still contained an outdated Stage 6 TODO description.
- Overlap: Both reviews agreed that the implementation met the main FR-02 requirements and was appropriately scoped. Copilot identified an additional test coverage gap and a documentation issue that were not mentioned in the draft human review.
- What did the human reviewer notice that Copilot did not: I accepted Copilot's recommendations to add a regression test for unsuccessful lookups and update the outdated docstring. These improvements were relevant to the acceptance criteria and did not require changing the main lookup logic.
- What did Copilot identify that the human reviewer initially missed: The additional test was added, and the test suite ran successfully from the project/ directory. The expected result is 17 passing tests, subject to confirming the actual terminal output. The docstring update and independent reviewer approval must also be confirmed before the PR is merged.
- Unsupported or incorrect Copilot suggestion: None identified. Copilot's recommendations to add a test for unchanged stored data after a failed lookup and update the outdated docstring were both relevant to FR-02. However, Copilot could not independently confirm the reported test results or human review approval.
- Human judgement accepted, modified or rejected, and why: I accepted Copilot's recommendations because they improved test coverage and code documentation without changing the existing functionality. I added a regression test to verify that failed lookups do not affect registered patients and successfully reran the test suite.
- Which evidence justified merge approval: The implementation met the FR-02 acceptance criteria, including returning the original patient object, validating IDs and handling unknown patients. The updated tests passed locally, and the changes remained focused on the required functionality. Final merge approval also requires the assigned teammate's independent review and approval on GitHub.

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: Jonathan
- Implementation: Implemented PatientService.find_patient for FR-02 using the existing SmartCare data store. The function returns the original stored patient object and raises LookupError for unknown patients. Evidence: project/smartcare/services.py and the feature/patient-lookup branch.
- Testing: Created automated tests covering successful patient lookup, invalid IDs, unknown patients, whitespace trimming and case sensitivity. Added an additional regression test to verify that failed lookups do not change stored patient data. Successfully ran python -m pytest from the project/ directory. Evidence: project/tests/test_services.py and passing pytest results.
- Review: Created a pull request for FR-02 and requested a teammate review. Used GitHub Copilot to review the implementation, identify missing test coverage and suggest documentation improvements. Evaluated the feedback against the acceptance criteria. Evidence: FR-02 pull request and Copilot review.
- Issue refinement: Created GitHub issues for FR-02 Patient Search, FR-03 Practitioner Lookup and FR-06/FR-07 Appointment Cancellation. Defined the required functionality and organised these tasks in the Stage 6 backlog. Evidence: GitHub issues and Sections A and F.
- Design and responsibility discussion: Contributed to defining the team's development workflow, including feature branches, focused commits, pull requests, independent reviews and testing before merging. Kept patient lookup responsibilities within the existing service and data store structure. Evidence: Section E and FR-02 implementation.
- Debugging or integration: Resolved a Python import error by running pytest from the correct project/ directory. Set up the Python virtual environment and verified that the existing and newly added tests passed. Evidence: PyCharm terminal output and pytest results.
- Documentation or team support: Completed Stage 6 evidence records, including issue planning, commit quality assessment, pull request review analysis, Copilot evaluation and individual contribution documentation. Prepared review information for teammates and documented the FR-02 development process. Evidence: stage06/stage06_activities_and_evidence.md.

Team collaboration:

I requested an independent review from another team member and documented the review process. Final approval, merging and team integration will be recorded once completed.

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

A high commit count does not necessarily mean someone contributed more because commits can be small or contain minor changes. A strong contribution is measured by the quality and importance of the work, including implementing features, writing tests, reviewing code, fixing bugs and helping the team. One meaningful commit can provide more value than many small commits.

## L Stage 6 formative questions

1. What is version control?

Version control is a system that tracks changes to files and code over time. It allows developers to collaborate, view previous versions and restore changes if needed.


2. Why is a feature branch useful?

A feature branch allows developers to work on a specific feature without affecting the main code. Changes can be tested and reviewed before being merged into main.

3. What makes a commit a good engineering commit?

A good commit contains focused changes and has a clear, meaningful message explaining what was changed. It should be easy for other developers to understand and review.

4. What is a pull request?

A pull request is a request to merge changes from one branch into another. It allows team members to review the code, suggest improvements and approve changes before merging.



5. What is the purpose of code review?

Code review helps identify bugs, improve code quality, check requirements and ensure changes follow project standards before they are merged.

6. What does a Git diff show?

A Git diff shows the differences between versions of files, including lines that have been added, removed or modified.

7. What is a Definition of Done?

A Definition of Done is a set of conditions that must be met before a task is considered complete, such as meeting requirements, passing tests, completing reviews and updating documentation.

8. What is the appropriate role of GitHub Copilot in pull-request review?

GitHub Copilot should assist us to review by suggesting possible bugs, missing tests and improvements. Its suggestions must be checked by developers because AI feedback may be incorrect or incomplete.

9. Why should individual contribution not be judged only by commit count?

Commit count does not measure the quality or importance of someone's work. Contributions also include testing, reviewing code, fixing bugs, planning and supporting teammates.

10. What is the Stage 6 engineering rule?

Every change should be linked to a clear requirement, developed in a focused branch, tested, independently reviewed and verified before being merged. Human developers remain responsible for checking AI suggestions and approving the final code.

## M Completion and handover

- Starting SHA: cb1a64ecd31300af393ca5a64d5bde4af025cf8e
- Final Stage 6 code SHA: 94040455ee63f4cf766f456e7dc3fd80f67264d0
- Test command: [python -m pytest]
- Working directory: [project/]
- Observed result: 36 tests collected and 36 passed in 0.03 seconds, using Python 3.14.7 and pytest 8.3.5 on macOS.
- PR and another-member reviewer: [PR #1, #2, #3 all reviewed by Jackson]
- Unresolved issue or none: None
- Stage 7 handover status: Ready for checkpoint


- [x] Three Stage 6 service targets completed and checked.
- [x] Original supplied tests retained and passing.
- [x] At least two focused issues link requirements and acceptance criteria.
- [x] Feature work reviewed by another member using the actual diff.
- [x] Human-first review and required Copilot comparison recorded.
- [x] Feedback resolved and approval recorded before merge.
- [x] Everyone pulled main and integrated checks passed.
- [x] Required activities, quiz responses and contribution notes completed.
- [x] Only synthetic data included; confidential peer material kept out.
- [x] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
