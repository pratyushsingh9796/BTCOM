# BTCOM Test

## Objective - Test Case for automation

1. Launch of the application URL(https://www.bt.com/)
2. Close accept Cookie pop-up if it appears
3. Hover to Mobile menu
4. From mobile menu, select Mobile phones
5. Verify the numbers of banners present below "See Handset details" should not be less than 3
6. Scroll down and click View SIM only deals
7. Validate the title for new page.
8. Validate “30% off and double data” was 125GB 250GB Essential Plan, was £27 £18.90 per month
9. Close the browser & exit

## Validations

There are 3 Validations that are being performed:

- **TestCase 1**- Validating if there are at least 3 banners present under "See Handset details".
  
- **TestCase 2**- Validating the title for the new page that appears after clicking on "SIM only deals"
  
- **TestCase 3**- Validating if the required Plan is present in the Option List i.e "30% off and double data" was 125GB 250GB Essential Plan, was £27 £18.90 per month


## Steps to execute

1. Clone this repository in local.
2. Open the repository folder in the Pycharm IDE (File --> Open --> Folder Path).
3. Setup virtual environment in your directory.
4. Install dependencies based on the requirement file (pip install -r requirements.txt).
5. Execute Python script (python main.py).
   
## Tools

- Language- Python
- Packages- Selenium, unittest
- IDE- Pycharm

## Future Scope

This automated test case provides a foundation for testing the functionality and content of the BT.com website. Future enhancements could include:

- Extending test coverage to include more scenarios and edge cases.
- Parameterizing test data to make it more versatile.
- Implementing robust error handling and reporting mechanisms for better test management.

## Conclusion

The BTCOM automated test case ensures the functionality and content of the BT.com website. By validating critical elements such as the number of banners, page titles, and specific plan details, it helps maintain the quality and reliability of the website.
