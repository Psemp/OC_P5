# Open Classrooms Project 5 - Open Food Facts API

# Description

This project is about using a public API ( openfoodfacts.org ) to create a database containing a sample of products and then using a script to find healthier products easily. The whole script is made using Python and MySQL.
The goal of the software is to be flexible : the user has the choice to easily modify the sample of data extracted from the API (less data, less requests, but also less choice, but more requests = more processing time).
If the user finds a suitable substitute and wants to keep it in the database to retrieve it later, a specific table is made to store barcodes from the origin and the substitute and the time the comparison was made.

# Installation

Softwares and scritps are written using Python 3.7 or 3.8 and MySQL 8.0.something.
Used librairies are in requirements.txt (note to self : create requirements.txt)

# Usage

Typical usage of the software should start with the selection of a category : -->

Normal Pathway = 

- User creates the database locally using the API Scraping script. It should take anywhere between 5 minutes and 3 decades depending on how many pages the user wants to include.
- User now selects a category in which he wants to search a specific product to compare. Using numbers from 0 to 10 (0 to change page).
- System displays product of selected category, user selects a product he wishes to compare using the same method as the categories.
- System returns all products qualified healthier based on their nutriscore (A = Good, E = Worst). System will order the results so the healthier products are shown first
- User has the choice to save his search to find it later if he wishes


# Project Status

Under development, more bugs than Skyrim
Main functions are working somewhat properly but many details needs to be added : ShortDesc and Pictures for products ; a mean of saving searches ; a better way of navigating the databases and other details like more accurate SQL queries (Ordering results etc.)