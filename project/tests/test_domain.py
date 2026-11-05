from datetime import datetime
import pytest
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)


# --- Patient Domain Tests ---

def test_patient_valid_construction():
    """Verify valid patient construction retains attributes."""
    patient = Patient("P1", "Alice Smith")
    assert patient.patient_id == "P1"
    assert patient.name == "Alice Smith"


def test_blank_patient_id_is_rejected():
    """Verify empty or whitespace-only patient ID raises ValueError."""
    with pytest.raises(ValueError):
        Patient("   ", "Alice Smith")


def test_blank_patient_name_is_rejected():
    """Verify empty or whitespace-only patient name raises ValueError."""
    with pytest.raises(ValueError):
        Patient("P1", "   ")


# --- Practitioner Domain Tests ---

def test_practitioner_valid_construction():
    """Verify valid practitioner construction retains attributes."""
    doc = Practitioner("DR1", "Dr. Bob", "Cardiology")
    assert doc.practitioner_id == "DR1"
    assert doc.name == "Dr. Bob"
    assert doc.specialty == "Cardiology"


def test_blank_practitioner_fields_rejected():
    """Verify blank practitioner ID, name, or specialty raises ValueError."""
    with pytest.raises(ValueError):
        Practitioner("", "Dr. Bob", "Cardiology")
    with pytest.raises(ValueError):
        Practitioner("DR1", "   ", "Cardiology")
    with pytest.raises(ValueError):
        Practitioner("DR1", "Dr. Bob", "")


# --- Appointment Domain Tests ---

def test_new_appointment_starts_scheduled():
    """Verify new appointment defaults to SCHEDULED status."""
    p = Patient("P1", "Alice")
    doc = Practitioner("DR1", "Dr. Bob", "GP")
    slot = datetime(2026, 11, 10, 10, 0)
    apt = Appointment("A1", p, doc, slot)

    assert apt.status == AppointmentStatus.SCHEDULED


def test_cancel_changes_status():
    """Verify cancelling a SCHEDULED appointment changes status to CANCELLED."""
    p = Patient("P1", "Alice")
    doc = Practitioner("DR1", "Dr. Bob", "GP")
    slot = datetime(2026, 11, 10, 10, 0)
    apt = Appointment("A1", p, doc, slot)

    apt.cancel()
    assert apt.status == AppointmentStatus.CANCELLED


def test_repeated_cancellation_is_rejected():
    """Verify cancelling an already CANCELLED appointment raises ValueError."""
    p = Patient("P1", "Alice")
    doc = Practitioner("DR1", "Dr. Bob", "GP")
    slot = datetime(2026, 11, 10, 10, 0)
    apt = Appointment("A1", p, doc, slot)

    apt.cancel()
    assert apt.status == AppointmentStatus.CANCELLED

    with pytest.raises(ValueError):
        apt.cancel()
    assert apt.status == AppointmentStatus.CANCELLED