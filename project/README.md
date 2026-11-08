# SmartCare Stage 6 starter

Requirements baseline: SmartCare A3 2026 revision 2. Python 3.13 and pytest 8.3.5 verified. Runtime uses only the standard library.

From this directory, using a Python environment with the development dependency installed:

```sh
python main.py
python -m pytest
```

If needed in your approved environment: `python -m pip install -r requirements-dev.txt`.

The demo registers synthetic records and books/finds an appointment. All supplied tests pass. Data exists only in this session and is lost on exit; FR-10 restart persistence is retired. Use synthetic information only.

`domain.py` contains the entities, status and guarded cancellation. `data_store.py` holds three dictionaries through add/find/list methods. The three services share that object. Supplied registration, booking, appointment lookup and conflict checking work. IDs are trimmed, non-blank and case-sensitive. Properties provide read-only identity/appointment state; changes go through domain methods. No special architecture terminology is required.

Stage 6 TODOs: service patient/practitioner lookup and cancellation. Stage 9 TODOs: pure query, named sort key, service listing and interactive menu. The starter TODO contracts are in docstrings. All three Stage 6 TODO calls deliberately raise NotImplementedError; future TODOs remain stubs. No PG rescheduling or assurance solution is supplied.

Service booking accepts IDs and a `datetime` (local, minute precision). Console parser accepts exactly `YYYY-MM-DD HH:MM`. Store lookups return None when absent; service lookups raise LookupError. Invalid values, duplicates, conflicts and illegal transitions raise ValueError. Lists are new containers holding the stored objects. No age, duration, patient-conflict or past-date rules apply.

## Stage 9: interactive menu

Run from the project/ folder:

    python -m pytest -q
    python main.py --interactive

Menu options: 1/2 register and find a patient, 3/4 register and find a practitioner, 5 book an appointment (date/time as YYYY-MM-DD HH:MM, e.g. 2026-10-01 09:00), 6 cancel, 7 find an appointment, 8 list a practitioner's appointments (leave the status blank for all, or type scheduled, cancelled or completed), 0 exit.

Scope and limitations:
- Data is only kept for the current session. Everything is lost when you exit, and that's intended.
- There's no rescheduling, no saving to a file or database, and no way to mark an appointment as completed yet.
- Invalid input (unknown menu choice, blank or unknown IDs, bad dates, invalid status) shows an error and returns to the menu without changing stored data.
