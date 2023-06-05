# F1-Stats-Website

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Presentation**

F1 stats website is use to create graphics of pilot best laps (for the moment).

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Installation**

To use this code you will need :
- Flask : ```pip install flask```
- FastF1 : ```pip install fastf1```

You have one python files :
- ```main.py``` : where you can find all the code of the website

In the folder ```templates```, you can find all the HTML files :
- ```home.html``` : where you can find the first prompt to choose the year.
- ```chooseRound.html``` : where you can find the prompt to choose the round.
- ```chooseGraphics.html``` : where you can find the prompt to choose the graphics and pilot.
- ```result.html``` : where you have the result.
- ```sessionNotAccessible.html``` : when they're an error with the round.

After, verify you are in the same folder as ```main.py``` in your terminal and type : ```flask --app main.py run``` or ```flask --app main.py --debug run``` if you want the debug mode.

Then go on ```http://127.0.0.1/``` and have fun !
