import  numpy as np 
import win32com.client as wincl
import time

X = np.array([200 , 250 , 300 , 350 , 400 , 450 , 500 , 550 , 600 , 650 , 700 , 750 , 800 , 850 , 900 , 950 , 1000])

Y = np.array([5 , 6.25, 7.5 , 8.75 , 10 , 11.25, 12.5 , 13.75 , 15 , 16.25 , 17.5, 18.75 , 20 , 21.25 , 22.5 , 23.75 , 25]
)

# Y = b0 + b1 * X


x_mean = np.mean(X)
y_mean = np.mean(Y)

b1 = sum((X - x_mean) * (Y - y_mean)) / sum((X - x_mean)**2)
b0 = y_mean - b1 * x_mean

speak = wincl.Dispatch("SAPI.spvoice")
speak.Speak("Hello user")
speak.Speak("plese Enter your name ")

user_name_input = input("plese Enter your name : ")

speak.Speak("Now your land price prediction ha been started now ")
speak.Speak("plese enter your land area ")
user_land_input = int(input("plese Enter your land Areas : "))
if user_land_input <= -0 :
    print("plese Enter a valid value : ")

speak.Speak("plese wait 5 second iam just calculating your land price")
print("plese wait 5 second iam just calculating your land price : ")
time.sleep(5)

speak.Speak("Your land price Calculated has been completed Successfully")
print("Your land price Calculated has been completed Successfully : ")

formula_price_pedict = b0 + b1 * user_land_input

speak.Speak("Congratulation" + user_name_input)
speak.Speak("Your Price on Screen")
print(f"Congratulation {user_name_input} now Your land Price on your Screen : ") 

time.sleep(2)

print(f"your land price is : " , round(formula_price_pedict , 2), "lakh")




