from bank import Bank
from login import Login
from register import Register
from clearscrn import Animate

if __name__ == '__main__':
    while True:
        Animate.clear()
        print('Welcome to Muffy Bank')
        print('1.Login')
        print('2.Create a new Account')
        print('3.Deposit amount')
        print('4.Exit')
        choice = int(input('Please choose an option: '))
        Animate.buffer()
        if choice == 1:
            attempts = 3
            flag = True
            logging_in = Login()
            Animate.clear()
            if not logging_in.login():
                attempts -= 1
                while attempts > 0:
                    print(f'You have {attempts} attempts left.')
                    log_again = input(
                        str('Would you like to try again??(Y/N): ')).upper()
                    if log_again == 'Y':
                        attempts -= 1
                        Animate.buffer()
                        Animate.clear()
                        if logging_in.login() is not False:
                            break
                    if log_again == 'N':
                        flag = False
                        Animate.buffer()
                        Animate.clear()
                        break
                if attempts == 0:
                    print('You ran out of the attempts!!!')
                    Animate.buffer()
                    Animate.clear()
                    continue
                if not flag:
                    continue
            while True:
                if logging_in:
                    print('1.Transfer amount')
                    print('2.Edit profile')
                    print('3.Logout')
                    login_user = int(input())
                    Animate.buffer()
                    Animate.clear()
                    if login_user == 1:
                        Bank.transfer()
                        print('1.back menu')
                        print('2.Logout')
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                    elif login_user == 2:
                        print('1.Password change')
                        print('2.Phone Number change')
                        print("3. Back")
                        edit_profile = int(input())
                        Animate.buffer()
                        Animate.clear()
                        if edit_profile == 1:
                            Bank.pass_change()
                            break
                        elif edit_profile == 2:
                            Bank.phone_change()
                            break
                        elif edit_profile == 3:
                            continue
                    elif login_user == 3:
                        Animate.buffer()
                        Animate.clear()
                        break

        elif choice == 2:
            flag = True
            while flag:
                Animate.clear()
                Register.register()
                Animate.buffer()
                if Bank.accounts is True:
                    try_again = input(
                        "Would you like to try again??..(Y/N): "
                    ).upper()
                    if try_again == 'N':
                        Animate.clear()
                        flag = False
                else:
                    flag = False
        elif choice == 3:
            Animate.clear()
            Bank.deposit()
            Animate.buffer()
        elif choice == 4:
            Animate.clear()
            break

        else:
            print("Invalid option!!! Please reconsider your choice.")
