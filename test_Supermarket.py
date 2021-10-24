import pytest
from Customer import Customer
from ShoppingCart import ShoppingCart
from Supermarket import Supermarket
from UnitItem import UnitItem

sk = Supermarket()
Lily = Customer('Lily')

def addItem():
    Joy = Customer('Joy')
    sk.customerList.append(Lily)
    sk.customerList.append(Joy)
    jCart = Joy.myCurrentCart = ShoppingCart()
    lCart = Lily.myCurrentCart = ShoppingCart()
    milk = UnitItem('Milk',2.99,1)
    candy = UnitItem('Candy',1.99,1)
    jCart._list.append(milk)
    milkCost = milk.calcCost()
    jCart._totalCost += milkCost
    lCart._list.append(candy)
    candyCost = candy.calcCost()
    lCart._totalCost += candyCost

def test_addCustomer():
    sk.customerList.append(Lily)
    assert sk.customerList == [Lily]
     
def test_findCustomer():
    sk.customerList.append(Lily)
    assert sk.findCustomer('Lily') == Lily
     
def test_getCustomerID():
    assert Lily.CardNumber == 1001  

def test_startShopping():
    sk.customerList.append(Lily)
    cart = Lily.myCurrentCart = ShoppingCart()
    assert Lily.myCurrentCart == cart

def test_currentClubPoint():
    addItem()
    round(float(Lily.calCurrentCost())/ 10,2)
    assert sk.currentClubPoint('Lily') == 0.2

def test_addCustUnitItem():
    assert sk.addCustUnitItem('Lily','Milk',2,1) == None

def test_calcCustCartTotal():
    cart = Lily.myCurrentCart = ShoppingCart()
    total = cart.calcTotalCost()
    assert total == 0

def test_calcTotalSales():
    sk.customerList.append(Lily)
    assert sk.calcTotalSales() == 0

def test_findTopCustomer():
    sk.customerList.append(Lily)
    assert sk.findTopCustomer() == 'Lily 1001 $0 0 \n '
    

def test_displayMonthlyCost():
    Joy = Customer('Joy')
    sk.customerList.append(Lily)
    sk.customerList.append(Joy)
    jCart = Joy.myCurrentCart = ShoppingCart()
    lCart = Lily.myCurrentCart = ShoppingCart()
    Joy.listCart = [jCart]
    Lily.listCart =[lCart]
    milk = UnitItem('Milk',2.99,1)
    candy = UnitItem('Candy',1.99,1)
    jCart._list.append(milk)
    milkCost = milk.calcCost()
    jCart._totalCost += milkCost
    lCart._list.append(candy)
    candyCost = candy.calcCost()
    lCart._totalCost += candyCost
    assert jCart._list == [milk]
    assert lCart._list == [candy]
    assert jCart._totalCost == 2.99
    assert lCart._totalCost == 1.99
    totalCost = 0
    for customer in sk.customerList:
        cart = customer.listCart
        for shoppingCart in cart:
            if shoppingCart._shoppingDate[3:10] == '10/2021':
                totalCost += shoppingCart.cartTotal
            return None 
    assert totalCost == 9.96

def test_displayMonthlyCost_error():
    Joy = Customer('Joy')
    sk.customerList.append(Lily)
    sk.customerList.append(Joy)
    jCart = Joy.myCurrentCart = ShoppingCart()
    lCart = Lily.myCurrentCart = ShoppingCart()
    Joy.listCart = [jCart]
    Lily.listCart =[lCart]
    milk = UnitItem('Milk',2.99,1)
    candy = UnitItem('Candy',1.99,1)
    jCart._list.append(milk)
    milkCost = milk.calcCost()
    jCart._totalCost += milkCost
    lCart._list.append(candy)
    candyCost = candy.calcCost()
    lCart._totalCost += candyCost
    assert jCart._list == [milk]
    assert lCart._list == [candy]
    assert jCart._totalCost == 2.99
    assert lCart._totalCost == 1.99
    totalCost = 0
    for customer in sk.customerList:
        cart = customer.listCart
        for shoppingCart in cart:
            if shoppingCart._shoppingDate[3:10] == 11/2021:
                totalCost += shoppingCart.cartTotal
    assert totalCost == 0
