# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Wed 4:30 - 6:30 Group 5
Members and UG/PG cohorts: Jonathan (jonathansv7), Jackson (JacksonSu3319170), Ayaz (AyazMohammed999), all UG
Record owner / contribution links for each member: Ayaz (AyazMohammed999) – Stage 8 owner. Contribution links will be added after the PR is merged.

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason:

- Appointment disappears after cancellation: Symptom. This is just what we noticed going wrong. It tells us something's broken but not why.
- The data-store removal path is probably being called: Hypothesis. It's a guess about what might be causing the problem, and we can test it. We'd need to check it against our actual code though, since the project doesn't have a public delete method.
- The failing test shows store.find_appointment('A1') returns None: Evidence. This is a real result from running a test, so it's something we can actually point to and check.
- The service layer is badly designed: Opinion. It's more of a personal judgement. It doesn't say what's actually wrong, so there's nothing specific we can test.
- Traceback points to smartcare/services.py line 42 in the example: Evidence. It's a fact from the error message, but it only shows where the error popped up, not what actually caused it.

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: 

- Scenario: I picked the cancelled appointment history scenario.
- Expected behaviour: Once appointment A1 is cancelled, we should still be able to find it with the status CANCELLED. FR-07 says cancelled appointments need to stay in the history.
- Observed behaviour: After cancelling A1, store.find_appointment('A1') returns None, so the appointment has basically disappeared.
- Minimal reproduction: Register patient P1 and practitioner DR1, book appointment A1, cancel it, then try to find A1 again.
- Initial hypothesis: My first guess is that the data store is deleting the appointment when it gets cancelled, instead of just changing its status.
- Evidence to inspect: I'd check the save and update methods in data_store.py, the cancel_appointment method in services.py, what the failing test actually outputs, and what's still stored after the cancellation.
- Note: I'll keep this first hypothesis in the record even if it turns out to be wrong later on.

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: 

- Cancelled appointments test: The test is the problem here, not the code. FR-07 says cancelled appointments have to stay in the history, so a test expecting them to be deleted is checking for the wrong thing. The test should be changed so it checks that the cancelled appointment can still be found with the status CANCELLED. Changing the code to delete appointments would just break the actual requirement.
- Different practitioners at the same time: This test doesn't match AC-04.2 either. AC-04.2 says a different practitioner at the same time is allowed. A conflict only happens when it's the same practitioner, at the exact same time, with an existing SCHEDULED appointment. So this test should be fixed to expect the booking to go through.
- Overall: Not every failing test is right. A test is only useful if it matches the requirement, so you have to check the requirement before deciding whether to change the code or the test.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: 

- Smells: The method is way too long at 70 lines and does too many things at once. It has duplicate status strings instead of using the existing enum, it changes the collections directly instead of going through SmartCareDataStore, it prints output even though printing belongs in the console, it mixes validation in with everything else, and it has four nested conditionals which make it hard to read and follow.
- Small refactorings: Pull the validation out into its own small helper, replace the status strings with the existing AppointmentStatus enum, use the SmartCareDataStore methods instead of touching the collections directly, remove the printing so the method just returns a result or raises an error, and use early returns to flatten out the nested ifs. None of these need any new architecture.
- Rename appt to appointment: Refactoring. It just makes the code easier to read.
- Extract a repeated conflict helper: Refactoring. It removes duplicate code without changing what it does.
- Add rescheduling: Feature. It's brand new behaviour, so it isn't part of a refactor.
- Restore retained cancellation lookup: Repair. It fixes broken behaviour so FR-07 works again.
- Replace a magic status string with the existing enum: Refactoring. The value stays the same, it's just cleaner and safer.
- Behaviour that must stay the same: The method should still return the same stored objects, raise the same ValueError and LookupError cases, keep cancelled appointments stored with the status CANCELLED, and follow the same conflict rule. All the existing tests should pass before and after the refactor.

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:

- Failure I used: tests/test_appointment_cancellation.py::test_cancelled_appointment_remains_stored
- What failed: It threw LookupError: Appointment not found. The line that failed was line 45 in the test, assert service.find_appointment("A1") is appointment.
- Expected vs what actually happened: I expected to get the same A1 appointment back with its status as CANCELLED. Instead I just got a LookupError and nothing came back.
- How the error got there: The test asks AppointmentService to find A1, and the service then asks the data store for it. The data store gives back None, so the service throws the LookupError at line 140 in services.py.
- Requirement it breaks: FR-07 (AC-05.2) says cancelled appointments have to stay in the history, and FR-06 (AC-05.1) says cancelling should change the status to CANCELLED.
- My three guesses, from most to least likely:
  1. The data store's find_appointment is skipping cancelled appointments. To check, I'd cancel A1 and then compare list_appointments() with find_appointment('A1'). If A1 shows up in the list but can't be found, the lookup is the problem.
  2. Cancelling is removing or replacing A1 in the store. To check, I'd see if A1 is still in list_appointments() after cancelling, and whether it's the same object as before.
  3. The ID isn't matching because of spaces or capital letters. To check, I'd try finding A1 before cancelling it. If that works, the ID is fine.
- Why the traceback isn't enough on its own: The traceback points to line 140 in services.py, but that line only throws the error because the data store handed back None. So it tells you where the error showed up, not why the data store couldn't find A1. You still have to look at data_store.py and actually test it to find the real cause.

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: 

Changing the code as soon as you see a failure is kind of like guessing. You might fix the thing you can see, but not the real problem behind it. You could also break something that was already working. And sometimes the test is the thing that's wrong, not the code, so you'd just be making it worse. I think it's better to slow down a bit, figure out how to make the problem happen again, write down what I think is causing it and check that first. Then I can make a small fix and actually prove it worked.


Classification responses (1–5, each with reason): See A.1 above.
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: See A.2 above.
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: See A.5 above.

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: 22d9bfb7df2a385abfd74bbf7ca1595384ca6a3f. This is main after the Stage 7 tests PR was merged, and it's our passing baseline for FR-01 to FR-07.
- Baseline test command / working directory / observed result / evidence: I ran python -m pytest -q from project/ on main and got 44 passed in 0.17s.
- Clean preparation SHA if a record-only commit followed Stage 7: Not applicable. The preparation started straight from the Stage 7 main SHA above.
- Branch and preparer / how teammates obtained this branch: The branch is debug/stage08 and it was prepared by our tutor, Pranav. Each of us got it by running git fetch origin and then git switch --track origin/debug/stage08.
- Downloaded tool version, source SHA256 and --check outcome: We didn't get the tool ourselves because it's staff-controlled. Pranav ran preparation utility version 1.1 himself, so we don't have the SHA256 or the --check output.
- --apply and --verify output summaries / artefact references: Pranav ran these. In his email he confirmed the verification passed and both expected debugging symptoms were added correctly.
- Bounded diff inspected and recovery location (not committed): git diff --stat 22d9bfb 029e78b shows only one file was changed, project/smartcare/data_store.py (11 insertions, 18 deletions). Nothing else was touched. The recovery files are kept by teaching staff and were never in our repo.
- Prepared faulty-state commit SHA: 029e78b3314f41b336b0778a1ee6f17782ad8acb
- Preparation or recovery issues and resolution, if any: None of us could make the in-person session, so Pranav did the preparation remotely. Jackson added him as a temporary collaborator, he pushed debug/stage08, and his access was removed afterwards. main stayed the same.
- Initial prepared full-suite command / result / key failures: I ran python -m pytest -q from project/ on debug/stage08 and got 3 failed, 41 passed in 0.40s. The failures were test_cancelled_appointment_remains_stored and test_cannot_cancel_twice (both LookupError: Appointment not found), and test_conflict_rule_and_different_practitioner (DID NOT RAISE ValueError).

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: After an appointment gets cancelled, trying to look it up again gives LookupError: Appointment not found. So the cancelled appointment basically disappears.
- Expected behaviour and requirement: The appointment should still be stored and found with the status CANCELLED. FR-06 (AC-05.1) says cancelling changes the status to CANCELLED, and FR-07 (AC-05.2) says cancelled appointments have to stay in the history.
- Minimal synthetic reproduction steps: Register patient P1 and practitioner D1, book appointment A1, cancel A1, then try to find or cancel A1 again. It raises LookupError instead of finding it.
- Meaningful failing test path/name and exact relevant failure: tests/test_appointment_cancellation.py::test_cancelled_appointment_remains_stored and tests/test_appointment_cancellation.py::test_cannot_cancel_twice. Both fail with LookupError: Appointment not found, raised at smartcare/services.py line 140.
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: find_appointment in data_store.py had an extra condition, appointment.status.value != "cancelled", so it skipped over any cancelled appointment. My check script showed A1 was still in list_appointments() after cancelling, but find_appointment('A1') returned None. So it was hidden, not deleted. Copilot's top suggestion agreed once I checked it against this.
- Smallest justified fix / diff / why other behaviour is preserved: I removed just that one status condition, so find_appointment matches on the ID only. It still rejects blank IDs with ValueError, still returns the same stored object, and still returns None for unknown IDs (so the service still raises LookupError). Nothing else in the file was changed.
- Repair SHA / focused verification result: f2e6e19. python -m pytest -q tests/test_appointment_cancellation.py tests/test_stage8_regressions.py::test_data_store_still_finds_cancelled_appointment from project/ gave 11 passed.

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: Booking the same practitioner at the exact same time goes through when it should be blocked.
- Expected behaviour and requirement: FR-05 (AC-04.1) says booking the same practitioner, at the exact same time, while there's already a SCHEDULED appointment, should raise ValueError. AC-04.2 says a different practitioner at the same time is still allowed.
- Minimal synthetic reproduction steps: Register patient P1 and practitioners D1 and D2, book A1 for P1 with D1 at 2026-10-01 09:00, then try to book another appointment with D1 at the same time. No error is raised.
- Meaningful failing test path/name and exact relevant failure: tests/test_starter.py::test_conflict_rule_and_different_practitioner fails at line 127 with Failed: DID NOT RAISE <class 'ValueError'>.
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: has_practitioner_conflict in data_store.py used != instead of == when comparing the practitioner ID, so it looked for clashes with every other practitioner instead of the same one. My check script showed it returned False for D1 (should be True) and True for D2 (should be False).
- Smallest justified fix / diff / why other behaviour is preserved: I changed that one != to ==. Everything else in the check stayed the same. It still needs the exact same time, still only counts SCHEDULED appointments (so cancelled ones free up the slot), and still respects the excluded appointment ID.
- Repair SHA / focused verification result: 946dfe1. python -m pytest -q tests/test_starter.py::test_conflict_rule_and_different_practitioner tests/test_stage8_regressions.py::test_different_practitioner_same_time_is_allowed from project/ gave 2 passed.

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: I think something in data_store.py is losing or hiding the appointment after it's cancelled. Maybe find_appointment only returns appointments that are still SCHEDULED, or the cancelled appointment isn't saved back properly. This makes sense because the prep only changed data_store.py, and the error happens straight after cancelling.
Evidence intended to inspect / competing explanation / discriminating check: I'll check find_appointment and how appointments are saved in data_store.py. Another possibility is that cancel_appointment in services.py is removing it, but that file wasn't changed by the prep. To tell them apart, I'll book and cancel A1, then check if A1 is still in the store's appointments collection. If it's still there, the lookup is the problem. If it's gone, the saving or removal is the problem.
Member and saved sequence/time or commit showing this preceded consultation: Ayaz, recorded and committed before using Copilot (see commit "Record Stage 8 baseline, symptoms and human hypotheses")

### F8-02 human entry
Likely cause and why plausible: I think has_practitioner_conflict in data_store.py isn't detecting the clash properly. It might be comparing the wrong thing, like the patient instead of the practitioner, or checking for the wrong status. This fits because the booking just goes through with no error, and the prep only changed data_store.py.
Evidence intended to inspect / competing explanation / discriminating check: I'll look at has_practitioner_conflict in data_store.py. Another possibility is that book_appointment in services.py isn't calling the check at all, but services.py wasn't changed. To tell them apart, I'll book A1 with D1 at 09:00 and then call has_practitioner_conflict directly for D1 at the same time. If it returns False, the check itself is broken.
Member and saved sequence/time or commit showing this preceded consultation: Ayaz, recorded and committed before using Copilot (see commit "Record Stage 8 baseline, symptoms and human hypotheses")

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: Ayaz used the exact handout prompt structure in GitHub Copilot Chat on github.com, after committing Section E. This was the first prompt in the chat: https://github.com/copilot/c/22622eeb-e466-4c90-a934-e9fb6c9a72b0
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: find_appointment skips cancelled appointments. I checked the code and ran a quick script. A1 was still in list_appointments() but find_appointment('A1') returned None, and the code has the condition status.value != "cancelled". Correct. Accept, because the code and the runtime result both back it up.
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: The code being run might be different from the code I inspected. Copilot said this because it looked at my old Assignment 2 repo instead of our group repo. The traceback points to this project's smartcare/services.py, and git diff --stat shows data_store.py is the file the prep changed. Wrong. Reject, because it was based on the wrong repository.
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: The appointment ID might not match exactly. The stored ID is exactly 'A1', and A1 can be found fine before it's cancelled. It only goes missing after cancelling. Wrong. Reject, because the problem depends on the status, not the ID.
Final human conclusion and comparison with initial hypothesis: The root cause is the status filter in find_appointment, which hides cancelled appointments even though they're still stored. This matches my Section E hypothesis that find_appointment only returns non-cancelled appointments. It's different from my A.2 tutorial guess that the appointment was being deleted, since it's actually still there, just hidden.

### F8-02 Copilot review
Actual prompt / output reference and member: Ayaz used the exact handout prompt structure in GitHub Copilot Chat on github.com, after committing Section E. This was the second prompt in the same chat: https://github.com/copilot/c/22622eeb-e466-4c90-a934-e9fb6c9a72b0
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: The practitioner check uses != instead of ==. The code has appointment.practitioner.practitioner_id != practitioner_id, and my script showed has_practitioner_conflict returned False for D1 (should be True) and True for D2 (should be False). I also checked that book_appointment in services.py raises ValueError when the check returns True, so the caller is fine. Correct. Accept.
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: The two checks might have used different data or exclusions. Both checks ran straight after each other on the same store, with only A1 booked and no excluded ID. Wrong. Reject.
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: The IDs or status values might not match. The IDs are exact strings and A1's status value really is 'scheduled'. Wrong as a cause, so reject. While checking this, I noticed that "scheduled" is hardcoded as a string instead of using AppointmentStatus.SCHEDULED, which I've noted as a possible refactor.
Final human conclusion and comparison with initial hypothesis: The root cause is the inverted != comparison in has_practitioner_conflict. It flags a different practitioner as a clash and misses the same practitioner. This matches my Section E hypothesis that it was comparing the wrong thing. The evidence also showed a second effect I hadn't spotted: a different practitioner at the same time gets wrongly blocked, which breaks AC-04.2 and isn't caught by any current test.

## G. Failing to passing regression evidence 

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | bc543d3 (regression tests added, no fixes yet) | python -m pytest -q from project/ | 5 failed, 41 passed. F8-01 failures: test_cancelled_appointment_remains_stored and test_cannot_cancel_twice (LookupError), and test_data_store_still_finds_cancelled_appointment (assert None is appointment) |
| F8-01 after repair | f2e6e19 | python -m pytest -q tests/test_appointment_cancellation.py tests/test_stage8_regressions.py::test_data_store_still_finds_cancelled_appointment from project/ | 11 passed |
| F8-02 before repair | bc543d3 (the conflict check code didn't change until 946dfe1) | python -m pytest -q from project/ | F8-02 failures: test_conflict_rule_and_different_practitioner (DID NOT RAISE ValueError) and test_different_practitioner_same_time_is_allowed (ValueError: Practitioner already has a SCHEDULED appointment) |
| F8-02 after repair | 946dfe1 | python -m pytest -q tests/test_starter.py::test_conflict_rule_and_different_practitioner tests/test_stage8_regressions.py::test_different_practitioner_same_time_is_allowed from project/ | 2 passed |
| Full suite after both repairs, before refactor | 946dfe1 | python -m pytest -q from project/ | 46 passed in 0.16s |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: For F8-01, test_data_store_still_finds_cancelled_appointment checks that the store returns the exact same appointment object (using is) and that its status is CANCELLED. So if the appointment gets hidden, replaced or not cancelled properly, the test fails. For F8-02, test_different_practitioner_same_time_is_allowed checks that a second practitioner at the same time actually gets booked and stays SCHEDULED, which catches the wrong blocking that no test picked up before. The existing starter test still checks that the same practitioner at the same time raises ValueError. All 44 original tests still pass, so the fixes didn't break anything that already worked.
Unrelated failures investigated / resolution: Not applicable. The only failures were the 3 caused by the prepared defects and my 2 new regression tests, and all 46 tests pass after both fixes.


## H. Refactoring decision and before/after verification

Smell and exact location: Magic status string in has_practitioner_conflict in project/smartcare/data_store.py. It checks appointment.status.value == "scheduled" using a hardcoded string instead of the AppointmentStatus enum that's already imported at the top of the file.
Small proposed structural change / why justified: Change it to appointment.status == AppointmentStatus.SCHEDULED. It's safer because a typo in a string wouldn't be caught, but a typo in the enum name would throw an error straight away. It also matches how the rest of the project uses statuses. It's one line and doesn't add anything new.
External behaviour to preserve / relevant tests: The conflict rule has to stay exactly the same. Same practitioner, same exact time, existing SCHEDULED appointment means a conflict, while a different practitioner or a cancelled appointment doesn't count. Relevant tests are test_conflict_rule_and_different_practitioner, test_different_practitioner_same_time_is_allowed, and the cancelled-slot tests, plus the full suite.
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: 8e9298d. In has_practitioner_conflict, I changed appointment.status.value == "scheduled" to appointment.status == AppointmentStatus.SCHEDULED. That's the only line that changed.
Focused and full after-refactor commands / working directory / results / evidence: From project/, python -m pytest -q tests/test_starter.py::test_conflict_rule_and_different_practitioner tests/test_stage8_regressions.py::test_different_practitioner_same_time_is_allowed gave 2 passed, and python -m pytest -q gave 46 passed in 0.16s. My first two attempts at the change had typos (SCHEDULED without AppointmentStatus, then a wrong attribute), and both times the full suite failed straight away with 1 failed, 45 passed. I fixed the line and reran before committing.
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: Accepted after revising. The final change gives the exact same results as before, with the same 46 tests passing as before the refactor. So the conflict rule works exactly the same, it's just clearer and safer now.

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? Copilot's second suggestion for F8-01, that the code being run might be different from the code I looked at. It sounded smart and careful, but it only said that because it looked at my old Assignment 2 repo instead of our group repo. Once I checked the traceback and git diff, it was clear the code being run was exactly what I was looking at. It did the same thing again for F8-02, which showed me it can sound confident while looking at the completely wrong thing.

2. What evidence changed your group's view? My first guess in A.2 was that the cancelled appointment was being deleted. The check script changed that, because it showed A1 was still in list_appointments() but find_appointment('A1') returned None, so it was being hidden, not deleted. For F8-02, the script showed the conflict check returned True for a different practitioner, which revealed a second problem (AC-04.2 being broken) that none of the existing tests had caught.

3. How did regression tests protect the refactoring? They actually caught me. My first two tries at the refactor had small typos, and both times the full suite failed straight away with 1 failed, 45 passed, pointing right at the line I'd changed. Without the tests, I might have committed broken code thinking it was just a harmless clean-up. I only committed once all 46 passed again.

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: 

Honestly, the main thing is to not just jump in and start changing code. I'd try to get the bug to happen again first so I know what I'm dealing with. Then I'd write down what was supposed to happen, what actually happened, and what I reckon is causing it. Once I've checked that against the evidence, then I'd start fixing.

2. Where should expected behaviour come from during debugging?

Response: 

It should come from the requirements. For example, FR-07 says cancelled appointments have to stay in the history, so that's what I'd go by. I wouldn't just trust what the code or the tests are doing, because either one could be the thing that's actually wrong.

3. What is a debugging hypothesis?

Response: 

It's pretty much my best guess about what's causing the bug, but it has to be something I can actually test. I write it down before I fix anything, then check if the evidence backs it up. If I end up being wrong, that's okay, I still keep it in the record and just add what I actually found.

4. What is a regression test and why is it retained?

Response: 

It's a test we keep after fixing a bug so the same bug doesn't come back. The code keeps changing, and it's easy to break something again without noticing. If that happens, the test fails and we know about it straight away.

5. What is meant by root cause?

Response: 

The root cause is the real reason the bug happened, not just where the error pops up. The traceback might point to one line, but the problem could've actually started somewhere else. So if I only fix the line where the error shows, the bug could still be hiding underneath.

6. What is refactoring?

Response: 

It's when you clean up the code so it's easier to read and work on, but it still does exactly the same thing. Like giving variables better names or moving repeated code into one helper. All the tests should still pass the same way after.

7. What is a swallowed exception?

Response:

It's when the code catches an error and then just ignores it. Nothing tells you anything went wrong, so it looks like everything's fine. That makes the bug really hard to find because there's no error to go off.

8. What is a code smell?

Response:

It's something in the code that seems a bit off, like a really long method, the same code copied in a few places or heaps of nested if statements. It's not always a bug, but it usually means the code is messy and could be cleaned up with some refactoring.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: 

Suggestions which have been verified. Copilot may give false suggestions and does not always know the requirements of your project. Therefore, you should check the suggestions against the code, the requirements and the tests.

10. What is the Stage 8 engineering rule?

Response: 

Diagnose before you fix. Work out what's really going on first by getting the bug to happen again and checking the evidence. Then make the smallest fix and use tests to show it works and nothing else broke.

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
