# Front End Automation Challenge


This project is  proof of concept built in Python with Selenium to automate a web application.

# Prerequisites: 📋

  - Python3 and pip3 must be installed

### Installing Requirements 🔧 
```sh
$pip3 install -r requirements.txt

```
### How to run the tests ⚙️
```sh
$ python3 -m unittest tests/{TEST_FILE}.py

```
### Run in different Browser
You need to only update the property "browser"
in tests/data.json with :
- "chrome"
- "firefox"

and run normally
# Where TEST_FILE could be :
 - loginTest.py
 - invalidLoginTest.py
 - shoppingcartTest.py
 - productsTest.py
 - informationTest.py
