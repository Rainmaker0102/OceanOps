# debug
# Debug class to generate default data

import global_info
import b2b_info, b2c_info

class debugg():
    def generateDefaultData(self):
        global_info.b2b_accounts = b2b_info.accounts
        global_info.b2b_orders = b2b_info.orders
        global_info.b2c_accounts = b2c_info.accounts
        global_info.b2c_orders = b2c_info.orders

    def run(self):
        print("WARNING: This is a debug module to regenerate default data for the program.")
        print("IT WILL OVERWRITE ANY DATA CURRENTLY LOADED INTO PROGRAM MEMORY. It will NOT touch JSON files.")
        while True:
            selection = input("Would you like to [G]enerate data or [Q]uit? ")
            match selection.upper():
                case "Q":
                    print("Quitting the debug menu. Your data has not been altered.")
                    break
                case "G":
                    self.generateDefaultData()
                    print("Default data has finished regenerating. Returning to the Dashboard")
                    break
                case _:
                    print("Invalid input. Please select an option from the following valid inputs.")
        print()

if __name__ == "__main__":
    my_debugg = debugg()
    my_debugg.run()
