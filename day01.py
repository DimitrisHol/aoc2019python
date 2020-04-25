def fuelCalculation(distance) : 
    
    return (distance // 3) - 2


totalFuel = 0
totalFuel2 = 0
with open("input/01.txt") as f: 
    
    
    
    
    for line in f : 
        line = line.rstrip()
        
        #Part 1 
        fuel = fuelCalculation(int(line))
        totalFuel += fuel
        
        # Part 2 
        fuelNeeded = fuelCalculation(int(line))
        totalFuel2 += fuelNeeded

        while fuelNeeded > 6 :

            fuelNeeded = fuelCalculation(fuelNeeded)
            totalFuel2 += fuelNeeded
        
        
        
print(totalFuel)
print(totalFuel2)