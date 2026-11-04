
import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService


def test_find_registered_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    registered_patient = service.register_patient("P1", "Alex Smith")
    found_patient = service.find_patient("P1")

    assert found_patient is registered_patient


def test_find_patient_with_trimmed_id():
    store = SmartCareDataStore()
    service = PatientService(store)

    registered_patient = service.register_patient("P1", "Alex Smith")

    assert service.find_patient("  P1  ") is registered_patient


def test_find_unknown_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(LookupError):
        service.find_patient("UNKNOWN")


def test_find_patient_case_sensitive():
    store = SmartCareDataStore()
    service = PatientService(store)
    service.register_patient("P1", "Alex Smith")

    with pytest.raises(LookupError):
        service.find_patient("p1")


@pytest.mark.parametrize("invalid_id", ["", "   ", None, 123])
def test_find_patient_invalid_id(invalid_id):
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(ValueError):
        service.find_patient(invalid_id)


def test_failed_patient_lookup_does_not_change_stored_data():
    store = SmartCareDataStore()
    service = PatientService(store)

    original_patient = service.register_patient("P1", "Alex Smith")

    with pytest.raises(LookupError):
        service.find_patient("UNKNOWN")

    assert service.find_patient("P1") is original_patient
