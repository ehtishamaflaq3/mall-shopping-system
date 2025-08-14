#GREAT MALL SYSTEM(CLI).
# INSTRUCTIONS:-
#1.ADMIN THIS PERSON HANDLE ALL THE [INVENTORY(ADD/REMOVE)]&[CASHIER(ADD/REMOVE)]&[HELPER(ADD/REMOVE)]&[REGISTERATION (ONLINE USER ACCOUNTS/)]
#2.CASHIER THIS PERSON [TOTAL THE CART]&[CREATE BILL]&[DISCOUNT IN FINAL BILL ON RATE]. 
#3.HELPER THIS PERSON UPDATE STOCK[ADD/REMOVE].
#4.USER [CART(ADD/REMOVE)]&[QUANTITY(INCREASE/DECREASE)].
# ---------------------------------------------------------------------------------
# 1. Start program → Show welcome message.
# 2. Ask the user for their role (admin/cashier/helper/user).
# 3. Based on role → Show menu of that role.
# 4. Perform the selected action (add item,calculate bill,update stock).
# 5. Return to the same menu until user chooses "Exit".
#                              [ADMIN SECTION]

#                              [CASHIER SECTION]
def calculateTotal(user_item):
     total=0
     print("Here Your Total bill listed below sir!")
     for item in user_item:
          total+=item*QUANTITY
          print(f"Your Total Amount is RS {total}")
          break

def applydiscount(user_item):
     choice=input("Want to need discount: (Yes/No)")
     if choice=="Yes":
          applydiscount=total*0.10
          total-=applydiscount
          print(f"Discount Apply RS: {apply_discount}")
          print(f"Total You Have To Pay Rs: {total}")
     elif choice=="No":
          print(f"Total Amount To Pay Rs: {total}")
          break
          

#                              [HELPER SECTION]

#                              [USER SECTION]


#                             [MAIN SECTION]
def main():
    while True:
            print("ENTE")
            role=input("ENTER YOUR ROLE(admin/cashier/helper/user/exit):- ")
            if role=="admin":
                pass
            elif role=="cashier":
                 pass
            elif role=="helper":
                 pass
            elif role=="user":
                 pass
            elif role=="exit":
                 break
            else:
                 print("INVALID CHOICE")

main()
