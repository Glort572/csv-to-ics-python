# 📅📲 CSV to ICS Converter: A Python Script for Automating Calendar Events

This Python script automates the conversion of CSV files to ICS format, simplifying the process of adding multiple events across different days. Included are sample CSV and ICS files to demonstrate the script's functionality.

⚠️ **WARNING:** Avoid using the ICS file in this repo on your Outlook or Google Calendar if you don't want a calendar of yours to have a hundred of useless events!
Anyway, if you don't care and want to try using it, then do it but don't blame me for the consequences. Forewarned is forearmed.

❌ **PROBLEM:** The ICS file will not add notifications to remind you of the events while creating the appointments and, unfortunately, you'll have to add them manually. However, there is a **solution** for this: [**Bulk Edit Calendar Events**](https://bulkeditcalendarevents.com/) by [Derek Antrican](https://github.com/derekantrican).
P.S. Derek's program is closed-source. However, it's virus-free, so tell your OS to install it if you get a "virus/malware warning" after clicking on the installer.

## 📄 Instructions
Before executing the script, ensure that your CSV file follows these guidelines:
- cells are separated by a colon `;`
- events on the same day (and, consequently, in the same cell) are separated by a comma `,`
- the time of the event and its name are separated by a dot `.`
- the start time and end time of the event are separated by a dash `-`

After preparing the CSV file accordingly, execute the script to generate the ICS file. You can then open the ICS file using Google Calendar in your browser, the Outlook app on your PC, or any other compatible calendar application on your phone.
