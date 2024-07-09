# biz_dash
# This file is what displays the dashboard for the business management system
from global_info import business_name, FUNC_NOT_SUPPORTED
from load import fileLoader


class DashboardDisplay():
    def __init__(self, active=True):
        self.biz_name = business_name
        self.active = active
    
    def run(self):
        while self.active == True:
            print(f"{self.biz_name} OceanOps Management System")
            print("What would you like to do today?")
            selection = input("[Q]uit, [L]oad data files, View [A]ccounts, View [O]rders: ").upper()
            match selection:
                case "Q":
                    print("Exiting the Dashboard")
                    break
                case "L":
                    loader = fileLoader()
                    loader.run()
                case "A":
                    print("Account functionality: " + FUNC_NOT_SUPPORTED + "\n")
                case "O":
                    print("Order functionality: " + FUNC_NOT_SUPPORTED + "\n")
                case _:
                    print("That input was not accepted: Input not in input list. Please try again\n")
            

if __name__ == "__main__":
    mainDash = DashboardDisplay()
    mainDash.run()