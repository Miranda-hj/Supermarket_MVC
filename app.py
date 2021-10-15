# import tkinter as tk
# from tkinter import Frame, ttk
# from tkinter.messagebox import showinfo
# from tkinter.constants import END, LEFT, TOP
from flask import Flask, render_template,request,jsonify
from Supermarket import Supermarket

market = Supermarket()

app = Flask(__name__)



@app.route('/')
def superMarket():
    # read file
    try: 
        customerName = []
        customerNumberList = []
        f_customer = open('./asessment_part_2/Customers.txt','r')
        customer = f_customer.readlines()
        for name in customer:
            customerList = name.replace('\n', '')
            customerName.append(customerList)
        print(customerName)
        for cName in customerName:
            market.addCustomer(cName)
            id = market.getCustomerID(cName)
            customerNumberList.append(id)
        # close file      
        f_customer.close()
    except:
        print("Error")
    return render_template('supermarket.html', customer = market.customerList, 
    shoppingCart = market.shoppingCart, customerName = customerName, customerNumberList = customerNumberList )


@app.route('/startShopping',methods = ['POST'])
def startShopping():
    pass

@app.route('/nextCustomer',methods = ['POST'])
def nextCustomer():
    pass

@app.route('/exit',methods = ['POST'])
def exit():
    pass

@app.route('/customerInfo',methods = ['POST'])
def customerInfo():
    pass

@app.route('/ddtoCart',methods = ['POST'])
def addtoCart():
    cName = request.form.get('customerName')
    prodName = request.form.get('ProdName')
    try: 
        qty = request.form.get('unitNumber')
        price = request.form.get('pricePerUnit')
        market.addCustUnitItem(cName, prodName, price, qty)
    except:
        price = request.form.get('pricePerKilo')
        market.addCustWeightItem(cName, prodName, price)
    else:
        print("Error")
    

@app.route('/newItem',methods = ['POST'])
def newItem():
    pass

@app.route('/checkOut',methods = ['POST'])
def checkOut():
    cName = request.form.get('customerName')
    market.calcCustCartTotal(cName)

@app.route('/salesbyCustomer',methods = ['POST'])
def salesByCustomer():
    pass

@app.route('/totalSales',methods = ['POST'])
def totalSales():
    pass

@app.route('/topCustomer',methods = ['POST'])
def topCustomer():
    pass

@app.route('/averageCart',methods = ['POST'])
def averageCart():
    pass

if __name__ == '__main__':
    Flask.run(app,debug=True)