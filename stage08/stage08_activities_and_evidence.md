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

Response and reason: [complete] 

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: 

Changing the code as soon as you see a failure is kind of like guessing. You might fix the thing you can see, but not the real problem behind it. You could also break something that was already working. And sometimes the test is the thing that's wrong, not the code, so you'd just be making it worse. I think it's better to slow down a bit, figure out how to make the problem happen again, write down what I think is causing it and check that first. Then I can make a small fix and actually prove it worked.


Classification responses (1–5, each with reason): See A.1 above.
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: See A.2 above.
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: [complete]
- Baseline test command / working directory / observed result / evidence: [complete]
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [complete] | [complete] | [complete] |
| F8-01 after repair | [complete] | [complete] | [complete] |
| F8-02 before repair | [complete] | [complete] | [complete] |
| F8-02 after repair | [complete] | [complete] | [complete] |
| Full suite after both repairs, before refactor | [complete] | [complete] | [complete] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

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

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

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
