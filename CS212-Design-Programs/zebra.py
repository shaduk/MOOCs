import itertools

houses = [1,2,3,4,5]
orderings = list(itertools.permutations(houses))

def imright(h1, h2):
    return h1-h2 == 1
    
def nextto(h1, h2):
    return abs(h1-h2) == 1
    
def zebra_puzzle():
    houses = first,_,middle,_,_ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
            for(red, green, ivory, yellow, blue) in orderings
            if imright(green,ivory)
            for(Norwegian, Englishman, Spaniard, Japanese, Ukranian) in orderings
            if Norwegian is first
            if nextto(Norwegian,blue)
            if Englishman is red
            for(dog, fox, horse, snails, ZEBRA) in orderings
            if Spaniard is dog
            for(coffee, tea, milk, oj, WATER) in orderings
            if coffee is green
            if milk is middle
            if tea is Ukranian
            for(OldGold, Kools, Chesterfields, Luckystrike, Parliaments) in orderings
            if OldGold is snails
            if Kools is yellow
            if nextto(Chesterfields, fox)
            if nextto(Kools,horse)
            if Luckystrike is oj
            if Japanese is Parliaments
            )
            
            
print zebra_puzzle()

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while(sum(times) <= n):
            times.append(timedcall(fn, *args)[0])
        
    return min(times), average(times), max(times)
