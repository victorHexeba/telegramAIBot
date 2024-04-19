import hexebaML
import hexeba_binance
import time
import binance
from datetime import datetime
import tweepy
from binance.client import Client
import sys
import telebot
from telebot import types
key1="T0JJcmRlNDB5ZWxpRXdsQVplSG06MTpjaQ"
key2="JyHayeECaIJTtjIXzODCNJzO27koEorJBTpD3bqTGsaONPMLrQ"
secret1="2282928749-N6NqJ9I2apHsCT7B0b3s5NJgLDkha4hNmKku5aI6"
secret2="fOg6AxFz9IYvrWtFFuNGfxA76BAKfknbvFERV1ndlAT6q"
auth = tweepy.OAuthHandler(key1, key2)
bot = telebot.TeleBot("1279865343:AAHeNYVTk_L8vDswHZesTZ-p5qUzxtXcM00")
auth.set_access_token(secret1,secret2)
api = tweepy.API(auth)
apikey1 = "lCfjiDfO19vYrVD39z8ABo8LyGGiQwR4TEL7GRPqzwr5CHNmlY7tebfc5jyu9DMg"
apikey2 = "nla4D5Xo5FbEmWYeay8SLb1dIWk9dsUAJoan8V9ks5gBPGsNcJFSfSHPSPgY4Djl"
modulename = "vcapital"
tradestarttime = "tradestarttime"
folder = "capital"
tradefile = "tradetrack"
badpairs = "badpairsbrain"
check = hexebaML.read_file(modulename,folder)
def start():
    hexebaML.clean_brain(modulename,folder)
    check = hexebaML.read_file(modulename,folder)
    if(check==""):
        
        newid = ["algoname","apikey1","apikey2","symbol","tradestate","leverage","position","balance","entryprice","exitprice","takeprofit_long","takeprofit_short","stoploss_long","stoploss_short","datetime","wallet_percent","tstoplong_in","tstopshort_in","max_long","max_short","longbalance","shortbalance","hedgestate"]
        data = ["Hedge Profiter","lCfjiDfO19vYrVD39z8ABo8LyGGiQwR4TEL7GRPqzwr5CHNmlY7tebfc5jyu9DMg","nla4D5Xo5FbEmWYeay8SLb1dIWk9dsUAJoan8V9ks5gBPGsNcJFSfSHPSPgY4Djl","BTCUSDT","closed","20","long","1000","29800","30000","29000","30000","30000","30000","020119","90","inactive","inactive","90","90","500","500","0"]
        hexebaML.update_full_module_with_list(modulename,newid,data,folder)

    tradestate = hexebaML.readbrain_with_idname("tradestate",modulename,folder)
    hedgestate = hexebaML.readbrain_with_idname("hedgestate",modulename,folder)
    if(hedgestate == "0"): 


        open_trade(modulename,folder)     
    else:

        close_trade(modulename,folder)
    print("DONE CHECKING....")
  #  sys.modules[__name__].__dict__.clear()   

def close_trade(modulename,folder):
    symbol = hexebaML.readbrain_with_idname("symbol",modulename,folder)
    takeprofit_long = float(hexebaML.readbrain_with_idname("takeprofit_long",modulename,folder))
    takeprofit_short = float(hexebaML.readbrain_with_idname("takeprofit_short",modulename,folder))
    stoploss_long = float(hexebaML.readbrain_with_idname("stoploss_long",modulename,folder))
    stoploss_short = float(hexebaML.readbrain_with_idname("stoploss_short",modulename,folder))
    max_short = float(hexebaML.readbrain_with_idname("max_short",modulename,folder))
    max_long = float(hexebaML.readbrain_with_idname("max_long",modulename,folder))
    entry = float(hexebaML.readbrain_with_idname("entryprice",modulename,folder))
    tstoplong = hexebaML.readbrain_with_idname("tstoplong_in",modulename,folder)
    tstopshort = hexebaML.readbrain_with_idname("tstopshort_in",modulename,folder)
    price_now = float(hexeba_binance.check_price(apikey1,apikey2,symbol))
    position = float(hexebaML.readbrain_with_idname("hedgestate",modulename,folder))
    # if(max_long==entry):
    #     entry = price_now
    # if(max_short==entry):
    #     entry = price_now
    p_pnl_long = max_long - entry
    p_pnl_short = entry - max_short
    c_pnl_long = price_now - entry
    c_pnl_short = entry - price_now
    c_pnl_long_percent = abs(c_pnl_long/p_pnl_long)*100
    c_pnl_short_percent = abs(c_pnl_short/p_pnl_short)*100
    tstop = 5
    pstop = 100-tstop
    new_data = price_now
    parent_data1 = takeprofit_long
    parent_data2 = takeprofit_short
    rangepercent = 0.5
    s = hexebaML.range_check(new_data,parent_data2,rangepercent)
    l = hexebaML.range_check(new_data,parent_data1,rangepercent)
    
    
    parent_data3 = stoploss_long
    parent_data4 = stoploss_short
    rangepercentx = 3
    sllong = hexebaML.range_check(new_data,parent_data3,rangepercentx)
    slshort = hexebaML.range_check(new_data,parent_data4,rangepercentx)
    if(position == 1):
        
        print("C_PNL_LONG_PERCENT:{} TSTOP:{} MAX LONG:{} PRICE NOW:{}".format(c_pnl_long_percent,pstop,max_long,price_now))
    if(position == 2):
        print("C_PNL_LONG_PERCENT:{} TSTOP:{} MAX SHORT:{} PRICE NOW:{}".format(c_pnl_long_percent,pstop,max_short,price_now))
    if(position == 1):
        if(tstoplong == "inactive"):
            hexebaML.update_brain_with_idname("tstoplong_in","active",modulename,folder)
            hexebaML.update_brain_with_idname("max_long",price_now,modulename,folder)
        if(price_now > max_long):
            hexebaML.update_brain_with_idname("max_long",price_now,modulename,folder)
        if(c_pnl_long_percent <= pstop):

            hedgeduration = hexebaML.time_difference_file("hedgeclosetime",folder)
            if(hedgeduration >= 30):
                message = "trailingstop"
                close_long(message,modulename,folder)

    if(position == 2):
        if(tstopshort == "inactive"):
            hexebaML.update_brain_with_idname("tstopshort_in","active",modulename,folder)
            hexebaML.update_brain_with_idname("max_short",price_now,modulename,folder)
        if(price_now < max_short):
            hexebaML.update_brain_with_idname("max_short",price_now,modulename,folder)
        if(c_pnl_short_percent <= pstop):
            
            hedgeduration = hexebaML.time_difference_file("hedgeclosetime",folder)
            if(hedgeduration >= 30):
                message = "trailingstop"
                close_short(message,modulename,folder)

    if((position == 1)and(l == "yes")and(price_now >= takeprofit_long)):
        hedgeduration = hexebaML.time_difference_file("hedgeclosetime",folder)
        if(hedgeduration >= 30):
            message = "fixedstop"
            close_long(message,modulename,folder)
    if((position == 2)and(s == "yes")and(price_now <= takeprofit_short)):
        hedgeduration = hexebaML.time_difference_file("hedgeclosetime",folder)
        if(hedgeduration >= 30):
            message = "fixedstop"
            close_short(message,modulename,folder)
    if((position==4)):
        if((price_now >= stoploss_short)and(slshort=="yes")):
            close_hedge_short(modulename,folder)
            
        if((price_now <= stoploss_long)and(sllong=="yes")):
            close_hedge_long(modulename,folder)
        tradeduration = hexebaML.time_difference_file("time",folder)
        if(tradeduration >= 86400):
    #        hexeba_binance.close_hedge_long(apikey1,apikey2,symbol)
     #       hexeba_binance.close_short(apikey1,apikey2,symbol)
            hexebaML.update_brain_with_idname("hedgestate","0",modulename,folder)
            state = "real"
            message = "THIS TRADE HAS BEEN CLOSED FORCEFULLY AS IT EXCEEDED THE PERMITTED DURATION PER TRADE"
            update_socials(state,message)
            #close_hedge long then close short

       
        
n = 0
def take_trade(n):
    try:
        highest_earner = hexeba_binance.get_highest_gainer_by_id(n)
        symbol = highest_earner["symbol"]
        check2 = hexebaML.read_file(tradefile,folder)
        checkresult = hexebaML.check_brain(symbol,badpairs,folder)
        badpairsdata = hexebaML.read_brain(folder,badpairs)
        if(check2==""):
            newid = ["symbol","profit","loss","margin","symbolstate"]
            data = [symbol,"0","0","0","good"]
            hexebaML.update_full_module_with_list(tradefile,newid,data,folder) 
        tsymbol = hexebaML.readbrain_with_idname("symbol",tradefile,folder)
        tsymbolstate = hexebaML.readbrain_with_idname("symbolstate",tradefile,folder)

        interval = "1h"
        supports, resistances = hexeba_binance.get_support_resistance_levels(symbol,interval)
        price_now = float(hexeba_binance.check_markprice(apikey1,apikey2,symbol))
        suplen = len(supports)
        reslen = len(resistances)
        new_sups = []
        new_res = []
        l1=0
        l2=0
        for i in range(suplen):
            sup = float(supports[i])
            l1 = price_now - ((0.5/100)*price_now)
            l2 = price_now - ((2/100)*price_now)
            if((sup <= l1)and(sup >= l2)):
                new_sups.append(sup)
        p1 = 0
        p2=0
        for j in range(reslen):
            res = float(resistances[j])
            # p1 = price_now + ((0.5/100)*price_now)
            # p2 = price_now + ((1/100)*price_now)
            p1 = price_now + ((0.5/100)*price_now)
            p2 = price_now + ((2/100)*price_now)
            if((res >= p1)and(res <= p2)):
                new_res.append(res)
        if(((tsymbol==symbol)and(tsymbolstate=="bad"))or(checkresult==1)):
            lengthbadpairs = len(badpairsdata)
            if(lengthbadpairs >= 2):
                hexebaML.update_file("",badpairs,folder)
            new_res = []  
            new_sups = []
            hexebaML.learn_brain(symbol,badpairs,folder)
            update_socials("real","WILL BE MOVING ON TO ANOTHER ALTCOIN AS LIMIT REACHED FOR LOSSES PER ALTCOIN FOR {}".format(symbol))
        new_resistance = min(new_res)
        new_support = max(new_sups)
        
        entry = hexeba_binance.check_price(apikey1,apikey2,symbol)
        price_now = float(entry)
        # new_resistance = new_resistance - ((0.25/100)*price_now)
        # new_support = new_support + ((0.25/100)*price_now)

        new_resistance = new_resistance - ((0.025/100)*price_now)
        new_support = new_support + ((0.025/100)*price_now)
        su = price_now - new_support
        sk = (4.5/6)*su
        stoploss_long = price_now - sk
        ru = new_resistance - price_now
        ry = (4.5/6)*ru
        stoploss_short = price_now + ry
        takeprofit_long = new_resistance
        takeprofit_short = new_support
        direction = "hedge"
        return symbol,direction,takeprofit_long,stoploss_long,takeprofit_short,stoploss_short
   
    except Exception as e:
        print("NOT ADVISABLE TO TRADE THIS:", e)     
        symbol = "BTCUSDT"
        takeprofit_long = 0
        takeprofit_short = 0
        stoploss_long = 0
        stoploss_short = 0
        direction = "bad trade"
        print("BAD TRADE")
        time.sleep(10)
        n = n+1
        return take_trade(n)

def open_trade(modulename,folder):
    algoname = hexebaML.readbrain_with_idname("algoname",modulename,folder)
    balance = float(hexebaML.readbrain_with_idname("balance",modulename,folder))
    leverage = float(hexebaML.readbrain_with_idname("leverage",modulename,folder))
    wallet_percent = hexebaML.readbrain_with_idname("wallet_percent",modulename,folder)
    n = 0
    symbol,direction,takeprofit_long,stoploss_long,takeprofit_short,stoploss_short = take_trade(n)
    longbal = balance/2
    shortbal = balance / 2
    if(direction != "bad trade"):
        price = hexeba_binance.check_price(apikey1,apikey2,symbol)
        tradetime = datetime.now()
        tradetime = hexebaML.set_time(tradetime,"time",folder)
        ttime = hexebaML.read_file("time",folder)
        hexebaML.update_brain_with_idname("balance",balance,modulename,folder)
        hexebaML.update_brain_with_idname("symbol",symbol,modulename,folder)
        hexebaML.update_brain_with_idname("shortbalance",shortbal,modulename,folder)
        hexebaML.update_brain_with_idname("longbalance",longbal,modulename,folder)
        hexebaML.update_brain_with_idname("tradestate","open",modulename,folder)
        hexebaML.update_brain_with_idname("hedgestate","4",modulename,folder)
        state = hexebaML.readbrain_with_idname("hedgestate",modulename,folder)
        hexebaML.update_brain_with_idname("position",direction,modulename,folder)
        hexebaML.update_brain_with_idname("entryprice",price,modulename,folder)
        hexebaML.update_brain_with_idname("takeprofit_long",takeprofit_long,modulename,folder)
        hexebaML.update_brain_with_idname("takeprofit_short",takeprofit_short,modulename,folder)
        hexebaML.update_brain_with_idname("stoploss_long",stoploss_long,modulename,folder)
        hexebaML.update_brain_with_idname("stoploss_short",stoploss_short,modulename,folder)
        hexebaML.update_brain_with_idname("tstoplong_in","inactive",modulename,folder)
        hexebaML.update_brain_with_idname("tstopshort_in","inactive",modulename,folder)
        cvc = (((0.5)/100)*float(price)) + float(price)
        hexebaML.update_brain_with_idname("max_long",cvc,modulename,folder)
        hexebaML.update_brain_with_idname("max_short",cvc,modulename,folder)
        hexebaML.update_brain_with_idname("wallet_percent",wallet_percent,modulename,folder)
        message = "{} POSITION OPENED FOR {}\nENTRY PRICE: {}\nLEVERAGE:{}X\nALGO NAME:{}\nBALANCE:${}\nTRADE TIME:{}".format(str(direction).upper(),str(symbol).upper(),price,leverage,algoname,int(balance),ttime)
        print("OPENING TRADE......")
        state = "real"
        update_socials(state,message)
        print("TRADE OPENED......")
        hexebaML.update_file("no","resetstate","iuserbinance")
        # print(symbol)
        leverage = "20"
        wall_percent = "96"
        
     #   hexeba_binance.open_hedge(apikey1,apikey2,symbol,leverage,wall_percent)
        hexebaML.set_now_time(tradestarttime,folder)

def close_hedge_long(modulename,folder):
    apikey1 = hexebaML.readbrain_with_idname("apikey1",modulename,folder)
    apikey2 = hexebaML.readbrain_with_idname("apikey2",modulename,folder)
    longbal = hexebaML.readbrain_with_idname("longbalance",modulename,folder)
    leverage = float(hexebaML.readbrain_with_idname("leverage",modulename,folder))
    entry = float(hexebaML.readbrain_with_idname("entryprice",modulename,folder))
    symbol = hexebaML.readbrain_with_idname("symbol",modulename,folder)
    price_now = hexeba_binance.check_price(apikey1,apikey2,symbol)
    timern = datetime.now()

    hexebaML.update_brain_with_idname("max_long",price_now,modulename,folder)
    hexebaML.update_brain_with_idname("max_short",price_now,modulename,folder)
    contract_quantity = float(longbal) * leverage
    unrealized_pnl = contract_quantity * ((1 / float(entry)) -
                                        (1 / float(price_now)))
    profit_dollars = unrealized_pnl * float(price_now)
    newbalance = float(longbal) + (profit_dollars)   
    hexebaML.update_brain_with_idname("longbalance",str(newbalance),modulename,folder)
    hexebaML.update_brain_with_idname("exitprice",price_now,modulename,folder)
    hexebaML.update_brain_with_idname("hedgestate","2",modulename,folder)
    message = "CLOSED THE LONG POSITION OF THE TRADE\nSYMBOL:{}\nEXIT PRICE:{}\nTRADE TIME:{}".format(str(symbol).upper(),price_now,str(timern))
    state = "real"
    print("CLOSING POSITION 1 SHORT")
 #   update_socials(state,message)
    hexebaML.update_file("no","resetstate","iuserbinance")
 #   hexeba_binance.close_hedge_long(apikey1,apikey2,symbol)
    chatid = "941034600"
    bot.send_message(chatid,message)
    tradetime = datetime.now()
    tradetime = hexebaML.set_time(tradetime,"hedgeclosetime",folder)
    hexebaML.update_file("{}".format(price_now),"hedgeexitprice","capital")
    
def close_hedge_short(modulename,folder):
    apikey1 = hexebaML.readbrain_with_idname("apikey1",modulename,folder)
    apikey2 = hexebaML.readbrain_with_idname("apikey2",modulename,folder)
    leverage = float(hexebaML.readbrain_with_idname("leverage",modulename,folder))
    entry = float(hexebaML.readbrain_with_idname("entryprice",modulename,folder))
    shortbal = hexebaML.readbrain_with_idname("shortbalance",modulename,folder)
    symbol = hexebaML.readbrain_with_idname("symbol",modulename,folder)
    price_now = hexeba_binance.check_price(apikey1,apikey2,symbol)
    timern = datetime.now()
    hexebaML.update_brain_with_idname("max_long",price_now,modulename,folder)
    hexebaML.update_brain_with_idname("max_short",price_now,modulename,folder)
    hexebaML.update_brain_with_idname("exitprice",price_now,modulename,folder)
    contract_quantity = float(shortbal) * leverage
    unrealized_pnl = contract_quantity * ((1 / float(price_now)) -
                                        (1 / float(entry)))
    profit_dollars = unrealized_pnl * float(price_now)

    newbalance = float(shortbal) + (profit_dollars) 

    hexebaML.update_brain_with_idname("shortbalance",str(newbalance),modulename,folder)
    hexebaML.update_brain_with_idname("hedgestate","1",modulename,folder)
    message = "CLOSED THE SHORT POSITION OF THE TRADE\nSYMBOL:{}\nEXIT PRICE:{}\nTRADE TIME:{}".format(str(symbol).upper(),price_now,str(timern))
    state = "real"
    print("CLOSING POSITION 1 SHORT")
 #   update_socials(state,message)
    hexebaML.update_file("no","resetstate","iuserbinance")
  #  hexeba_binance.close_hedge_short(apikey1,apikey2,symbol)
    chatid = "941034600"
    bot.send_message(chatid,message)
    tradetime = datetime.now()
    tradetime = hexebaML.set_time(tradetime,"hedgeclosetime",folder)
    hexebaML.update_file("{}".format(price_now),"hedgeexitprice","capital")

def close_long(message,modulename,folder):
    msg = message
    apikey1 = hexebaML.readbrain_with_idname("apikey1",modulename,folder)
    apikey2 = hexebaML.readbrain_with_idname("apikey2",modulename,folder)
    leverage = float(hexebaML.readbrain_with_idname("leverage",modulename,folder))
    max_long = float(hexebaML.readbrain_with_idname("max_long",modulename,folder))
    exitprice = float(hexebaML.readbrain_with_idname("exitprice",modulename,folder))
    symbol = hexebaML.readbrain_with_idname("symbol",modulename,folder)
    balance = float(hexebaML.readbrain_with_idname("balance",modulename,folder))
    longbal = hexebaML.readbrain_with_idname("longbalance",modulename,folder)
    shortbal = hexebaML.readbrain_with_idname("shortbalance",modulename,folder)
    entry = hexebaML.readbrain_with_idname("entryprice",modulename,folder)
    entry2 = hexebaML.readbrain_with_idname("entryprice",modulename,folder)
    price = hexeba_binance.check_price(apikey1,apikey2,symbol)
    price_now = price
    contract_quantity = float(longbal) * leverage
    unrealized_pnl = contract_quantity * ((1 / float(entry)) -
                                        (1 / float(price_now)))
    profit_dollars = unrealized_pnl * float(price_now)
    newbalance = float(longbal) + (profit_dollars)   
    # print(profit_dollars)
    # print(longbal)
    # time.sleep(30)
    hexebaML.update_brain_with_idname("longbalance",str(newbalance),modulename,folder)  

    longbal = float(hexebaML.readbrain_with_idname("longbalance",modulename,folder))
    shortbal = float(hexebaML.readbrain_with_idname("shortbalance",modulename,folder))
    newbalance = float(longbal) + float(shortbal)
    hexebaML.update_brain_with_idname("balance",newbalance,modulename,folder) 
    hexebaML.update_brain_with_idname("hedgestate","0",modulename,folder)
    tradetime = datetime.now()
    tradetime = hexebaML.set_time(tradetime,"time",folder)
    ttime = hexebaML.read_file("time",folder)
    
    profit = float(hexebaML.readbrain_with_idname("profit",tradefile,folder))
    loss = float(hexebaML.readbrain_with_idname("loss",tradefile,folder))
    tsymbol = hexebaML.readbrain_with_idname("symbol",tradefile,folder)
    
    if(newbalance > balance):
        
        message = "*******TOOK PROFIT BY {} FOR #{} LONG*******\nENTRY PRICE:${}\nHIGHEST PRICE:{}\nEXIT PRICE:${}\nLEVERAGE:{}X\nOLD BALANCE:${}\nNEW BALANCE:${}\nTRADE TIME:{}".format(str(msg).upper(),symbol,entry2,max_long,price,leverage,int(balance),int(newbalance),ttime) 
        if(tsymbol==symbol):
            profit = profit+1
        else:
            profit = 1
    if(newbalance < balance):
        message = "*******CLOSED TRADE BY {} FOR #{} LONG*******\nENTRY PRICE:${}\nHIGHEST PRICE:{}\nEXIT PRICE:${}\nLEVERAGE:{}X\nOLD BALANCE:${}\nNEW BALANCE:${}\nTRADE TIME:{}".format(str(msg).upper(),symbol,entry2,max_long,price,leverage,int(balance),int(newbalance),ttime) 
        if(tsymbol==symbol):
            loss = loss+1
        else:
            loss = 1


    margin = ((newbalance-float(balance))/float(balance))*100
    if((margin<=-9)or(loss>=2)):
        symbolstate = "bad"
        hexebaML.learn_brain(symbol,badpairs,folder)
    else:
        symbolstate = "good"
    newid = ["symbol","profit","loss","margin","symbolstate"]
    data = [symbol,profit,loss,margin,symbolstate]
    hexebaML.update_full_module_with_list(tradefile,newid,data,folder) 
    
    hexebaML.update_brain_with_idname("tradestate","closed",modulename,folder)
    hexebaML.update_brain_with_idname("balance",newbalance,modulename,folder)
    hexebaML.update_brain_with_idname("datetime",ttime,modulename,folder)  
    print("CLOSING TRADE......")
    state = "real"
    update_socials(state,message)
    print("CLOSED TRADE......")
    hexebaML.update_brain_with_idname("tstoplong_in","inactive",modulename,folder)
    hexebaML.update_file("yes","resetstate","iuserbinance")
  #  hexeba_binance.close_long(apikey1,apikey2,symbol)


def close_short(message,modulename,folder):
    msg = message
    apikey1 = hexebaML.readbrain_with_idname("apikey1",modulename,folder)
    apikey2 = hexebaML.readbrain_with_idname("apikey2",modulename,folder)
    leverage = float(hexebaML.readbrain_with_idname("leverage",modulename,folder))
    max_short = float(hexebaML.readbrain_with_idname("max_short",modulename,folder))
    symbol = hexebaML.readbrain_with_idname("symbol",modulename,folder)
    balance = float(hexebaML.readbrain_with_idname("balance",modulename,folder))
    longbal = hexebaML.readbrain_with_idname("longbalance",modulename,folder)
    shortbal = hexebaML.readbrain_with_idname("shortbalance",modulename,folder)
    entry = hexebaML.readbrain_with_idname("entryprice",modulename,folder)
    entry2 = hexebaML.readbrain_with_idname("entryprice",modulename,folder)
    price = hexeba_binance.check_price(apikey1,apikey2,symbol)
    price_now = hexeba_binance.check_price(apikey1,apikey2,symbol)

    contract_quantity = float(shortbal) * leverage
    unrealized_pnl = contract_quantity * ((1 / float(price_now)) -
                                        (1 / float(entry)))
    profit_dollars = unrealized_pnl * float(price_now)
    # print(profit_dollars)
    # print(shortbal)
    # time.sleep(30)
    newbalance = float(shortbal) + (profit_dollars)
    hexebaML.update_brain_with_idname("shortbalance",str(newbalance),modulename,folder)  

    longbal = hexebaML.readbrain_with_idname("longbalance",modulename,folder)
    shortbal = hexebaML.readbrain_with_idname("shortbalance",modulename,folder)  

    newbalance = float(longbal) + float(shortbal)
    hexebaML.update_brain_with_idname("balance",newbalance,modulename,folder)  
    hexebaML.update_brain_with_idname("hedgestate","0",modulename,folder)

    tradetime = datetime.now()
    tradetime = hexebaML.set_time(tradetime,"time",folder)
    ttime = hexebaML.read_file("time",folder)

    profit = float(hexebaML.readbrain_with_idname("profit",tradefile,folder))
    loss = float(hexebaML.readbrain_with_idname("loss",tradefile,folder))
    tsymbol = hexebaML.readbrain_with_idname("symbol",tradefile,folder)
    
    
    if(newbalance > balance):
        message = "*******TOOK PROFIT BY {} FOR #{} SHORT*******\nENTRY PRICE:${}\nLOWEST PRICE:{}\nEXIT PRICE:${}\nLEVERAGE:{}X\nOLD BALANCE:${}\nNEW BALANCE:${}\nTRADE TIME:{}".format(str(msg).upper(),symbol,entry2,max_short,price,leverage,int(balance),int(newbalance),ttime) 
        if(tsymbol==symbol):
            profit = profit+1
        else:
            profit = 1
    if(newbalance < balance):
        message = "*******CLOSED TRADE BY {} FOR #{} SHORT*******\nENTRY PRICE:${}\nLOWEST PRICE:{}\nEXIT PRICE:${}\nLEVERAGE:{}X\nOLD BALANCE:${}\nNEW BALANCE:${}\nTRADE TIME:{}".format(str(msg).upper(),symbol,entry2,max_short,price,leverage,int(balance),int(newbalance),ttime) 
        if(tsymbol==symbol):
            loss = loss+1
        else:
            loss = 1
    margin = ((newbalance-float(balance))/float(balance))*100
    if((margin<=-9)or(loss>=2)):
        symbolstate = "bad"
        hexebaML.learn_brain(symbol,badpairs,folder)
    else:
        symbolstate = "good"
    newid = ["symbol","profit","loss","margin","symbolstate"]
    data = [symbol,profit,loss,margin,symbolstate]
    hexebaML.update_full_module_with_list(tradefile,newid,data,folder) 
        
        
    hexebaML.update_brain_with_idname("tradestate","closed",modulename,folder)
    hexebaML.update_brain_with_idname("balance",newbalance,modulename,folder)
    hexebaML.update_brain_with_idname("datetime",ttime,modulename,folder)  
    hexebaML.update_brain_with_idname("tstopshort_in","inactive",modulename,folder)
    print("CLOSING TRADE......")
    state = "real"
    update_socials(state,message)
    print("CLOSED TRADE......")
    hexebaML.update_file("yes","resetstate","iuserbinance")
 #   hexeba_binance.close_short(apikey1,apikey2,symbol)

def update_socials(state,message):
    if(state=="virtual"):
        
        api.update_status(message)
    if(state == "real"):
        chatid2 = "608774711"
        groupid = "@hexebagroup"
        chatid = "941034600"
        bot.send_message(chatid,message)
      #  bot.send_message(chatid,"MESSAGE FROM LOCAL SERVER")
        bot.send_message(chatid2,message)
        bot.send_message(chat_id=groupid,text=message)
        
# start()
# sys.modules[__name__].__dict__.clear()
# def startx():
#     import hexebaML
#     import sys
#     x = hexebaML.c_rand("rand","capital",0,10)
#     hexebaML.update_file(x,"capitalrand","capital")
#     print(x)
   # sys.modules[__name__].__dict__.clear()

# import sys
# if(1>0):
#     import hexebaML
#     import sys
#     x = hexebaML.c_rand("rand","capital",0,10)
#     hexebaML.update_file(x,"capitalrand","capital")
    # sys.modules[__name__].__dict__.clear()    

while True: 
    try:
        
        start()
        time.sleep(2)
    except Exception:
        pass
        time.sleep(2)
#     adjustedtime = 3
#     time.sleep(adjustedtime)