from maskpass import advpass
from random import randint
from bank import Bank
from validation import Validate
from base64 import b64encode
import pickle
class Register:
    @classmethod
    def register(cls):
        regis_nums={}
        acc_no = ''
        cash = 0.00
        condition=False
        print("Creating a new account")
        name = input("Enter your full name: ").title()
        phone = input("Enter your active phone number: ")
        password = advpass("Enter a strong password(8-32 characters): ")
        enc_password = b64encode(password.encode("utf-8"))
        trans_pin = advpass(
                "Enter a 4 digit transaction pin for fund transfer: ")
        enc_trans_pin = b64encode(trans_pin.encode("utf-8"))
        conditions = Validate()
        if conditions.validate_pass(password) and conditions.validate_phone(phone) and conditions.validate_transpin(
                    trans_pin):
            try:
                with open("registeredNumbers.txt","rb") as f:
                    regis_nums=pickle.load(f)
                    if phone in regis_nums.values():
                        condition=True
                if condition is False:
                    acc_no = 'MUF' + str('%0.4d' % randint(0, 9999))
                    with open("registeredNumbers.txt","wb") as f:
                        regis_nums[acc_no]=phone
                        pickle.dump(regis_nums,f)
                    Bank(name, phone, enc_password, enc_trans_pin, acc_no, cash)
                else:
                    print("This number has already an active account in this bank.")
            except:
                acc_no = 'MUF' + str('%0.4d' % randint(0, 9999))
                with open("registeredNumbers.txt","wb+") as f:
                    regis_nums[acc_no]=phone
                    pickle.dump(regis_nums,f)
                Bank(name, phone, enc_password, enc_trans_pin, acc_no, cash)
            
      
