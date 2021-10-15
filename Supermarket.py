from Customer import Customer
from ShoppingCart import ShoppingCart
from UnitItem import UnitItem
from WeightItem import WeightItem
from typing import List

class Supermarket:

    #constructor
    def __init__(self) -> None:
        self.customerList = []
        self.shoppingCart = []

    #getter for the list of customers
    @property 
    def CustomerList(self) -> List[Customer]:
        return self.customerList

    #creates and adds new customer to the customer list
    def addCustomer(self, cname:str):
        aCustomer = Customer(cname)
        self.customerList.append(aCustomer)

    # finds a customer object based on a customer's name
    def findCustomer(self, cname:str) -> Customer:
        for customer in self.customerList:
            if customer.CustomerName == cname:
                return customer
        return None

    # finds a customer's card number based on a customer's name
    def getCustomerID(self, cname:str) -> int:
        for customer in self.customerList:
            if customer.CustomerName == cname:
                return customer.CardNumber
        return None

    # gets the club point for a selected customer 
    def getCustomerClubPoint(self, cname:str) -> int:
        for customer in self.customerList == cname:
            if customer.CustomerName == cname:
                print (customer.ClubPoint)

    # adds unit item to the customer's current cart and returns the cost
    def addCustUnitItem(self, cname:str, prod:str, price:float, qty:int) -> float:
        pass

    # adds weight item to the customer's current cart and returns the cost
    def addCustWeightItem(self, cname:str, prod:str, price:float) -> float:
        pass

    # calculates customer's current cart total
    def calcCustCartTotal(self, cname:str) -> float:
        pass

    # adds the current cart to the customer's cart list
    def addCustCart(self, cname:str) -> None:
        pass

    # customer starts shopping with an empty cart
    def startShopping(self, cname:str) -> None:
         for customer in self.customerList == cname:
            if customer.CustomerName == cname:
                pass

    #calculates total sales for the supermarket
    def calcTotalSales(self) -> float:
        pass

    # gets the list of customers and their transactions 
    def listCustomerTransaction(self) -> str:
        pass

    #finds customer with the most purchase
    def findTopCustomer(self) -> str:
        pass

    # calculates the customer's cart average
    def getCustAvg(self) -> float:
        pass

    # displays transaction details for a customer
    def getCustomerTransDetail(self, nm:str) -> str:
        pass

