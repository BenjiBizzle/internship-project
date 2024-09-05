from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRICE_ELEMENTS = (By.CSS_SELECTOR, ".number-price-text")


@then('Click on “Secondary” option at the left side menu')
def click_on_secondary_menu(context):
    context.app.main_page.click_secondary()
    # context.driver.find_element(*CLICK_SECONDARY_OPTION).click()
    sleep(3)


@then('Verify the right page opens')
def verify_right_url(context):
    context.app.main_page.verify_current_url()
    sleep(3)


@then('Click on Filters')
def click_filters(context):
    context.app.main_page.click_filters()
    sleep(3)


@then('Filter the products by price range from 1200000 to 2000000 AED')
def filter_product_by_price_range(context):
    sleep(5)
    context.app.main_page.click_from_price()
    context.app.main_page.click_to_price()
    context.app.main_page.click_apply()
    sleep(3)


# @then('Verify the price in all cards is inside the range (1200000 - 2000000)')
# def verify_price_in_all_cards(context):
#     expected_price =
#     prices = context.driver.find_elements(*PRICE_ELEMENTS)
#     for price in prices:
#         price.click()
#
#         selected_price = context.driver.find_elements(*PRICE_ELEMENTS).text
#         print('price', selected_price)
#
#         selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
#         actual_colors.append(selected_color)
#         print(actual_colors)
#
#     assert expected_price == actual_colors, f'Expected {expected_price} did not match actual {actual_colors}'
@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def verify_price_in_all_cards(context):
    # Define the expected range
    min_price = 1200000
    max_price = 2000000

    # Locate all price elements on the page
    prices = context.driver.find_elements(*PRICE_ELEMENTS)  # Replace PRICE_ELEMENTS with the actual locator

    # List to store prices that are out of range
    out_of_range_prices = []

    for price in prices:
        # Get the text of the price element
        price_text = price.text

        # Clean up the text to extract the numerical value
        # This assumes prices might have commas or currency symbols that need to be removed
        try:
            price_value = int(price_text.replace(',', '').replace('AED', '').strip())

            # Check if the price is within the range
            if price_value not in range(min_price, max_price+1):
                out_of_range_prices.append(price_value)

        except ValueError:
            print(f"Could not convert price: {price_text}")  # Print an error message if conversion fails

    # Assert that all prices are within the expected range
    assert len(out_of_range_prices) == 0, f'There are {len(out_of_range_prices)} out of range prices'
    sleep(5)