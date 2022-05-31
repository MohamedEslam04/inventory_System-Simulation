import random

showRoom = 4;
inventory = 3;
SH_R_E_U = []; # showroom ending unit
INV_E_U = []; # inventory ending unit
period = 3;
SH_S_L = 5; # showroom standard level (capacity)
Inv_S_L = 10; # inventory standard level (capacity)
leadTime = 2;
allLeadTime = [];
flag = 0;
demand = 0;
allDemand = [];
order =5;
allOrders = [];
demandAfterPeriod = 0;
shortageCondetion = 0;
i = 1;
nomOfDays = 1000;

for i in range(nomOfDays):
    # the refill of the inventory and the showroom
    if i == (flag + leadTime):
        # Refill the showroom
        if showRoom < SH_S_L:
            shortage = SH_S_L - showRoom; # the shortage of cars in the showroom
            showRoom = showRoom + shortage; # refill the showroom
            order = order - shortage; # Remove the cars that have been used in the showroom from the order
        # Refill the inventory
        if order > 0:
            inventory = inventory + order; # refill the inventory with the rest of the order

    # the simulation process
    # Generate the demand using random variable r1
    r1 = random.uniform(0,1);
    if 0.01 <= r1 < 0.04:
        demand = 0;
    elif 0.04 <= r1 < 0.34:
        demand = 1;
    elif 0.34 <= r1 < 0.70:
        demand = 2;
    elif 0.70 <= r1 < 0.86:
        demand = 3;
    elif 0.86 <= r1 < 1:
        demand = 4;

    allDemand.append(demand);
    demandAfterPeriod = demandAfterPeriod + demand; # collect all demand during the period time
    if demand <= inventory:
        inventory = inventory - demand;
    else:
        restCars = demand - inventory; #restCars is the deffirence between demand and the rest of cars in the inventory
        showRoom = showRoom - restCars;
        inventory = 0;

    # the review after the period time
    if i % period == 0:
        r2 = random.uniform(0, 1);
        if 0.01 <= r2 < 0.5:
            leadTime = 1;
        elif 0.5 <= r2 < 0.85:
            leadTime = 2;
        elif 0.85 <= r2 < 1:
            leadTime = 3;
        allLeadTime.append(leadTime);
        order = demandAfterPeriod; # order new cars depending on the demand during the period time
        allOrders.append(order);
        demandAfterPeriod = 0;
        flag = i; # flag is to the day of the review. the leadTime will be added to this flag

    # counting the days that had shortage
    if (showRoom+inventory) < 0:
        shortageCondetion +=1;

    SH_R_E_U.append(showRoom);
    INV_E_U.append(inventory);

# 1. The average ending units in showroom and the inventory.
SH_Av_E_U = sum(SH_R_E_U)/nomOfDays;
INV_Av_E_U = sum(INV_E_U)/nomOfDays;
DemandAv = sum(allDemand)/nomOfDays;
leadTimeAv = sum(allLeadTime)/nomOfDays;
print("The average ending units in showroom = ", int(SH_Av_E_U));
print("The average ending units in inventory = ", int(INV_Av_E_U));
print("The average of demand = ", int(DemandAv));
print("The average of lead time = ", int(leadTimeAv));

# 2. The number of days when a shortage condition occurs.
print("The number of days when a shortage condition occurs = ", shortage);

# Histogarms for the showroom and inventory ending points
# import matplotlib.pyplot as plt
#
# plt.hist(SH_R_E_U, bins=100)
# plt.show()
# plt.hist(INV_E_U, bins=100)
# plt.show()
# plt.hist(allDemand, bins=100)
# plt.show()