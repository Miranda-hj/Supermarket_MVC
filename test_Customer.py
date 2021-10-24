import pytest
from Customer import Customer
from ShoppingCart import ShoppingCart


cus = Customer('Lily')

def test_init_():
    assert cus.myCurrentCart == None
    assert cus.myName == 'Lily'
    assert cus.myTotal == 0
    assert cus.myClubPoint == 0
    assert cus.myCardNumber == 1001
    assert cus.listCart == []

def test_addToCartList():
    cus.myCurrentCart = ShoppingCart()
    cus.listCart.append(cus.myCurrentCart)
    assert  cus.listCart == [cus.myCurrentCart]

def test_calCurrentCost():
    cus.myCurrentCart = ShoppingCart()
    cus.CurrentCart._totalCost = 10
    assert cus.calCurrentCost() == 10

def test_updateTotal():
    cus.myCurrentCart = ShoppingCart()
    cus.CurrentCart._totalCost = 10
    assert cus.updateTotal() == 10

def test_calcClubPoint():
    cus.myCurrentCart = ShoppingCart()
    cus.CurrentCart._totalCost = 10
    assert cus.calcClubPoint() == 1

def test_updateClubPoint():
    cus.myCurrentCart = ShoppingCart()
    update = cus.calcClubPoint = 10
    assert update + cus.myClubPoint == 10
    cus.ClubPoint = update + cus.myClubPoint
    assert cus.ClubPoint == 10

def test_custTrans():
    assert cus.custTrans() == 'Lily 1001 $0 0 \n '

def test_cartAverage():
    cus.myTotal = 10
    cus.myClubPoint = 1
    cus.listCart = ['1 milk','2 sugar']
    average = cus.myTotal/len(cus.CartList)
    assert average == 5
