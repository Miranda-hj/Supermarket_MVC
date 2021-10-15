from abc import ABC, abstractmethod

class Item (ABC):

    #constructor 
    def __init__(self, prodName:str, price:float) -> None:
        self._myProdName = prodName
        self._myPrice = price
    
    #getter and setter for myProdName
    @property
    def ProductName(self) -> str:
        return self._myProdName
    
    @ProductName.setter
    def ProductName(self, value:str) -> None:
        self._myProdName = value

    #getter and setter for myPrice
    @property
    def ProductPrice(self) -> float:
        return self._myPrice

    @ProductPrice.setter
    def ProductPrice(self, value:float) -> None:
        self._myPrice = value

    #abstract method to calculate cost of the item
    @abstractmethod
    def calcCost(self) -> float:
        pass

    #represents the class object as a string
    def __str__(self) -> str:
        return self.ProductName + self._myPrice  



    