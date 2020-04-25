with open("input/02.txt") as f : 
    
    data = f.read()
    
    initialData= [int(x) for x in data.split(",")]
    numbers = initialData.copy()
    numbers[1] = 12
    numbers[2] = 2
    
# ----- PART 1 ----- #
    for i in range(0 , len(numbers) , 4):
        
        if numbers[i] == 1:
            numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
        elif numbers[i] == 2:
            numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]      
        elif numbers[i] == 99:
            break
        else:
            print("something went terribly wrong")
            quit()
    
    print("PART 1 :" , numbers[0])

# ----- PART 1 ----- #

# ----- PART 2 ----- #

    numbers = initialData.copy()
    
    for noun in range(100):
        for verb in range(100):
            
            numbers = initialData.copy()
            numbers[1] = noun
            numbers[2] = verb

            for i in range(0 , len(numbers) , 4):

                if numbers[i] == 1:
                    numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
                elif numbers[i] == 2:
                    numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]      
                elif numbers[i] == 99:
                    break
                else:
                    break
            if numbers[0] == 19690720:
                print("PART 2 :", noun , verb , numbers[0] ,"answser",  100*noun +verb )
                break
        if numbers[0] == 19690720:
            break    
        
# ----- PART 2 ----- #
    
    
    
    
    
        
