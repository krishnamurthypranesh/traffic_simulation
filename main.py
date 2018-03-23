import random

class Vehical:
    def __init__(self, speed, id):
        self.original = speed
        self.speed = speed
        self.stopd = False
        self.id = id

    def set_stop(self):
        self.speed = 0
        self.stopd = True

    def reset(self):
        self.speed = self.original

    def get_speed(self):
        return self.speed

class Model:
    def __init__(self, length):
        # length of the road
        self.length = length
        self.vehical = None
        # create an empty road of given length
        self.road = [' ']*self.length

    def generate_road(self, vehical):
        """ Generates a road with vehicals with a minimum of 1 cell space """
        self.vehical = vehical
        if self.road[:1] == [' ']:
            self.road[0] = vehical.id
        #print(self.road)

    def set_position(self):
        """ Edits the position of the vehical based on the speed and position of the vehical """
        try:
            index = self.road.index(self.vehical.id)
            if self.road[index+1] != ' ':
                self.vehical.set_stop()
                return
            elif self.vehical.stopd:
                self.vehical.reset()
            distance = self.vehical.speed
            index += distance + 1
            self.road.remove(self.vehical.id)
            self.road.insert(index, self.vehical.id)
        except ValueError:
            pass
        except IndexError:
            self.road[index] = ' '


    def get_model(self):
        """ returns the road """
        return self.road

# create 'n' random vehicals with random speeds (min->1, max->5)
vehicals = [Vehical(random.randrange(1, 5), ''.join(random.sample("qwaszxedcrfvtgbyhnujkimlop", 5))) for _ in range(100)]

# create a road of length 1000
road = Model(10)

# iterate for a 1000 cycles
for _ in range(10):
    print(road.get_model())
    for vehical in vehicals:
        road.generate_road(vehical)
        road.set_position()
