Herb_Cost,Carn_cost,Aqua_Cost=input("enter cost of each <=10000").split()
Cost_Herb=int(Herb_Cost);Cost_Carn=int(Carn_cost);Cost_Aqua=int(Aqua_Cost)
Herb_Area,Carn_Area,Aqua_Area=input("enter area of each animal <=500").split()
Area_Herb=int(Herb_Area);Area_Carn=int(Carn_Area);Area_Aqua=int(Carn_Area)
No_Herb,Min_Area_Herbs=input("enter no.of herbs <= 20 & min area of herbs <=15").split()
Herb_No=int(No_Herb);Herbs_Min_Area=int(Min_Area_Herbs)
No_Carn,Min_Area_Carns=input("enter no.of carns<= 20 & min area of carns <=15").split()
Carn_No=int(No_Carn);Carns_Min_Area=int(Min_Area_Carns)
No_Aqua,Min_Area_Aqua=input("enter no.of aqua<=20 & min area of aqua <=15").split()
Aqua_No=int(No_Aqua);Aqua_Min_Area=int(Min_Area_Aqua)
Max_Area_Zoo=int(input("entr zoo area <=1000"))
if (Cost_Herb>Cost_Carn) and (Cost_Herb>Cost_Aqua):
   area1=Area_Of_Herbs=Herb_No*Herbs_Min_Area
   cost1=Total_Cost_Herbs=Area_Of_Herbs*Cost_Herb
elif (Cost_Carn>Cost_Herb) and (Cost_Carn>Cost_Aqua):
    area1=Area_Of_Carns=Carn_No*Carns_Min_Area
    cost1=Total_Cost_Carns=Area_Of_Carns*Cost_Carn
else:
    area1=Area_Of_Aqua=Aqua_No*Aqua_Min_Area
    cost1=Total_Cost_Aqua=Area_Of_Aqua*Cost_Aqua
print()
if (Cost_Herb<Cost_Carn) and (Cost_Herb<Cost_Aqua):
    area2=Area_Herb
    cost2=Area_Herb*Cost_Herb
elif (Cost_Carn<Cost_Herb) and (Cost_Carn<Cost_Aqua):
    area2=Area_Carn
    cost2=Area_Carn*Cost_Carn
else:
    area2=Area_Aqua
    cost2=Area_Aqua*Cost_Aqua
print()
if (Cost_Herb>Cost_Carn and Cost_Carn>Cost_Aqua or Cost_Aqua>Cost_Carn and Cost_Carn>Cost_Herb):
    RemainingCost=Cost_Carn
elif (Cost_Carn>Cost_Herb and Cost_Herb>Cost_Aqua or Cost_Aqua>Cost_Herb and Cost_Herb>Cost_Carn):
    RemainingCost=Cost_Herb
else:
    RemainingCost=Cost_Aqua
print()
remainingarea=Max_Area_Zoo-(area1+area2)
cost3=remainingarea*RemainingCost
Min_Cost_Zoo=cost1+cost2+cost3
print(Min_Cost_Zoo)

