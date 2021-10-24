from ShoppingCart import ShoppingCart
from typing import List



class Customer:
    NextID = 1001
    #constructor
    def __init__(self, cname:str) -> None:
        self.myCardNumber = Customer.NextID
        Customer.NextID += 1
        self.myCurrentCart = None
        self.myName = cname
        self.myTotal = 0  
        self.myClubPoint = 0  # awards 1 point for each $10.00 spent at the supermarket.
        self.listCart = []

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
    def ClubPoint(self) -> float:
        return self.myClubPoint

    @ClubPoint.setter
    def ClubPoint(self, value:int) -> None:
        self.myClubPoint = value

    #getter for the current cart
    @property
    def CurrentCart(self) ->ShoppingCart:
        return self.myCurrentCart
    
    #getter for the list of carts
    @property
    def CartList(self) -> List[ShoppingCart]:
        return self.listCart

    #getter for the total purchase to date
    @property
    def TotalToDate(self) -> float:
        return self.myTotal

    #represents the class object as a string
    def __str__(self) -> str:
        return str(self.CustomerName) + " " + str(self.myCardNumber) + " $" + str(self.myTotal) + " " + str(self.myTotal)

    #add current cart to the list of carts
    def addToCartList(self) -> None:
        self.listCart.append(self.myCurrentCart)

    #calculate current cart cost 
    def calCurrentCost(self) -> float:
        cost = self.CurrentCart.calcTotalCost()
        return cost 

    #update total purchase to date
    def updateTotal(self) -> None:
        preTotal = self.myTotal
        updateCost = self.calCurrentCost()
        totalCost = preTotal + updateCost
        self.myTotal = totalCost
        return totalCost

    #calculate club point for the current cart
    def calcClubPoint(self) -> float:
        clubPoint = round(float(self.calCurrentCost())/ 10,2)
        return clubPoint
        
    #update the total club point
    def updateClubPoint(self) -> None:
        prePoint = self.myClubPoint
        updatePoint = self.calcClubPoint()
        totalPoint = prePoint + updatePoint
        self.ClubPoint = totalPoint

    #list the summary of all the previous transactions
    def custTrans(self) -> str:
        detailList = ""
        for cList in self.listCart:
            summary = cList.summary()
            detailList = detailList + str(summary)
        return str(self.CustomerName) + " " + str(self.myCardNumber) + " $" + str(self.myTotal) + " " + str(self.myClubPoint) + " \n " + detailList

    #List the details of all the previous transactions
    def custDetailTrans(self) -> str:
        detailList = ""
        for cList in self.listCart:
            detailList = detailList + " " + str(cList)
        return str(self.CustomerName) + " " + str(self.myCardNumber) + " $" + str(self.myTotal) + " " + str(self.myClubPoint) + " \n " + detailList

    #average cart total 
    def cartAverage(self) -> str:
        try:
            totalCost = self.myTotal
            number = len(self.CartList)
            average = totalCost / number
        except:
            average = 0
        return self.__str__() + "\nAverage Purchase: $" + str(average)


