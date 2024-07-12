# accounts
# This is the display & control for accounts

import global_info
from load import fileLoader

class accountManager():
    def __init__(self, mode):
        self.loader = fileLoader()
        mode = mode.upper()
        self.mode = mode.upper()
        match self.mode:
            case "B2B":
                self.accounts = global_info.b2b_accounts
            case "B2C":
                self.accounts = global_info.b2c_accounts
    
    def refresh_accs(self):
        match self.mode:
            case "B2B":
                self.accounts = global_info.b2b_accounts
            case "B2C":
                self.accounts = global_info.b2c_accounts

    def read_accs(self):
        print("##############################")
        for account_no, dict in self.accounts.items():
            print(f"Account No: {account_no}")
            for key, value in dict.items():
                print(f"\t{key}: {value or "NULL"}")

    def read_acc(self, acc):
        for key, value in acc.items():
            print(f"\t{key}: {value or "NULL"}")

    def select_acc(self):
        while True:
            selectable = None
            self.read_accs()
            selection = input("Please give me the account number you'd like to select or [Q]uit: ")
            if selection.upper() == "Q":
                print("Exiting the selector")
                return None
            try:
                selectable = self.accounts[selection]
            except KeyError:
                print("That number was not a valid account number. Please give a valid account number from the following list")
            finally:
                if selectable != None:
                    return selectable
                else:
                    continue

    def create_acc(self):
        if self.mode == "B2B":
            account_no = max((int(key) for key in self.accounts.keys()), default=0) + 1
            print(f"Welcome to the account creator! You'll be creating account No: {account_no}")
            while True:
                account_name = input("Enter the new account name, '$back' to restart or [Q]uit: ")
                if account_name.upper() == "Q":
                    break
                elif account_name == "$back":
                    continue
                account_phone = input("Enter the new account phone in the format XXX-XXX-XXXX or '$back' to restart: ")
                if account_phone == "$back":
                    continue
                account_email = input("Enter the new account email in the format 'name@example.com' or '$back' to restart: ")
                if account_email == "$back":
                    continue
                print("Is the following correct for your account?")
                print(f"Account No: {account_no}")
                print(f"Account Name: {account_name}")
                print(f"Account Phone: {account_phone}")
                print(f"Account Email: {account_email}")
                confirmation = input("Y/n: ").upper()
                if confirmation != "" and confirmation != "Y":
                    restart_confirm = input("Would you like to [R]estart? ").upper()
                    if restart_confirm == "R":
                        continue
                    else:
                        break
                else:
                    self.accounts[account_no] = {
                        "name": account_name,
                        "phone": account_phone,
                        "email": account_email,
                    }
                    print("The account has been created successfully!")
                    break
        elif self.mode == "B2C":
            account_no = max((int(key) for key in self.accounts.keys()), default=0) + 1
            print(f"Welcome to the account creator! You'll be creating account No: {account_no}")
            while True:
                account_fname = input("Enter the new account first name, '$back' to restart or [Q]uit: ")
                if account_fname.upper() == "Q":
                    break
                elif account_fname == "$back":
                    continue
                account_lname = input("Enter the new account last name or '$back' to restart: ")
                if account_lname == "$back":
                    continue
                account_phone = input("Enter the new account phone in the format XXX-XXX-XXXX or '$back' to restart: ")
                if account_phone == "$back":
                    continue
                account_email = input("Enter the new account email in the format 'name@example.com' or '$back' to restart: ")
                if account_email == "$back":
                    continue
                print("Is the following correct for your account?")
                print(f"Account No: {account_no}")
                print(f"Account First Name: {account_fname}")
                print(f"Account Last Name: {account_lname}")
                print(f"Account Phone: {account_phone}")
                print(f"Account Email: {account_email}")
                confirmation = input("Y/n: ").upper()
                if confirmation != "" and confirmation != "Y":
                    restart_confirm = input("Would you like to [R]estart? ").upper()
                    if restart_confirm == "R":
                        continue
                    else:
                        break
                else:
                    self.accounts[account_no] = {
                        "first name": account_fname,
                        "first name": account_lname,
                        "phone": account_phone,
                        "email": account_email,
                    }
                    print("The account has been created successfully!")
                    break

    def update_acc(self, updateable):
        if updateable == None:
            pass
        else:
            while True:
                print("Welcome to the updater!")
                print("Please select the attribute you'd like to update")
                self.read_acc(updateable)
                selection = None
                if self.mode == "B2B":
                    selection = input("[N]ame, [P]hone, [E]mail, or [Q]uit when you're finished: ").upper()
                    match selection:
                        case "Q":
                            print("Exiting the updater")
                            break
                        case "N":
                            new_name = input("Enter the new name for the account or [Q]uit to cancel: ")
                            if new_name.upper() != "Q":
                                updateable["name"] = new_name
                                print("Your changes have been applied")
                        case "P":
                            new_phone = input("Enter the new account phone in the format XXX-XXX-XXXX or [Q]uit to cancel: ")
                            if new_phone.upper() != "Q":
                                updateable["phone"] = new_phone
                                print("Your changes have been applied")
                        case "E":
                            new_email = input("Enter the new account email in the format 'name@example.com' or [Q]uit to cancel: ")
                            if new_email.upper() != "Q":
                                updateable["email"] = new_email
                                print("Your changes have been applied")
                        case _:
                            print("Invalid input. Please select from the following list of inputs.")
                        


    def delete_acc(self, deleteable):
        if deleteable == None:
            pass
        else:
            print("Welcome to the deleter!")
            print(f"You're about to delete the below account")
            self.read_acc(deleteable)
            confirmation = input("Are you sure you want to delete this? y/N: ")
            if confirmation.upper() == "Y":
                key_to_delete = next((key for key, value in self.accounts.items() if value == deleteable), None)
                if key_to_delete is not None:
                    del self.accounts[key_to_delete]
                    print("Deletion successful")
            else:   
                print("Deletion cancelled. Data has not been changed")


    def run(self):
        print(f"Welcome to the {self.mode} Account Manager")
        while True:
            print(f"Below are a list of your current accounts")
            self.read_accs()
            print("What would you like to do in the account mananger?")
            selection = input("[C]reate, [U]pdate, [D]elete, [L]oad from file, [S]ave to file, [Q]uit: ")
            match selection.upper():
                case "Q":
                    print("Exiting the account manager")
                    break
                case "C":
                    self.create_acc()
                case "U":
                    self.update_acc(self.select_acc())
                case "D":
                    self.delete_acc(self.select_acc())
                case "L":
                    if self.accounts != {}:
                        confirm = input("This will overwrite any accounts currently loaded into memory. Are you sure? y/N: ").upper()
                        if confirm == "Y":
                            self.loader.global_load(f"{self.mode.lower()}_accounts.json")
                            print(f"Files loaded from {self.mode.lower()}_accounts.json")
                            self.refresh_accs()
                        else:
                            print("The loaded accounts have not been altered")
                    else:
                        self.loader.global_load(f"{self.mode.lower()}_accounts.json")
                        print(f"Files loaded from {self.mode.lower()}_accounts.json")
                    self.refresh_accs()
                case "S":
                    if f"{self.mode.lower()}_accounts.json" not in self.loader.valid_files:
                        with open(f"{self.mode.lower()}_accounts.json", "w") as file:
                            pass
                    self.loader.global_dump(f"{self.mode.lower()}_accounts.json")
                    print(f"Files saved to {self.mode.lower()}_accounts.json")
                    # self.refresh_accs()
                case _:
                    print("Invalid input. Please select from one of the following valid inputs.")