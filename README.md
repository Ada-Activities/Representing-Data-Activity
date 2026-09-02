# Cool Dev Conf: Nested Data Activity

## One-Time Activity Setup

Choose **one teammate** to execute the following steps just once at the beginning of the activity:

1. Navigate to the folder where you wish to save activities. This could be your `projects` folder, or you may want to create a new folder for all of your activities.

    If you followed Ada's recommended file system structure from the Intro to Dev Environment lesson in Learn, you can navigate to your projects folder with the following command:

    ```bash
    $ cd ~/Developer/projects
    ```

    Or, if you want to create a new folder for all of your activities:

    ```bash
    $ cd ~/Developer
    $ mkdir activities
    $ cd activities
    ```

    If you've already created an activities directory, you can navigate to it with the following command:

    ```bash
    $ cd ~/Developer/activities
    ```

2. In Github click on the "Fork" button to fork the repository to your Github account. This will make a copy of the activity in your Github account. 

3. "Clone" the activity into your working folder. This command makes a new folder named for the activity repository, and then puts the activity into this new folder.

   ```bash
   $ git clone <clone_url_for_the_activity>
   ```

   The `<>` syntax indicates a placeholder. You should replace `<clone_url_for_the_activity>` with the actual URL you'd use to clone this repository. If you click the green "Code" button on the GitHub page for this repository, you'll see a URL that you can copy to your clipboard.
 
   Use `ls` to confirm there's a new activity folder

4. Move your location into this activity folder

   ```bash
   $ cd errors-and-debugging
   ```

5. Create a virtual environment named `venv` for this activity:

   ```bash
   $ python3 -m venv venv
   ```

6. Activate this environment:

   ```bash
   $ source venv/bin/activate
   ```

   Verify that you're in a python3 virtual environment by running:
   
   - `$ python --version` should output a Python 3 version
   - `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this activity with

   ```bash
   # Must be in activated virtual environment
   $ pip install -r requirements.txt
   ```

   Not all activities will have dependencies, but there will still be an included `requirements.txt` file.

Summary of one-time activity setup:
- [ ] Fork the activity repository
- [ ] `cd` into your working folder, such as your `projects` or `activities` folder
- [ ] Clone the activity onto your machine
- [ ] `cd` into the folder for the activity
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Introduction 
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

### Optional Practice

If you finished writing `list_event_types` and `total_attendance`, work on implementing the
functions below for additional practice.

3. `get_scholarship_attendees(conference_data, year)`: return a list of names of attendees who
   used a scholarship ticket (i.e. their tier isn't `None`) in a given year.
4. `most_popular_event_type(conference_data)`: return the event type with the most total
   sign-ups across all years. This one needs a loop inside a loop, since you have to add up
   counts across every year.

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
