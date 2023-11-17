# CSV to ICS Converter: A Python Script for Automating Calendar Events

This Python script automates the conversion of CSV files to ICS format, simplifying the process of adding multiple events across different days. Included are sample CSV and ICS files to demonstrate the script's functionality.

**WARNING:** Avoid using the ICS file in this repo on your Outlook or Google Calendar if you don't want a calendar of yours to have a hundred of useless events!
Anyway, if you don't care and want to try using it, then do it but don't blame me for the consequences. Forewarned is forearmed.

## Instructions
Before executing the script, ensure that your CSV file follows these guidelines:
- Cells are separated by a colon `;`.
- Events on the same day (and, consequently, in the same cell) are separated by a comma `,`.
- The time of the event and its name are separated by a dot `.`.
- The start time and end time of the event are separated by a dash `-`.

After preparing the CSV file accordingly, execute the script to generate the ICS file. You can then open the ICS file using Google Calendar in your browser, the Outlook app on your PC, or any other compatible calendar application on your phone.