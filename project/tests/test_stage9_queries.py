"""Stage 9 query, purity and practitioner listing tests."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.queries import appointment_sort_key, select_appointments
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

EIGHT = datetime(2026, 10, 1, 8)
NINE = datetime(2026, 10, 1, 9)
NEXT_DAY = datetime(2026, 10, 2, 9)


def make_source():
    """Return an unsorted source list plus the named appointments."""
    patient = Patient('P1', 'Alex Example')
    d1 = Practitioner('D1', 'Sam Example', 'General')
    d2 = Practitioner('D2', 'Morgan Example', 'General')
    a1 = Appointment('A1', patient, d1, NINE)
    a2 = Appointment('A2', patient, d1, NINE)
    a3 = Appointment('A3', patient, d1, NEXT_DAY)
    b1 = Appointment('B1', patient, d2, EIGHT)
    a2.cancel()
    source = [a3, a2, b1, a1]
    return source, a1, a2, a3, b1


def ids(appointments):
    """Return appointment IDs in order."""
    return [appointment.appointment_id for appointment in appointments]


def make_services():
    """Return a store and appointment service with P1, D1 and D2."""
    store = SmartCareDataStore()
    PatientService(store).register_patient('P1', 'Alex Example')
    PractitionerService(store).register_practitioner(
        'D1', 'Sam Example', 'General',
    )
    PractitionerService(store).register_practitioner(
        'D2', 'Morgan Example', 'General',
    )
    return store, AppointmentService(store)


# ---------- Pure query: select_appointments / appointment_sort_key ----------

def test_practitioner_isolation():
    """QRY-01: only the requested practitioner's appointments; D2 is the control."""
    source, a1, a2, a3, b1 = make_source()
    assert ids(select_appointments(source, 'D1')) == ['A1', 'A2', 'A3']
    assert select_appointments(source, 'D2') == [b1]


def test_default_status_returns_all_statuses():
    """QRY-02: no status means every status, including CANCELLED."""
    source, a1, a2, a3, b1 = make_source()
    result = select_appointments(source, 'D1')
    assert a2 in result
    assert a2.status == AppointmentStatus.CANCELLED


@pytest.mark.parametrize(
    'status, expected',
    [
        (AppointmentStatus.SCHEDULED, ['A1', 'A3']),
        (AppointmentStatus.CANCELLED, ['A2']),
        (AppointmentStatus.COMPLETED, []),
    ],
)
def test_each_status_filter(status, expected):
    """QRY-02: each explicit status returns only that status."""
    source, *_ = make_source()
    result = select_appointments(source, 'D1', status)
    assert ids(result) == expected
    assert all(appointment.status == status for appointment in result)


def test_equal_time_ties_break_by_id():
    """QRY-03: same date/time is ordered by appointment ID."""
    source, a1, a2, a3, b1 = make_source()
    result = select_appointments(source, 'D1')
    assert result[0] is a1
    assert result[1] is a2
    assert a1.date_time == a2.date_time


def test_sort_key_returns_date_time_then_id():
    """FP-03: the named key returns (date_time, appointment_id)."""
    source, a1, *_ = make_source()
    assert appointment_sort_key(a1) == (NINE, 'A1')


def test_named_key_reuse_matches_query_order():
    """FP-03: sorting with the same named key gives the query's order."""
    source, *_ = make_source()
    d1_only = [a for a in source if a.practitioner.practitioner_id == 'D1']
    expected = sorted(d1_only, key=appointment_sort_key)
    assert select_appointments(source, 'D1') == expected


def test_source_order_and_fields_unchanged():
    """FP-02: the source list and every appointment field are not changed."""
    source, *_ = make_source()
    before = [
        (a.appointment_id, a.patient, a.practitioner, a.date_time, a.status)
        for a in source
    ]
    result = select_appointments(source, 'D1')
    after = [
        (a.appointment_id, a.patient, a.practitioner, a.date_time, a.status)
        for a in source
    ]
    assert after == before
    assert result is not source


def test_repeated_calls_give_same_result_in_new_lists():
    """FP-01: same inputs give the same result every time."""
    source, *_ = make_source()
    first = select_appointments(source, 'D1')
    second = select_appointments(source, 'D1')
    assert first == second
    assert first is not second


def test_empty_source_returns_new_empty_list():
    """FP-02: an empty source returns a new empty list."""
    source = []
    result = select_appointments(source, 'D1')
    assert result == []
    assert result is not source


def test_already_sorted_source_returns_new_list():
    """FP-02: an already sorted source still returns a new list."""
    source, a1, a2, a3, b1 = make_source()
    sorted_source = [a1, a2, a3]
    result = select_appointments(sorted_source, 'D1')
    assert result == sorted_source
    assert result is not sorted_source


def test_result_holds_actual_stored_objects():
    """FP-02: the new list reuses the same Appointment objects."""
    source, a1, a2, a3, b1 = make_source()
    result = select_appointments(source, 'D1')
    assert result[0] is a1
    assert result[2] is a3


def test_query_prints_nothing(capsys):
    """FP-01: the query performs no output."""
    source, *_ = make_source()
    select_appointments(source, 'D1')
    assert capsys.readouterr().out == ''


# ---------- Service listing: list_practitioner_appointments ----------

def test_known_practitioner_with_no_matches_returns_empty():
    """QRY-04: known practitioner, no appointments -> empty list."""
    store, service = make_services()
    service.book_appointment('A1', 'P1', 'D1', NINE)
    assert service.list_practitioner_appointments('D2') == []


def test_unknown_practitioner_raises_lookup_error():
    """QRY-04: unknown practitioner -> LookupError."""
    store, service = make_services()
    with pytest.raises(LookupError):
        service.list_practitioner_appointments('D99')


@pytest.mark.parametrize('blank_id', ['', '   '])
def test_blank_practitioner_raises_value_error(blank_id):
    """QRY-04: blank practitioner ID -> ValueError."""
    store, service = make_services()
    with pytest.raises(ValueError):
        service.list_practitioner_appointments(blank_id)


def test_invalid_status_rejected_and_state_unchanged():
    """QRY-04: a non-enum status -> ValueError; stored data unchanged."""
    store, service = make_services()
    a1 = service.book_appointment('A1', 'P1', 'D1', NINE)
    before = [(a.appointment_id, a.status) for a in store.list_appointments()]
    with pytest.raises(ValueError):
        service.list_practitioner_appointments('D1', 'scheduled')
    after = [(a.appointment_id, a.status) for a in store.list_appointments()]
    assert after == before
    assert service.list_practitioner_appointments('D1') == [a1]


def test_padded_practitioner_id_uses_registered_id():
    """Service passes the registered practitioner's ID to the query."""
    store, service = make_services()
    a1 = service.book_appointment('A1', 'P1', 'D1', NINE)
    assert service.list_practitioner_appointments(' D1 ') == [a1]


def test_cancelled_history_retained_and_listed():
    """FR-07: cancelled A1 is findable and listed, but not under SCHEDULED."""
    store, service = make_services()
    a1 = service.book_appointment('A1', 'P1', 'D1', NINE)
    service.cancel_appointment('A1')
    assert service.find_appointment('A1') is a1
    assert a1.status == AppointmentStatus.CANCELLED
    assert service.list_practitioner_appointments('D1') == [a1]
    assert service.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED,
    ) == []


def test_cancelled_slot_is_freed_and_both_listed_in_order():
    """FR-05/FR-07: after cancelling, the slot can be rebooked; both listed."""
    store, service = make_services()
    a1 = service.book_appointment('A1', 'P1', 'D1', NINE)
    service.cancel_appointment('A1')
    a3 = service.book_appointment('A3', 'P1', 'D1', NINE)
    assert service.list_practitioner_appointments('D1') == [a1, a3]
    assert service.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED,
    ) == [a3]