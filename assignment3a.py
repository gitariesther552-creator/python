earnings = 80000

if earnings < 5999:
    print("The monthly contribution is 150.00:",)
elif earnings >=5999 and earnings <=7999:
    print("The monthly contribution is 300.00:",)
elif earnings >=7999 and earnings <=11999:
    print("The monthly contribution is 400.00:",)
elif earnings >=11999 and earnings <=14999:
    print("The monthly conribution is 500.00:",)
elif earnings >=14999 and earnings <=19999:
    print("The monthly contribution is 600.00:",)
elif earnings >=19999 and earnings <=24999:
    print("The monthly contribution is 750.00:",)
elif earnings >=24999 and earnings <=29999:
    print("The monthly contribution is 850.00:",)
elif earnings >=29999 and earnings <=49999:
    print("The monthly contribution is 1000.00:",)
elif earnings >=49999 and earnings <=99999:
    print("The monthly contribution is 1500.00:",)
elif earnings == 100000:
    print("The monthly interest is 2000.00:",)
else:
    print("Out of contibution")
