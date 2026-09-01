# Cool Dev Conf: Nested Data Lab

Imagine there is a small online conference named "Cool Dev Conf." The organizers collect and
analyze attendee info during each conference, so they can understand which years and conference
events were the most popular. Cool Dev Conf is held yearly. The conference has many different
event types: long talks, short talks, panels, workshops, and affinity groups. After 3 years of
running Cool Dev Conf, Cool Dev Conf started to provide different tiers of scholarship tickets in
order to encourage new attendees.

Here's the sign-up data the organizers have collected so far, across 4 years:

| Year | Event Type      | Attendee | Scholarship Tier |
|------|-----------------|----------|-------------------|
| 2021 | Long Talk       | Priya    | none |
| 2021 | Workshop        | Jordan   | none |
| 2021 | Panel           | Alicia   | none |
| 2022 | Workshop        | Priya    | none |
| 2022 | Affinity Group  | Jordan   | none |
| 2022 | Long Talk       | Sam      | none |
| 2023 | Short Talk      | Priya    | none |
| 2023 | Workshop        | Sam      | none |
| 2023 | Panel           | Devon    | none |
| 2024 | Workshop        | Priya    | community |
| 2024 | Long Talk       | Devon    | full-ride |
| 2024 | Panel           | Sam      | partial |
| 2024 | Short Talk      | Riley    | community |

## Goal

This data starts out as a flat list of records; one dictionary per sign-up. Your job is to
reshape it into a **nested** dictionary organized by year and then event type, and then write a
few functions that loop over that nested structure to answer real questions the organizers care
about, like which event type is the most popular and who used a scholarship ticket.

## Working in your group

Work in groups of 3-4. Pick one person to be the **driver** (typing/sharing their screen) and
everyone else is a **navigator** (reading the instructions, thinking through the logic out loud,
and catching bugs).

If your group gets stuck tracing through a nested loop, try sketching a **loop table**: a table
tracking what each loop variable is set to on every pass through the loop. It's a handy way to
see exactly where your logic goes wrong.

## Part A: Reshape the data

Open `main.py`. At the top, you'll find `registrations`, a flat list of dictionaries, one dict per row of the table.

Implement `reshape_conference_data(registrations)` so it returns a nested dictionary shaped like
this:

```python
conference_data[year][event_type] -> list of (attendee, scholarship_tier) tuples

# for example:
conference_data[2021]["long talk"] -> [("Priya", None)]
conference_data[2024]["workshop"]  -> [("Priya", "community")]
```

Loop over `registrations` once. For each record, you'll need to check whether the year is
already a key in `conference_data`, and whether the event type is already a key in that year's
dictionary, adding empty dictionaries/lists as needed before you append.

**Before moving on**, use direct indexing (no loop) to confirm
`conference_data[2021]["long talk"]` matches the table above.

## Part B: Answer the questions

Now that you have a nested structure, implement each of the following functions in `main.py`,
one at a time. After each one, re-run `python3 main.py` and check that the printed output looks
right before moving to the next.

1. `list_event_types(conference_data, year)`: return a list of every event type offered in a
   given year.
2. `total_attendance(conference_data, year)`: return the total number of sign-ups (across all
   event types) for a given year.
3. `most_popular_event_type(conference_data)`: return the event type with the most total
   sign-ups across all years. This one needs a loop inside a loop, since you have to add up
   counts across every year.
4. `get_scholarship_attendees(conference_data, year)`: return a list of names of attendees who
   used a scholarship ticket (i.e. their tier isn't `None`) in a given year.

## Running your code

Run the file from your terminal with:

```bash
python3 main.py
```

Any function that still just contains `pass` will print `None`. As your group implements each
function, re-run the file — the output updates automatically to show your real results.

The nested `conference_data` structure gets printed with `pprint` (short for "pretty print"), a
built-in Python function that lays out nested dictionaries and lists one piece at a time instead
of jamming everything onto one line — much easier to read while you're checking your work.

## Checking your work

Once you're done, you can compare your implementation against
a fully worked solution on the `solution` branch:

```bash
git checkout solution
```
