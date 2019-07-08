import random
import math

# source: http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/
def nextTime(rateParameter): # functions that cause random values
    return -math.log(1.0 - random.random()) / rateParameter # Poisson distribution
random.seed(21)

q_ns = [] # how many cars are on the ns road for a certain period of time
q_ew = [] # how many cars are on the ew road for a certain period of time
q_ped = [] # how many people are on the crosswalk for a certain period of time
for i in range(36000): # 10 hours simulation
    q_ns.append(0)
    q_ew.append(0)
    q_ped.append(0)
t1 = 0 # t = time
t2 = 0
t3 = 0
while t1 < 36000:
    q_ns[int(t1)] = 1
    t1 = t1 + math.ceil(nextTime(1/10.0)) # increased by 10 seconds
while t2 < 36000:
    q_ew[int(t2)] = 1
    t2 = t2 + math.ceil(nextTime(1/10.0))
while t3 < 36000:
    q_ped[int(t3)] = 1
    t3 = t3 + math.ceil(nextTime(1/10.0))

state = 1
t = 0
i = 0
ns_car = 0 # total cars on ns road
ew_car = 0 # total cars on ew road
ped = 0 # total people on crosswalk
w_ns = 0 # total time cars wait on ns road
w_ew = 0 # total time cars wait on ew road
w_ped = 0 # total time people wait on crosswalk
ox_ns = 0 # whether there is car on ns road
ox_ew = 0 # whether there is car on ew road
ox_ped = 0 # whether there is car on crosswalk
while t < 36000:
    print "time:", t
    if q_ns[t] == 1:
        ox_ns = 1
    if q_ew[t] == 1:
        ox_ew = 1
    if q_ped[t] == 1:
        ox_ped = 1
    if i < 15:
        state = 1
        ox_ns = 0
        ox_ped = 0
        print state
        if q_ns[t] == 0 and ox_ew == 1 and q_ped[t] == 0: # if there is no car on ns road, there is a car on ew road, there is no car on crosswalk
            i = 15
    if i >= 15 and i < 20:
        state = 2
        print state
    if i >= 20 and i < 35:
        state = 3
        ox_ew = 0
        print state
        if ox_ns == 1 and q_ew[t] == 0 and ox_ped == 0: # if there is a car on ns road, there is no car on ew road, there is no car on crosswalk
            i = 35
        if ox_ns == 1 and q_ew[t] == 0 and ox_ped == 1: # if there is a car on ns road, there is no car on ew road, there is a car on crosswalk
            i = 35
        if ox_ns == 0 and q_ew[t] == 0 and ox_ped == 1: # if there is no car on ns road, there is no car on ew road, there is a car on crosswalk
            i = 35
    if i >= 35 and i < 40:
        state = 4
        print state
    if i == 40:
        state = 1
        print state
        i = 0
    if state == 1: # ns, ped
        ns_car = ns_car + q_ns[t]
        ew_car = ew_car + q_ew[t]
        if q_ew[t] == 1:
            w_ew = w_ew + 20 - i
    if state == 2: # yellow
        ns_car = ns_car + q_ns[t]
        ew_car = ew_car + q_ew[t]
        if q_ns[t] == 1:
            w_ns = w_ns + 40 - i
        if q_ew[t] == 1:
            w_ew = w_ew + 20 - i
    if state == 3: # ew
        ns_car = ns_car + q_ns[t]
        ew_car = ew_car + q_ew[t]
        ped = ped + q_ped[t]
        if q_ns[t] == 1:
            w_ns = w_ns + 40 - i
        if q_ped[t] == 1:
            w_ped = w_ped +40 - i
    if state == 4: # yellow
        ns_car = ns_car + q_ns[t]
        ew_car = ew_car + q_ew[t]
        ped = ped + q_ped[t]
        if q_ns[t] == 1:
            w_ns = w_ns + 40 - i
        if q_ew[t] == 1:
            w_ew = w_ew + 60 - i
        if q_ped[t] == 1:
            w_ped = w_ped + 40 - i
    if state == 1 or state == 2:
        ped = ped + q_ped[t]
    i = i + 1
    t = t + 1
print "ns - cars:", ns_car
print "ew - cars:", ew_car
print "ped - people:", ped
print "ns - cars waiting signal, average time:", w_ns, float(w_ns)/ns_car # average waiting time on ns road
print "ew - cars waiting signal, average time:", w_ew, float(w_ew)/ew_car # average waiting time on ew road
print "ped - people waiting signal, average time:", w_ped, float(w_ped)/ped # average waiting time on crosswalk
