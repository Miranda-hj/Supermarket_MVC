import pytest
from Item import Item
from UnitItem import UnitItem
from WeightItem import WeightItem
import random


def test_init_():
    assert UnitItem('Milk',4,1)._myProdName == 'Milk'
    assert UnitItem('Milk',4,1)._myPrice == 4
    assert WeightItem('Pork',18.99)._myWeight == 0

def test_calcCost():
    assert UnitItem('Milk',4,1).calcCost() == 4
    pork = WeightItem('Pork',18.99)
    weight = round(random.uniform(0.0,4.00),2)
    pork._myWeight = weight
    assert pork.calcCost() == weight * 18.99

def test_scale():
    weight = round(random.uniform(0.0,4.00),2)
    pork = WeightItem('Pork',18.99)
    pork._myWeight = weight
    assert pork._myWeight == weight


