# b2c_info
# Stub for B2C info; accounts and orders

accounts = {
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

orders = {
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
        "account": "Amazon",
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
        "account": "Amazon",
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
        "account": "SUSE",
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
        "account": "SUSE",
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
        "account": "SUSE",
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