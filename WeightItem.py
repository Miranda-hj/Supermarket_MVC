from Item import Item
import random


class WeightItem(Item):

    #constructor for UnitItem
    def __init__(self, prodName:str, price:float) -> None:
        self._myWeight = 0.00
        Item.__init__(self,prodName,price)
        
    #getter and setter for myWeight
    @property
    def ProductWeight(self) -> int:
        return self._myWeight

    @ProductWeight.setter
    def ProductQuantity(self, qty:int) -> None:
        self._myWeight = qty

    #calculates cost of the weight item
    def calcCost(self) -> float:
        return self._myWeight * self._myPrice

    #represents the class object as a string
    def __str__(self) -> str:
        return self._myProdName + " $" + str(self._myPrice) + " " + str(self._myWeight) + " $" + str(round((self._myWeight * self._myPrice),2))
 
    #method to generate random number between 0.0 and 4.0
    def scale (self) -> float:
        weight = round(random.uniform(0.0,4.00),2)
        self._myWeight = weight
        return self._myWeight
