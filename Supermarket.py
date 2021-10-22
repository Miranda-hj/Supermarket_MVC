from Customer import Customer
from ShoppingCart import ShoppingCart
from UnitItem import UnitItem
from WeightItem import WeightItem
from typing import List

class Supermarket:

    #constructor
    def __init__(self) -> None:
        self.customerList = []

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

    #get the current club points for a given customer
    def currentClubPoint(self,cname:str) ->int:
        customer = self.findCustomer(cname)
        print(customer,"!!!!!!!!!!#")
        point = customer.calcClubPoint()
        print('current!!!!!',point)
        return point

    # gets the club point for a selected customer 
    def getCustomerClubPoint(self, cname:str) -> int:
        customer = self.findCustomer(cname)
        print(customer,"!@#")
        customer.updateClubPoint()
        point = customer.ClubPoint
        print ("total @@@@@@@",point)
        return point

    # adds unit item to the customer's current cart
    def addCustUnitItem(self,cname:str, prod:str, price:float, qty:int) -> float:
        customer = self.findCustomer(cname)
        customer.CurrentCart.addUnitItem(prod, price, qty)
        print('tttttttttttttttttttt',Customer(customer))

    # adds weight item to the custoer's current cart and returns the weight
    def addCustWeightItem(self, cname:str, prod:str, price:float) -> float:
        customer = self.findCustomer(cname)
        weight = ShoppingCart().addWeightItem(prod, price) / price
        weightItem = round(weight,2)
        print("123",weightItem)
        return weightItem

    # calculates customer's current cart total
    def calcCustCartTotal(self, cname:str) -> float:
        customer = self.findCustomer(cname)
        totalCost = customer.calCurrentCost()
        return totalCost

    # adds the current cart to the customer's cart list
    def addCustCart(self, cname:str) -> None:
        customer = self.findCustomer(cname)
        print(customer)
        customer.addToCartList()
        customer.updateTotal()
        print("22222222222")

    # customer starts shopping with an empty cart
    def startShopping(self, cname:str) -> None:
        customer = self.findCustomer(cname)
        print('shopping',customer)
        customer.myCurrentCart = ShoppingCart()

    #calculates total sales for the supermarket
    def calcTotalSales(self) -> float:
        print("debaugging")
        for customer in self.customerList:
            print(customer)
            cusName = Customer(customer)
            totalSales = cusName.updateTotal()
            print('3',totalSales)
            return totalSales

    # gets the list of customers and their transactions 
    def listCustomerTransaction(self) -> str:
        print('sssssssssssssssssssssssss',self.customerList)
        detailList = ""
        for customer in self.customerList:
            print(customer,'wwwwwwwwwwwwww')
            detailList = detailList + customer.custTrans() + "/n"
            print(type(detailList))
            return detailList

    #finds customer with the most purchase
    def findTopCustomer(self) -> str:
        pass

    # calculates the customer's cart average
    def getCustAvg(self) -> float:
        pass

    # displays transaction details for a customer
    def getCustomerTransDetail(self, cname:str) -> str:
        customer = self.findCustomer(cname)
        ww = customer.myTotal
        print("1111111111111111",ww)
        cusDetail = customer.custDetailTrans()
        return cusDetail

    def displayMonthlyCost(self):
        pass