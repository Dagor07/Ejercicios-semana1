Person = {
 "Name" : "Daniel", 
 "Lastname" : "González", 
 "Age" : 23, 
 "ID" : 123456789,}

for dat, prueba in Person.items():
    print (f"{dat}:{prueba}")
    
numbers = ["uno", "uno", "dos", "tres", "uno", "dos"]
counterNumbers ={}
for number in numbers:
    if number in counterNumbers:
        counterNumbers[number] +=1
    else:
        counterNumbers[number] = 1

print(counterNumbers)