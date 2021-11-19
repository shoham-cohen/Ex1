from Call import Call

class Calls:
    def __init__(self, callslist, elevlist):
        self.callslist = callslist
        self.elevlist = elevlist


    def Elevator_placement(self):
        x = 0
        for k in range(0, len(self.elevlist) - 1):
            self.callslist[x].elv = k
            x = x + 1
        for i in self.callslist:
            if i.elv == -1:
                corrent_time = i.time
                temp = self.elevlist[0]
                for j in self.elevlist:
                    if(abs(self.elev_position(j,corrent_time)-i.source) < abs(self.elev_position(temp,corrent_time) - i.source)):# אם המעלית הנבדקת קרובה יותר מהמעלית ששמורה
                        #if(self.elev_direction(j,corrent_time) == self.Call_direction(i)):#אם הכיוון של המעלית הנבדקת שווה לכיוון של הקריאה
                            temp = j#תשמור את המעלית הנבדקת מכיוון שהיא הכי טובה עד עכשיו להיות המעלית שכדי לקרוא לה לאותה קריאה
                i.elv = temp.id#תשמור בקריאה את המעלית שכי כדי לקרוא לה


    def Call_direction(self, Call)->str:
        if Call.source == Call.destination:
            return "same"
        if Call.source>Call.destination:
            return "down"
        else:
            return "up"

    def elev_direction(self, elev, time)->str:
        list = self.callslist
        last_place_call = list[0]
        for i in list:
            if i.elv == elev.id and time > i.time:
                last_place_call = i
        if last_place_call.source == last_place_call.destination:
            return "same"
        if last_place_call.source > last_place_call.destination:
            return "down"
        else:
            return "up"


    def elev_position(self, elev, time)->int:
        allcallslist = []
        time2 = 0.0
        topfloor = 0.0
        flage = True
        x = 0
        for i in self.callslist:
            if flage == True:
                if i.elv == elev.id:
                    x = i.destination
                    if i.destination > topfloor:
                        time2 = float(time2 + elev.opentime + elev.closetime + elev.starttime + elev.stoptime + (i.destination - topfloor)/elev.speed)
                        topfloor = i.destination
                    else:
                        time2 += elev.opentime + elev.closetime + elev.starttime + elev.stoptime
            if(time2>=time):
                flage = False
                return int(i.destination - ((time2-elev.closetime - elev.opentime - elev.stoptime)-time)*elev.speed)
        return x




