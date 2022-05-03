from maskpass import advpass
from base64 import b64encode, b64decode
import pickle
import os
from validation import Validate
from clearscrn import Animate


class Bank:
    acc_details={}
    def __init__(self, name, phone, password, trans_pin, acc_no, cash) -> None:
        self.name = name
        self.phone = phone
        self.password = password
        self.trans_pin = trans_pin
        self.acc_no = acc_no
        self.cash = cash
        Bank.accounts(self.name, self.phone, self.password, self.trans_pin, self.acc_no, self.cash)

    @classmethod
    def accounts(cls, name, phone, password, trans_pin, acc_no, cash):
        try:
            acc_details = {
            'customer name': name,
            'phone': phone,
            'password': password,
            'trans_pin': trans_pin,
            'account no': acc_no,
            'balance': cash
            }
            print("You have successfully created an account in this bank.")
            Animate.buffer()
            print("Your account details are: ")
            for key, value in acc_details.items():
                if key == "password" or key == "trans_pin":
                    continue
                else:
                    print(key, ":", value)
            with open(f"{phone}.pkl", "wb+") as f:
                pickle.dump(acc_details, f)
                return True
        except Exception as e:
            print (e)

    @staticmethod
    def check_details(phone, password):
        condition = False
        try:
            Animate.buffer()
            with open(f"{phone}.pkl", "rb") as f:
                user_details = pickle.load(f)
                valid_pass = b64decode(user_details.get("password")).decode("utf-8")
                if valid_pass == password:
                    condition = True
            return condition
        except Exception as e:
            print(e)
            print("You have entered incorrect phone number.")

    @staticmethod
    def deposit():
        try:
            phone = input("Enter your registered phone number: ")
            with open(f'{phone}.pkl', 'rb') as fb:
                user_dict = pickle.load(fb)
                cash = user_dict.get("balance")
            depo_amount = float(input("Enter the deposit amount.: "))
            cash += depo_amount
            Animate.buffer()
            print("Amount deposited successfully.")
            user_dict.update({"balance": cash})
            with open(f'{phone}.pkl', 'wb') as f:
                pickle.dump(user_dict, f)
        except Exception as e:
            print(e)
    @staticmethod
    def transfer():
        try:
            phone = input("Please enter your registered phone number")
            with open(f"{phone}.pkl", "rb") as f1:
                sender_dict = pickle.load(f1)
                s_cash = sender_dict.get("balance")
                print(f"Available balance: {s_cash}")
                receiver = input("Please enter receiver's phone number: ")
                receiver_name = input("Please enter the receiver name: ")
                trans_cash = float(input("Please enter the transfer amount: "))
                if trans_cash <= s_cash:
                    trans_pin = advpass("Please enter your transaction pin: ")
                    valid_transpin = b64decode(sender_dict.get("trans_pin")).decode("utf-8")
                    if trans_pin == valid_transpin:
                            with open(f"{receiver}.pkl", "rb") as f2:
                                receiverdict = pickle.load(f2)
                                r_cash = receiverdict.get("balance")
                                r_cash += trans_cash
                                s_cash -= trans_cash
                                print(f"Available balance: {s_cash}")
                                receiverdict.update({"balance": r_cash})
                                sender_dict.update({"balance": s_cash})
                                with open(f"{receiver}.pkl", "wb") as f3:
                                    pickle.dump(receiverdict, f3)
                                with open(f"{phone}.pkl", "wb") as f:
                                    pickle.dump(sender_dict, f)
                                print(
                                    f"{trans_cash} Transferred to {receiver_name} successfully")
                    else:
                        print("You enter incorrect transaction pin!!!")
                else:
                    print("You do not have sufficient balance!!!")

        except Exception as e:
            print(e)
            print("You do not have an active account in this bank.")

    @staticmethod
    def pass_change():
        try:
            phone = input(f"Please enter your registered phone number: ")
            curr_pass = advpass(
                "Please Enter current Password For Confirmation. : ")
            if Bank.check_details(phone, curr_pass):
                new_pass = advpass("Enter new password: ")
                confirm_pass = advpass("Enter your new password again: ")
                confirm = Validate()
                if new_pass == confirm_pass and confirm.validate_pass(confirm_pass) is True:
                    newpass = b64encode(new_pass.encode("utf-8"))
                    with open(f'{phone}.pkl', 'rb') as fb:
                        userdict = pickle.load(fb)
                    userdict.update({"password": newpass})
                    with open(f'{phone}.pkl', 'wb') as f:
                        pickle.dump(userdict, f)
                    Animate.buffer()
                    print("Password changed successfully")
                else:
                    print("New Password and Confirmation password are not same.")
            else:
                print("Current password does not match!!!")
        except Exception as e:
            print(e)

    @staticmethod
    def phone_change():
        try:
            phone = input("Please enter your registered phone number: ")
            input_password = advpass("Please enter your current password: ")
            if Bank.check_details(phone, input_password) is True:
                new_phone = input("Enter your new phone number: ")
                check = Validate()
                if check.validate_phone(new_phone) is True:
                    with open(f"{phone}.pkl", "rb") as f:
                        userdict = pickle.load(f)
                        userdict.update({"phone": new_phone})
                    os.rename(f"{phone}.pkl", f"{new_phone}.pkl")
                    with open(f"{new_phone}.pkl", "wb") as f:
                        pickle.dump(userdict, f)
                    Animate.buffer()
                    print("Phone Number changed successfully")
        except Exception as e:
            print(e)
