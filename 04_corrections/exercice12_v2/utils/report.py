def generate_report(products):
    print("\n--- Phase 4: Rapport et Validation ---")

    if not products:
        print("Aucun produit extrait")
        return

    print(f"\nNombre total de résultats: {len(products)}")

    print("\n3 Premiers Produits:")
    for product in products[:3]:
        print(f"  - {product['name']}: ${product['price']:.2f} ")

    print("\nTous les Produits:")
    for product in products:
        print(f"  - {product['name']}: ${product['price']:.2f} ")

    cheapest = min(products, key=lambda x: x["price"])
    print(f"\nProduit le moins cher:")
    print(f"  {cheapest['name']}: ${cheapest['price']:.2f}")

    most_expensive = max(products, key=lambda x: x["price"])
    print(f"\nProduit le plus cher:")
    print(f"  {most_expensive['name']}: ${most_expensive['price']:.2f}")

    prices = [p["price"] for p in products]
    avg_price = sum(prices) / len(prices)
    print(f"\nPrix moyen: ${avg_price:.2f}")
