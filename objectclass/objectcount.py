class ObjectCounter:

    numberOfObject = 0

    def __init__(self):
        ObjectCounter.numberOfObject+=1

    #static method
    def displayCount():
        print(ObjectCounter.numberOfObject)

o1=ObjectCounter()
o2=ObjectCounter()

ObjectCounter.displayCount()
