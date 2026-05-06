
def generate_report(books):
    print("\n--- Phase 3: Rapport et Statistiques ---")

    if not books:
        print("Aucun livre extrait")
        return

    print(f"\nNombre total de livres: {len(books)}")

    print("\n5 Premiers Livres:")
    for book in books[:5]:
        print(f"  {book['id']}. {book['title']}")
        print(f"     Prix: £{book['price']:.2f} | Rating: {book['rating']} | {book['availability']}")

    prices = [b['price'] for b in books]
    avg_price = sum(prices) / len(prices)
    min_price = min(prices)
    max_price = max(prices)

    print(f"\nStatistiques de Prix:")
    print(f"  Prix moyen: £{avg_price:.2f}")
    print(f"  Prix minimum: £{min_price:.2f}")
    print(f"  Prix maximum: £{max_price:.2f}")

    ratings = {}
    for book in books:
        rating = book["rating"]
        if rating not in ratings:
            ratings[rating] = 0
        ratings[rating] += 1

    print(f"\nDistribution par Note:")
    for rating in sorted(ratings.keys()):
        print(f"  {rating} étoiles: {ratings[rating]} livres")