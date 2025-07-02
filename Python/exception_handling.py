try:
    print(x)
#except NameError:
   # print("Variable x is not defined")
#except:
    #print("an exception occurred")
    
except:
    print("somthing went wrong")
    
finally:
    print("the 'try except' is finished")
    
    x = -1
    if x < 0:
         raise Exception("sorry, no numbers below zero")