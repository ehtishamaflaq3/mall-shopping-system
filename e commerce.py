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
class Admin:
    def __init__(self,inventory,cashier,helper,user):
         self.inventory=inventory
         self.cashier=cashier
         self.helper=helper
         self.user=user
    #  -------------INVENTORY MANAGEMENT-------------
    def add_item(self,item,price,stock):
         pass
    def remo_item(self,name):
         pass
    # -------------CASHIER MANAGEMENT----------------
    def add_cashier(self,name):
         pass
    def remo_cashier(self,name):
         pass
    # -------------HELPER MANAGEMENT----------------
    def add_helper(self,name):
         pass
    def remo_helper(self,name):
         pass
    # -------------ALL REGISTER USERS---------------
    def add_users(self,name):
         pass
    def remo_user(self,name):
         pass

#-----------------------------------------------------------------------------------
#                           [CASHIER SECTION]
class cashier:
    def calculateTotal(user_item):
     total=0
     print("Here Your Total bill listed below sir!")
     for item in user_item:
          total+=item*qty
          print(f"Your Total Amount is RS {total}")
          

     def applydiscount(user_item):
          choice=input("Want to need discount: (Yes/No)")
          if choice=="Yes":
             applydiscount=total*0.10
             total-=applydiscount
             print(f"Discount Apply RS: {apply_discount}")
             print(f"Total You Have To Pay Rs: {total}")
          elif choice=="No":
            print(f"Total Amount To Pay Rs: {total}")
            
          
     def createbill(user_item):
          total=sum(user_item)
          print("Total Bill!")
          print(f"Total Amount You Have To Pay RS: {total}")
          choice=input("Sir Want To Need Bag: (Yes/No)")
          if choice=="Yes":
               total+=20
               print(f"Total Amount You Have To Pay RS: {total}")
          elif choice=="No":
               print(f"Total Amount You Have To Pay RS: {total}")
          print("Thanks For Shopping Sir!")
#                              [HELPER SECTION]

#                              [USER SECTION]


#                             [MAIN SECTION]
def main():
    while True:
            role=input("ENTER YOUR ROLE(admin/cashier/helper/user/exit):- ")
            if role=="admin":
                print("=======WELLCOME TO THE ADMIN MENU========")
                print("1. Add Inventory Item")
                print("2. Remove Inventory Item")
                print("3. Add Cashier")
                print("4. Remove Cashier")
                print("5. Add Helper")
                print("6. Remove Helper")
                print("7. REGISTER NEW USER")
                print("8. REMOVE USER")
                print("9. EXIT")
                admin_choice=int(input("YOUR CHOICE(1-9):- "))
                match admin_choice:
                     case 1:
                          pass
                     case 2:
                          pass
                     case 3:
                          pass
                     case 4:
                          pass
                     case 5:
                          pass
                     case 6:
                          pass
                     case 7:
                          pass
                     case 8:
                          pass
                     case 9:
                          break
                     case _:
                          print("INVALID CHOICE")
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
