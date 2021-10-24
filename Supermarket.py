from Customer import Customer
from ShoppingCart import ShoppingCart
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
        point = customer.calcClubPoint()
        return point

    # gets the club point for a selected customer 
    def getCustomerClubPoint(self, cname:str) -> int:
        customer = self.findCustomer(cname)
        customer.updateClubPoint()
        point = customer.ClubPoint
        return point

    # adds unit item to the customer's current cart
    def addCustUnitItem(self,cname:str, prod:str, price:float, qty:int) -> None:
        customer = self.findCustomer(cname)
        customer.CurrentCart.addUnitItem(prod, price, qty)

    # adds weight item to the custoer's current cart and returns the weight
    def addCustWeightItem(self, cname:str, prod:str, price:float) -> float:
        customer = self.findCustomer(cname)
        customer.CurrentCart.addWeightItem(prod, price) 
        for item in customer.CurrentCart._list:
            weight = item._myWeight
        return weight

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

    # customer starts shopping with an empty cart
    def startShopping(self, cname:str) -> None:
        customer = self.findCustomer(cname)
        customer.myCurrentCart = ShoppingCart()

    #calculates total sales for the supermarket
    def calcTotalSales(self) -> float:
        totalCost = 0
        for customer in self.customerList:
            sales = customer.myTotal
            totalCost += sales
        return totalCost

    # gets the list of customers and their transactions 
    def listCustomerTransaction(self) -> str:
        detailList = ""
        for customer in self.customerList:
            detailList += customer.custTrans() + "\n"
        return detailList

    #finds customer with the most purchase
    def findTopCustomer(self) -> str:
        topCost = []
        for customer in self.customerList:
            cost = customer.myTotal
            topCost.append(cost)
        maxPurchase = max(topCost)
        for customer in self.customerList:
            if customer.myTotal == maxPurchase:
                cusDetail = customer.custDetailTrans()
        return cusDetail

    # calculates the customer's cart average
    def getCustAvg(self) -> str:
        cusAugList = ""
        for customer in self.customerList:
            cusAverage = customer.cartAverage()
            cusAugList += cusAverage + "\n\n"
        return cusAugList
        
    # displays transaction details for a customer
    def getCustomerTransDetail(self, cname:str) -> str:
        customer = self.findCustomer(cname)
        cusDetail = customer.custDetailTrans()
        return cusDetail

    #select customer total sales for month
    def displayMonthlyCost(self, month:str) -> str: 
        monthMessage = "Sales for Month: " + month + "\n"
        totalCost = 0
        for customer in self.customerList:
            cart = customer.listCart
            for shoppingCart in cart:
                if shoppingCart._shoppingDate[3:10] == month:
                    monthMessage += customer.__str__() + "\n"
                    totalCost += shoppingCart.cartTotal  
        return monthMessage + "Total: $" + str(totalCost)
               
           