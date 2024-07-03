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
                quit()
            password = getpass("Password: ")
            if users[username] == password:
                print(f"Welcome, {username}")
                print("#########################################")
                myDash = DashboardDisplay()
                myDash.run()
            print("User not found. Please try again.\n")

if __name__ == "__main__":
    myLogin = Login()
    myLogin.run()