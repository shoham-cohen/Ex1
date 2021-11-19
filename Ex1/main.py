import csv
import json

from Calls import Calls

from Building import Building
from Call import Call
from Elevator import Elevator

file = open("B1.json", "r")
data = json.load(file)
elevtors_list = [] #########################################רשימה של כל המעליות מהקובץ
for i in data["_elevators"]:
    elevator = Elevator(float(i["_id"]), i["_speed"], i["_minFloor"], i["_maxFloor"], i["_closeTime"], i["_openTime"], i["_startTime"], i["_stopTime"])
    elevtors_list.append(elevator)
building = Building(data["_minFloor"], data["_maxFloor"], elevtors_list)
file.close()

r = csv.reader(open("Calls_a.csv", "r"))
lines = list(r)
callslist = []############################################רשימה של כל הקריאות
for i in lines:
    newcall = Call(float(i[1]), float(i[2]), float(i[3]), -1)
    callslist.append(newcall)

c = Calls(callslist, elevtors_list)
c.Elevator_placement()

x = 0
for i in lines:
      i[5] = int(c.callslist[x].elv)
      #i.append(' Done, dt, 164.5625272709607')
      print(i)
      x = x + 1

writer = csv.writer(open("Elevator_Calls_placement.csv", 'w', newline=""))
writer.writerows(lines)

