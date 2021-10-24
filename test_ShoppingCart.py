
import pytest
from ShoppingCart import ShoppingCart
from UnitItem import UnitItem
from WeightItem import WeightItem
from datetime import datetime

sc = ShoppingCart()

def test_init_():
    assert sc._shoppingDate == datetime.now().strftime('%y/%m/%Y %H:%M:%S')
    assert sc._list == []
    assert sc._totalCost == 0

def test_addUnitItem():
    item = UnitItem('Milk',2.99,1)
    sc._list.append(item)
    assert sc._list == [item]
    cost = item.calcCost()
    assert cost == 2.99
    sc._totalCost += cost
    assert sc._totalCost == 2.99
    

def test_addweight():
    witem = WeightItem('Pork',18.99)
    witem.scale
    sc._list.append(witem)
    assert sc._list == [witem]

def test_calcTotalCost():
    assert sc.calcTotalCost() == 2.99

