#!/usr/bin/python3
"""
In this task, you will create a Python function
that generates personalized invitation files
from a template with placeholders and a list of objects.
Each output file should be named sequentially, starting from 1.
You will also implement specific error handling for various edge cases.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template
    and a list of attendees.
    """


    # Check input types
    if not isinstance(template, str):
        print("Error: The template must be a string.")
        return
    if (not isinstance(attendees, list) or
            not all(isinstance(attendee, dict) for attendee in attendees)):
        print("Error: The attendees list must contain only dictionaries.")
        return

    # Check if the template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return


    # Generate files for each attendee
    i = 0

    for attendee in attendees:
        # Replace placeholders using str.replace()
        invitation_text = template.replace("{name}", attendee.get(
            "name", "N/A") or "N/A")
        invitation_text = invitation_text.replace(
            "{event_title}", attendee.get("event_title", "N/A") or "N/A")
        invitation_text = invitation_text.replace(
            "{event_date}", attendee.get("event_date", "N/A") or "N/A")
        invitation_text = invitation_text.replace(
            "{event_location}", attendee.get("event_location", "N/A") or "N/A")

        i += 1

        # Create the output file
        filename = f"output_{i}.txt"

        # Check if the file already exists
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists.\
                  It will be overwritten.")

        with open(filename, "w", encoding="utf-8") as file:
            file.write(invitation_text)

        print(f"Invitation generated: {filename}")
