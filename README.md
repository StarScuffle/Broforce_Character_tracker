# Broforce_Character_tracker
Due to the way Broforce caclulates the RNG for character rolls you aren't able to get the same character any more often than once every 27 times.
As such you only have 8 possible characters to roll on level restart or breaking out a POW, however to know which characters those are you'd have to constantly keep track of all 35 characters and in which order they were rolled.
This task while theoretically possible for a human to do whould be near superhuman.

As such I created this program which takes screenshots of the game several times per second and can detect all characters currently in the game and keep track of them to display the currently avalible characters to roll.

Program requirements
------------------------
Probably Windows 10, I've yet to test it with other operating systems

at least 800MB of storage space

a 1080p screen for Broforce to be played in fullscreen mode on (I plan to update for different resolutions in the future)

Due to the way the system works currently you'll likely need a second monitor to see the program this'll be one of the first things I go about fixing

Broforce must be run on your main monitor as currently that's the only location the program looks at

Nothing can be blocking the character icon in the bottom left of the screen and that's how the program identifies which character has been rolled

The program also with get messed up if you capture a new POW during boss ending cutscenes when the character icon dissapears

Usage
---------------------------
Run Main.exe and a command terminal should show up

Simply launch Broforce and load up any game

Once your character is onscreen you should see something along the lines of

"Current Bro is [InsertaBro]"

Keep playing the game and after 28 rolls the program will display the 8 characters currently rollable
