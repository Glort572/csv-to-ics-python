# A Python script to convert a CSV to ICS in a "bizarre" way

I made this code to automate the boring task of putting many different events in several days.
I put a CSV file and an ICS file as examples to make you fully understand the way the script works.

## In short
The Python script checks for:
- cells separated by a colon `;`
- events on the same day (and consequently in the same cell) separated by a comma `,`
- the separation sign between the time of the event and the name (a dot) `.`
- the separation sign between the start and the end of the event (a dash) `-`

After that, the ICS file is finally generated and you can open it on Google Calendar on the browser or the Outlook app on your PC or even Calendar/Outlook/etc. on your phone.