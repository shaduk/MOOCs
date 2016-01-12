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