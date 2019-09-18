# automation-store
Practice of websites automation testing. Website for testing coverage: http://automationpractice.com/index.php

# Planned coverage
[x] Critical Path (Registration/Login/Search/Add to cart/Checkout/View Order)
[x] Home Page
[] Catalogue
[] Contact Form

# How to run
1. Checkout repository `git clone git@github.com:idobushovska/automation-store.git && cd automation-store`
2. Create your virtual env and install dependencies by running command: `virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`
3. Download & Install chromedriver
    a. In case of Mac OS: `LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_mac64.zip && mkdir .bin/ && unzip chromedriver_mac64.zip && mv chromedriver .bin/ && rm chromedriver_mac64.zip`
    b. In case of Linux: `LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip && mkdir .bin/ && unzip chromedriver_linux64.zip && mv chromedriver .bin/ && rm chromedriver_linux64.zip`
4. Run tests: `python test_runner.py`
