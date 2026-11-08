"""Stage 9 integrated service workflow tests (UI-01/UI-02 service level)."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

NINE = datetime(2026, 10, 1, 9, 0)


def snapshot(store):
    """Record IDs and statuses so rejected actions can be checked."""
    return (
        [p.patient_id for p in store.list_patients()],
        [d.practitioner_id for d in store.list_practitioners()],
        [(a.appointment_id, a.status) for a in store.list_appointments()],
    )


def test_full_session_workflow_with_rejections():
    """One shared store and services through a whole session."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    alex = patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner('D1', 'Sam Example', 'General')
    practitioners.register_practitioner('D2', 'Morgan Example', 'General')
    assert patients.find_patient('P1') is alex

    before = snapshot(store)
    with pytest.raises(ValueError):
        patients.register_patient('P1', 'Someone Else')
    assert snapshot(store) == before
    assert patients.find_patient('P1').name == 'Alex Example'

    with pytest.raises(LookupError):
        appointments.book_appointment('A1', 'P99', 'D1', NINE)
    assert snapshot(store) == before

    a1 = appointments.book_appointment('A1', 'P1', 'D1', NINE)
    assert a1.status == AppointmentStatus.SCHEDULED

    before = snapshot(store)
    with pytest.raises(ValueError):
        appointments.book_appointment('A9', 'P1', 'D1', NINE)
    assert snapshot(store) == before

    a2 = appointments.book_appointment('A2', 'P1', 'D2', NINE)
    assert a2.status == AppointmentStatus.SCHEDULED

    appointments.cancel_appointment('A1')
    before = snapshot(store)
    with pytest.raises(ValueError):
        appointments.cancel_appointment('A1')
    assert snapshot(store) == before

    assert appointments.find_appointment('A1') is a1
    assert a1.status == AppointmentStatus.CANCELLED
    assert appointments.list_practitioner_appointments('D1') == [a1]
    assert appointments.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED,
    ) == []

    a3 = appointments.book_appointment('A3', 'P1', 'D1', NINE)
    assert appointments.list_practitioner_appointments('D1') == [a1, a3]
    assert appointments.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED,
    ) == [a3]
    assert appointments.list_practitioner_appointments('D2') == [a2]

    before = snapshot(store)
    with pytest.raises(ValueError):
        appointments.list_practitioner_appointments('D1', 'scheduled')
    with pytest.raises(LookupError):
        appointments.list_practitioner_appointments('D99')
    assert snapshot(store) == before
