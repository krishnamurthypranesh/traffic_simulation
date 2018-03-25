""" A traffic sumulation model based on the Nagel–Schreckenberg cellular automation where """

import random

class Vehical:
    def __init__(self, speed, id):
        self.speed = speed
        self.id = id

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

class Model:
    def __init__(self, length):
        # length of the road
        self.length = length
        self.vehical = None
        # create an empty road of given length
        self.road = [" "]*self.length

    def generate_road(self, vehical):
        """ Generates a road with vehicals with a minimum of 1 cell space """
        self.vehical = vehical
        if self.road[:1] == [" "]:
            self.road[0] = vehical.id
        #print(self.road)

    def set_position(self):
        """ Edits the position of the vehical based on the speed of the vehical """
        try:
            index = self.road.index(self.vehical.id)
            distance = self.vehical.speed
            if self.road[index+1] != " ":
                """ If the cell ahed of the vehical is not empty"""
                print('here 1')
                self.vehical.set_speed(self.vehical.speed-1)
            # elif self.road[index+1] != " ":
            #     """ if the neighbouring cell is not empty """
            if self.road[index+distance+1] != " ":
                """ if the cell the vehical will appear next is not empty """
                # self.vehical.set_speed(-1)
                print('here 2')
                print('id:', self.vehical.id, 'speed:', self.vehical.speed, 'distance:', distance, 'index:', index, end='')
                self.vehical.set_speed(distance-index-1)
                print(' new_speed',self.vehical.speed)
            distance = self.vehical.speed
            index += distance + 1
            self.road.remove(self.vehical.id)
            self.road.insert(index, self.vehical.id)
        except ValueError:
            # for list inclusion
            pass
        except IndexError:
            # This exception occurs when the object is at the end of the list
            self.road[index] = " "

    def get_model(self):
        """ returns the road """
        return self.road

# create 'n' random vehicals with random speeds (min->1, max->5)
vehicals = [Vehical(random.randrange(1, 5), ''.join(random.sample("qwaszxedcrfvtgbyhnujkimlop", 5))) for _ in range(10)]

# create a road of length 'l'
road = Model(20)

for i, vehical in enumerate(vehicals):
    road.generate_road(vehical)
    print(i, '==>',road.get_model())
    road.set_position()
