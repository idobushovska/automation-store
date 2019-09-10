#!/usr/bin/env python

config = {
    "website": {
        "homepage": "http://automationpractice.com/index.php",
        "login": "test21@email.com",
        "pass": "test1234"
    },
    "selenium": {
        "drivers": ["Chrome", "Firefox"],
        "Chrome": {
            "driver_path": ".bin/chromedriver"
        },
        "Firefox": {
            "driver_path": ".bin/geckodriver"
        }
    }
}