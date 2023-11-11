# Zillow Rental Listings Scraper

## Project Overview
This project involves a Python script that scrapes rental property listings from Zillow, extracts relevant data like price, address, and listing URL, and then automatically populates and submits this information to a Google Form. It leverages BeautifulSoup for web scraping and Selenium for automating web browser interactions.

## Goal
The aim is to automate the process of collecting rental property information from Zillow for analysis or record-keeping purposes, without manually browsing and entering data.

## Reasoning
Manually searching for rental properties and compiling data can be time-consuming and inefficient. This automated script simplifies data collection, enabling users to focus on analysis and decision-making.

## How It Works
1. **Setup URL and WebDriver**: The script starts with the URL of the Zillow page to scrape and initializes the Chrome WebDriver.
2. **Web Scraping**: The BeautifulSoup library is used to parse HTML content from Zillow and extract information like prices, addresses, and URLs of listings.
3. **Automated Form Submission**: Selenium automates the process of filling out a Google Form with the scraped data for each listing.
4. **Loop Through Listings**: The script iterates through all the listings, submitting each one to the form.

## Code Explanation
- **Libraries Used**:
  - `BeautifulSoup` from `bs4`: For parsing HTML and extracting data.
  - `requests`: To send HTTP requests.
  - `selenium`: For automating web browser interactions.
- **Script Flow**:
  1. Fetch HTML content from Zillow using `requests`.
  2. Parse the HTML to find listings details using `BeautifulSoup`.
  3. Extract and print the prices, addresses, and URLs of the listings.
  4. Use Selenium's WebDriver to automate data entry in a Google Form.
  5. Submit the form for each listing and then close the browser.

## How to Use
1. Update the `chrome_driver_path`, `URL`, and Google Form URL in the script.
2. Ensure Chrome WebDriver is installed and compatible with your browser version.
3. Run the script to start scraping and submitting data.

## Future Enhancements
- Extend functionality to handle dynamic web pages.
- Include error handling and logging.
- Implement user-friendly inputs for URLs and WebDriver paths.

## Disclaimer
This script is for educational purposes. Respect Zillow's terms of service and use ethical scraping practices.

---

*Efficient Data Collection Made Easy!*
