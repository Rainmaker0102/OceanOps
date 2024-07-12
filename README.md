# OceanOps
Python based CLI business management tool with support loading data from JSON

## Operation
1. Open the folder OceanOps and run the command `python src/login.py` to start the program from the beginning
2. Login with user credentials in global_info.py
3. You then have the main option of View [A]ccounts and [Q]uit (orders yet to come).
4. There are two secret options at this level, including [L]oading & dumping data files to and from global_info, and [DEBUG]
5. Accounts is the account manager, with full CRUD implementation and file Loading & Saving.
6. Loading is the interface to the load module.
7. Debug is the default data generator.
8. Inputting Q when it is an option takes you back to the previous module, until you exit the program.

## Improvements
1. Implement the order manager
2. Pretty up the UI with termcolor
4. Curses?!?!