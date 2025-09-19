class Bank_account:
    def __init__(self, account_name:str, account_number:int):
        self.account_name:str = account_name
        self.account_number:int = account_number

    def get_account_number(self)->int:
        return self.account_number


