#!/usr/bin/env python

config = {
    "website": {
        "homepage": "http://automationpractice.com/index.php",
        "catalogue": "http://automationpractice.com/index.php?id_category=8&controller=category",
        "email": "test23@email.com",
        "passwd": "test1234",
        "new_customer": {
            "firstname": "Gregory",
            "lastname": "House",
            "company": "Ira's networks",
            "address": "5234 Santana Row",
            "city": "Mountain View",
            "state": "California",
            "zip": "94043",
            "mobile": "4083843847",
            "email_pattern": "as_{}@autostore.com",
            "passwd": "test1234$",
            "dob": "03/13/1987"
        }
    },
    "selenium": {
        "drivers": ["Chrome"],
        "Chrome": {
            "driver_path": ".bin/chromedriver"
        }
    }
}