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

print(payment(14000-2500,0.08/12,48))
print(Presentpayment(0.08/12,24,632))
print(payment(Presentpayment(0.08/12,24,280),0.05/12,24))
print(payment(Presentpayment(0.08/12,24,280),0.08/12,24))
f1= FV(37160.26,0.06,1)
f2 =FV(18000,0.07,3)*0.27
f3 = FV(55000,0.08,12)
p1 = PV(1600,0.05,1)

test1 = annuity(5000001,25,0.08)
#print (test1)
print (Futurepayment(0.07,19,4100))
#print ('Buy:'+str(f1))
#jeff
#print ('Untouch:'+str(f2))  #marge
#print ('Less:'+str(f1-f2))