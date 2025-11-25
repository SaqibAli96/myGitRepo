
def printNum():
    list1 = []
    for i in range(10):
        list1.append(i)
    return list1

#even checker added below

def eve_checker(list1):
    for i in list1:
        if i%2 == 0:
            print(i)

eve_checker(printNum())
