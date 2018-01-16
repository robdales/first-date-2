#characters.py lpthw
#character classes for first_date2.py
from random import choice
from sys import exit
class Hero(object):

    counter = 0
    fired_count = 0

class Linda(object):

    interests = {
        'Animal': 'Swans',
        'Color': 'Brown',
        'Element': 'Meitnerium',
        'Flower': 'Snapdragon',
        'Fruit': 'Cranberry',
        'Spice': 'Parsley',
        'Gemstone': 'Selenite',
        'Metal': 'Gold',
        'Musical Instrument': 'Violin',
        'Season': 'Autumn',
    }
    
    def action(self):
        print "OMG! Linda is in the room."
        print "Now is your opportunity to get a date!"        
        print '"Oh, hello Walter!  How are you?"'
        raw_input("> ")
        item =  (choice(Linda.interests.keys()))
        print '"That\'s great to hear! I was just thinking about %ss.\nDo you like %ss?"' % (item, item)
        answer = raw_input("(yes, no)> ")

        if answer == 'yes':
            print '"Oh, very nice!  I bet you can\'t pick out my favorite!"'
            answer = raw_input("( %s )> " % item)
            answer = answer.title() 

            if answer == Linda.interests.get(item):
                print '"Yes!  Wow, I am impressed!  I love %s! I am seeing a whole new side to you!"' % (Linda.interests.get(item))
                Hero.counter += 1

            else:
                 print "No, %s, you creep!  %s!? Reeeealy?!  Jerk!" % (Linda.interests.get(item), answer)

        else:
            print '"Oh, ok.  I guess we have different things on our minds."'
        
        if Hero.counter >= 1:
            
            print "Linda looks receptive to your advances now.  You can get a date."
            answer = raw_input('ask Linda out?\n(yes,no)> ')

            if answer == 'yes':
                print "So, do it then!"
                raw_input("> ")            
                print '"What?  Like a date?  Oh, ok- why not!"'
                print "Congratulations! You won! You got a date with Linda!"
                exit(1)
            else:
                print 'what were you playing this game for the whole time you clod?'
        
class Coach(object):

    def action(self):
    
        item =  choice(Linda.interests.keys())
        print "A friend at work wants to be your wingman"
        print '"Hey buddy, I know you\'re trying to score a date with Linda."'
    
        a = choice([1,2,3])
        if a == 1:   
            print '"Here\'s a tip."'
            print '"Word is that Linda was talking about %ss and likes %s"' % (item, Linda.interests.get(item))
        elif a == 2:
            print '"Check out the \'storage closet\' next time you get up."'
            print '"I\'ll send Linda over!"'
        elif a == 3:
            print '"Yo!"'
        else:
            print "error"

class Boss(object):

    def action(self):
        if Hero.fired_count == 0:
            print "Uh-oh, here comes the boss!"
            print '"What are you doing out of your desk Walter?"'
            Hero.fired_count += 1
            print "Strike %s with the boss!" % Hero.fired_count

        elif Hero.fired_count == 1:
            print "Uh-oh, it's your boss again!"
            print '"Walter! Not at your desk again?  You are on thin ice!"'
            Hero.fired_count += 1
            print "Strike %s with the boss!" % Hero.fired_count

        elif Hero.fired_count == 2:
            print "Uh-oh, it's your boss! You better run this time!"
            print '"Pack your stuff up!  I want you out by the end of the day!"'
            print "Dope!  You got fired!"
            exit(1)
