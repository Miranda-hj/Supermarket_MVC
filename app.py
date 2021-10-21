# import tkinter as tk
# from tkinter import Frame, ttk
# from tkinter.messagebox import showinfo
# from tkinter.constants import END, LEFT, TOP
from flask import Flask, render_template,request,jsonify
from Supermarket import Supermarket
from Customer import Customer

market = Supermarket()

app = Flask(__name__)



@app.route('/')
def superMarket():
    # read file
    try: 
        customerName = []
        customerNumberList = []
        f_customer = open('./asessment_part_2/SUpermarket_MVC/Customers.txt','r')
        customer = f_customer.readlines()
        for name in customer:
            customerList = name.replace('\n', '')
            customerName.append(customerList)
        print(customerName)
        for cName in customerName:
            market.addCustomer(cName)
            id = market.getCustomerID(cName)
            customerNumberList.append(id) 
        f_customer.close()
    except:
        print("Error")
    return render_template('supermarket.html', customerName = customerName, id = customerNumberList )


@app.route('/selectCustomer',methods = ['POST'])
def selectCustomer():
     customer = request.form['name']
     customerID = market.getCustomerID(customer)
     return jsonify({"cardNumber": customerID})

@app.route('/startShopping',methods = ['POST'])
def startShopping():
    cusName = request.form['name']
    print('customer:',cusName)
    market.startShopping(cusName)
    return jsonify()

@app.route('/customerInfo',methods = ['POST'])
def customerInfo():
    customer = request.form['customerName']
    print(customer)
    customerID = market.getCustomerID(customer)
    customerClubPoint = market.getCustomerClubPoint(customer)
    DetailTrans = market.getCustomerTransDetail(customer)
    totalCost = market. getCustomerClubPoint(customer)*10
    message = customer + " " +  str(customerID) + " " + str(customerClubPoint) + " " +  str(totalCost) + "\n   " + str(DetailTrans)
    return jsonify({"message": message})


@app.route('/addtoCart',methods = ['POST'])
def addtoCart():
    cName = str(request.form['customerName'])
    prodName = str(request.form['ProdName'])
    try: 
        qty = int(request.form['unitNumber'])
        price = float(request.form['pricePerUnit'])
        market.addCustUnitItem(cName, prodName, price, qty)
        message = prodName + ' $' + str(round(price*qty,2))
    except:
        price = float(request.form['pricePerKilo'])
        weight = market.addCustWeightItem(cName, prodName, price)
        message = prodName + ' $' + str(round(price*weight,2))
        return jsonify({'weight':weight,"message": message})
    return jsonify({"message": message})
     

@app.route('/checkOut',methods = ['POST'])
def checkOut():
    cName = str(request.form['name'])
    total = market.calcCustCartTotal(cName)
    market.addCustCart(cName)
    currentPoint = market.currentClubPoint(cName)
    currentPointMessage = "Club Point Earned " + str(currentPoint)
    TotalPoint = market.getCustomerClubPoint(cName)
    TotalPointMessage = "New Club Point " + str(TotalPoint)
    return jsonify({'totalCost':total,"currentPoint":currentPointMessage,"TotalPoint":TotalPointMessage})


@app.route('/salesByCustomer',methods = ['POST'])
def salesByCustomer():
    detail = market.listCustomerTransaction()
    message = str(detail)
    print('customer:',detail)
    return jsonify({'message':message})

@app.route('/totalSales',methods = ['POST'])
def totalSales():
    total = market.calcTotalSales()
    return jsonify({'total':total})

@app.route('/topCustomer',methods = ['POST'])
def topCustomer():
    message = market.findTopCustomer()
    return jsonify({'message':message})

@app.route('/averageCart',methods = ['POST'])
def averageCart():
    message = market.getCustAvg()
    return jsonify({'message':message})

@app.route('/monthlyDisplay',methods = ['POST'])
def monthlyDisplay():
    market.displayMonthlyCost()
    pass

if __name__ == '__main__':
    Flask.run(app,debug=True)