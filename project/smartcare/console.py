"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')


MENU = (
    '\nSmartCare menu\n'
    '1. Register patient\n'
    '2. Find patient\n'
    '3. Register practitioner\n'
    '4. Find practitioner\n'
    '5. Book appointment\n'
    '6. Cancel appointment\n'
    '7. Find appointment\n'
    '8. List practitioner appointments\n'
    '0. Exit'
)


def parse_status(text: str) -> AppointmentStatus | None:
    """Turn typed status text into an AppointmentStatus; blank means all."""
    cleaned = text.strip().lower()
    if cleaned == '':
        return None
    for status in AppointmentStatus:
        if status.value == cleaned:
            return status
    raise ValueError(
        'Status must be blank, scheduled, cancelled or completed',
    )


def run_menu() -> None:
    """Run the register/find/book/cancel/list/exit menu for one session.

    One store and one set of services are used for the whole session.
    Expected errors are reported and the menu continues.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    while True:
        print(MENU)
        choice = input('Choose an option: ').strip()
        try:
            if choice == '1':
                patient = patients.register_patient(
                    input('Patient ID: '),
                    input('Patient name: '),
                )
                print(f'Registered patient {patient.patient_id}: {patient.name}')
            elif choice == '2':
                patient = patients.find_patient(input('Patient ID: '))
                print(f'{patient.patient_id}: {patient.name}')
            elif choice == '3':
                practitioner = practitioners.register_practitioner(
                    input('Practitioner ID: '),
                    input('Practitioner name: '),
                    input('Specialty: '),
                )
                print(
                    f'Registered practitioner {practitioner.practitioner_id}: '
                    f'{practitioner.name} ({practitioner.specialty})',
                )
            elif choice == '4':
                practitioner = practitioners.find_practitioner(
                    input('Practitioner ID: '),
                )
                print(
                    f'{practitioner.practitioner_id}: {practitioner.name} '
                    f'({practitioner.specialty})',
                )
            elif choice == '5':
                appointment_id = input('Appointment ID: ')
                patient_id = input('Patient ID: ')
                practitioner_id = input('Practitioner ID: ')
                date_time = parse_date_time(
                    input('Date/time (YYYY-MM-DD HH:MM): ').strip(),
                )
                appointment = appointments.book_appointment(
                    appointment_id,
                    patient_id,
                    practitioner_id,
                    date_time,
                )
                print(f'Booked {format_appointment(appointment)}')
            elif choice == '6':
                appointment = appointments.cancel_appointment(
                    input('Appointment ID: '),
                )
                print(f'Cancelled {format_appointment(appointment)}')
            elif choice == '7':
                appointment = appointments.find_appointment(
                    input('Appointment ID: '),
                )
                print(format_appointment(appointment))
            elif choice == '8':
                practitioner_id = input('Practitioner ID: ')
                status = parse_status(
                    input('Status (blank for all, or scheduled/cancelled/completed): '),
                )
                results = appointments.list_practitioner_appointments(
                    practitioner_id,
                    status,
                )
                if not results:
                    print('No matching appointments.')
                for appointment in results:
                    print(format_appointment(appointment))
            elif choice == '0':
                print('Exiting. Session-only data: records are lost on exit.')
                break
            else:
                print('Unknown choice. Please pick a number from the menu.')
        except (ValueError, LookupError) as error:
            print(f'Error: {error}')
