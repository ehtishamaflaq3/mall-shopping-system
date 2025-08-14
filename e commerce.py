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
inventory_all={
     "ELECTRONICS":{
            "LAPTOP":{"PRICE":60000,"STOCK":500},
            "MOBILE PHONE": {"PRICE": 35000, "STOCK": 650},
            "SMARTPHONE": {"PRICE": 55000, "STOCK": 500},
            "GAMING LAPTOP": {"PRICE": 150000, "STOCK": 200},
            "TABLET": {"PRICE": 25000, "STOCK": 300},
            "SMART WATCH": {"PRICE": 15000, "STOCK": 200},
            "HEADPHONES": {"PRICE": 5000, "STOCK": 400},
            "BLUETOOTH SPEAKER": {"PRICE": 8000, "STOCK": 150},
            "TELEVISION 32 INCH": {"PRICE": 35000, "STOCK": 120},
            "TELEVISION 55 INCH": {"PRICE": 80000, "STOCK": 90},
            "DIGITAL CAMERA": {"PRICE": 45000, "STOCK": 80},
            "DSLR CAMERA": {"PRICE": 120000, "STOCK": 40},
            "CAMERA TRIPOD": {"PRICE": 5000, "STOCK": 200},
            "MICROWAVE OVEN": {"PRICE": 25000, "STOCK": 150},
            "REFRIGERATOR": {"PRICE": 90000, "STOCK": 100},
            "AIR CONDITIONER": {"PRICE": 120000, "STOCK": 70},
            "WASHING MACHINE": {"PRICE": 60000, "STOCK": 80},
            "VACUUM CLEANER": {"PRICE": 20000, "STOCK": 110},
            "ELECTRIC KETTLE": {"PRICE": 5000, "STOCK": 300},
            "BLENDER": {"PRICE": 8000, "STOCK": 250},
            "COFFEE MAKER": {"PRICE": 15000, "STOCK": 90},
            "INDUCTION COOKTOP": {"PRICE": 18000, "STOCK": 75},
            "TOASTER": {"PRICE": 6000, "STOCK": 130},
            "IRON": {"PRICE": 4000, "STOCK": 220},
            "GAMING CONSOLE": {"PRICE": 85000, "STOCK": 60},
            "VR HEADSET": {"PRICE": 70000, "STOCK": 30},
            "PRINTER": {"PRICE": 20000, "STOCK": 100},
            "SCANNER": {"PRICE": 15000, "STOCK": 50},
            "EXTERNAL HARD DRIVE": {"PRICE": 12000, "STOCK": 140},
            "USB FLASH DRIVE": {"PRICE": 2000, "STOCK": 500},
            "ROUTER": {"PRICE": 8000, "STOCK": 150},
            "PROJECTOR": {"PRICE": 50000, "STOCK": 60}
     },
     "CLOTHING":{
        "MEN T-SHIRT": {"PRICE": 1200, "STOCK": 500},
        "MEN SHIRT": {"PRICE": 2500, "STOCK": 400},
        "MEN JEANS": {"PRICE": 3500, "STOCK": 350},
        "MEN TROUSERS": {"PRICE": 2200, "STOCK": 300},
        "MEN SHORTS": {"PRICE": 1500, "STOCK": 200},
        "MEN SUIT": {"PRICE": 12000, "STOCK": 100},
        "MEN JACKET": {"PRICE": 8000, "STOCK": 150},
        "MEN HOODIE": {"PRICE": 3500, "STOCK": 200},
        "MEN SWEATER": {"PRICE": 3000, "STOCK": 180},
        "MEN KURTA": {"PRICE": 2500, "STOCK": 250},
        "MEN WAISTCOAT": {"PRICE": 5000, "STOCK": 120},
        "WOMEN DRESS": {"PRICE": 5000, "STOCK": 300},
        "WOMEN KURTI": {"PRICE": 2500, "STOCK": 280},
        "WOMEN SAREE": {"PRICE": 7000, "STOCK": 150},
        "WOMEN ABAYA": {"PRICE": 6000, "STOCK": 120},
        "WOMEN BLOUSE": {"PRICE": 2000, "STOCK": 200},
        "WOMEN JEANS": {"PRICE": 3500, "STOCK": 250},
        "WOMEN SKIRT": {"PRICE": 2800, "STOCK": 180},
        "WOMEN LEHENGA": {"PRICE": 15000, "STOCK": 80},
        "WOMEN SHAWL": {"PRICE": 3000, "STOCK": 160},
        "KIDS T-SHIRT": {"PRICE": 800, "STOCK": 300},
        "KIDS SHIRT": {"PRICE": 1200, "STOCK": 250},
        "KIDS JEANS": {"PRICE": 2000, "STOCK": 200},
        "KIDS TROUSERS": {"PRICE": 1500, "STOCK": 200},
        "KIDS FROCK": {"PRICE": 2500, "STOCK": 180},
        "KIDS HOODIE": {"PRICE": 1800, "STOCK": 150},
        "FOOTWEAR MEN": {"PRICE": 3500, "STOCK": 200},
        "FOOTWEAR WOMEN": {"PRICE": 3000, "STOCK": 200},
        "FOOTWEAR KIDS": {"PRICE": 2000, "STOCK": 150},
        "CAP": {"PRICE": 800, "STOCK": 300},
        "SCARF": {"PRICE": 1200, "STOCK": 200},
        "BELT": {"PRICE": 1000, "STOCK": 250}
     },
     "GROCERY":{
           "RICE 5KG": {"PRICE": 1500, "STOCK": 300},
        "RICE 10KG": {"PRICE": 2800, "STOCK": 250},
        "WHEAT FLOUR 10KG": {"PRICE": 1200, "STOCK": 400},
        "WHEAT FLOUR 20KG": {"PRICE": 2300, "STOCK": 300},
        "SUGAR 5KG": {"PRICE": 750, "STOCK": 350},
        "SUGAR 10KG": {"PRICE": 1400, "STOCK": 250},
        "COOKING OIL 1L": {"PRICE": 500, "STOCK": 500},
        "COOKING OIL 5L": {"PRICE": 2300, "STOCK": 200},
        "GHEE 1KG": {"PRICE": 700, "STOCK": 300},
        "GHEE 5KG": {"PRICE": 3300, "STOCK": 150},
        "MILK 1L": {"PRICE": 250, "STOCK": 500},
        "MILK POWDER 500G": {"PRICE": 600, "STOCK": 200},
        "BREAD": {"PRICE": 150, "STOCK": 400},
        "BUNS PACK": {"PRICE": 200, "STOCK": 350},
        "EGGS 12PCS": {"PRICE": 300, "STOCK": 400},
        "BUTTER 200G": {"PRICE": 400, "STOCK": 180},
        "CHEESE 200G": {"PRICE": 500, "STOCK": 160},
        "YOGURT 1KG": {"PRICE": 300, "STOCK": 220},
        "TEA 500G": {"PRICE": 900, "STOCK": 250},
        "COFFEE 200G": {"PRICE": 1200, "STOCK": 150},
        "SALT 1KG": {"PRICE": 50, "STOCK": 600},
        "BLACK PEPPER 100G": {"PRICE": 400, "STOCK": 180},
        "RED CHILLI POWDER 200G": {"PRICE": 300, "STOCK": 200},
        "CUMIN SEEDS 200G": {"PRICE": 250, "STOCK": 200},
        "BASMATI RICE 5KG": {"PRICE": 2000, "STOCK": 220},
        "PASTA 500G": {"PRICE": 300, "STOCK": 180},
        "NOODLES PACK": {"PRICE": 150, "STOCK": 300},
        "BISCUITS PACK": {"PRICE": 250, "STOCK": 400},
        "CHOCOLATE BAR": {"PRICE": 200, "STOCK": 250},
        "SOFT DRINK 1.5L": {"PRICE": 180, "STOCK": 350},
        "JUICE 1L": {"PRICE": 250, "STOCK": 300}
     },
     "FURNITURE":{
        "SOFA 3-SEATER": {"PRICE": 55000, "STOCK": 50},
        "SOFA 5-SEATER": {"PRICE": 85000, "STOCK": 40},
        "SOFA BED": {"PRICE": 65000, "STOCK": 30},
        "RECLINER CHAIR": {"PRICE": 30000, "STOCK": 60},
        "WOODEN CHAIR": {"PRICE": 5000, "STOCK": 200},
        "PLASTIC CHAIR": {"PRICE": 2000, "STOCK": 300},
        "DINING TABLE 4-SEATER": {"PRICE": 40000, "STOCK": 50},
        "DINING TABLE 6-SEATER": {"PRICE": 60000, "STOCK": 40},
        "DINING TABLE 8-SEATER": {"PRICE": 80000, "STOCK": 30},
        "WOODEN BED KING": {"PRICE": 90000, "STOCK": 35},
        "WOODEN BED QUEEN": {"PRICE": 75000, "STOCK": 40},
        "SINGLE BED": {"PRICE": 50000, "STOCK": 50},
        "BUNK BED": {"PRICE": 65000, "STOCK": 20},
        "MATTRESS KING": {"PRICE": 35000, "STOCK": 60},
        "MATTRESS QUEEN": {"PRICE": 30000, "STOCK": 70},
        "WARDROBE 2-DOOR": {"PRICE": 45000, "STOCK": 50},
        "WARDROBE 3-DOOR": {"PRICE": 60000, "STOCK": 40},
        "WARDROBE SLIDING": {"PRICE": 75000, "STOCK": 30},
        "TV CABINET": {"PRICE": 25000, "STOCK": 80},
        "BOOKSHELF SMALL": {"PRICE": 15000, "STOCK": 90},
        "BOOKSHELF LARGE": {"PRICE": 25000, "STOCK": 70},
        "COFFEE TABLE": {"PRICE": 12000, "STOCK": 100},
        "SIDE TABLE": {"PRICE": 7000, "STOCK": 120},
        "DRESSING TABLE": {"PRICE": 30000, "STOCK": 60},
        "STUDY TABLE": {"PRICE": 20000, "STOCK": 80},
        "COMPUTER TABLE": {"PRICE": 18000, "STOCK": 70},
        "OFFICE CHAIR": {"PRICE": 15000, "STOCK": 100},
        "STOOL": {"PRICE": 3000, "STOCK": 150},
        "SHOE RACK": {"PRICE": 8000, "STOCK": 90},
        "CABINET STORAGE": {"PRICE": 20000, "STOCK": 60}
     },
     "COSMETICS AND BEAUTY":{
        "PERFUME 100ML": {"PRICE": 2500, "STOCK": 200},
        "LIPSTICK": {"PRICE": 800, "STOCK": 300},
        "NAIL POLISH": {"PRICE": 300, "STOCK": 400},
        "FOUNDATION": {"PRICE": 1500, "STOCK": 250},
        "FACE CREAM": {"PRICE": 1200, "STOCK": 200},
        "SUNSCREEN": {"PRICE": 1000, "STOCK": 220},
        "HAIR OIL": {"PRICE": 500, "STOCK": 300},
        "SHAMPOO 500ML": {"PRICE": 800, "STOCK": 250},
        "CONDITIONER 500ML": {"PRICE": 900, "STOCK": 200},
        "MAKEUP KIT": {"PRICE": 3500, "STOCK": 150},
        "EYE SHADOW PALETTE": {"PRICE": 1200, "STOCK": 180},
        "EYELINER": {"PRICE": 500, "STOCK": 220},
        "MASCARA": {"PRICE": 700, "STOCK": 200},
        "BODY LOTION": {"PRICE": 900, "STOCK": 250},
        "HAND CREAM": {"PRICE": 400, "STOCK": 300},
        "HAIR BRUSH": {"PRICE": 300, "STOCK": 400},
        "FACE WASH": {"PRICE": 500, "STOCK": 250},
        "LIP BALM": {"PRICE": 200, "STOCK": 350},
        "BEARD OIL": {"PRICE": 600, "STOCK": 180},
        "HAIR STRAIGHTENER": {"PRICE": 2500, "STOCK": 100}
     },
     "SPORTS AND FITNESS":{
        "CRICKET BAT": {"PRICE": 2500, "STOCK": 150},
        "FOOTBALL": {"PRICE": 1500, "STOCK": 200},
        "BASKETBALL": {"PRICE": 1800, "STOCK": 180},
        "BADMINTON RACKET": {"PRICE": 1200, "STOCK": 250},
        "TENNIS RACKET": {"PRICE": 3000, "STOCK": 150},
        "TABLE TENNIS BAT": {"PRICE": 800, "STOCK": 200},
        "TREADMILL": {"PRICE": 120000, "STOCK": 30},
        "EXERCISE CYCLE": {"PRICE": 45000, "STOCK": 40},
        "DUMBBELL 10KG": {"PRICE": 3000, "STOCK": 100},
        "BARBELL ROD": {"PRICE": 5000, "STOCK": 80},
        "YOGA MAT": {"PRICE": 1500, "STOCK": 200},
        "SKIPPING ROPE": {"PRICE": 500, "STOCK": 300},
        "BOXING GLOVES": {"PRICE": 2500, "STOCK": 100},
        "SPORTS SHOES": {"PRICE": 4000, "STOCK": 150},
        "KNEE SUPPORT": {"PRICE": 700, "STOCK": 200},
        "ELBOW SUPPORT": {"PRICE": 600, "STOCK": 200},
        "GYM GLOVES": {"PRICE": 800, "STOCK": 200},
        "WATER BOTTLE": {"PRICE": 500, "STOCK": 300},
        "SWIMMING GOGGLES": {"PRICE": 1000, "STOCK": 150},
        "WHISTLE": {"PRICE": 200, "STOCK": 400}
     },
    "JEWELLERY & ACCESSORIES": {
        "GOLD RING": {"PRICE": 50000, "STOCK": 50},
        "SILVER RING": {"PRICE": 5000, "STOCK": 100},
        "GOLD NECKLACE": {"PRICE": 150000, "STOCK": 20},
        "SILVER NECKLACE": {"PRICE": 10000, "STOCK": 50},
        "BRACELET": {"PRICE": 3000, "STOCK": 100},
        "ANKLET": {"PRICE": 2000, "STOCK": 120},
        "EARRINGS": {"PRICE": 4000, "STOCK": 150},
        "WATCH MEN": {"PRICE": 15000, "STOCK": 80},
        "WATCH WOMEN": {"PRICE": 12000, "STOCK": 90},
        "SUNGLASSES": {"PRICE": 3000, "STOCK": 150},
        "HANDBAG": {"PRICE": 5000, "STOCK": 100},
        "WALLET MEN": {"PRICE": 2000, "STOCK": 150},
        "WALLET WOMEN": {"PRICE": 1800, "STOCK": 150},
        "HAIR CLIP": {"PRICE": 200, "STOCK": 300},
        "HAIR BAND": {"PRICE": 150, "STOCK": 300},
        "CAP": {"PRICE": 500, "STOCK": 200},
        "BELT MEN": {"PRICE": 1500, "STOCK": 150},
        "BELT WOMEN": {"PRICE": 1200, "STOCK": 150},
        "BROOCH": {"PRICE": 800, "STOCK": 150},
        "RING SET": {"PRICE": 3000, "STOCK": 80}
    },
     "PHARMACY & HEALTH CARE": {
        "PARACETAMOL 500MG": {"PRICE": 50, "STOCK": 1000},
        "ASPIRIN 300MG": {"PRICE": 80, "STOCK": 800},
        "VITAMIN C TABLETS": {"PRICE": 200, "STOCK": 500},
        "MULTIVITAMINS": {"PRICE": 500, "STOCK": 400},
        "COUGH SYRUP": {"PRICE": 150, "STOCK": 300},
        "DIGESTIVE TABLETS": {"PRICE": 100, "STOCK": 300},
        "THERMOMETER": {"PRICE": 500, "STOCK": 200},
        "BLOOD PRESSURE MONITOR": {"PRICE": 3000, "STOCK": 100},
        "GLUCOSE METER": {"PRICE": 2500, "STOCK": 80},
        "HAND SANITIZER 500ML": {"PRICE": 200, "STOCK": 500},
        "FACE MASK PACK": {"PRICE": 300, "STOCK": 400},
        "FIRST AID KIT": {"PRICE": 1500, "STOCK": 150},
        "BANDAGES PACK": {"PRICE": 100, "STOCK": 300},
        "PAINKILLER GEL": {"PRICE": 250, "STOCK": 200},
        "ANTISEPTIC LIQUID": {"PRICE": 150, "STOCK": 300},
        "EYE DROPS": {"PRICE": 200, "STOCK": 200},
        "EAR DROPS": {"PRICE": 250, "STOCK": 150},
        "INHALER": {"PRICE": 300, "STOCK": 200},
        "COTTON PACK": {"PRICE": 150, "STOCK": 300},
        "DISPOSABLE GLOVES PACK": {"PRICE": 250, "STOCK": 200}
    },
    
    "SHOES": {
        "MEN FORMAL SHOES": {"PRICE": 5000, "STOCK": 200},
        "MEN CASUAL SHOES": {"PRICE": 3500, "STOCK": 250},
        "MEN SNEAKERS": {"PRICE": 4000, "STOCK": 200},
        "MEN SANDALS": {"PRICE": 2500, "STOCK": 200},
        "MEN SLIPPERS": {"PRICE": 1500, "STOCK": 250},
        "WOMEN HEELS": {"PRICE": 4000, "STOCK": 150},
        "WOMEN FLATS": {"PRICE": 3000, "STOCK": 200},
        "WOMEN SNEAKERS": {"PRICE": 3500, "STOCK": 150},
        "WOMEN SANDALS": {"PRICE": 2500, "STOCK": 200},
        "WOMEN SLIPPERS": {"PRICE": 1500, "STOCK": 200},
        "KIDS SCHOOL SHOES": {"PRICE": 2500, "STOCK": 150},
        "KIDS SNEAKERS": {"PRICE": 2000, "STOCK": 200},
        "KIDS SANDALS": {"PRICE": 1500, "STOCK": 200},
        "SPORTS SHOES MEN": {"PRICE": 4000, "STOCK": 150},
        "SPORTS SHOES WOMEN": {"PRICE": 3500, "STOCK": 150},
        "SPORTS SHOES KIDS": {"PRICE": 2500, "STOCK": 150},
        "HIKING BOOTS": {"PRICE": 5000, "STOCK": 100},
        "RAIN BOOTS": {"PRICE": 3000, "STOCK": 100},
        "WORK BOOTS": {"PRICE": 4500, "STOCK": 80},
        "LOAFERS": {"PRICE": 3500, "STOCK": 150}
    },
    
    "FRUITS": {
        "APPLE": {"PRICE": 200, "STOCK": 500},
        "BANANA": {"PRICE": 100, "STOCK": 400},
        "ORANGE": {"PRICE": 150, "STOCK": 350},
        "GRAPES": {"PRICE": 250, "STOCK": 300},
        "MANGO": {"PRICE": 300, "STOCK": 250},
        "PINEAPPLE": {"PRICE": 350, "STOCK": 200},
        "PAPAYA": {"PRICE": 200, "STOCK": 200},
        "WATERMELON": {"PRICE": 150, "STOCK": 300},
        "MELON": {"PRICE": 150, "STOCK": 250},
        "PEAR": {"PRICE": 200, "STOCK": 200},
        "PEACH": {"PRICE": 250, "STOCK": 180},
        "PLUM": {"PRICE": 250, "STOCK": 180},
        "CHERRY": {"PRICE": 400, "STOCK": 150},
        "STRAWBERRY": {"PRICE": 350, "STOCK": 150},
        "BLUEBERRY": {"PRICE": 500, "STOCK": 100},
        "RASPBERRY": {"PRICE": 500, "STOCK": 100},
        "BLACKBERRY": {"PRICE": 500, "STOCK": 100},
        "KIWI": {"PRICE": 300, "STOCK": 150},
        "COCONUT": {"PRICE": 150, "STOCK": 150},
        "POMEGRANATE": {"PRICE": 350, "STOCK": 150}
    },
    
    "VEGETABLES": {
        "POTATO": {"PRICE": 80, "STOCK": 500},
        "ONION": {"PRICE": 100, "STOCK": 400},
        "TOMATO": {"PRICE": 120, "STOCK": 350},
        "CUCUMBER": {"PRICE": 150, "STOCK": 300},
        "CARROT": {"PRICE": 100, "STOCK": 300},
        "BEETROOT": {"PRICE": 150, "STOCK": 250},
        "SPINACH": {"PRICE": 80, "STOCK": 200},
        "CABBAGE": {"PRICE": 120, "STOCK": 200},
        "CAULIFLOWER": {"PRICE": 150, "STOCK": 200},
        "BROCCOLI": {"PRICE": 200, "STOCK": 180},
        "BELL PEPPER": {"PRICE": 250, "STOCK": 180},
        "CHILLI": {"PRICE": 100, "STOCK": 200},
        "GARLIC": {"PRICE": 300, "STOCK": 200},
        "GINGER": {"PRICE": 250, "STOCK": 200},
        "LETTUCE": {"PRICE": 150, "STOCK": 150},
        "MUSHROOM": {"PRICE": 400, "STOCK": 120},
        "OKRA": {"PRICE": 120, "STOCK": 200},
        "EGGPLANT": {"PRICE": 150, "STOCK": 200},
        "ZUCCHINI": {"PRICE": 200, "STOCK": 150},
        "GREEN BEANS": {"PRICE": 150, "STOCK": 150}
    },
}

cashiers_lists=[]
helpers_lists=[]
user_all=[]
class Admin:
    def __init__(self,inventory,cashier,helper,user):
         self.inventory=inventory
         self.cashier=cashier
         self.helper=helper
         self.user=user
    #  -------------INVENTORY MANAGEMENT-------------
    def add_item(self,category,name,price,stock):
        if category not in self.inventory:
             self.inventory[category]={}
        self.inventory[category][name]={"PRICE":price,"STOCK":stock}
        print(f"NAME: {name} PRICE: {price} STOCK: {stock} IS ADDED TO {category} CATEGORY.")
    def remo_item(self,category,name):
         pass
        # if category in self.inventory:
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
            # break
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
# main()
