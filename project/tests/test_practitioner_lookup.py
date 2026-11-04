
import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PractitionerService


def test_find_registered_practitioner():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    practitioner = service.register_practitioner(
        "PR1", "Dr Smith", "General Practice"
    )

    assert service.find_practitioner("PR1") is practitioner


def test_find_practitioner_with_trimmed_id():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    practitioner = service.register_practitioner(
        "PR1", "Dr Smith", "General Practice"
    )

    assert service.find_practitioner("  PR1  ") is practitioner


def test_find_unknown_practitioner():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(LookupError):
        service.find_practitioner("UNKNOWN")


def test_find_practitioner_case_sensitive():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    service.register_practitioner(
        "PR1", "Dr Smith", "General Practice"
    )

    with pytest.raises(LookupError):
        service.find_practitioner("pr1")


@pytest.mark.parametrize("invalid_id", ["", "   ", None, 123])
def test_find_practitioner_invalid_id(invalid_id):
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(ValueError):
        service.find_practitioner(invalid_id)


def test_failed_practitioner_lookup_preserves_data():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    practitioner = service.register_practitioner(
        "PR1", "Dr Smith", "General Practice"
    )

    with pytest.raises(LookupError):
        service.find_practitioner("UNKNOWN")

    assert service.find_practitioner("PR1") is practitioner
