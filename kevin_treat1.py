num = int (input ("Enter Number : "))

result = list (map (lambda x: 2**x, range (num)))

for i in range (num):

              print ("2 raised to the power", i, "is", result [i])
