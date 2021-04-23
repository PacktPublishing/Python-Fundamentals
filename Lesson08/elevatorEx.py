class Elevator:
    occupancy_limit = 8

    def __init__(self, occupants=0):
        self.floor = 0
        if occupants <= Elevator.occupancy_limit:
            self.occupants = occupants
        else:
            self.occupants = Elevator.occupancy_limit
            print('too many occupants', occupants - Elevator.occupancy_limit, 'left outside')

    def add_occupants(self,num):
        self.occupants +=  num
        if self.occupants > Elevator.occupancy_limit:
            print('too many occupants', self.occupants - Elevator.occupancy_limit, 'left outside')
            self.occupants = Elevator.occupancy_limit

    def remove_occupants(self,num):
        if self.occupants - num > 0:
            self.occupants -= num
        else:
            print('elevator empty')
            self.occupants = 0

    def goto_floor(self,floor):
        if floor < -5 or floor > 50:
            print('floor',floor,'does not exist')
        else:
            self.floor = floor

elevator1 = Elevator(6)
elevator1.add_occupants(7)
elevator2 = Elevator(11)
elevator1.goto_floor(20)
elevator1.remove_occupants(99)
elevator2.goto_floor(99)
print(elevator1.__dict__)
print(elevator2.__dict__)

"""
    ATTRIBUTES
    Occupants attribute which is 0 by default
    floor attribute which is 0 by default

    METHODS:
    Add_occupants
    Go to floor

    PROPERTIES:
    Occupants can only be added if the occupants limit (8) has not been exceeded
    Only floors from -5 to 50 exist
"""
