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
        self._totalCost = 0

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
        return self._totalCost

    @cartTotal.setter
    def cartTotal(self,value):
        self._totalCost = value
    
    #represents the class object as a string
    def __str__(self) -> str:
        return self._shoppingDate + " $"  + str(self._totalCost) + "  \n       " +  " ".join([str(item) for item in self._list]) + "\n"

    #adds unit item to the cart and returns the cost
    def addUnitItem(self, prod:str, uprice:float, qty:int) -> float:
        item = UnitItem(prod,uprice,qty)
        string = item.displayUnitItem()
        print(string)
        self._list.append(string)
        cost = item.calcCost()
        self._totalCost = self._totalCost + cost
        print("total",self.cartTotal) 
        print(self.__str__())
        return self.__str__()

    #adds weight item to the cart and returns the cost
    def addWeightItem(self, prod:str, wprice:float) -> float:
        item = WeightItem(prod,wprice)
        item.scale()
        # weight = item.ProductWeight
        self._list.append(item)
        cost = round(item.calcCost(),2)
        preCost = self.cartTotal
        totalCost = preCost + cost
        self.cartTotal = totalCost
        return self.__str__()

    #calculate the total cost of the items in the cart
    def calcTotalCost(self) -> float:
        return self.cartTotal
        
