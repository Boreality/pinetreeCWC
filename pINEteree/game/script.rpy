# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("payne peamits")
define b = Character("bachlagod")
define c = Character("cashier")


transform mydefault:
    zoom 0.7
    xpos 30
    ypos 20

transform mydefaultcenter:
    zoom 0.7
    xpos 0
    ypos 20

transform randOnlooker:
    zoom 0.5
    xpos renpy.random.randint(-100,2000)
    ypos renpy.random.randint(-100,400)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.




    p "my names panye"
    p "penuts payne"
    scene bg bedroom with dissolve
    show peanits chill at mydefault


    p "I looooooooooooove blazing that skunk bubba kush"
    p "Im a creature"
    show peanits annoyed
    p "don't Fuck with me"

    "its 4am and payne's neighbors dont fuck with him"
    "we're past smell complaint. {w}we're past legal proceedings. {w}we're past the LAW."
    show peanits chill
    p "i NEED baklava"
    "and it was so"
    show peanits annoyed
    "but there is no baklava anywhere in payne's room"
    p "... {nw} eff it"
    hide peanits with vpunch  
    "payne jumps out the window onto a SUV which breaks his fall"
    show bg forest with dissolve
    "he drives a few miles into the woods then goes up to a tree"
    show peanits chill at mydefault
    p "tree.."
    "payne sniffs the tree"
    p "I.. need baklava.."
    "he smokes his blunt some more"
    show peanits annoyed with dissolve
    p "..so bad.."
    show peanits chill with dissolve
    "the tree is so fucked up"
    "its got curves like canyons"
    show peanits inlove with dissolve
    p "I think im. in love."
    hide peanits with moveoutbottom
    "payne passes out particularly promiscuously at the base of the tree"
    scene bg black
    centered  "{size=160}3 months later{/size}"
    show bg forest with dissolve
    p "woah.."
    p "this shit is on another level.."
    show peanits tree 
    "Payne has {w} Become {w} the tree"
    hide peanits tree
    show peanits tree at mydefault with dissolve
    p "fuuckk dude"
    p "and Im still so HUNGRYY"
    "Wait."
    p "Bro of course, it aint in the woods, what was I thinkinnn"
    p "its in the moeowerfuckin grocery store!!"
    scene bg grocerystore with dissolve
    "Payne goes to the meowtherfucking grocery store"
    "he opens the door handle with his wooden hands and walks in"
    show peanits tree at mydefault with dissolve
    p "Yo anyone see the meowther-"
    hide peanits tree
    show scaredonlooker1 at randOnlooker
    "Terrified Civilian 1" "YAWOWOWOWWW WHAT IS THATTT"
    show scaredonlooker2 at randOnlooker
    "Terrified Civilian 2" "ITS A FUCKIN WHAT THE THE HEELLLL"
    show scaredonlooker3 at randOnlooker
    "Terrified Civilian 3" "WOAHAHHAHHHHH"
    show scaredonlooker4 at randOnlooker
    "Terrified Civilian 4" "OH MY GYOWDDDDDDD"
    show scaredonlooker5 at randOnlooker
    "Terrified Civilian 5" "WAAAAAAAAAAAAAAAAAAH"
    show scaredonlooker6 at randOnlooker
    "Terrified Civilian 6" "IS THAT A .. WHATT???"
    show scaredonlooker7 at randOnlooker
    "Terrified Civilian 7" "HES SO BIGG"
    show scaredonlooker8 at randOnlooker
    "Terrified Civilian 8" "WOODEN BOY??!"
    show scaredonlooker9 at randOnlooker
    "Terrified Civilian 9" "IS THAT A WOODEN BOY???"
    show scaredonlooker10 at randOnlooker
    "Terrified Civilian 10" "OH MY GOOODD THATS A FREAKING WOODEN BOYY"
    show scaredonlooker11 at randOnlooker
    scene bg grocerystore
    show peanits tree
    p "guys I just need some uhh."
    p "shit I need another hit.."
    "he takes another hit"
    hide peanits tree
    show scaredonlooker1 at randOnlooker
    show scaredonlooker2 at randOnlooker
    show scaredonlooker3 at randOnlooker
    show scaredonlooker4 at randOnlooker
    show scaredonlooker5 at randOnlooker
    show scaredonlooker6 at randOnlooker
    show scaredonlooker7 at randOnlooker
    show scaredonlooker8 at randOnlooker
    show scaredonlooker9 at randOnlooker
    show scaredonlooker10 at randOnlooker
    show scaredonlooker11 at randOnlooker
    "Terrified Civilian 11" "A SMOKING WOODEN BOOYYYYYY"
    show scaredonlooker12 at randOnlooker
    "Terrified Civilian 12" "AAAAAAAAAAAAAAAA"
    show scaredonlooker13 at randOnlooker
    "Terrified Civilian 13" "SO SCARRYYYYYYYYY"
    scene bg grocerystore
    show peanits tree at mydefault
    p "Yo uhh cash man"
    show clerk:
        zoom 0.7
        xpos 1000
        ypos 20
    c "Gyhuuu--u-u yea?"
    p "gimme uhh.. one snack of the gods {w} you know the one"
    show clerk with vpunch
    c "Yea! Sure! Haha, take whatever you want!!"
    p "uhh anything? dude ur being really generous right now"
    scene bg grocerystore
    show scaredonlooker14 at randOnlooker
    "Terrified Civilian 14" "im so fucking scared right now"
    show scaredonlooker15 at randOnlooker
    "Terrified Civilian 15" "Im so fucking SCARRED right now"
    show scaredonlooker16 at randOnlooker
    "Terrified Civilian 16" "Brooooo what I am go dooooooooo"
    show scaredonlooker17 at randOnlooker
    "Terrified Civilian 17" "No man u gotta think on the positive side"
    show scaredonlooker13:
        xzoom -1
    "Terrified Civilian 16" "Nah man this Aint it, this aint my day..."
    show scaredonlooker18 at randOnlooker
    "Terrified Civilian 18" "Fuckin. wow."
    scene bg grocerystore
    show peanits tree at mydefault
    p "uhhhhhhhhh {w} ummmmmmmm"
    hide peanits tree
    show peanits tree happy at mydefault
    p "oh there it is!!"
    show baklava with dissolve:
        xpos 900
        ypos 20
    "holy fuck. it's the baklava"
    p "holy fuck. it's the baklava"
    "it appears to be in some kind of clear enclosure."
    "with great intent, {w} intensity, {w} and vigor, {w} paynits ripped the packaging open."
    scene bg god
    show peanits god:
        zoom 1
        xpos -20
        ypos 100
    "it's beautiful."
    show baklagod:
        zoom 1.0
        xpos 800
        ypos -20
    b "son"
    b "you are beautiful as you are"
    b "trust in the light coming from your blunt and you will never go wrong"
    p "woahh."
    "holy shiiiiiit"
    b "I am your bachlava"
    p "I knoww man"
    "the bachlava reaches out to treenits"
    "clouds are moving all around them like its an important moment right now"
    "treenits sees the layered temptation. {w}he gives in instantly"
    p "so tasty.."
    "the clouds transform into pistacho bachlava"
    "the ground becomes the dry wavy tops of the bachalva toppings"
    "treenits looks down and the same things on his arms"
    "treenits becomes bachlivits"
    p "oh ho.."
    p "im so fucking high right now{nw}"
    scene bg grocerystore with dissolve

    p "I need to get back to my crib for real.."
    show clerk:
        zoom 0.7
        xpos 1000
        ypos 20
    c "aint no way that tree is still here"

    scene bg bedroom with dissolve
    "bachlivits somehow finds his way back to his crib"

    p "home again.."
    p "damn"
    "peanits sits down on the carpet floor."
    "theres a penny nudging against his big toe"
    "peanits doesnt move it."
    "it's wall staring time"
    scene bg black
    centered  "{size=160} {cps=2}9 years later{/cps}{/size}"
    show bg bedroom with dissolve
    "peanits in room thats overgrown and surrounded"
    "peanits looks at the wall, completely locked in"
    "his roots are all over the room and theyre the same wavey texture as the bachlava"
    "his crib holds a new strain of bachlava that nobody has ever heard of"
    "the bachlava, tree, and weed cells are symbiotically making a new creature"
    show bg ethereal with dissolve
    show peanits obzen
    "a new world."
    jump finalcredits

label finalcredits:
    scene black
    show screen creditscreen
    pause 30 # or however long it takes to scroll through in a reasonable speed
    pause
    hide screen creditscreen
    return

screen creditscreen:
    vbox:
        xsize 1000 # horizontal size of the credits
        ysize 4500 # how much vertical space your rolling credits take.
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            easein 50: # or however long it takes to scroll through in a reasonable speed
                yalign 1.0
        vbox:
            ysize 720 # enter vertical resolution, so that it starts with an empty screen
        text "meal of the gods":
            font "AlteHaasGroteskBold.ttf"
            color "#F9A"
            size 100
            xalign 0.5
        text "Team Pine Tree":
            font "AlteHaasGroteskBold.ttf"
            color "#79F"
            size 50
            xalign 0.5
        text ""
        text "Made with Ren'Py.":
            font "AlteHaasGroteskBold.ttf"
            bold True
            xalign 0.5
        vbox:
            ysize 100 # some empty space in between
        text "Sponsored by:":
            font "AlteHaasGroteskBold.ttf"
            color "#79F"
            size 50
            xalign 0.5
        text ""
        add "bachlavacredits.jpg": # adding a picture in-between the text
            zoom 0.2
            xalign 0.5
        text "thanks for reading            .":
            font "AlteHaasGroteskBold.ttf"
            bold True
            xalign 0.5

