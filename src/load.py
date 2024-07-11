# load
# This is the display for loading json files

from os import listdir
from json import dump, load
# from global_info import b2b_accounts, b2b_orders, b2c_accounts, b2c_orders
import global_info

class fileLoader():
    def __init__(self, active=True, data_dir="data/"):
        self.data_dir = data_dir
        self.loadables = {load_key: load_value for load_key, load_value in enumerate(listdir(self.data_dir))}
        self.active = active
        self.valid_files = list(self.loadables.values())
    
    def get_loadables(self):
        return self.loadables

    def load(self, loadable):
        match loadable:
            case "b2b_accounts.json":
                with open(self.data_dir+loadable, "r") as file:
                    global_info.b2b_accounts = load(file)
            case "b2c_accounts.json":
                with open(self.data_dir+loadable, "r") as file:
                    global_info.b2c_accounts = load(file)
            case "b2b_orders.json":
                with open(self.data_dir+loadable, "r") as file:
                    global_info.b2b_orders = load(file)
            case "b2c_orders.json":
                with open(self.data_dir+loadable, "r") as file:
                    global_info.b2c_orders = load(file)
            case _:
                raise Exception(f"{loadable} is not a valid file. Only valid files are {self.valid_files}")

    def dump(self, dumpable):
        match dumpable:
            case "b2b_accounts.json":
                with open(self.data_dir+dumpable, "w") as file:
                    dump(global_info.b2b_accounts, file)
            case "b2c_accounts.json":
                with open(self.data_dir+dumpable, "w") as file:
                    dump(global_info.b2c_accounts, file)
            case "b2b_orders.json":
                with open(self.data_dir+dumpable, "w") as file:
                    dump(global_info.b2b_orders, file)
            case "b2c_orders.json":
                with open(self.data_dir+dumpable, "w") as file:
                    dump(global_info.b2c_orders, file)
            case _:
                raise Exception(f"{dumpable} is not a valid file. Only valid files are {self.valid_files}")

    def run(self):
        print("Welcome to the file loader!")
        selected = False
        while not selected:
            print("Below are a list of available files to load")
            print("##############################")
            for load_key, load_value in self.loadables.items():
                print(f"{load_key}\t{load_value}")
            print("##############################")
            selection = input("Please select the number of the file you would like to load or dump. [Q]uit: ")
            if selection.upper() == "Q":
                print("Exiting the File Loader")
                break
            else:
                selection = self.loadables[int(selection)]
                if selection[-5:] != ".json":
                    print("Invalid file, please select a '.json'")
                elif selection in self.loadables.values():
                    print(f"You have selected {selection}")
                    lord = ""
                    while lord.upper() != "Q":
                        lord = input("Would you like to [L]oad, [D]ump, or [Q]uit? ")
                        match lord.upper():
                            case "Q":
                                print("Exiting the loader")
                                break
                            case "L":
                                self.load(selection)
                                print("Here's the effects of the load")
                                print(f"B2B Accounts: {global_info.b2b_accounts}")
                                print(f"B2B Orders: {global_info.b2b_orders}")
                                print(f"B2C Accounts: {global_info.b2c_accounts}")
                                print(f"B2C Orders: {global_info.b2c_orders}")
                                lord = "Q"
                            case "D":
                                self.dump(selection)
                                print("Here's the effects of the dump")
                                with open(self.data_dir + selection, "r") as file:
                                    data = load(file)
                                    print(data)
                                lord = "Q"
                            case _:
                                print("Invalid input. Please choose from the list of valid inputs")
                    
                else:
                    print("Your selection was invalid. ")
