from selenium import webdriver
from booksPage import BooksPage

def main():
    driver = webdriver.Chrome()
    page = BooksPage(driver)

    try:
        print("=" * 60)
        print("EXTRACTION DE DONNÉES DE LIVRES")
        print("=" * 60)

        print("\n--- Phase 1: Navigation ---")
        page.open()
        print("Accédé à books.toscrape.com")

        page.wait_for_books_to_load()
        print("Livres chargés")

        print("\n--- Phase 2: Extraction des Données ---")
        books = page.extract_book_data()
        print(f"{len(books)} livres extraits avec succès")

        for book in books:
            print(f"Livre {book['id']}: {book['title']} - £{book['price']:.2f} ({book['rating']})")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()

if __name__ == "__main__":
    main()