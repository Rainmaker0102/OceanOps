# load
# This is the display for loading json files

from os import listdir
from json import dump, load
# from global_info import b2b_accounts, b2b_orders, b2c_accounts, b2c_orders
import global_info

class fileLoader():
    def __init__(self, active=True):
        self.loadables = {load_key: load_value for load_key, load_value in enumerate(listdir("../data"))}
        self.active = active
        self.valid_files = list(self.loadables.values())
    
    def get_loadables(self):
        return self.loadables

    def load(self, loadable):
        match loadable:
            case "b2b_accounts.json":
                global_info.b2b_accounts = load(loadable)
            case "b2c_accounts.json":
                global_info.b2c_accounts = load(loadable)
            case "b2b_orders.json":
                global_info.b2b_orders = load(loadable)
            case "b2c_orders.json":
                global_info.b2c_orders = load(loadable)
            case _:
                raise Exception(f"Not a valid file. Only valid files are {self.valid_files}")

    def dump(self, dumpable):
        match dumpable:
            case "b2b_accounts.json":
                with open(dumpable, "w") as file:
                    dump(global_info.b2b_accounts, file)
            case "b2c_accounts.json":
                with open(dumpable, "w") as file:
                    dump(global_info.b2c_accounts, file)
            case "b2b_orders.json":
                with open(dumpable, "w") as file:
                    dump(global_info.b2b_orders, file)
            case "b2c_orders.json":
                with open(dumpable, "w") as file:
                    dump(global_info.b2c_orders, file)
            case _:
                raise Exception(f"Not a valid file. Only valid files are {self.valid_files}")

    def run(self):
        print("Welcome to the file loader!")
        print("Below are a list of available files to load")
        print("##############################")
        for load_key, load_value in self.loadables.items():
            print(f"{load_key}\t{load_value}")
        selected = False
        while not selected:
            selection = input("Please select the number of the file you would like to load or [Q]uit: ")
            if selection.upper() == "Q":
                print("Exiting the File Loader")
                break
            else:
                selection = int(selection)
            if selection in self.loadables:
                print(f"You have selected {self.loadables[selection]}")
            else:
                print("Your selection was invalid. ")
