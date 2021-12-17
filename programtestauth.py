import itertools

def condense(input):
    sum = 0
    for i in  input:
        sum += ord(i)
    return format(sum % 16,'b').zfill(4)

symbol = ["0","1","2","3","4","5","6","7","8","9"]

listOfM = [item for item in itertools.product(symbol,repeat=2)]

dictionnaireOfCollision = dict()

def testcolision():
    for i in listOfM:
        dictionnaireOfCollision[condense(i)] = []
        for j in listOfM:
            if(i!=j):
                if(condense(i)==condense(j)):
                    if ''.join(j) not in dictionnaireOfCollision[condense(i)]:
                        dictionnaireOfCollision[condense(i)].append(''.join(j))
                    if ''.join(i) not in dictionnaireOfCollision[condense(i)]:
                        dictionnaireOfCollision[condense(i)].append(''.join(i))

def findpreimagefirst(y):
    for m in listOfM:
        if condense(m)==y:
            return ''.join(m)
    return None


def findpreimagesecond(i):
    for j in listOfM:
        if(i!=j):
            if(condense(i)==condense(j)):
                return ''.join(j)

print("CONDENSE: ",condense("0006"))
# testcolision()
# print("dict",dictionnaireOfCollision)

def testPreimageFirstAll():
    for i in itertools.product(["0","1"],repeat=4):
        print(f"preimage premier ordre {''.join(i)} = h({findpreimagefirst(condense(i))})")

def testPreimageSecondAll():
    for i in listOfM:
        print(f"preimage second ordre x={''.join(i)} est x'={findpreimagesecond(i)} h(x)={condense(i)}")

# print("trouver préimage premier de 0001",findpreimagefirst("0110"))
# print("trouver préimage second de 15",findpreimagesecond("15"))
testPreimageFirstAll()
testPreimageSecondAll()