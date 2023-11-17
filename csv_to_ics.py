import csv
from datetime import datetime, timedelta
from icalendar import Calendar, Event

def convert_csv_to_ics(input_file, output_file):
    # Open the CSV file and read data
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        rows = list(reader)

    # Create the ICS calendar
    cal = Calendar()

    for i in range(0, len(rows), 2):
        date_row = rows[i]
        time_row = rows[i + 1]

        for j in range(len(date_row)):
            if time_row[j]:
                # Extract the info about the events from the hours cell
                event_info_list = time_row[j].split(',')

                # Extract the date without gaps in excess
                date_cleaned = date_row[j].strip()

                # Create the date in the correct format
                event_date = datetime.strptime(date_cleaned, "%d %b %Y")

                # Analyse each event in the list
                for event_info in event_info_list:
                    # Extract the start time and the end time (with the dot as separator)
                    time_info = event_info.split('.')
                    title = time_info[1].strip() if len(time_info) > 1 else ''
                    
                    start_end_times = time_info[0].split('-')
                    start_time = start_end_times[0].strip()
                    end_time = start_end_times[1].strip() if len(start_end_times) > 1 else ''

                    # The event gets created only if time is specified
                    if start_time and end_time:
                        # Creation of the event
                        event = Event()
                        event.add('summary', title)
                        event.add('location', 'Tartini Conservatory, Via Carlo Ghega, 12, 34132 Trieste TS, Italy')
                        event.add('dtstart', event_date.replace(hour=int(start_time.split(':')[0]), minute=int(start_time.split(':')[1])))
                        event.add('dtend', event_date.replace(hour=int(end_time.split(':')[0]), minute=int(end_time.split(':')[1])))
                        event.add('alarm', {'trigger': timedelta(hours=-1), 'action': 'DISPLAY'})
                        cal.add_component(event)

    # Write the ICS calendar in the output file
    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())

# Input and output file names (if you don't add them, the script will never work)
convert_csv_to_ics('<your_input_file_name_here>.csv', '<your_output_file_name_here>.ics')
