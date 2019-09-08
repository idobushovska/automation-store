Add description
# automation-store
Practice of websites automation testing

# How to run
1. Checkout repository `git checkout git@github.com:idobushovska/automation-store.git`
1. Create your virtual env and install dependencies by running command: ` virtualenv .env && source .env/bin/activate && pip install -r requirements.txt `
1. Install chromedriver
    1. In case of Mac OS:
        1. Download Chromedriver: `LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_mac64.zip`
        1. Install Chromedriver `mkdir .bin/ && unzip chromedriver_mac64.zip && mv chromedriver .bin/ && rm chromedriver_mac64.zip`
    1. In case of Linux:
        1. Download Chromedriver: `LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip`
        1. Install Chromedriver `mkdir .bin/ && unzip chromedriver_linux64.zip && mv chromedriver .bin/ && rm chromedriver_linux64.zip`
