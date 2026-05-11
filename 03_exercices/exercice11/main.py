import os
import time
from selenium import webdriver
from search_page import SearchPage

SEARCH_TERMS = ["hammer", "wrench", "screwdriver"]


def compute_price_stats(products):
    prices = [p['price'] for p in products]
    return {
        'min': min(prices),
        'max': max(prices),
        'avg': sum(prices) / len(prices)
    }


def build_report(term, products):
    stats = compute_price_stats(products)
    products_sorted = sorted(products, key=lambda x: x['price'])
    cheapest = products_sorted[0]
    expensive = products_sorted[-1]

    report_lines = [
        "=" * 50,
        f"RAPPORT DE RECHERCHE : {term}",
        "=" * 50,
        f"Nombre total de résultats trouvés : {len(products)}",
        "\nTop 3 des produits :",
    ]

    for p in products[:3]:
        report_lines.append(f" - {p['name']} ({p['price_display']})")

    report_lines.extend([
        "\nStatistiques de prix :",
        f" - Prix minimum : {cheapest['price_display']} ({cheapest['name']})",
        f" - Prix maximum : {expensive['price_display']} ({expensive['name']})",
        f" - Prix moyen   : {stats['avg']:.2f}",
        "=" * 50,
    ])

    return "\n".join(report_lines)


def save_report(term, report_text, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"rapport_recherche_{term}.txt"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    return file_path


def run_tp_search():
    
    driver = webdriver.Chrome()
    search_page = SearchPage(driver)

    try:
        search_page.open()
        assert search_page.is_form_ready(), "Le formulaire de recherche n'est pas prêt."
        print("Formulaire de recherche vérifié.")

        output_dir = os.path.abspath("output")

        for term in SEARCH_TERMS:
            print(f"\n--- Recherche pour : {term} ---")
            search_page.search_for(term)
            search_page.wait_for_results()
            time.sleep(1)

            products = search_page.get_results_data()
            assert len(products) > 0, f"Aucun résultat trouvé pour '{term}'."
            print(f"Extraction réussie ({len(products)} produits) pour '{term}'.")

            report_text = build_report(term, products)
            report_path = save_report(term, report_text, output_dir)
            print(report_text)
            print(f"[INFO] Rapport enregistré : {report_path}")

        print("\nTous les rapports de recherche ont été générés.")

    except Exception as e:
        print(f"Erreur durant l'automatisation : {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tp_search()