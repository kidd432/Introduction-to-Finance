__author__ = 'nake12'
import math


def FV(initialPayments,interestrate,period):
    futurevalue = initialPayments*math.pow((1+interestrate),period)
    return futurevalue

def PV(futurevalue,interestrate,period):
    presentvalue = futurevalue/math.pow((1+interestrate),period)
    return presentvalue

def Futurepayment(rate,year,annuity):
    futurePayment = annuity * ((math.pow((1+rate),year)-1)/(rate))
    return futurePayment

def annuity(payment,year,rate):
    ann = payment/ ((math.pow((1+rate),year)-1)/(rate))
    return  ann

def Presentpayment(rate,year,annuity):
    PV = annuity * ((1-(1/math.pow((1+rate),year)))/rate)
    return PV

def payment(PV,rate,year):
    pmt = PV/((1-(1/math.pow((1+rate),year)))/rate)
    return pmt

def EAR(rate,periods):
    ear = math.pow((1+rate/periods),periods)-1
    return ear

def NPV(cashflow,rate):
    temp = 0;
    for index, item in enumerate(cashflow):
        temp += item/math.pow((1+rate),index)
    return round(temp,0)

def IRR(cashflow):
    upper = 1;
    lower =0;
    threshold = 1e-8;
    while(abs(upper-lower)>threshold):
        uppervalue = NPV(cashflow,upper)
        lowervalue = NPV(cashflow,lower)
        midvalue = NPV(cashflow,((upper+lower)/2))
        midpoint = (upper+lower)/2
        if(midvalue==0):
            return round((upper+lower)/2,5)
        if((lowervalue*midvalue)<0):
            upper = midpoint
        if((uppervalue*midvalue)<0):
            lower = midpoint

    return round(midpoint,5)

def discountpaybackperiod(payment,annualsaving,rate):
    i = 2
    while(payment<0):
        payment += annualsaving/(math.pow((1+rate),i))
        i = i +1

    return i

print (discountpaybackperiod(-5150,1300,0.06))
print(IRR([-10600,400, 500,1400, 2500,2500,4000,4000]))
lawn = [-1900,506,506,506,506,506,506,506,506,506,506,506,506,506]

print(NPV(lawn,0.1/52))
cf = [-100, 39, 59, 55, 20]
#print ('Buy:'+str(f1))
#jeff
#print ('Untouch:'+str(f2))  #marge
#print ('Less:'+str(f1-f2))