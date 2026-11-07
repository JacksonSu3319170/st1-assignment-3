# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: Wed 4:30 - 6:30 Group 5
Members and responsibilities: Jonathan (jonathansv7), Jackson (JacksonSu3319170), Ayaz (AyazMohammed999), all UG. Ayaz owns Stage 9.
Stage 8 integrated SHA, command, working directory and actual result: 68958695e23da07eb218554cc9c29237734fe0e5, python -m pytest -q from project/, 46 passed in 0.19s.

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity | Required session/domain state | We need it to register patients and find them later (FR-01/FR-02) |
| Appointment history | Required session/domain state | Cancelled ones still have to stick around (FR-07) |
| Temporary menu choice | Transient | It's just what the user picked, we don't need it after that |
| Practitioner specialty | Required session/domain state | It's part of the practitioner's details (FR-03) |
| Debug print output | Transient | It's only for us to see what's going on, it's not data |
| Appointment status | Required session/domain state | We need to know if it's scheduled, cancelled or done (FR-06/FR-07) |

What is intentionally lost on exit? Basically everything. It's all just kept in memory, so when you close the program it's all wiped. That's fine though, because we're not meant to save anything between runs.

### A2 Interface and domain data plan

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key | appointment: Appointment | tuple[datetime, str] (date, then ID) | Just gives back what to sort by. That's it | date_time and appointment_id on the Appointment |
| select_appointments | appointments: list[Appointment], practitioner_id: str, status: AppointmentStatus or None | New sorted list[Appointment] | Grabs one practitioner's appointments, and only one status if you ask for it. It doesn't check if the practitioner is real and it doesn't mess with the original list | The practitioner's ID and AppointmentStatus |
| Service listing | practitioner_id: str, status: AppointmentStatus or None | New list[Appointment] | Checks the practitioner exists first (ValueError if blank, LookupError if unknown) and that the status is valid (ValueError if not). Then gets the list from the store and runs select_appointments on it | SmartCareDataStore.find_practitioner |
| Console | Whatever the user types in | Stuff printed on screen | Reads input, turns it into the right type, calls the service and shows a proper message if something goes wrong. Then back to the menu | Just calls the services |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: Patients have an ID and a name, and practitioners have an ID, name and specialty. None of them can be blank. Appointments have an ID, the real Patient and Practitioner objects, a date_time and a status. The query just reads those fields and gives back the same appointments. I'm not adding any new fields.

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input | An appointment shouldn't be asking the user anything | Let the console ask, then the service calls cancel() |
| Service prints/reads the menu | That's the console's job, not the service's | The console does the menu. The service just does the work |
| Query sorts its source in place | .sort() changes the list you passed in | Use sorted() so you get a new list and the old one stays the same |
| Store prints Appointment saved | The store shouldn't print stuff | It should just save and return it, and let the console print. It's easier to test like that too |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: .sort() reorders the actual list and returns None. sorted() doesn't touch the original and gives you a new list, so result is not appointments, but they've got the same objects in them. To check nothing got changed, I'd save the order of IDs before running it, then check it's still the same after, and that result is not appointments. Checking the length is pointless, because sorting in place doesn't change the length.

Score-example prediction and explanation of passing the named key: I reckon ordered comes out as [('Chen', 5), ('Ali', 8), ('Bea', 8)]. Chen's lowest so he's first, and Ali and Bea are tied on 8, so it goes by name. scores stays the same, and ordered is a new list. You write key=score_key (no brackets) so sorted() can use the function on each item. If you put brackets, it runs it straight away and breaks.

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion: Cancelling just marks it as CANCELLED, it doesn't delete it, because FR-07 says we've got to keep the history. To prove it, I'd book A1, cancel it, then look it up again and make sure it's the same one with status CANCELLED. Then I'd list all the practitioner's appointments and A1 should still be there. But if I only list SCHEDULED ones, A1 shouldn't show up, since it's not scheduled anymore.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: The console is the only part that turns text the user types into proper types. For example, it changes "cancelled" into AppointmentStatus.CANCELLED and a date string into a datetime. The service only accepts a real AppointmentStatus or None, and anything else, like the plain string "scheduled", gets a ValueError instead of quietly returning nothing. The service also checks the practitioner first and then passes the registered practitioner's ID to the query, so typing " D1 " with spaces still works. The query itself just filters and sorts, and gives back a new list holding the same appointment objects.

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| QRY-01 | Appointments for D1 and D2 | select_appointments in queries.py | Only D1's appointments come back, and D2's are left out | Practitioner isolation test with D2 as the control |
| QRY-02 | Appointments that are SCHEDULED, CANCELLED and COMPLETED | select_appointments with no status, then each status | No status gives all of them. Each status gives only that kind. A status with no matches gives an empty list | Status filter tests |
| QRY-03 | Appointments at different times, plus two at the same time with different IDs | select_appointments using appointment_sort_key | Sorted by date and time, and same-time ones sorted by ID. The original list order and fields don't change | Ordering and tie-break test |
| QRY-04 | A known practitioner with no matches, an unknown ID, a blank ID, and the string 'scheduled' as a status | AppointmentService.list_practitioner_appointments in services.py | Known with no matches gives an empty list, unknown gives LookupError, blank gives ValueError, and a non-enum status gives ValueError | Service listing tests |
| FP-01 | The same inputs run twice | select_appointments | Same result both times. No globals, no printing, no input | Repeated-call test and reading the code |
| FP-02 | An empty list, an already sorted list and an unsorted list | select_appointments | Always a brand new list (result is not the source), and the objects inside don't change | New-list tests |
| FP-03 | A single appointment | appointment_sort_key | Returns (date_time, appointment_id), and sorting actually uses it | Direct key test |
| FR-07 | A1 booked and then cancelled | Service listing | A1 still shows up with no status filter, but not when filtering by SCHEDULED | Retained history workflow test |
| UI-01 | Menu inputs for a full run through | run_menu in console.py, started with main.py --interactive | Register, find, book, conflict, cancel, list and exit all work in one session | Console demo |
| UI-02 | Bad inputs like an unknown menu choice, blank or unknown IDs, a bad date or a bad status | Console | Shows an error message, nothing in the data changes, and you can keep using the menu | Console demo |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: Empty means the practitioner is real but has no matching appointments, so you just get an empty list and that's fine. Unknown means the ID looks okay but nobody's registered with it, so that's a LookupError. Invalid means the ID is blank or the status isn't a real AppointmentStatus, so that's a ValueError. Only the console turns typed words into the enum, so the service never has to guess what a string means. The lists that come back are new, but they hold the actual stored appointment objects, so checks like "is" still work. When something gets rejected, the service raises the error before changing anything, and the console catches it, shows a message and goes back to the menu, so the stored data stays exactly the same.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| QRY-01 / test_practitioner_isolation | project/smartcare/queries.py select_appointments | One list with D1 and D2 appointments. D1 gives only A1, A2, A3 and D2 gives only B1, so D2 is the control | Passed | [e0a71cc test file](https://github.com/JacksonSu3319170/st1-assignment-3/blob/e0a71cc/project/tests/test_stage9_queries.py) |
| QRY-02 / test_default_status_returns_all_statuses | queries.py select_appointments | No status given, and cancelled A2 is still in the result | Passed | Same file |
| QRY-02 / test_each_status_filter (3 cases) | queries.py select_appointments | SCHEDULED gives A1, A3. CANCELLED gives A2. COMPLETED gives an empty list. Every returned appointment has the status asked for | 3 passed | Same file |
| QRY-03 / test_equal_time_ties_break_by_id | queries.py appointment_sort_key | A1 and A2 are both at 2026-10-01 09:00, and A1 comes first because of its ID | Passed | Same file |
| FP-03 / test_sort_key_returns_date_time_then_id | queries.py appointment_sort_key | The key for A1 is exactly (2026-10-01 09:00, 'A1') | Passed | Same file |
| FP-03 / test_named_key_reuse_matches_query_order | queries.py appointment_sort_key | sorted() with the same named key gives the same order as the query | Passed | Same file |
| FP-02 / test_source_order_and_fields_unchanged | queries.py select_appointments | The source IDs, dates and statuses are the same before and after, and result is not source | Passed | Same file |
| FP-01 / test_repeated_calls_give_same_result_in_new_lists | queries.py select_appointments | Two calls with the same input give equal results, but in different list objects | Passed | Same file |
| FP-02 / test_empty_source_returns_new_empty_list | queries.py select_appointments | An empty list in gives a new empty list out | Passed | Same file |
| FP-02 / test_already_sorted_source_returns_new_list | queries.py select_appointments | An already sorted list gives an equal list back, but not the same list object | Passed | Same file |
| FP-02 / test_result_holds_actual_stored_objects | queries.py select_appointments | result[0] is a1 and result[2] is a3, so the new list holds the real objects | Passed | Same file |
| FP-01 / test_query_prints_nothing | queries.py select_appointments | Captured output is empty after calling the query | Passed | Same file |
| QRY-04 / test_known_practitioner_with_no_matches_returns_empty | project/smartcare/services.py list_practitioner_appointments | D2 is registered but has no appointments, so it returns [] | Passed | Same file |
| QRY-04 / test_unknown_practitioner_raises_lookup_error | services.py list_practitioner_appointments | D99 raises LookupError | Passed | Same file |
| QRY-04 / test_blank_practitioner_raises_value_error (2 cases) | services.py list_practitioner_appointments | '' and '   ' both raise ValueError | 2 passed | Same file |
| QRY-04 / test_invalid_status_rejected_and_state_unchanged | services.py list_practitioner_appointments | The string 'scheduled' raises ValueError, the stored IDs and statuses stay the same, and a normal listing still works after | Passed | Same file |
| QRY-04 / test_padded_practitioner_id_uses_registered_id | services.py list_practitioner_appointments | ' D1 ' with spaces still finds A1 | Passed | Same file |
| FR-07 / test_cancelled_history_retained_and_listed | services.py list_practitioner_appointments | After cancelling, A1 is found (same object, CANCELLED), shows up with no filter, and doesn't show up under SCHEDULED | Passed | Same file |
| FR-05, FR-07 / test_cancelled_slot_is_freed_and_both_listed_in_order | services.py list_practitioner_appointments | After cancelling A1, A3 books the same slot. No filter gives [A1, A3] and SCHEDULED gives [A3] | Passed | Same file |

Commands from project/: python -m pytest -q tests/test_stage9_queries.py gave 22 passed in 0.12s, and python -m pytest -q gave 68 passed in 0.26s (the 46 earlier tests plus the 22 new ones). Commit e0a71cc.

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: select_appointments only uses the three things passed into it. It doesn't use any global variables or the data store, and it has no print() or input(). It builds its own new list called selected, adds matching appointments to it, and returns sorted(selected, ...), which is also a new list. It never calls .sort() on the list it was given and never changes any appointment. appointment_sort_key just returns a tuple and doesn't change anything. So the same input always gives the same output, with no side effects.

What the tests do and do not establish: The tests show the filtering, ordering, new-list behaviour and service errors all work for the cases I picked, and that all 46 earlier tests still pass. They don't prove it works for every possible input. COMPLETED is only tested as returning an empty list, because there's no way to make a completed appointment in the project yet. The no-output test only checks print, so the "no input" part comes from reading the code. The tests also don't cover the console, which is shown separately in section D.

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | | | | |
| UI-02 invalid-input recovery | | | | |
| Automated service workflow | | | | |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- reference -->
Actual prompt/context supplied: <!-- paste or accessible reference -->
Actual response: <!-- accessible reference -->

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| | | | | | |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!-- response -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
