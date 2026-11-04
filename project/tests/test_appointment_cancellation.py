
from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def make_appointment():
    store = SmartCareDataStore()

    PatientService(store).register_patient("P1", "Alex Smith")
    PractitionerService(store).register_practitioner(
        "PR1", "Dr Smith", "General Practice"
    )

    service = AppointmentService(store)
    appointment = service.book_appointment(
        "A1", "P1", "PR1", datetime(2026, 11, 10, 10, 0)
    )

    return service, appointment


def test_cancel_scheduled_appointment():
    service, appointment = make_appointment()

    result = service.cancel_appointment("A1")

    assert result is appointment
    assert appointment.status is AppointmentStatus.CANCELLED


def test_cancelled_appointment_remains_stored():
    service, appointment = make_appointment()

    service.cancel_appointment("A1")

    assert service.find_appointment("A1") is appointment
    assert appointment.status is AppointmentStatus.CANCELLED


def test_cannot_cancel_twice():
    service, appointment = make_appointment()
    service.cancel_appointment("A1")

    with pytest.raises(ValueError):
        service.cancel_appointment("A1")

    assert appointment.status is AppointmentStatus.CANCELLED


def test_cannot_cancel_completed_appointment():
    store = SmartCareDataStore()
    patient = PatientService(store).register_patient("P1", "Alex Smith")
    practitioner = PractitionerService(store).register_practitioner(
        "PR1", "Dr Smith", "General Practice"
    )

    from smartcare.domain import Appointment

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 10, 10, 0),
        AppointmentStatus.COMPLETED,
    )
    store.add_appointment(appointment)
    service = AppointmentService(store)

    with pytest.raises(ValueError):
        service.cancel_appointment("A1")

    assert appointment.status is AppointmentStatus.COMPLETED
    assert service.find_appointment("A1") is appointment


def test_cancel_unknown_appointment():
    service, appointment = make_appointment()

    with pytest.raises(LookupError):
        service.cancel_appointment("UNKNOWN")

    assert appointment.status is AppointmentStatus.SCHEDULED


@pytest.mark.parametrize("invalid_id", ["", "   ", None, 123])
def test_cancel_invalid_appointment_id(invalid_id):
    service, appointment = make_appointment()

    with pytest.raises(ValueError):
        service.cancel_appointment(invalid_id)

    assert appointment.status is AppointmentStatus.SCHEDULED


def test_cancel_with_trimmed_id():
    service, appointment = make_appointment()

    result = service.cancel_appointment("  A1  ")

    assert result is appointment
    assert appointment.status is AppointmentStatus.CANCELLED
