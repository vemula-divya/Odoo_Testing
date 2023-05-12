[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/15.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/15.0/administration/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/15.0/developer/howtos.html">the developer tutorials</a>



------------------------------
In this project added three types of testing for the Odoo Lunch application: unit testing, Selenium testing, and Keyword-Driven testing.

Odoo Lunch is a web-based application that allows users to order food online. It is a module in the larger Odoo ERP system, which is a suite of open-source business applications that cover various areas such as accounting, inventory management, project management, and more. Odoo Lunch is designed to help companies streamline their food ordering process and make it more efficient. Users can browse through the available menu items, place orders, and pay online using their preferred payment method. The application is customizable and can be adapted to suit the specific needs of different businesses.


**To set up environmental variables for Selenium automation, follow these steps:**

1. Install Python and add the following paths to the environmental variables:
- C:\Users\username\AppData\Local\Programs\Python\Python311\Scripts\
- C:\Users\username\AppData\Local\Programs\Python\Python311\

2. Install the ChromeDriver WebDriver and add the following path to the environmental variables:
- C:\Users\username\Downloads\chromedriver_win32

**To set up Odoo for unit testing and database management, follow these steps:
**
1. Install PostgreSQL and create a username and password for it.
2. During the installation of Odoo, enter the master password on the homepage and set up a new database with the name "Odoo_new" and password "Odoo_15". For a new user with the email "d1227@gmail.com", create a new database with the name "Odoo_new1", password "Odoo_151", and username "d1227@gmail.com".
3. To manage the database, go to http://localhost:8069/web/database/selector.

**UnitTest Cases:**


To run unit test cases for the lunch app in Odoo on the server, follow these steps:

1. In the odoo.conf file, set the following options:
- test_enable = True
- test_tags = lunch
- log_level = test
2. Add the necessary dependencies to the manifest.py file.
3. Run the server and check the odoo.log file by starting localhost.


**Selenium TestCases**


1)Install the ChromeDriver WebDriver and add the following path to the environmental variables:
- C:\Users\username\Downloads\chromedriver_win32
2)pip selenium install

**Keyword-Driven Test Case:**


1)Install the Selenium library for Robot Framework using pip command: pip install robotframework-seleniumlibrary
2)Similar to selenium we required webdriver as well.




