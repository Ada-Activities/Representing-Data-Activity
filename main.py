"""
Cool Dev Conf -- Nested Data Lab

Run this file from your terminal with:
    python3 main.py

As you implement each function below, its print statement at the bottom of
this file will start showing real output instead of None.
"""

# Raw registration records exported from the Cool Dev Conf database.
# Each dict is one attendee signing up for one event in one year.
registrations = [
    {"year": 2021, "event_type": "long talk", "attendee": "Priya", "scholarship_tier": None},
    {"year": 2021, "event_type": "workshop", "attendee": "Jordan", "scholarship_tier": None},
    {"year": 2021, "event_type": "panel", "attendee": "Alicia", "scholarship_tier": None},
    {"year": 2022, "event_type": "workshop", "attendee": "Priya", "scholarship_tier": None},
    {"year": 2022, "event_type": "affinity group", "attendee": "Jordan", "scholarship_tier": None},
    {"year": 2022, "event_type": "long talk", "attendee": "Sam", "scholarship_tier": None},
    {"year": 2023, "event_type": "short talk", "attendee": "Priya", "scholarship_tier": None},
    {"year": 2023, "event_type": "workshop", "attendee": "Sam", "scholarship_tier": None},
    {"year": 2023, "event_type": "panel", "attendee": "Devon", "scholarship_tier": None},
    {"year": 2024, "event_type": "workshop", "attendee": "Priya", "scholarship_tier": "community"},
    {"year": 2024, "event_type": "long talk", "attendee": "Devon", "scholarship_tier": "full-ride"},
    {"year": 2024, "event_type": "panel", "attendee": "Sam", "scholarship_tier": "partial"},
    {"year": 2024, "event_type": "short talk", "attendee": "Riley", "scholarship_tier": "community"},
]


def reshape_conference_data(registrations):
    """
    Part A: Turn the flat `registrations` list into a nested dictionary shaped like:
        conference_data[year][event_type] -> list of (attendee, scholarship_tier) tuples

    Example:
        conference_data[2021]["long talk"] -> [("Priya", None)]
    """
    conference_data = {}
    for record in registrations:
        year = record["year"]
        event_type = record["event_type"]
        attendee = (record["attendee"], record["scholarship_tier"])
        if year not in conference_data:
            conference_data[year] = {}
        if event_type not in conference_data[year]:
            conference_data[year][event_type] = []
        conference_data[year][event_type].append(attendee)
    return conference_data


def list_event_types(conference_data, year):
    """Part B, Q1: Return a list of every event type offered in a given year."""
    return list(conference_data[year].keys())


def total_attendance(conference_data, year):
    """Part B, Q2: Return the total number of sign-ups (all event types) for a given year."""
    total = 0
    for event_type, attendees in conference_data[year].items():
        total += len(attendees)
    return total


def most_popular_event_type(conference_data):
    """Part B, Q3: Return the event type with the most total sign-ups across all years."""
    totals = {}
    for year, events in conference_data.items():
        for event_type, attendees in events.items():
            if event_type not in totals:
                totals[event_type] = 0
            totals[event_type] += len(attendees)
    return max(totals, key=totals.get)


def get_scholarship_attendees(conference_data, year):
    """Part B, Q4: Return a list of names of attendees who used a scholarship ticket in a given year."""
    names = []
    for event_type, attendees in conference_data[year].items():
        for name, tier in attendees:
            if tier is not None:
                names.append(name)
    return names


if __name__ == "__main__":
    conference_data = reshape_conference_data(registrations)
    print("Nested conference data:", conference_data)

    print("2021 event types:", list_event_types(conference_data, 2021))
    print("2023 total attendance:", total_attendance(conference_data, 2023))
    print("Most popular event type:", most_popular_event_type(conference_data))
    print("2024 scholarship attendees:", get_scholarship_attendees(conference_data, 2024))
