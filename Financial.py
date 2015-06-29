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

def PAF(rate,growth,period):
    a1 = 1/(rate-growth)
    a2 = 1-(math.pow((1+growth),period)/math.pow((1+rate),period))
    return a1*a2

HPVn = 23000*PAF(0.07,0.04,45)
print(HPVn)

totaltuionpv = 14000+NPV([FV(14000,0.05,1),FV(14000,0.05,2),FV(14000,0.05,3)],0.07)
print(totaltuionpv)

livingpv = NPV([8000,8500,9000,9500],0.07)
print(livingpv)

CPVn = 43000*PAF(0.07,0.04,41)
print(CPVn)
print(752726.58-livingpv-totaltuionpv-HPVn)
#print ('Buy:'+str(f1))
#jeff
#print ('Untouch:'+str(f2))  #marge
#print ('Less:'+str(f1-f2))