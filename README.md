
README file for the python written RPG game using the OPC led simulator as interface.

My project consists in a small Zelda game with CMD and OPC as the user interface.
The user has to fight 5 randomly chosen bosses from a dictionary(lore friendly) with a selection of 12 weapons(lore friendly) that deal different amount of damage.
Besides damage, every weapon also has a "durability" value, if a weapon is used too much, the weapon breaks and cannot be used again.
The idea is that the player has to decide the best use case scenario for the weapons available and the remaining player health.
It is a turn based game, so everytime the user ends the turn and does damage, the boss will do damage to the player aswell.
The weapon selection screen is displyed with the CMD window, while the player's health is displayed on the OPC simulator. 
Total health 300, repressented by 3 hearths, every quarter is 25HP. The bosses have specific health between 200 and 500 and deal between 10-25 damage every turn(randomly generated).
To win the game the player has to kill all 5 bosses with the 300 health available, otherwise it's GAME OVER!
Everytime a boss has been defeated and new boss is selected, the player's health is restored back to 300HP. BUT NOT THE WEAPON DURABILITY!
There are different animations and sounds based on the activities happening in the game, all visible through the OPC simulator.


NOTE: IN THE DEMO VIDEO, THE SOUNDS FOR THE GAME ARE NOT RECORDED!

CHANGELOG:

Version 0.1:
- created .py file 
- added backgroud and defined LED positions for 1 heart

Version 0.2:
- created 3 distinct hearts 
- divided every hearth in 4 sections; total 12 sections rappresenting 300 health
- added Zelda logo when opening CMD
- added weapon selection screen
- added input selection system

Version 0.3:
- small changes to formatting
- added total_health and remaining_health variables
- animated the 12 sections so that they corispond to the player's health as defined:
300 hp  = 3 0/4    hearts
275 hp  = 2 3/4    hearts
250 hp  = 2 2/4    hearts 
225 hp  = 2 1/4    hearts
200 hp  = 2 0/4    hearts
175 hp  = 1 3/4    hearts
150 hp  = 1 2/4    hearts
125 hp  = 1 1/4    hearts
100 hp  = 1 0/4    hearts
 75 hp  = 0 3/4    hearts
 50 hp  = 0 2/4    hearts    
 25 hp  = 0 1/4    hearts
  0 hp  = 0 0/0    hearts
 
Note: currently selecting a weapon does direct damage to the player for debugging

Version 0.4:
- added while loop to "continue fighting" until the health has been depleted
- improved the health system
- improved menu interface
- small changes to formatting 

Version 0.5:
- added a new branch to git to test individual systems without altering main code
- tested a boss system code
- added more comments to the code
- added more items to the interface using the print function for more clarity

Version 0.6:
- added separate branch on Codelabs to test individual systems
- new boss system code:
         - dictionary with different bosses 
		 - health and name "generated" randomly from the dictionary
		 - added boss health and remaining health to the code, now the user can damage the bosses
		 - changes to formatting
- added more weapons

Version 0.7:
- added user health together with the boss health to the individual system 
- tested new rows formatting for the main code
- added "GAME OVER" and "YOU WON" screens to the interface 
- added more comments

Version 0.8:
- created:
         - random_damage.py file to test code for random damage from bosses to the user
		 - created new heart_test.py file to check LED assignations easier without main code alterations
		 - created strings_together.py to check different codes for string concatenation methods
		 - created OLD folder to keep old versions of individual systems files
- boss system code:
         - bosses can now deal damage to the user, taking advantage of that game over screen now :)
		 - bosses that have been already generated are removed from the dictionary so that the game can be ended
		 - balanced the weapons and boss damage so that the game can be completed
		 - added more comments
- main code: removed over 2000 lines of code by changing the formatting to columns for the led assignations
- added definitions to both the main code and individual systems to simply the code and reduce its length

Version 0.9:
- branch used for testing individual systems on Codelabs has been removed since it's not required anymore
- transfered the code from boss system to the main code
- fixed different bugs with the systems not working with eachother 
- added damage taken and boss health remaining information to the interface
- improved the overall code look
- added more comments
- added separate file that explains the health number to health display transaltion ("healthTranslation.txt")

Version 1.0 (this is the one):
- created new branch on Codelabs "old_version_working" representing the version 0.9 program
- added durability feature for every weapon: weapons cannot be used forever now and players have to think of the best use case scenario
- completetly reworked the weapons menu, better interface and now it is also showing the durability left for every weapon
- balanced the turn based system so that the game is fair and fun based on the weapons' damage and durability available
- added input checks: if the input is not a number the player would have to choose again, also if the input is too high inform user that no weapon is available in that slot
- added sound library, now there's a sound playing when: taking damage, defeating a boss, winning the game, losing the game (played async with the animation)
- added required files for the sound system in the master folder ("attack.wav", "bossclear.wav", "gameover.wav", "gamewon.wav")
- added animation for when taking damage
- added animation for when losing a full heart out of 3
- added animation for when unlocking the secret weapon
- added animation for when it's game over
- added animation for when the game has been completed and won
- divided every system and animation in a different definition and added checks for definition clashes in certain situations
- better formatting of code
- cleaned the code a bit, optimised, removed an additional 1000 lines of code
- added way more comments, for almost all lines of code
- spelling corrections
- added secret message
- added demo and explanation video inside the project's folder
- added "OLD" folder where the previous versions of some of the individual systems are located
- addded "individual_systems" folder to store the independent system .py files used during testing







