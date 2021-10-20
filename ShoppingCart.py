from typing import List
from UnitItem import UnitItem
from WeightItem import WeightItem
from Item import Item
from datetime import datetime


class ShoppingCart:

    #constructor
    def __init__(self) -> None:
        self._shoppingDate = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        self._list = []
        self._cartTotal = 0.00

    #getter for purchase date
    @property
    def PurchaseDate(self) -> datetime:
        return self._shoppingDate

    #getter for list of items in the cart
    @property
    def Items(self) -> List[Item]:
        return self._list

    @property
    def cartTotal(self) -> float:
        return self._cartTotal


    @cartTotal.setter
    def cartTotal(self,value) ->float:
        self._cartTotal = value

    #represents the class object as a string
    def __str__(self) -> str:
        return self._shoppingDate + " $" + str(self._cartTotal)

    #adds unit item to the cart and returns the cost
    def addUnitItem(self, prod:str, uprice:float, qty:int) -> float:
        item = UnitItem(prod,uprice,qty)
        self._list.append(item)
        cost = item.calcCost()
        preCost = self.cartTotal
        print(preCost)
        totalCost = preCost + cost
        print(totalCost)
        self.cartTotal = totalCost
        
        return cost

    #adds weight item to the cart and returns the cost
    def addWeightItem(self, prod:str, wprice:float) -> float:
        item = WeightItem(prod,wprice)
        item.scale()
        weight = item.ProductWeight
        print('weight:',weight)
        self._list.append(item)
        cost = round(item.calcCost(),2)
        print('cost',cost)
        preCost = self.cartTotal
        print(preCost)
        totalCost = preCost + cost
        self.cartTotal = totalCost
        print('uuuu',totalCost)
        return cost

    #calculate the total cost of the items in the cart
    def calcTotalCost(self) -> float:
        return self._cartTotal
