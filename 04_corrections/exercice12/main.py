from selenium import webdriver
from searchPage import SearchPage

driver = webdriver.Chrome()
page = SearchPage(driver)


try:
    page.open()

    page.wait_for_page_ready()

    page.search_products("hammer")

    page.wait_for_results()
      
    products = page.extract_product_data()

    for product in products:
         print(f"Produit {product['id']}: {product['name']} - ${product['price']:.2f}")


except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

finally:
    driver.quit()