from cmath import sqrt


print("Hello World !! Python here we go !!")

listNumData = [5,4,6,1]
lstFindsHighestThreeNumbers = lambda listNum : sorted(listNumData, reverse=True)[:3]
PowTwoOfNumber = lambda item : pow(item,2)
lstSummOfSquares = lambda lstNums : sqrt(sum(map(PowTwoOfNumber, lstFindsHighestThreeNumbers(lstNums))))

#res = pow(6,2) + pow(5,2) + pow(4,2)
#res2 = sqrt(res)
#print(res2)

print (listNumData)
print (lstFindsHighestThreeNumbers(listNumData))
print (lstSummOfSquares(listNumData))

#suma = lambda a,b,c,d : sqrt(a) + sqrt(b) + sqrt(c) + sqrt(d)

#print (suma(5,4,6,1))

