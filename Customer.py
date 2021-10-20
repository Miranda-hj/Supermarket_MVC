from datetime import time
from ShoppingCart import ShoppingCart
from typing import List

class Customer:
    NextID = 1001
    #constructor
    def __init__(self, cname:str) -> None:
        self.myCardNumber = Customer.NextID
        Customer.NextID += 1
        self.myCurrentCart = ShoppingCart()
        self.myName = cname
        self.myTotal = 0  
        self.myClubPoint = 0  # awards 1 point for each $10.00 spent at the supermarket.
        self.listCart =[]

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
        return str(self.CustomerName)

    #add current cart to the list of carts
    def addToCartList(self) -> None:
        print("print cart")
        currentCart = self.CurrentCart
        print(currentCart)
        self.listCart.append(currentCart)
        for x in self.listCart:
            print(x)

    #update total purchase to date
    def updateTotal(self) -> None:
        print("wwwwwnijhl")
        print(self.listCart)
        for x in self.listCart:
            print(x)
            print(self.listCart)
            if ShoppingCart.Items == x:
                total = x.calcTotalCost()
                print("1",total)
                return sum(total)

    #calculate club point for the current cart
    def calcClubPoint(self) -> int:
        clubPoint = self.CurrentCart.calcTotalCost() / 10
        print('212221',clubPoint)
        return clubPoint
        

    #update the total club point
    def updateClubPoint(self) -> None:
        prePoint = self.myClubPoint
        print("preoint",prePoint  )
        updatePoint = self.calcClubPoint()
        print("wewewt",updatePoint  )
        totalPoint = prePoint + updatePoint
        self.myClubPoint = totalPoint

    #list the summary of all the previous transactions
    def custTrans(self) -> str:
        for list in self.listCart:
           return list

    #List the details of all the previous transactions
    def custDetailTrans(self) -> str:
        for list in self.listCart:
            return self.CustomerName + " " + str(list)


    #average cart total 
    def cartAverage(self) -> float:
        for list in self.listCart:
            if ShoppingCart.Items == list:
                total = ShoppingCart.calcTotalCost()
                lenght = len(self.listCart)
                return sum(total) % lenght

