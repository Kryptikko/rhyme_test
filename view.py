from collections import Counter

"""
Example:
Served:

Order: #1 (11s) +2xRistretto (2s) +Espresso + Milk (1,5s) +Lungo + 2xMilk (3s) +Tea (2s) +Tea + Milk (2,5s)
Order #3 (2s) +Tea (2s)
Uncompleted:
Order: #2 (6s) +Lungo + 2xMilk(3s) +Hotmilk + Ristretto(3s) -Espresso -Espresso
Additional: What were the three most served drinks?
Most served: 1. Tea - 3 2. Ristretto - 2 3. Espresso - 1 (or Lungo - 1, doesn’t matter here)
Additional: Output the resources used for completing all drinks and the number of resources that were needed to complete the remaining drinks:
Example:
Used: Water: 0,986l Coffee: 54g Milk: 0,370l
Needed: Water: x,xxxl Coffee: xg Milk: x,xxxl
"""

all_beverages = sum(map(lambda order: map(lambda i: i.item, order.items), orders), [])

cnt = Counter(all_beverages)
for (key, value) in cnt.most_common():
    print "%s : %s" % (key, value)
