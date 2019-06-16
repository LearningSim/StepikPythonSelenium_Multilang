link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_can_add_product_to_basket(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
