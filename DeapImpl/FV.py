import random, math, csv
from deap import creator, base, tools, algorithms

CNRate = 0.015
SGRate = 0.005
def compoundfinal(value,rate,year):
    pv = round(value * math.pow((1 + rate),year),2)
    return pv

def startvalue():
    value = inputdata() #input("pls input the value:")
    year = 2 #input("pls input the number of the years:")
    print(compoundfinal(float(value),SGRate,int(year)))

def inputdata():
    sumcount = 0
    with open('./inputdata.csv') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if (row[1] == "x1"):
                monthvalue = 800
            elif (row[1] == "x2"):
                monthvalue = 800
            elif (row[1] == "x3"):
                monthvalue = 400
            else:
                monthvalue = float(row[1])
            sumcount = sumcount + monthvalue
    #print(sumcount/20)
    return sumcount
    

def mothliving():
    sumcount = 6.5 * 22 + 30 * 3
    sumcount = sumcount + 4 * (5 + 20 + 5)
    print(sumcount)

def switchfunc(arg):
    switcher = {1:inputdata,2:startvalue,3:mothliving,4:lambda:"",}
    func = switcher.get(arg,lambda:"nothing")
    return func()

def main():
    print("----start app-----\n")
    inputchose = input("pls select method:\n1. Add input\n2.View FV\n3.Plan Month Living Expense\n")
    switchfunc(int(inputchose))

main()
