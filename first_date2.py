#first_date2.py lpthw

from random import choice
from characters import Linda
from characters import Coach
from characters import Boss
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n --------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)  

class Desk(object):
    #player should return to the desk after each scene apart from Desk

    def enter(self):
        #at the desk the player picks a place to walk to
        print "You are seated at your desk"
        a = raw_input('Where would you like to go?(water cooler, coffee room)>')
        if a == 'water cooler':
            print "walking over to water cooler"
            return 'water_cooler'

        elif a == 'coffee room':
            return 'coffee_room'

        elif a == 'storage closet':
            return 'storage_closet' 
            
        else:
            print "sorry Walter, I can't do that!"
            return 'desk'
        
            
class WaterCooler(object):
    
    def enter(self):
        print "You walk from your desk to the water cooler."
        a = choice([Linda(),Coach(),Boss()])
        a.action()
        return 'desk'

class CoffeeRoom(object):
    
    def enter(self):
        print "You walk from your desk to the coffee room"
        print "You realize you did not bring a lunch today :(\n"
        a = choice([Linda(),Coach(),Boss()])
        a.action()
        return 'desk'
  
class StorageCloset(object):
    
     def enter(self):
        print "You walk from your desk to the storage closet."
        print "The dank smell of the mixture of bleach and concrete floor"
        print "swirls in your nostrils."
        print "You see office supplies on shelves and a mop in a bucket."
        a = Linda()
        a.action()
        return 'desk'

class Map(object):

    scenes = {
       'desk':Desk(),
        'water_cooler': WaterCooler(),
        'coffee_room': CoffeeRoom(),
        'storage_closet': StorageCloset()
        }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
print '''
  __ _          _         _       _         ____  
 / _(_)_ __ ___| |_    __| | __ _| |_ ___  |___ \ 
| |_| | '__/ __| __|  / _` |/ _` | __/ _ \   __) |
|  _| | |  \__ \ |_  | (_| | (_| | ||  __/  / __/ 
|_| |_|_|  |___/\__|  \__,_|\__,_|\__\___| |_____|
'''   
print "\nWelcome to 'First Date 2'!"
print "========================\n"
print "Your name is Walter and you want a date with Linda."
print "Try asking her out when you bump into her at the office!"
print "Don't let the boss catch you away from your desk though!"

a_map = Map('desk')
a_game = Engine(a_map)
a_game.play()
