# SmartCare — Software Technology 1 Assignment 3

## Project overview

SmartCare is a Python-based teaching application developed for Software Technology 1 Assignment 3 at the University of Canberra.

The application supports patient and practitioner registration, appointment booking, cancellation, appointment lookup, filtering and an interactive console.

This repository implements the common undergraduate (UG) requirements from the SmartCare 2026 Revision 2 baseline. PG-only rescheduling and assurance extensions are not applicable to this group.

**Release label:** `v1.0-UG` (planned)
**Verified code SHA:** `d960ba35b69dc469cf68100c311a19195064e70f`

## Environment and dependencies

The documented teaching baseline is Python 3.13 with pytest 8.3.5.

The integrated release candidate was tested on:

- Operating system: macOS
- Python: 3.14.7
- pytest: 8.3.5
- Regression result: 69 passed, 0 failed

The application runtime uses only the Python standard library. pytest is required for development testing.

Install the development dependency from the `project/` directory:

```bash
python -m pip install -r requirements-dev.txt
```

## Running SmartCare

Run these commands from the `project/` directory.

### Run the supplied demonstration

```bash
python main.py
```

This runs a demonstration using synthetic records and displays an example appointment.

### Run the interactive console

```bash
python main.py --interactive
```

The interactive console supports:

| Option | Operation |
|---|---|
| 1 | Register patient |
| 2 | Find patient |
| 3 | Register practitioner |
| 4 | Find practitioner |
| 5 | Book appointment |
| 6 | Cancel appointment |
| 7 | Find appointment |
| 8 | List practitioner appointments |
| 0 | Exit |

Appointment dates and times use the format `YYYY-MM-DD HH:MM`.

Appointment listing accepts a blank status to include all statuses, or `scheduled`, `cancelled` or `completed` to filter results.

Invalid inputs are handled with error messages so the user can return to the menu.

## Automated testing

Run the full regression suite from `project/`:

```bash
python -m pytest
```

The verified integrated test run collected 69 tests, with all 69 passing in 0.05 seconds.

Tests cover domain behaviour, services, practitioner lookup, appointment cancellation, Stage 8 regressions, appointment queries and integrated workflows.

The test result applies to commit:

`d960ba35b69dc469cf68100c311a19195064e70f`

## Implemented functionality

The common UG implementation includes:

- Patient registration and lookup by ID.
- Practitioner registration and lookup by ID.
- Appointment booking using patient and practitioner IDs.
- Prevention of conflicting scheduled appointments for the same practitioner.
- Allowing different practitioners to accept appointments at the same date and time.
- Appointment cancellation with guarded status transitions.
- Retention and retrieval of cancelled appointments.
- Practitioner appointment listing, status filtering and deterministic ordering.
- Query operations tested for their expected behaviour and purity.
- Interactive console operations and error handling.

## Architecture and repository structure

The application separates domain entities, in-memory storage, services, queries and console interaction.

- `main.py` — application entry point for the demonstration and interactive menu.
- `smartcare/domain.py` — domain entities, appointment status and guarded domain operations.
- `smartcare/data_store.py` — in-memory storage and record access.
- `smartcare/` — service and query implementations.
- `smartcare/console.py` — demonstration and interactive console interface.
- `tests/` — automated unit, regression, query and workflow tests.
- `requirements-dev.txt` — development testing dependencies.

Domain objects represent the application's core information and rules. Services coordinate registration, booking, cancellation and lookup. Queries provide read-oriented listing and filtering. The console manages user interaction.

## Data rules and limitations

SmartCare is an educational application, not a production healthcare system.

- Data is stored in memory for the current application session only.
- Records are lost when the application exits.
- No SQLite database, file persistence or other persistent storage is implemented.
- Appointment times use local date/time values with minute precision.
- IDs are trimmed, non-blank and case-sensitive.
- Unknown lookups and invalid operations produce appropriate errors.
- The application does not enforce appointment duration, patient scheduling conflicts or past-date restrictions.
- There is no interactive operation to mark appointments as completed.
- PG-only rescheduling is not implemented.
- Authentication, role