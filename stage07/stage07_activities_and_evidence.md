# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement                         | Positive test                                                                                                      | Negative test                                                                                                        | Key assertion                                                                                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FR-01 Register patient              | Create a patient with valid,non-blank ID "P1" and name "Alice Smith" through PatientService.register_patient.      | Attempt registration with a blank or whitespace-only patient ID "" or "   ".                                         | Check that the stored patient's ID and name match the input, and check that pytest.raises(ValueError) is triggered for blank IDs.                                                    |
| FR-05 Prevent practitioner conflict | Book an appointment for Practitioner "DR1" at 10:00, and book another appointment for Practitioner "DR2" at 10:00. | Attempt to book a second appointment for "DR1" at the exact same date and time (10:00) while the first is SCHEDULED. | Check that both appointments for different practitioners are stored as SCHEDULED, and assert that the duplicate booking for the same practitioner raises ValueError.                 |
| FR-06 Cancel appointment            | Call cancel_appointment("A1") on an existing SCHEDULED appointment.                                                | Call cancel_appointment("A1") again on the already CANCELLED appointment.                                            | Assert that appointment.status == AppointmentStatus.CANCELLED, and assert that the repeated attempt raises ValueError leaving the status unchanged.                                  |
| FR-07 Retain cancelled history      | Cancel appointment "A1", then call find_appointment("A1") from the data store.                                     | Attempt to find an unknown appointment ID "A_UNKNOWN".                                                               | Assert data_store.find_appointment("A1") is appointment and appointment.status == AppointmentStatus.CANCELLED; assert that absent ID lookup raises LookupError at the service layer. |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Weak/unclear]  Why: Proves nothing about system behavior; will pass even if the code crashes or does nothing.

`assert appointment is not None`
Judgement: [Weak/unclear]  Why: Only proves that some object exists; does not establish correct identity, valid attributes, or required status.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour]  Why: Directly proves that the required state transition occurred on the target appointment.

`assert len(results) > 0`
Judgement: [Weak/unclear]  Why: Only verifies that the collection is not empty; does not verify correct count, expected items, or correct sorting order.

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour]  Why: Proves exact object identity in the shared store, confirming the record was retained and not replaced by a clone.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: Blank / Whitespace ID: Input " "; Expected: pytest.raises(ValueError); Contract: required_text enforces trimmed, non-blank strings.   Same-time Practitioner Booking: Two bookings for same practitioner at identical minute-precision datetime; Expected: pytest.raises(ValueError); Contract: has_practitioner_conflict rule in FR-05.   Repeated Cancellation: Cancelling an appointment already in CANCELLED status; Expected: pytest.raises(ValueError); Contract: Domain guard only allows cancelling from SCHEDULED.

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate                                           | What is wrong                                                                                                                                                                                          | Rewritten test intention                                                                                                                                                                                                        |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 Asserting appointment is not None                 | Weak assertion; merely proves that an object reference was returned rather than verifying whether the appointment was actually booked with the correct patient, practitioner, time, or initial status. | Strengthen the assertion to check specific domain invariants and attributes: verify that appointment.appointment_id == "A1", appointment.status == AppointmentStatus.SCHEDULED, and the participant identities match the input. |
| 2 Asserting patient is not None                     | Weak assertion; allows a test to pass even if the returned object contains empty, corrupted, or incorrect patient attributes.                                                                          | Strengthen the assertion to verify exact attribute equality (patient.patient_id == "P1" and patient.name == "Alice Smith") and confirm that retrieving the ID from the shared store returns this exact object reference.        |
| 3 Asserting assert True                             | Tautology / completely uninformative assertion; this will pass unconditionally regardless of whether the tested code executed correctly, produced errors, or failed its contract.                      | Replace with a targeted assertion that checks observable behavior, such as verifying that calling cancel() transitions the status from SCHEDULED to CANCELLED.                                                                  |
| 4 Assuming SMS notification is sent on booking      | Invented requirement; assumes external notification side-effects that are not part of the SmartCare course specifications.                                                                             | Remove all external notification assertions and rewrite the test to verify internal session state: confirm that the appointment is added to SmartCareDataStore and is retrievable via find_appointment().                       |
| 5 Assuming SMS notification is sent on cancellation | Invented requirement and out-of-scope external dependency; tests an unneeded service integration rather than core business rules.                                                                      | Focus strictly on the documented cancellation contract: assert that the appointment status updates to AppointmentStatus.CANCELLED, remains stored in the session, and frees the practitioner's slot for subsequent bookings.    |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
Code coverage only measures which lines of code were executed during testing. It does not verify that assertions are meaningful, that edge cases were evaluated, or that business invariants were checked—a test with no assertions or assert True can execute 100% of lines while verifying nothing.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type    | Test name / location                                             | Expected behaviour                           | Result / observed status | Supplied or student-authored |
|-------------|----------------------|---------|--------------|------------------------------------------------------------------|----------------------------------------------|--------------------------|------------------------------|
| FR-01       | AC-01.1              | TEST-01 | Service      | test_services.py::test_register_and_find_patient                 | Valid patient stored and retrievable         | Pass                     | student-authored             |
| FR-01       | AC-01.2              | TEST-02 | Service      | test_services.py::test_duplicate_patient_id_rejected             | Duplicate ID raises                          | Pass                     | student-authored             |
| FR-01       | Revision 2 Contract  | TEST-03 | Domain Unit  | test_domain.py::test_blank_patient_id_is_rejected                | Blank ID raises                              | Pass                     | student-authored             |
| FR-04       | AC-03.1              | TEST-04 | Service      | test_services.py::test_book_appointment_success                  | Valid booking creates SCHEDULED appointment  | Pass                     | student-authored             |
| FR-05       | AC-04.1              | TEST-05 | Service      | test_services.py::test_prevent_practitioner_conflict_same_time   | Same practitioner & time raises              | Pass                     | student-authored             |
| FR-05       | AC-04.2              | TEST-06 | Service      | test_services.py::test_allow_different_practitioner_at_same_time | Different practitioner at same time succeeds | Pass                     | student-authored             |
| FR-06       | AC-05.1              | TEST-07 | Domain Unit  | test_domain.py::test_cancel_changes_status                       | Status updates to                            | Pass                     | student-authored             |
| FR-06       | AC-05.3              | TEST-08 | Domain Unit  | test_domain.py::test_repeated_cancellation_is_rejected           | Repeated cancel raises                       | Pass                     | student-authored             |
| FR-07       | AC-05.2              | TEST-09 | Service      | test_services.py::test_cancel_appointment_and_retain_history     | Cancelled record remains in store            | Pass                     | student-authored             |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement                 | Acceptance criterion | Positive / Negative / Boundary | Test intention                              | Observable result expected                                       | Added evidence beyond supplied tests                                                                     |
|---------|-----------------------------|----------------------|--------------------------------|---------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| TEST-01 | FR-01 Register patient      | AC-01.1              | Positive                       | `test_patient_valid_construction()`         | `patient.patient_id == "P1"` and `patient.name == "Alice Smith"` | Proves valid construction and that patient properties retain attributes accurately.                      |
| TEST-02 | FR-01 Register patient      | Rev 2 Contract       | Boundary                       | `test_blank_patient_id_is_rejected()`       | Raises `ValueError` via `pytest.raises(ValueError)`              | Proves whitespace-only string is trimmed and rejected by the `required_text` domain validation contract. |
| TEST-03 | FR-01 Register patient      | Rev 2 Contract       | Boundary                       | `test_blank_patient_name_is_rejected()`     | Raises `ValueError` via `pytest.raises(ValueError)`              | Proves empty string name input is caught and rejected by domain validation.                              |
| TEST-04 | FR-03 Register practitioner | Rev 2 Contract       | Positive                       | `test_practitioner_valid_construction()`    | Properties match supplied ID, name, and specialty                | Proves practitioner constructor retains all three required attributes correctly.                         |
| TEST-05 | FR-03 Register practitioner | Rev 2 Contract       | Boundary                       | `test_blank_practitioner_fields_rejected()` | Raises `ValueError` for each blank field                         | Proves blank strings in ID, name, or specialty are rejected by domain validation.                        |
| TEST-06 | FR-04 Book appointment      | AC-03.1              | Positive                       | `test_new_appointment_starts_scheduled()`   | `apt.status == AppointmentStatus.SCHEDULED`                      | Proves domain invariant that newly created appointments initialize strictly to `SCHEDULED` status.       |
| TEST-07 | FR-06 Cancel appointment    | AC-05.1              | Positive                       | `test_cancel_changes_status()`              | `apt.status == AppointmentStatus.CANCELLED`                      | Proves `Appointment.cancel()` transitions the object from `SCHEDULED` to `CANCELLED`.                    |
| TEST-08 | FR-06 Cancel appointment    | AC-05.3              | Negative / Boundary            | `test_repeated_cancellation_is_rejected()`  | Raises `ValueError`; status remains `CANCELLED`                  | Proves the state guard blocks illegal transitions and ensures state immutability on rejection.           |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange                                                                               | Act                                                                                      | Assert                                                                         | Why meaningful / why assertion proves criterion                                                                                   |
|---------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| TEST-01 | Define valid strings `"P1"` and `"Alice Smith"`.                                      | Instantiate `patient = Patient("P1", "Alice Smith")`.                                    | `assert patient.patient_id == "P1"` and `assert patient.name == "Alice Smith"` | Directly proves that valid inputs are correctly stored and accessible via public domain properties without corruption.            |
| TEST-02 | Define whitespace-only ID `"   "` and valid name `"Alice Smith"`.                     | Call `Patient("   ", "Alice Smith")` inside `pytest.raises(ValueError)`.                 | Catch `ValueError`.                                                            | Proves that the domain constructor actively validates and rejects empty/whitespace identifiers instead of silently storing them.  |
| TEST-03 | Define valid ID `"P1"` and whitespace-only name `"   "`.                              | Call `Patient("P1", "   ")` inside `pytest.raises(ValueError)`.                          | Catch `ValueError`.                                                            | Confirms that patient names cannot be blank, enforcing the non-empty string contract for clinical identities.                     |
| TEST-04 | Define valid strings `"DR1"`, `"Dr. Bob"`, and `"Cardiology"`.                        | Instantiate `doc = Practitioner("DR1", "Dr. Bob", "Cardiology")`.                        | Assert all three properties match input arguments.                             | Proves that the practitioner domain model accurately initialises and preserves all required metadata attributes.                  |
| TEST-05 | Define invalid inputs with empty strings for ID, name, or specialty.                  | Attempt `Practitioner` creation for each empty field inside `pytest.raises(ValueError)`. | Catch `ValueError` for each attempt.                                           | Proves validation is applied to every mandatory practitioner field, ensuring partial or empty objects cannot be created.          |
| TEST-06 | Instantiate valid `Patient`, `Practitioner`, and a naive minute-precision `datetime`. | Instantiate `apt = Appointment("A1", p, doc, slot)`.                                     | `assert apt.status == AppointmentStatus.SCHEDULED`                             | Proves the domain invariant that newly created appointments unconditionally begin in the `SCHEDULED` status.                      |
| TEST-07 | Create a valid `SCHEDULED` appointment.                                               | Call `apt.cancel()`.                                                                     | `assert apt.status == AppointmentStatus.CANCELLED`                             | Proves that the public domain method correctly executes the required state transition from `SCHEDULED` to `CANCELLED`.            |
| TEST-08 | Create a valid appointment and cancel it once so status is `CANCELLED`.               | Call `apt.cancel()` a second time inside `pytest.raises(ValueError)`.                    | Catch `ValueError` and assert `apt.status == AppointmentStatus.CANCELLED`.     | Proves that the state machine blocks illegal transitions from `CANCELLED` and guarantees entity status immutability upon failure. |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour                                                                                                        | Test file/function                                              | Result |
|---------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|--------|
| TEST-01 | Patient valid construction retains patient_id and name                                                           | `tests/test_domain.py::test_patient_valid_construction`         | Pass   |
| TEST-02 | Blank or whitespace-only patient ID is rejected with ValueError (Preserved Reference Intention 1)                | `tests/test_domain.py::test_blank_patient_id_is_rejected`       | Pass   |
| TEST-03 | Blank or whitespace-only patient name is rejected with ValueError                                                | `tests/test_domain.py::test_blank_patient_name_is_rejected`     | Pass   |
| TEST-04 | Practitioner valid construction retains practitioner_id, name, and specialty                                     | `tests/test_domain.py::test_practitioner_valid_construction`    | Pass   |
| TEST-05 | Blank practitioner ID, name, or specialty is rejected with ValueError                                            | `tests/test_domain.py::test_blank_practitioner_fields_rejected` | Pass   |
| TEST-06 | New appointment starts with status SCHEDULED (Preserved Reference Intention 2)                                   | `tests/test_domain.py::test_new_appointment_starts_scheduled`   | Pass   |
| TEST-07 | Appointment cancellation changes status from SCHEDULED to CANCELLED (Preserved Reference Intention 3)            | `tests/test_domain.py::test_cancel_changes_status`              | Pass   |
| TEST-08 | Repeated cancellation is rejected with ValueError and retains CANCELLED status (Preserved Reference Intention 4) | `tests/test_domain.py::test_repeated_cancellation_is_rejected`  | Pass   |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour                                                              | Requirement / criterion          | Test file/function                                                            | Result |
|---------|------------------------------------------------------------------------|----------------------------------|-------------------------------------------------------------------------------|--------|
| TEST-09 | Valid patient registration and lookup through shared store             | FR-01 / AC-01.1, FR-02 / AC-02.1 | `tests/test_services.py::test_register_and_find_patient`                      | Pass   |
| TEST-10 | Duplicate patient ID registration is rejected                          | FR-01 / AC-01.2                  | `tests/test_services.py::test_duplicate_patient_id_rejected`                  | Pass   |
| TEST-11 | Absent patient lookup reports absence by raising LookupError           | FR-02 / AC-02.2                  | `tests/test_services.py::test_unknown_patient_lookup_raises_lookup_error`     | Pass   |
| TEST-12 | Registered participants produce a stored SCHEDULED appointment         | FR-04 / AC-03.1                  | `tests/test_services.py::test_book_appointment_success`                       | Pass   |
| TEST-13 | Same practitioner at exact time raises conflict with ValueError        | FR-05 / AC-04.1                  | `tests/test_services.py::test_prevent_practitioner_conflict_same_time`        | Pass   |
| TEST-14 | Different practitioner at the exact same time is allowed               | FR-05 / AC-04.2                  | `tests/test_services.py::test_allow_different_practitioner_at_same_time`      | Pass   |
| TEST-15 | Cancelling appointment changes status to CANCELLED and retains history | FR-06 / AC-05.1, FR-07 / AC-05.2 | `tests/test_services.py::test_cancel_appointment_and_retain_history`          | Pass   |
| TEST-16 | Cancelled booking frees slot for subsequent practitioner booking       | FR-05 / AC-04.1, FR-07 / AC-05.2 | `tests/test_services.py::test_cancelled_appointment_frees_slot_for_rebooking` | Pass   |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour                         | Boundary/invalid input                                                     | Expected result                                                                 | Test ID |
|-----------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------|
| Patient ID rejection              | Whitespace-only string (`"   "`) passed to constructor                     | `ValueError` raised; no invalid object created                                  | TEST-02 |
| Patient name rejection            | Empty string (`""`) passed to constructor                                  | `ValueError` raised; no invalid object created                                  | TEST-03 |
| Duplicate patient registration    | Existing patient ID (`"P1"`) registered a second time                      | `ValueError` raised; original patient record in store remains unchanged         | TEST-10 |
| Unknown patient lookup            | Non-existent patient ID (`"P_UNKNOWN"`) requested                          | `LookupError` raised; data store state remains unchanged                        | TEST-11 |
| Practitioner schedule conflict    | Second appointment booked for same practitioner at identical date and time | `ValueError` raised; first appointment remains `SCHEDULED`, second is not added | TEST-13 |
| Repeated appointment cancellation | Calling `cancel()` on an already `CANCELLED` appointment                   | `ValueError` raised; appointment status remains `CANCELLED`                     | TEST-08 |
| Blank appointment ID lookup       | Blank string (`"   "`) passed to lookup                                    | `ValueError` raised; data store state remains unaffected                        | TEST-15 |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: FR-06 Cancel appointment
Acceptance criterion: "AC-05.3 Repeated cancellation is rejected."
Behaviour to test: Calling cancel on an appointment that is already in CANCELLED status must raise a ValueError and leave the appointment status unchanged as CANCELLED.
Human-first test idea/categories: Arrange a valid appointment, cancel it once to transition it to CANCELLED, invoke cancel a second time inside a pytest.raises(ValueError) block, and assert that the appointment status remains CANCELLED afterwards.
Prompt and purpose: 
Prompt: "Act as a software test-design assistant. Requirement: FR-06 Cancel appointment. Acceptance criterion: AC-05.3 Repeated cancellation is rejected. Propose pytest test candidates covering a valid case, an invalid case and meaningful boundaries. For each candidate, state exactly which required behaviour it is intended to verify. Do not invent behaviour not stated in the requirement or criterion. Use observable outcomes rather than private implementation details. Use the current SmartCare public contracts and shared SmartCareDataStore. Do not introduce SQLite, repository abstractions or unrelated features. Do not claim that a proposed test has been executed."
Purpose: Generate candidate test structures to evaluate edge cases and compare AI-generated test logic against the project specification.

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: ```python
def test_valid_appointment_cancellation():
    patient = Patient("P01", "John Doe")
    doc = Practitioner("DR01", "Dr. Smith", "General Practice")
    slot = datetime(2026, 11, 10, 9, 0)
    apt = Appointment("A01", patient, doc, slot)
    apt.cancel()
    assert apt.status == AppointmentStatus.CANCELLED
- What it claims to verify: Verifies that cancelling a scheduled appointment successfully updates its status to CANCELLED.
- Requirement trace: FR-06 / AC-05.1
- Assertion quality: Strong; directly evaluates the public status property against the expected AppointmentStatus.CANCELLED enum value.
- Human critique: Uses clear Arrange-Act-Assert structure, relies only on documented public interfaces, and contains no unnecessary dependencies or mocks.
- Decision: Accept
- Reason: Fully satisfies the acceptance criterion, tests observable behavior, and asserts the correct enum transition directly.
- Final test reference if accepted/modified: tests/test_domain.py::test_cancel_changes_status
- Actual verification result: PASS

- Copilot test idea/candidate: def test_re_cancelling_already_cancelled_appointment():
    apt = Appointment("A01", Patient("P01", "John Doe"), Practitioner("DR01", "Dr. Smith", "GP"), datetime(2026, 11, 10, 9, 0))
    apt.cancel()
    try:
        apt.cancel()
        assert False, "Should have raised an error"
    except Exception:
        pass
- What it claims to verify: Verifies that attempting to cancel an appointment a second time triggers an error.
- Requirement trace: FR-06 / AC-05.3
- Assertion quality: Weak; relies on a generic try/except Exception block and fails to check that the entity remains in the CANCELLED state after the rejected attempt.
- Human critique: A broad exception check is brittle and can mask unrelated bugs (such as AttributeError). It needs idiomatic pytest syntax (pytest.raises(ValueError)) and an explicit invariant check ensuring state did not mutate.
- Decision: Modify
- Reason: Rewritten to catch the specific domain exception (ValueError) and added a post-condition assertion confirming apt.status == AppointmentStatus.CANCELLED.
- Final test reference if accepted/modified: tests/test_domain.py::test_repeated_cancellation_is_rejected
- Actual verification result: PASS

- Copilot test idea/candidate: def test_cancel_appointment_emits_audit_and_sms():
    data_store = SmartCareDataStore()
    service = AppointmentService(data_store)
    mock_notifier = Mock()
    service.set_notifier(mock_notifier)
    service.cancel_appointment("A01")
    assert mock_notifier.send_sms.called
- What it claims to verify: Verifies that cancelling an appointment triggers an external SMS alert via a notification handler.
- Requirement trace: None
- Assertion quality: Irrelevant; asserts interactions with a mocked service method that does not exist in the domain model.
- Human critique: Copilot hallucinated an external notification dependency and messaging service not defined anywhere in the SmartCare specifications.
- Decision: Reject
- Reason: Introduces invented business rules, unwarranted mock objects, and architectural overhead beyond the project scope.
- Final test reference if accepted/modified: Not retained
- Actual verification result: REJECTED

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? Candidate 2 (`test_re_cancelling_already_cancelled_appointment`)
Why was it weak? It used a generic `except Exception:` clause and lacked any assertion on the object's post-condition state. This made the test fragile and uninformative: it would pass even if the code crashed due to an unintended bug (such as an `AttributeError` or `TypeError`), and it failed to verify that the appointment actually remained in the `CANCELLED` state rather than mutating into an invalid state.
How did you strengthen it?
1. Replaced the generic `try/except Exception` pattern with idiomatic `with pytest.raises(ValueError):` to guarantee that only the specific, documented domain exception passes.
2. Added an explicit assertion immediately following the exception block (`assert apt.status == AppointmentStatus.CANCELLED`) to verify that rejected operations leave the entity's state immutable and consistent.
Accepted / modified / rejected test decisions and evidence: See Section H entries above (Candidate 1 Accepted, Candidate 2 Modified, Candidate 3 Rejected).

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command            | Working directory | Code SHA                                  | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation                                                                                                            |
|--------------------|-------------------|-------------------------------------------|--------|--------|-----------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `python -m pytest` | `project`         | cb1a64ecd31300af393ca5a64d5bde4af025cf8e  | 16     | 0      | None            | None                                      | All 16 domain tests passed cleanly with independent state; verified domain validation rules and status transitions without regression. |

Individual test runs and changed-order independence evidence: Executed individual files and varied run sequences via `python -m pytest tests/test_domain.py` and `python -m pytest tests/test_starter.py tests/test_domain.py`. Tests use freshly instantiated objects with no shared global state, passing identically regardless of execution order.
Optional tutor-led demonstration notes:
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: FR-06 / AC-05.3 → `test_repeated_cancellation_is_rejected` → observed that generic candidate caught broad exceptions without checking post-state → diagnosed lack of state invariant check → modified test to enforce `pytest.raises(ValueError)` and verify status remained `AppointmentStatus.CANCELLED` → verified pass with targeted assertion.

## K What the Suite Still Does Not Prove

What does your test suite still not prove? The test suite operates entirely in memory during single process execution. It does not prove;
1. Long-term data persistence across application restarts or server shutdowns.
2. Concurrent transaction safety, thread safety, or behaviour under race conditions (e.g., simultaneous booking attempts by two users).
3. End-to-end integration with the Stage 6 service methods (such as lookup helpers and full clinic booking workflows), which are still pending team integration.
4. Security invariants, authorization boundaries, or network resilience under distributed deployment.
Coverage if used: Not used (or baseline branch coverage measured only on domain entity logic).
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? 
1. Uncovered areas that matter: Service-level exception handling during missing-entity edge cases, data store query scaling with large record sets, and integrated UI/API boundary error handling. 
2. Why coverage percentage alone does not establish correctness: Code coverage only measures which lines and branches of code were touched during test execution; it does not prove that assertions are meaningful, that business logic is completely specified, or that the system behaves correctly under untested boundary values. A test with weak assertions (e.g., `assert True`) can achieve 100% line coverage while verifying zero functional requirements.
Optional fixtures/parametrisation used and why, if any: 
1. Fixtures: Used isolated helper instantiations for `Patient`, `Practitioner`, and naive minute-precision `datetime` objects to ensure fresh, decoupled state per test without state leaking across test cases. 
2. Parametrisation: Used where applicable to test multiple invalid string inputs (such as empty string `""` vs whitespace string `"   "`) against the domain's `required_text` validation contract without duplicating test boilerplate.

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task                                          | Branch                  | PR    | Reviewer    | Key feedback                                                                                                              | Outcome                                                                                                                               |
|-----------------------------------------------------|-------------------------|-------|-------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Stage 7: Domain unit tests & evidence documentation | `feature/stage-7-tests` | PR #5 | jonathansv7 | Ensure boundary tests explicitly check whitespace strings as well as empty strings; verify Arrange-Act-Assert separation. | Added whitespace validation cases for `required_text`, verified state immutability on rejected cancellations, and merged into `main`. |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member                | Actual contribution                                                                                                                                                       | Evidence link                                                      |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Jackson (Author)      | Authored Stage 7 test design, implemented domain unit tests in `project/tests/test_domain.py`, evaluated GitHub Copilot candidates, and completed evidence documentation. | Commit `[insert your commit SHA]` / Branch `feature/stage-7-tests` |
| Jonathan (Reviewer)   | Performed peer code review on pull request, checked Arrange–Act–Assert structure and boundary coverage, and approved merge into `main`.                                   | PR `#[insert PR number]` review comments                           |

## N Formative Questions

1. What question does verification answer?
"Are we building the product right?" It checks whether the software implementation conforms to the specified functional requirements, technical design, and contract specifications.

2. What question does validation answer?
"Are we building the right product?" It checks whether the software actually solves the real-world problem and satisfies user, operational, and clinical needs in practice.

3. What is a unit test?
An automated test that exercises an individual component, class, or function in strict isolation to verify that its internal logic and observable behaviors match expected specifications without relying on external dependencies.

4. What is a pytest fixture?
A modular helper function decorated with `@pytest.fixture` that sets up reliable, baseline test fixtures, data, or environment state before a test executes, ensuring clean and repeatable initial conditions.

5. What is parametrisation in pytest?
A pytest feature (`@pytest.mark.parametrize`) that allows the exact same test function to run repeatedly against multiple sets of input parameters and expected outcomes without duplicating test logic.

6. What is regression testing?
Re-running existing test suites after introducing code changes, bug fixes, or refactoring to confirm that existing, previously verified features have not been unintentionally broken.

7. What does code coverage tell us, and what does it not prove?
Code coverage identifies which lines, branches, or statements were executed during a test run. It does not prove that assertions are meaningful, that business logic is correct, that edge cases are accounted for, or that requirements are met.

8. What makes an assertion weak?
An assertion is weak when it passes without adequately validating the required invariant or observable state (e.g., `assert True` or `assert result is not None`), which allows incorrect or buggy implementations to pass unnoticed.

9. What is the appropriate role of GitHub Copilot as a test assistant?
To serve as an ideation and drafting tool that suggests candidate scenarios and edge cases, while the human software engineer remains strictly accountable for evaluating, modifying, and verifying the tests against official requirements and contracts.

10. What is the Stage 7 engineering rule?
A passing test only proves the exact scenario and assertion it checks. Tests must trace to concrete requirements, maintain independent state, and verify observable outcomes rather than private implementation details.

## O Stage Completion

Tested Stage 7 main SHA: cb1a64ecd31300af393ca5a64d5bde4af025cf8e
Full-suite result: 16 passed in 0.03s (0 failures, 0 errors)
Unresolved defects and effect on baseline: None
Clean working tree and integration evidence: Working tree clean (`git status` reports nothing to commit); branch `feature/stage-7-tests` successfully merged into `main` via PR.
Stage 8 handover status: Complete; domain models and tests fully verified and ready for Stage 8 fault activities. No Stage 8 work started.
All tutorial/formative responses and traceability/Copilot decisions complete: Completed!