# A Python script to convert a CSV to ICS in a "bizarre" way

I made this code to automate the boring task of putting many different events in several days.
I put a CSV file and an ICS file as examples to make you fully understand the way the script works.

**WARNING:** Don't use that ICS file on your Outlook or Google Calendar if you don't want a calendar of yours to have a hundred of useless events!
Anyway, if you don't care and want to try using it, then do it but don't blame me for the consequences. Forewarned is forearmed.

## In short
The Python script checks for:
- cells separated by a colon `;`
- events on the same day (and consequently in the same cell) separated by a comma `,`
- the separation sign between the time of the event and the name (a dot) `.`
- the separation sign between the start time and the end time of the event (a dash) `-`

So, before executing the script, make sure you've prepared the CSV by following the instructions that I wrote above.

After that, the ICS file is finally generated and you can open it on Google Calendar on the browser or the Outlook app on your PC or even Calendar/Outlook/etc. on your phone.