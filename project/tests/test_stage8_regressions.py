"""Stage 8 regression tests for the two prepared defects."""

from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def setup_store():
    store = SmartCareDataStore()
    PatientService(store).register_patient('P1', 'Alex Example')
    PractitionerService(store).register_practitioner('D1', 'Sam Example', 'General')
    PractitionerService(store).register_practitioner('D2', 'Morgan Example', 'General')
    return store, AppointmentService(store)


def test_data_store_still_finds_cancelled_appointment():
    """F8-01 / FR-07: a cancelled appointment stays findable in the store."""
    store, service = setup_store()
    appointment = service.book_appointment('A1', 'P1', 'D1', datetime(2026, 10, 1, 9))
    service.cancel_appointment('A1')
    assert store.find_appointment('A1') is appointment
    assert appointment.status == AppointmentStatus.CANCELLED


def test_different_practitioner_same_time_is_allowed():
    """F8-02 / AC-04.2: another practitioner at the same time is not a conflict."""
    store, service = setup_store()
    service.book_appointment('A1', 'P1', 'D1', datetime(2026, 10, 1, 9))
    second = service.book_appointment('A2', 'P1', 'D2', datetime(2026, 10, 1, 9))
    assert store.find_appointment('A2') is second
    assert second.status == AppointmentStatus.SCHEDULED
