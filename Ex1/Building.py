from Elevator import Elevator


class Building:

    def __init__(self, _minfloor, _maxfloor, elevators_list):
        self.minFloor = _minfloor
        self.maxFloor = _maxfloor
        self.elevators_list = elevators_list
