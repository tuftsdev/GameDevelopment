"Bobo Dihobo" by Tucker Stone
understand "above" as up.

[Definition and execution of the pet verb.  Used 2x in the game.]
petting is an action applying to one visible thing.
understand "pet" as petting.
understand "pet [thing]" as petting.
understand "pat [thing]" as petting.
didpet is a number variable. didpet is 0.
didcat is a number variable. didcat is 0.
carry out petting:
	if the visible thing is Woofy and didpet is 0:
		say "You pet Woofy.  He barks and wags his tail, then snuffles around in the trash and drags out a pair of ratty pants.  An old 2 dollar bill pokes from the pocket, and you grab it with suprise and glee.  Do these things even count as money anymore?";
		increment didpet;
		award 2 points;
	otherwise if the visible thing is Woofy and didpet is greater than 0:
		say "Woofy thumps his leg and wags even harder.  He loves you!";
	otherwise if the visible thing is the cat and didcat is 0:
		say "You shush the cat soothingly and approach with one hand outstretched.  The cat growls, but you place your hand on its back and pet lovingly before it can lash out.  Obviously torn between shredding your hand and purring loudly, the cat relaxes a little and waits for more.";
		increment didcat;
	otherwise if the visible thing is the cat and didcat is 1:
		say "You stroke the cat with renewed confidence.  Your dirty hobo fingernails provide excellent scratching action.  The cat begins to purr loudly, and lies down to proffer its belly.";
		increment didcat;
	otherwise if the visible thing is the cat and didcat is greater than 1:
		say "After petting the cat's belly, it is clear with who the cat's allegiance lies.  The key on its collar is ripe for the taking.";
	otherwise:
		say "You probably shouldn't be petting that.";


[definition of the Beg action.]
begging is an action applying to visible thing.
understand "beg" as begging.
understand "beg [thing]" as begging.
didbeg is a number variable.  didbeg is 0.
carry out begging:
	if didbeg is less than 1:
		say "You put forth your hands and mumble incoherently about spare change.  Most pedestrians turn down their head and walk faster, but a select few throw some coins at you.  You've gathered a sweet dollar and are feeling good about your begging; perhaps you should have another go at it.";
		increment didbeg;
		award 1 point; 
	otherwise if didbeg is 1:
		say "Once again, you accost the pedestrians and ask for money.  One college student stops, however.   'Here you go, man.  Good luck!' He reaches into his pocket and gives you a dollar bill.  You whistle a thank you through your remaining teeth and pocket the bill.";
		increment didbeg;
		award 1 point;
	otherwise:
		say "You do what hobos do best and beg your heart out, but no avail.  No money comes your way.";

When play begins:
say "You find yourself in a Back Alley, clothes dirty and fingernails crusted.  You look down at yourself and take in your appearance; the ragged jacket, fingerless gloves, shopping bag shoes, and tattered pants all add to your incredibly homeless appearance.  Your chipped nametag reads 'Bobo'.  You look up and see an opening at the end of the alley; there is a chain link fence behind you and buildings on either side.  Rising from your soggy cardboard bed, you stretch and get ready to start the day.
	[line break]Looking around you, however, your stomach plunges as you realize that something is wrong.  [bold type]Your most prized possession in the world is missing: your polka-dotted bindle. [roman type] You angrily adorn your paper bag hat and start thinking about how to retrieve what is rightfully yours."

[BACK ALLEY]
The Back Alley is a room.  "A dingy, foul-smelling alley.  Puddles of unknown liquids and piles of unknown solids surround you.  To the [bold type]north [roman type]you can see an opening in the buildings.  Your own personal box is just [bold type] south[roman type] of you."
A box is here.  "A small box lies by the wall, somewhat greasy and wet." The description is "A tattered and damp box.  An intriguing smell wafts through the flaps."
[CARDBOARD HOUSE]
The Cardboard House is a room.  The cardboard house is south of the Back Alley. "You are in a cardboard box, the one you call home.  There is literally nothing here, since it's a box and you are homeless.  Go back and explore!"

[some variables and their uses, used to smooth out gameplay]
boxtaken is a number variable. boxtaken is 0.
After taking the box:
	increment boxtaken;
	say "You pick up the small box.".

havesandwich is a number variable. havesandwich is 0.
Instead of taking the sandwich:
	if (boxtaken is 1):
		say "You grasp the sandwich with your dirty hands and put it safely in a secret pocket, deep within your coat.";
		increment havesandwich;
	otherwise:
		say "You can't see any sandwich.";

instead of opening the box:
	if (boxtaken is 1) then say "You open the box and see a delicious looking sandwich.";
	otherwise say "You should probably take the box first."

The sandwich is edible.  The sandwich is in the box.  The description is "A tasty sandwich.  This is probably invaluable among hobos."
Instead of eating the sandwich, say "You aren't hungry.  Maybe this will come in handy somewhere else..."


[COMMONS - Main area.  A few interactable people / animals here, branches off to a few places]
The Commons is a room. "A large area with burning barrels and some benches.  You can see someone warming himself by the fire, and a dog rooting through some trash.  The Back Alley is south of you, there is a large building to the [bold type]north [roman type]with a locked door, and the street is to the [bold type]east.[roman type]".
The Commons is north of Back Alley.
Skinny Steve is here.  "You recognize the scrawny man by the fire as Skinny Steve, a friendly hobo.  You should[bold type] ask him about how he is[roman type]." Skinny Steve is a person. The description is "A skinny, shivering man.  He seems to have no body fat, the poor man."


[conversations with Steve.   Unfortunately, they must be instantiated by saying 'ask skinny steve about how he is']
histeve is a number variable. histeve is 0.
After asking Skinny Steve about "how he is":
	If histeve is 0 :
		say "Skinny Steve whips around, startled by your stealthy approach. 'Oh, its just you.  Good to see you, Bobo. God I'm so hungry.'";
		 increment histeve;
	otherwise if histeve is 1 :
		say "Skinny Steve grimaces and looks down at his stomach.  He looks hungry.  You feel a twinge of pity and think about [bold type]giving[roman type] him some food";
		increment histeve.
giving is an action applying to one visible thing.
understand "give [thing]" as giving.
instead of giving:
	if histeve >= 1 and (havesandwich is 1):
		say "Skinny Steve's mouth waters and stomach growls as you flourish the sandwich you found earlier. 'Please, Bobo.  Gimme that!  You wont regret it.' [line break] You reluctantly hand over the sandwich.  Skinny Steve cackles and says 'Much obliged.  Here's a buck, its all I have.'";
		award 1 point;
		remove the sandwich from play;
		decrement havesandwich;
	otherwise if histeve is less than 1 and havesandwich is 1:
		say "You should probably talk to him first.";
	otherwise if histeve >= 1 and (havesandwich is less than 1):
		say "You don't have anything to give to Skinny Steve!";

Woofy is here.  "The dog's collar reads Woofy.  He seems to be snuffling around eagerly in the trash." Woofy is an animal.


[THE STREET - where begging happens.]
The Street is a room. "Cars drive by on occasion, and [bold type]pedestrians[roman type] walk by briskly.  This area is a commonly-frequented [bold type]begging[roman type] area in the hobo community."
The Street is east of The Commons.

Pedestrians are here.  Pedestrians are a thing. "Pedestrians hustle and bustle; you can almost smell the money in their pockets."

The Steel Door is a door.  It is scenery.  It is south of The Lobby and north of The Commons. "A huge steel door with multiple locking mechanisms and an eye hole.  A crudely painted sign saying '5$' rests in front of it."


[opening of the house event.  Happens only once, once the player has a score (money value) of 5]
common_door_open is a number variable.  common_door_open is 0.

Instead of going north in the commons:
	if (common_door_open is 0):
		say "You walk up to the solid door and knock.  A gruff voice says 'Its 5 dollars to get in here,  you stinky bum.  Good luck coming up with any money.'  You frown and turn back.";
	otherwise:
		move player to the lobby;
Every turn when in the Commons:
	if score is 5 and common_door_open is 0:
		say "You walk up to the Steel Door and knock angrily on the door. 'Listen pal, if you don't shove off ill-'  The voice cuts off as you produce the money you've scrounged together.  After a few heavy clunks, the door creaks open.";
		increment common_door_open;


[THE HOUSE - Inside the house, where all the action is.  Player needs to find some things and unlock a few doors in order to win]
Instead of going south while in the lobby:
	say "you try the door, but it's locked tight.  You have no choice but to go further into the house."

The Lobby is a room. "The door slams shut behind you.  The air is dusty and dry, and  old tapestries and rugs decorate the area.  There are stairs at the end of the room, but the room is mysteriously empty apart from that."

Upstairs is a room.  Upstairs is above the lobby. "A long hallway with multiple rooms branching off.   There are doors to the [bold type]east[roman type], [bold type] west[roman type], [bold type] north[roman type], and an attic trapdoor [bold type] above [roman type] you."

The pamphlet is here.  The pamphlet is a thing. "A white pamphlet lies on the ground, its pure white color an unsettling contrast to the dusty and dank appearance of the house."  The description is "You open up the pamphlet and read  the contents: 'Hello there.  I see that you have at last done something productive and made your way to this building.  You see, every day I look outside and see filth like you wandering around, mooching from society and being unpleasant to the sight and smell.  I have been luring dirty humans like you into this house for weeks by taking their boxes, and sleeping bags, and polka dotted bindles.  I plan on culling you mongrels from civilization, one at a time.[line break]  You, sir, have a challenge ahead of you.  IF you find what is yours, then you have passed the test and may leave.  Otherwise, you will find my accomplices downstairs...less than forgiving.[line break]  You have little time.  Use it wisely."


[BEDROOM - Has the trapdoor key in the cabinet]
The Bedroom is a room.  The bedroom is east of Upstairs. "You appear to be in an old bedroom.  The layer of dust on everything is thick and oppressive, and the bed looks uncomfortable and old.  Light drifts in from the window, illuminating the thick air."

The cabinet is here.  "A towering cabinet stands in the corner.  It does not seem quite as dusty as the rest of the room." The cabinet is a thing.  the cabinet can be locked.  the cabinet is locked.  the collar unlocks the cabinet.  The description is "The cabinet seems immovable and unbreakable.  There is only one feature to the solid wood doors: a keyhole."

The cieling key is a thing.  the cieling key is inside the cabinet.  The description is "A tiny key, made out of very shiny aluminum."

The bed is here.  The bed is scenery. "A regal looking bed, very musty sheets, perfectly made."

The wooden door is a door.  It is closed.  It is scenery.  It is south of the closet and north of upstairs.

[CLOSET- where the knife is.  Gotta have that.]
The Closet is a room. "A tiny closet devoid of any clothes, boots, or items.  Something catches your eye above the door frame." .

The note is here. The note is a thing."There seems to be a note stuck to the wall, right above the door frame and out of sight."  The description is "Scribbled on the note is a message: 'take this, be careful in the atti~'.  The message appears to have abruptly ended."
The knife is a thing.  The knife is inside the note. The description is "A somewhat dull knife, but has maintained its point.  Be careful with this."

haveknife is a number variable. haveknife is 0.
After taking the knife:
	increment haveknife.

[STUDY - interaction with cat.  Player can die here!]
The Study is a room.  "A musty old study, with a table and chair.  Atop the table is, much to your suprise, a cat.  The cat sees you enter and arches its back.  You can see a key on its collar."  It is west of Upstairs.

The table is here.  It is scenery.  The description is "An old and chipped table.  Nothing interesting."

The chair is here.  It is scenery.  The description is "A rickety looking chair.  Don't sit here."

The cat is here. "The cat  looks wary and very much dangerous.  Its claws are bared, but it looks quite fluffy...".  The cat is an animal.

The cabinet key is here.  "The key on the cat's collar glints at you.  You should probably get that."

The collar is here. " ".  

Instead of taking the cabinet key:
	if didcat is less than 2:
		say "You reach out for the key on the cat's collar.  However, the cat hisses and mauls your hand.  Ouch. [line break]  Apparently, you think as your vision blurs and you stagger to the floor, cat scratch fever is real.";
		end the game in death;
	if didcat greater than 1:
		say "The key, as it turns out, is just part of the collar. Take the collar instead, that should probably work.";

The trapdoor is a door.  it is scenery.  "A typical attic trapdoor, the string dangles down into the room.  However, there is a lock preventing you from opening it."  It is locked.  The trapdoor is above upstairs and below the attic.  The cieling key unlocks the trapdoor.

The attic is a room. "You clamber up into the stuffy attic.  The air is warm and oppressive.  There is barely enough room to stand, so you hunch as you reach the top of the ladder."

Paranoid Pete is here.  Paranoid Pete is a person. "A hunched and slavering figure is on the other side of the attic.  He is constantly mumbling and picking his fingers.  He whirls around and snarls at you, foam flying from his mouth. 'Who's there?! You're from the Chrysler buildng, aren't cha?  Go back and tell them their rays wont affect me!'"

The Bindle is here.  The Bindle is a thing.  "Behind the crazed figure, you can see [bold type] your bindle![roman type]  You only have one option... [bold type]battling[roman type] Paranoid Pete.  Make sure you're ready..."

didwin is a number variable. didwin is 0.

Before taking the bindle:
	if didwin is 0:
		end the game in death;
		
[THE FINAL BATTLE - OMG! fighting paranoid pete!  If you have the knife, you win.  Otherwise, you get beaten to death with your own arms.]
battling is an action applying to one thing.
understand "battle" as battling.
understand "battle [thing]" as battling.
carry out battling:
	if the one thing is Paranoid Pete and haveknife is 0:
		say "Letting loose your most bestial roar, you charge Paranoid Pete and tackle him.  With seemingly inhuman strength, he screams and tears off your arms.  You have just enough time to look surprised before he beats you to death with your own arms.";
		end the game in death;
	if the one thing is Paranoid Pete and haveknife is 1:
		say "Letting loose a bestial roar, you take out the knife you found and charge Paranoid Pete.  He reaches out to stop you, but you slash his hands.  Recoiling, he screams and crashes through the window behind him and plummets out, landing on a comfortable bed of broken bottles.  Breathing heavily, you sheath your knife and turn back to the bindle.  A single tear of joy falls from your eye, and you sling your prized possesion over your shoulder and head to the stairs.";
		increment didwin;
		award 100 points;
		end the game in victory;
