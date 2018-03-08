
def chapter1():
    print('You see a bowl full of food and your owner making breakfast, do you eat your food in the bowl or try to beg for human food?\n\n')
    foodChoice = input("Choose 'beg for human food' or 'eat your own food': ")
    while True:

        if foodChoice not in ['beg for human food','eat your own food']:
            print('Are you really a cat? Choose again.')
            continue
        else:
            if foodChoice == 'beg for human food':
                print('Your human pushes you away and you\'re left with your own food\n')
                chapter2()
                break
            else:
                print('You humbly eat your own food, way to let down the dignity of cats.\n')
                endOfChapter()
                break




def chapter2():
    print('They turn away at the last minute and you\'re able to steal the last bit of food. It\'s ham! You make off with your victory and go to find a nice spot to clean yourself post treat.\n\n')
    spotChoice = input('Do you sit on the counter where you stole the ham or do you run underneath the kitchen table? Choose "sit on the counter" or "go under the table": ')
    while True:
        if spotChoice not in ['sit on the counter', 'go under the table']:
            print('Are you a dog? Please choose "sit on the counter" or "go under the table"')
            continue
        else:
            if spotChoice == 'sit on the counter':
                print('Your human sees you licking yourself and thinks you\'re cute. They give you a treat and pet you.\n\n')
                endOfChapter()
                break
            else:
                print('You hid underneath the kitchen table. Your owner continues to look for you and walks into the living room.\n\n')
                chapter3()
                break

def chapter3():
    print('You\'ve managed to steal the ham and get away with it. Now you want to take a nap but you\'re not sure where to do it.\n\n')
    napChoice = input('Do you sleep on a warm pile of clothes in the laundry room or do you sleep next to the window. Please choose "laundry room" or "warm pile of clothes" ')

    while True:
        if napChoice not in['warm pile of clothes', 'laundry room']:
            print('I know you\'re a cat but please choose an option. "warm pile of clothes" or "laundry room" ')
            continue
        else:
            if napChoice == 'warm pile of clothes':
                alternateEnding()
                break
            else:
                endOfChapter()
                break

def alternateEnding():
    print('You sneak up to the bedroom and make your bed in a pile of freshly done laundry. Life is good, but of course it is...because you\'re a cat, meow')
def endOfChapter():
        print('You then go and curl up under the sun shining from a window in the laundry room, there\'s nothing more you will do in this story. Good bye')
chapter1()
