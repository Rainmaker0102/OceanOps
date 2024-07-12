# biz_dash
# This file is what displays the dashboard for the business management system
from global_info import business_name, FUNC_NOT_SUPPORTED
from load import fileLoader
from debug import debugg
from accounts import accountManager

class dashboardDisplay():
    def __init__(self, active=True):
        self.biz_name = business_name
        self.active = active

    def run(self):
        while self.active == True:
            print(f"{self.biz_name} OceanOps Management System")
            print("What would you like to do today?")
            selection = input("[Q]uit, View [A]ccounts: ")
            match selection.upper():
                case "Q":
                    print("Exiting the Dashboard")
                    break
                case "DEBUG":
                    print("Entering the debug menu.")
                    my_debugg = debugg()
                    my_debugg.run()
                case "L":
                    loader = fileLoader()
                    loader.run()
                case "A":
                    mode = input("Which mode, 1. 'B2B' or 2. 'B2C'? [Q]uit to cancel: ")
                    match mode.upper():
                        case "Q":
                            pass
                        case "1":
                            my_account_mgr = accountManager("B2B")
                            my_account_mgr.run()
                        case "B2B":
                            my_account_mgr = accountManager("B2B")
                            my_account_mgr.run()
                        case "2":
                            my_account_mgr = accountManager("B2C")
                            my_account_mgr.run()
                        case "B2C":
                            my_account_mgr = accountManager("B2C")
                            my_account_mgr.run()
                        case _:
                            print("Invalid input. Please retry")
                case _:
                    print("That input was not accepted: Input not in input list. Please try again\n")
        print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
