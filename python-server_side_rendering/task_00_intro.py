#!/bin/python3


def generate_invitations(template, attendees):
    # Check if template is not a string
    if not isinstance(template, str):
        print("Error: The template must be a string")
        return

    # Check if attendees is a list and if each item in the list is a dictionary
    if not (
            isinstance(attendees, list) and
            all(isinstance(item, dict) for item in attendees)
            ):
        print("Error: The attendees must be a list of dictionaries")
        return

    # Check for empty parameters
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        try:
            content = template
            for key in ['name', 'event_title', 'event_date', 'event_location']:
                value = attendee.get(key, "N/A")
                content = content.replace(
                        f"{{{key}}}",
                        value if value is not None else "N/A"
                )

            filename = f"output_{index}.txt"
            with open(filename, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Error creating invitation: {e}")
