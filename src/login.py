# login
# This the page that manages logging in

# Python Imports
from getpass import getpass

# Project Imports
from global_info import users
from biz_dash import DashboardDisplay

class Login():
    def __init__(self, active=True):
        self.active = active

    def run(self):
        while self.active:
            print("Welcome to OceanOps! Please sign in. [Q]uit")
            username = input("Username: ")
            if username.upper() == "Q":
                print("Thanks for using OceanOps. Have a nice day!")
                break
            password = getpass("Password: ")
            if username not in users.keys():
                print("User was not found. Please try again.\n")
            elif users[username] != password:
                print("Password incorrect. Please try again.\n")
            else:
                print(f"Welcome, {username}")
                print("#########################################")
                myDash = DashboardDisplay()
                myDash.run()

if __name__ == "__main__":
    myLogin = Login()
    myLogin.run()