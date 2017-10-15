#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

boop=("nope")

convo={"speak":0}

inventory={
    "magic_eight_ball":0,
    "gumball":0,
    "tv_remote":0,
    "money":0,
    "dumbell":0,
    "ouija_planchette":0,
    "key":0,
    "nothing":1
}

def basement():
    while boop==("nope"):
        print("You are in the basement. From here you can see the laundry room, storage room, pool table, TV, and old pinball machine. Dennis is also sitting on the floor working on his... project. Whatever it is, it looks almost done.\n1 - Speak to Dennis\n2 - Inspect Basement\n3 - Inspect pool table\n4 - Inspect pinball machine\n5 - Inspect TV\n6 - Enter Laundry room\n7 - Enter Storage room\n8 - Check inventory\n9 - Give Dennis something (this will end the game)")
        answer_b = input()
        if answer_b==("1"):
            convo["speak"]+=1
            talking_dennis()
        if answer_b==("2"):
            print("The basement is where this family keeps most of the stuff that wont fit anywhere else, or stuff they would rather forget about. Most of the room is being taken up by Dennis' project at the moment. On normal days, you two would be playing pool or trying to beat the boss of the newest video game.\n")
            continue
        if answer_b==("3"):
            print("For some reason this family tries to play pool with the most random items from around the house. They have all of the proper equipment to play correctly, they just don't want to. You once found what you hope was a fake skull stuffed into one of the pockets. This time you find a magic eight ball.\n")
            inventory["magic_eight_ball"]=1        
            continue
        if answer_b==("4"):
            print("You decide to play with the pinball machine for a bit. You learned last year that it was easier to win if you rocked the machine back and forth. When you started shaking it this time, a gumball fell from somewhere in the machine. Maybe one of Dennis' little siblings stuck it in there.\n")
            inventory["gumball"]=1        
            continue
        if answer_b==("5"):
            print("Going over to the TV, you are astounded by how many remotes have piled up next to the TV stand. It's not just 5 or 6, there are about 50 or 60 remotes slowly melding together. You figure no one would miss one of the remotes, so you pry one out from the bottom of the stack.\n")
            inventory["tv_remote"]=1        
            continue
        if answer_b==("6"):
            laundry_room()
        if answer_b==("7"):
            print("yjhb")
            #storage_room()
            continue
        if answer_b==("8"):
            print("srdhf")
            #inventory()
            continue
        if answer_b==("9"):
            ending()
        else:
            print("Please enter a number between 1 and 9.")
            
            
def talking_dennis():
    if convo["speak"]==1:
        print("'Hey, have you found anything yet? Well, just let me know when you have something to give me.'\n")
        basement()
    if convo["speak"]==2:
        print("'Do you need any help? You look kind of confused.'\n")
        basement()
    if convo["speak"]==3:
        print("'Oh, I just remembered! Here's the key to the storage room. You should find some more stuff in there, just try to stay away from the pile in the very back.'\n")
        inventory["key"]==1
        basement()
    if convo["speak"]>=4:
        print("Sorry, I don't have anything else to help you.'\n")
        basement()
 
def laundry_room():
    print("You are in the laundry room. From here, you can see the washer, dryer, and cleaning supplies.\n1 - Inspect washer\n2 - Inspect Dryer\n3 - Inspect cleaning supplies\n4 - Leave laundry room\n5 - Inspect laundry room")
    answer_1 = input()
    if answer_1==("1"):
        print("Ah, this washer. A few years ago, you made the mistake of dumping an entire gallon of detergent in it because you thought it would make everything stay clean for a month. Well, it did, but it also covered the whole laundry room in lavender scented bubbles.")

def ending():
    print("You have: ")
    for key in inventory:
        if key==1:
            print(key)
        if key==0:
            continue
    print("What would you like to give Dennis?")
    giving =input()
    if giving==("magic_eight_ball"):
        print("'Hah! I've been wondering where that went!'\nDennis places the magic eight ball into the middle of what looks like a magic circle you would find in a bad horror movie. Surprisingly, it seems to do something. Dennis says that the magic eight ball should now be able to correctly predict any future. After multiple tests confirming that it could predict the future, you both agree it would be best to sell it on ebay.")
        boop==("yep")
    if giving==("gumball"):
        print("'I guess that will work.'\nAfter chewing the gum, Dennis used it as an adhesive to fix a piece on a model mecha suit from his favorite anime. Unexpectedly, the little machine whired to life and flew into a nearby vent to get away from the giant creatures before it. Even to this day, Dennis can hear the occasional running of tiny metal feet.")
        boop==("yep")
    if giving==("tv_remote"):
        print("'Great, I know exactly what to do with this!'\nUsing the batteries from the remote, Dennis powers a small toy gun and tests it out by shooting at a near by wall. Unfortunatly, the rubber pellet bounces back and hits you in the eye, blinding that eye forever.")
        boop==("yep")
        
        
 
print("'Oh, hey, I'm glad you're here! I need some help making my... project. I'm not sure what it is just yet. Do you think you could get something from around the basement? What I make will depend on what you give me.'\n1 - Sure, I'll help!\n2 - I don't feel like it.")
help = input()
if help == ("1"):
    print ("'Great, thanks! Feel free to go anywhere in the basement.'")
    basement()
if help == ("2"):
    print ("'Oh...Okay.\nYour friend tries his best to make something, but without your help, he just gives up on his project and plays video games with you.'")
else:
    print("'Sorry, what was that? I couldn't quite understand you.'")
    






