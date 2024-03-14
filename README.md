# DND 5e Program

### Video Demo
TBD

### Description
There are a lot of Dungeons & Dragons programs out there but a lot of them work on outdated knowledge as well as being full of ads or require a monthly subscription. So I made my own.  
The program features customizable dice rolls with unique character sheets. Users may save or load their own files.  
Each character sheet has the character's name, their pronouns, and stats. Dice roll modifiers are automatically applied on each roll.  
One can also create a campaign sheet detailing everything the party has encountered so far.  
Users may use the bestiary or spellbook to quickly look up anything that they need. 
The program abides by the [Wizards of the Coast's Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy).

### Current Features
> Dice Rolls  
> Imports DND API

### To Be Implemented
> HTML/CSS Web Interface  
> Optional Campaign Sheets  
> Optional Character Sheets  
> Combat Functionality  
> Bestiary  

### Current Issues
Bestiary loads very slowly. This is due to the API throttling my requests. Will build an SQL database to save all requests to.  
Bottom navbar doesn't work.  
Settings don't work. SQL needs to be implemented.

### Work Documentation
I made a HTML/CSS layout first. My first page was the menu for testing out different types of designs.  
I chose Flask because its documentation is great. I researched the DND API which supports every encounter you can find in a standard DND campaign. This allowed me to quickly create the bestiary as well as the spellbook which will allow me to create the character sheet.

### Creator
This project is created and maintained solely by me.

### Sources
[Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)  
[DND 5e API](https://www.dnd5eapi.co/)  
[Hit Chance Formula](https://rpg.stackexchange.com/questions/70335/how-do-i-calculate-the-chance-to-hit-a-given-ac)  
[SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)  
[HP Calculation Formula](https://www.omnicalculator.com/other/hit-points)  
[Color Palette](https://colorhunt.co/palette/1b262c0f4c753282b8bbe1fa)  
[Flask WebGUI Tutorial](https://medium.com/@fareedkhandev/create-desktop-application-using-flask-framework-ee4386a583e9)  

### Misc
The project is free and open source. The .gitignore solely features setup files.
