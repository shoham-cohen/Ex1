class Call:
    def __init__(self, time, source, destination, elv=-1):
        self.time = time
        self.source = source
        self.destination = destination
        self.elv = elv

    def gettime(self) -> float:
        time = float(self.time)
        return time

    def getsource(self) -> float:
        return float(self.source)

    def getdestination(self) -> float:
        return float(self.destination)

    def getelv(self) -> float:
        return self.elv

    def __str__(self) -> str:
        return f"time of call: {self.time} floor source: {self.source} destination: {self.destination} elv: {self.elv}"

    def __repr__(self) -> str:
        return f"time of call: {self.time} floor source: {self.source} destination: {self.destination} elv: {self.elv}"
