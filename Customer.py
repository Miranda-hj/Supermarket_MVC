from ShoppingCart import ShoppingCart
from typing import List

class Customer:
    NextID = 1001
    #constructor
    def __init__(self, cname:str) -> None:
        self.myCardNumber = Customer.NextID
        Customer.NextID += 1
        self.myCurrentCart = []
        self.myName = cname
        self.myTotal = 0  
        self.myClubPoint = 0  # awards 1 point for each $10.00 spent at the supermarket.

    #getter and setter for customer's name
    @property
    def CustomerName(self) -> str:
        return self.myName

    @CustomerName.setter
    def CustomerName(self, value:str) -> None:
        self.myName = value

    #getter for card number
    @property
    def CardNumber(self) -> str:
        return self.myCardNumber

    #getter and setter for club point
    @property
    def ClubPoint(self) -> str:
        return self.ClubPoint

    @ClubPoint.setter
    def ClubPoint(self, value:int) -> None:
        self.myClubPoint = value

    #getter for the current cart
    @property
    def CurrentCart(self) ->ShoppingCart:
        return self.CurrentCart

    #getter for the list of carts
    @property
    def CartList(self) -> List[ShoppingCart]:
        return self.CartList

    #getter for the total purchase to date
    @property
    def TotalToDate(self) -> float:
        return self.myTotal

    #represents the class object as a string
    def __str__(self) -> str:
        return self.CustomerName + self.myCardNumber

    #add current cart to the list of carts
    def addToCartList(self) -> None:
        pass

    #update total purchase to date
    def updateTotal(self) -> None:
        pass

    #calculate club point for the current cart
    def calcClubPoint(self) -> int:
        clubPoint = self.TotalToDate / 10
        print(clubPoint)
        return clubPoint

    #update the total club point
    def updateClubPoint(self) -> None:
        updatePoint = self.calcClubPoint()
        self.myClubPoint += updatePoint

    #list the summary of all the previous transactions
    def custTrans(self) -> str:
        pass

    #List the details of all the previous transactions
    def custDetailTrans(self) -> str:
        pass

    #average cart total 
    def cartAverage(self) -> float:
        pass

