import pickle
from maskpass import advpass
from bank import Bank
from clearscrn import Animate


class Login:
    @staticmethod
    def login():
        try:
            logged_in = False
            print("Logging in")
            phone = input("Enter Phone Number: ")
            password = advpass('Enter password: ')
            if Bank.check_details(phone, password) is True:
                with open(f'{phone}.pkl', 'rb') as f:
                    new_dict = pickle.load(f)
                    logged_in = True
                    name = new_dict.get("customer name")
                    acc_no = new_dict.get("account no")
                    balance = new_dict.get("balance")
                    Animate.buffer()
                    Animate.clear()
                    print(f'''You are successfully logged in.
                    Registered Details:
                    Account holder: {name}
                    Account no. :{acc_no}
                    Total Balance : {balance}
                    ''')
            else:
                print("Incorrect login credentials!!!!")
        except Exception as e:
            print(e)
        return logged_in
