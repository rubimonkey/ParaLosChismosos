#Ejemplo 1
#animals = ['cat', 'dog', 'monkey']
#for idx, animal in enumerate(animals):
    #print(idx, animal, "bien")

#Ejemplo 2
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

#Ejemplo 3
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0 and x > 0]
print("Even squares of this are: ", even_squares)
