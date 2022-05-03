class Validate:
    def __init__(self):
        self.conditions = True

    def validate_pass(self, password):
        try:
            assert len(password) in range(
                8, 32), "Please enter password within defined range"
        except AssertionError as msg:
            self.conditions = False
            print(msg)
        return self.conditions

    def validate_phone(self, phone):
        try:
            assert len(phone) == 10, "Not a valid phone number"
        except AssertionError as msg:
            self.conditions = False
            print(msg)
        return self.conditions

    def validate_transpin(self, trans_pin):
        try:
            assert len(trans_pin) == 4, "Enter a four digit pin."
        except AssertionError as msg:
            self.conditions = False
            print(msg)
        return self.conditions
