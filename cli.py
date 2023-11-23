import click
from db import add_event, get_all_events, update_event, delete_event
from models import Event


def get_max_column_widths(events, padding=2, max_desc_length=50):
    """ Calculate maximum width for each column. """
    max_widths = {'_id': len('ID'), 'title': len('Title'),
                  'location': len('Location'), 'date': len('Date'),
                  'description': len('Description')}
    for event in events:
        max_widths['_id'] = max(max_widths['_id'], len(str(event['_id'])))
        max_widths['title'] = max(max_widths['title'], len(event['title']))
        max_widths['location'] = max(
            max_widths['location'], len(event['location']))
        max_widths['date'] = max(max_widths['date'], len(event['date']))
        max_widths['description'] = max(
            max_widths['description'],
            min(len(event['description']), max_desc_length)
        )

    for key in max_widths:
        max_widths[key] += padding

    return max_widths


def interactive_cli():
    while True:
        click.echo("\nEvent Management System")
        click.echo("1: Add Event")
        click.echo("2: List Events")
        click.echo("3: Update Event")
        click.echo("4: Delete Event")
        click.echo("5: Exit")
        choice = click.prompt("\nChoose an option", type=int)

        if choice == 1:
            title = click.prompt("Enter title")
            date = click.prompt("Enter date (MM-DD-YYYY)")
            while not Event.validate_date(date):
                click.echo("Invalid date format. Please use MM-DD-YYYY.")
                date = click.prompt("Enter date (MM-DD-YYYY)")
            location = click.prompt("Enter location")
            description = click.prompt("Enter description")
            event = Event(title, date, location, description)
            event_id = add_event(event)
            click.echo(f'Event added with ID: {event_id}')

        elif choice == 2:
            events = get_all_events()
            if isinstance(events, str) or not events:
                click.echo("No events found." if not events else events)
            else:
                max_widths = get_max_column_widths(events)
                header_format = (
                    "{:<" + str(max_widths['_id']) + "} {:<" +
                    str(max_widths['title']) + "} {:<" +
                    str(max_widths['location']) + "} {:<" +
                    str(max_widths['date']) + "} {:<" +
                    str(max_widths['description']) + "}"
                )
                row_format = (
                    "{:<" + str(max_widths['_id']) + "} {:<" +
                    str(max_widths['title']) + "} {:<" +
                    str(max_widths['location']) + "} {:<" +
                    str(max_widths['date']) + "} {:<" +
                    str(max_widths['description']) + "}"
                )
                click.echo(header_format.format(
                    'ID', 'Title', 'Location', 'Date', 'Description'))
                click.echo("-" * sum(max_widths.values()))

                for event in events:
                    # Check if the description is longer than 50 characters
                    if len(event['description']) > 50:
                        truncated_desc = event['description'][:47] + '...'
                    else:
                        truncated_desc = event['description']
                    click.echo(row_format.format(
                        str(event['_id']), event['title'], event['location'],
                        event['date'], truncated_desc
                    ))

        elif choice == 3:
            events = get_all_events()
            if not events:
                click.echo("No events available to edit.")
            else:
                click.echo("\nSelect an event to edit:")
                for idx, event in enumerate(events, start=1):
                    echo_message = (
                        f"{idx}: {event['title']} at {event['location']} "
                        f"on {event['date']}"
                    )
                    click.echo(echo_message)
                selected = click.prompt(
                    "Enter the number of the event to edit", type=int)
                if selected < 1 or selected > len(events):
                    click.echo("Invalid selection.")
                else:
                    event_to_edit = events[selected - 1]
                    click.echo(f"Editing Event: {event_to_edit['title']}")
                    title = click.prompt(
                        "Enter new title (press enter to keep current)",
                        default=event_to_edit['title'])
                    date = click.prompt(
                        "Enter new date (MM-DD-YYYY) "
                        "(press enter to keep current)",
                        default=event_to_edit['date'])
                    while date and not Event.validate_date(date):
                        click.echo("Invalid date. Use MM-DD-YYYY.")
                        date = click.prompt(
                            "Enter new date (MM-DD-YYYY) "
                            "(press enter to keep current)",
                            default=event_to_edit['date'])
                    location = click.prompt(
                        "Enter new location (press enter to keep current)",
                        default=event_to_edit['location'])
                    description = click.prompt(
                        "Enter new description (press enter to keep current)",
                        default=event_to_edit['description'])
                    update_data = {
                        k: v for k, v in [
                            ('title', title), ('date', date),
                            ('location', location),
                            ('description', description)
                        ] if v != event_to_edit.get(k)
                    }
                    response = update_event(
                        str(event_to_edit['_id']), update_data)
                    click.echo(response)

        elif choice == 4:
            events = get_all_events()
            if not events:
                click.echo("No events available to delete.")
            else:
                click.echo("\nSelect an event to delete:")
                for idx, event in enumerate(events, start=1):
                    click.echo(
                        f"{idx}: {event['title']} at {event['location']} on {event['date']}")  # noqa: E501
                selected = click.prompt(
                    "Enter the number of the event to delete", type=int)
                if selected < 1 or selected > len(events):
                    click.echo("Invalid selection.")
                else:
                    event_to_delete = events[selected - 1]
                    confirmation = click.confirm(
                        f"Are you sure you want to delete the event: {event_to_delete['title']}?",  # noqa: E501
                        default=False)
                    if confirmation:
                        response = delete_event(str(event_to_delete['_id']))
                        click.echo(response)
                    else:
                        click.echo("Deletion cancelled.")

        elif choice == 5:
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid option, please choose again.")


if __name__ == '__main__':
    interactive_cli()
