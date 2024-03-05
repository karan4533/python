from collections import defaultdict


jug1, jug2, aim = 3, 4, 2  

visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2, steps=[]): 
    # Checks for our goal and 
    # returns true if achieved.
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        steps.append((amt1, amt2))
        print("Steps:")
        for step in steps:
            print(step)
        return True

   
    if not visited[(amt1, amt2)]:
        steps.append((amt1, amt2))

 
        visited[(amt1, amt2)] = True

       
        return (waterJugSolver(0, amt2, steps) or
                waterJugSolver(amt1, 0, steps) or
                waterJugSolver(jug1, amt2, steps) or
                waterJugSolver(amt1, jug2, steps) or
                waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
                               amt2 - min(amt2, (jug1-amt1)), steps) or
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
                               amt2 + min(amt1, (jug2-amt2)), steps))

  
    else:
        return False


print("Steps:")
waterJugSolver(0, 1)
