from Item import Item
class UnitItem(Item):

    #constructor for UnitItem
    def __init__(self, prodName:str, price:float, qty:int) -> None:
        self.myQuanity = qty
        Item.__init__(self,prodName,price)

    #getter and setter for myQuantity
    @property
    def ProductQuantity(self) ->int:
        return self.myQuanity

    @ProductQuantity.setter
    def ProductQuantity(self, value:int) -> None:
        self.myQuanity = value

    #calculates cost of the unit item
    def calcCost(self) -> float:
        return self._myPrice * self.myQuanity

    #represents the class object as a string
    def __str__(self) -> str:
        return self._myProdName + self._myPrice + self.myQuanity
