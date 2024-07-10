# global_info
# This file stores basic info about the user that's not too sensitive
# Stub for the proper JSON handling

business_name = "Revature"
FUNC_NOT_SUPPORTED = "Functionality is not supported, please code me"

users = {
    "seand": "twelvefortytwo",
    "cheeser": "iowawawa",
    "willt": "oneweek",
    "admin": "admin"
}

b2b_accounts = {
    1: {
        "name": "Microsoft",
        "phone": "456-785-1257",
        "email": "biz@microsoft.com",
    },
    2: {
        "name": "Amazon",
        "phone": "682-742-9152",
        "email": "biz_relations@amazon.com",
    },
    3: {
        "name": "SUSE",
        "phone": "682-742-9152",
        "email": "biz_relations@amazon.com",
    },
}

b2b_orders = {
    1.0: {
        "account": 1,
        "invoice": {
            "items": {
                "Windows 10 License": {
                    "SKU": 123456,
                    "price": 100.00
                }, 
                "Xbox Game Pass 1MO": {
                    "SKU": 343434,
                    "price": 1.00
                }, 
                "Flight simulator": {
                    "SKU": 908765,
                    "price": 12.45
                },
                },
            "total price": 123.45,
            "date": "03-07-2024",
            "time": "13:45"
        }
    },
    2.0: {
        "account": 2,
        "invoice": {
            "items": {
                "Roomba Robot Vacuum Cleaner": {
                    "SKU": 100101,
                    "price": 99.99
                }, 
                },
            "total price": 99.99,
            "date": "04-07-2024",
            "time": "9:00"
        }
    },
    2.1: {
        "account": 2,
        "invoice": {
            "items": {
                "Roomba Robot Vacuum Cleaner": {
                    "SKU": 100101,
                    "price": -99.99
                }, 
                },
            "total price": -99.99,
            "date": "04-07-2024",
            "time": "15:15"
        }
    },
    3.0: {
        "account": 3,
        "invoice": {
            "items": {
                "SLES Support Subscription": {
                    "SKU": 350551,
                    "price": 199.99
                }, 
                },
            "total price": 199.99,
            "date": "05-01-2024",
            "time": "9:00"
        }
    },
    3.1: {
        "account": 3,
        "invoice": {
            "items": {
                "SLES Support Subscription": {
                    "SKU": 350551,
                    "price": 199.99
                }, 
                },
            "total price": 199.99,
            "date": "05-02-2024",
            "time": "9:00"
        }
    },
    3.2: {
        "account": 3,
        "invoice": {
            "items": {
                "SLES Support Subscription": {
                    "SKU": 350551,
                    "price": 199.99
                }, 
                },
            "total price": 199.99,
            "date": "05-02-2024",
            "time": "9:00"
        }
    },
}

b2c_accounts = {
    1: {
        "first name": "Elizabeth",
        "last name": "Herring",
        "phone": "208-445-7592",
        "email": "ElizabethSHerring@teleworm.us",
    },
    2: {
        "first name": "James",
        "last name": "Daley",
        "phone": "415-537-0379",
        "email": "jamesNDaley@teleworm.us",
    },
    3: {
        "first name": "Thomas",
        "last name": "Elswick",
        "phone": "216-390-9772",
        "email": "ThomasLElswick@dayrep.com",
    },
}

b2c_orders = {
    1.0: {
        "account": 1,
        "invoice": {
            "items": {
                "Windows 10 License": {
                    "SKU": 123456,
                    "price": 100.00
                }, 
                "Xbox Game Pass 1MO": {
                    "SKU": 343434,
                    "price": 1.00
                }, 
                "Flight simulator": {
                    "SKU": 908765,
                    "price": 12.45
                },
                },
            "total price": 123.45,
            "date": "03-07-2024",
            "time": "13:45"
        }
    },
    2.0: {
        "account": 2,
        "invoice": {
            "items": {
                "Roomba Robot Vacuum Cleaner": {
                    "SKU": 100101,
                    "price": 99.99
                }, 
                },
            "total price": 99.99,
            "date": "04-07-2024",
            "time": "9:00"
        }
    },
    2.1: {
        "account": 2,
        "invoice": {
            "items": {
                "Roomba Robot Vacuum Cleaner": {
                    "SKU": 100101,
                    "price": -99.99
                }, 
                },
            "total price": -99.99,
            "date": "04-07-2024",
            "time": "15:15"
        }
    },
    3.0: {
        "account": 2,
        "invoice": {
            "items": {
                "SLES Support Subscription": {
                    "SKU": 350551,
                    "price": 199.99
                }, 
                },
            "total price": 199.99,
            "date": "05-01-2024",
            "time": "9:00"
        }
    },
    3.1: {
        "account": 3,
        "invoice": {
            "items": {
                "SLES Support Subscription": {
                    "SKU": 350551,
                    "price": 199.99
                }, 
                },
            "total price": 199.99,
            "date": "05-02-2024",
            "time": "9:00"
        }
    },
    3.2: {
        "account": 3,
        "invoice": {
            "items": {
                "SLES Support Subscription": {
                    "SKU": 350551,
                    "price": 199.99
                }, 
                },
            "total price": 199.99,
            "date": "05-02-2024",
            "time": "9:00"
        }
    },
}