requires python 2.7
source env/bin/active
pip install -r requirments.txt
python3 -m venv ./env


Coffee shop
At the Rhyme team, we enjoy our coffee, except Sergey... Sergey prefers tea. Ivo almost always gets Ristretto single or double shot, Ned’s preferences range between Espresso to Lungo with milk. Nadya sometimes gets just a cup of milk.

Ristretto: 22ml of water 9g of coffee 1s to make
Espresso: 35ml of water 9g of coffee 1s to make
Lungo: 70ml of water 9g of coffee 2s to make
Tea: 250 ml of water 2s to make
Hot Milk: 250 ml of milk 2s to make

Each drink can have Milk added to it. One add-on of Milk is 20ml. Addon of milk takes 0,5s.
Write a simple go application that accepts two arguments:
./shop <number of coffee machines> <input file with orders in JSON format>
Each coffee machine starts with:
● 1l of water
● 55g of coffee
● 0,5l of milk
There is unlimited tea in the shop.
Orders should be served in the same order they were received. One coffee machine can make one drink at a time. If there is not enough water, coffee or milk in a given machine, the drink should be made on another machine if possible.
Example of contents of input file: [ { “order”: 1,
“items”: [
{ “item”: “ristretto”, “add”: [“ristretto”] }, { “item”: “espresso”, “add”: [“milk”]}, { “item”: “lungo”, “add”: [“milk”, “milk”] }, { “item”: “tea”}, { “item” “tea”, “add”: [“milk”]}, ] }, { “order”: 2, “items”: [
{ “item”: “lungo”, “add”: [“milk”, “milk”] }, { “item”: “hotmilk”, “add”: [“ristretto”] }, { “item”: “espresso”}, { “item”: “espresso”}, ] }, { “order”: 3, “items”: [
{ “item”: “tea”} ], } ]
For example, if there is no more coffee in all machines and the shop cannot finish the second order after the “hotmilk” is completed, the shop still can finish the third order and serve a cup of tea.
The goal is to serve as many completed orders as possible.
The output of the program should be all served drinks grouped by orders and the time it took to serve a given order. All drinks that were completed but not served (because the order was not fully completed) should be listed at the bottom as “uncompleted order”.
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

