# Top Down Shooter

This is my new project idea. I realized I was struggling with Django, so I decided to make a last-minute change and create a video game.

The game is a top-down tile-based shooter boss battle. One of the goals that I set for myself was to use an RNG tile base, though given the amount of time I had left (about a week due to switching projects late), I did not incorporate this into the code. I followed tutorials mostly, and attempted to combine several tutorials, which nearly worked, except for movement.

My initial project was a meditation app; however, I realized a bit too late that Django probably was not best for displaying a moving image, and for having buttons (in hindsight, this project idea would have worked much better in HTML). That is why I changed to a pygame project.

Sources are currently in the python file and below.

# Progress Report

(April) So far, I have not been able to figure out why my pip was not being seen by python.

(April) I have managed to resolve the issue by uninstalling Python, removing all Python files in AppData, and then reinstalling Python 64-bit. Then, I followed https://packaging.python.org/tutorials/installing-packages/ to check if pip is installed. I have also installed Django.

(April) I installed Django and virtualenv, as well as a new directory for the project, though I am still trying to figure out where to go from here. Right now, when I try to turn on the virtualenv, I get something that says "'virtualenv' is not recognized as an internal or external command, operable program or batch file." On the part that says "Creating a Project in Django" in the book (page 400)

(April 20-ish) I searched for a guide to integrate an image into Django, though I couldn't find anything.

(May 3) Realized I was struggling with Django and was making literally no progress, so I just changed the project. I think Django isn't the right program for what I wanted to do (which probably would have been easier on HTML)

(May 11) I have committed to making a top-down shooter in the vein of "Realm of the Mad God" or something like that. Since I don't have a lot of time left, I need to allocate time this weekend and before the presentation next week. So far I have the map assets (look in the "topdown" folder).

(May 13) I managed to get somewhat far, as I have created a world and added sprites for a player and a boss. However, I couldn't make the player move. The sprites were created using classes.

(May 18) I figured out movement by using the Kids Can Code tutorial, and I made the code more organized by following the Kids Can Code tutorial on a tile-based shooter. However, the project is incomplete. I am still missing projectiles, hp bars. Additionally, I hit a hurdle where my boss would not appear, though I ran out of time to resolve the issue. So far, the work with the RNG tiles is in the file called "mainNotInUse.py" because at the moment I am not using any of the assets in that file (though if I decide to pick this up again I will try to use RNG tiles in the game, but given the time I have now, it won't work). I also just realized that this is now due on the 23rd.

# Works Incorporated
- UsingPython.com: http://usingpython.com/pygame/
- Seth Kenlon's game tutorial: https://opensource.com/article/17/12/game-python-add-a-player and https://opensource.com/article/17/12/game-python-moving-player
- Kids Can Code Youtube channel (specifically the tile-based shooter series and game development series): https://www.youtube.com/playlist?list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw
- Sprites from Kenney Topdown Shooter (open source): http://kenney.nl/assets/topdown-shooter
- "archer.png", "boss.png" from "Realm of the Mad God" (a video game), "floor.png" from this tutorial: http://usingpython.com/pygame-images/, "water.gif" from a Google search

# Works Incorporated in Django project (https://github.com/thefakemacaw/meditationApp)
- Eric Mathes' "Python Crash Course"
- DjangoProject tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial01/
