from typing import List
from UnitItem import UnitItem
from WeightItem import WeightItem
from Item import Item
from datetime import date, datetime

class ShoppingCart:

    #constructor
    def __init__(self) -> None:
        self._shoppingDate = datetime.now()
        self._list = []

    #getter for purchase date
    @property
    def PurchaseDate(self) -> datetime:
        return self._shoppingDate

    #getter for list of items in the cart
    @property
    def Items(self) -> List[Item]:
        return self._list

    #represents the class object as a string
    def __str__(self) -> str:
        return self._shoppingDate + self._list

    #adds unit item to the cart and returns the cost
    def addUnitItem(self, prod:str, uprice:float, qty:int) -> float:
        item = UnitItem(prod,uprice,qty)
        self._list.append(item)

    #adds weight item to the cart and returns the cost
    def addWeightItem(self, prod:str, wprice:float) -> float:
        item = WeightItem(prod,wprice)
        self._list.append(item)

    #calculate the total cost of the items in the cart
    def calcTotalCost(self) -> float:
        unitCost  = UnitItem.calcCost()
        weightCost = WeightItem.calcCost()
        return unitCost + weightCost



