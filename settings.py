#!/usr/bin/env python

config = {
    "website": {
        "homepage": "http://automationpractice.com/index.php",
        "email": "test21@email.com",
        "passwd": "test1234",
        "new_customer": {
            "firstname": "Greg",
            "lastname": "House",
            "company": "Ira's networks",
            "address": "5234 Santana Row",
            "city": "Mountain View",
            "state": "California",
            "zip": "90344",
            "mobile": "209000001",
            "email_pattern": "as_{}@autostore.com",
            "passwd": "test1234$",
            "dob": "02/24/1987"
        }
    },
    "selenium": {
        "drivers": ["Chrome"],
        "Chrome": {
            "driver_path": ".bin/chromedriver"
        }
    }
}