
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


def generate_report_pretty(books):
    RESET = "\033[0m"
    BOLD = "\033[1m"

    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    RED = "\033[31m"

    print(f"\n{BOLD}{CYAN}--- Phase 3: Rapport et Statistiques ---{RESET}")

    if not books:
        print(f"{YELLOW}Aucun livre extrait{RESET}")
        return

    print(f"\n{BOLD}Nombre total de livres:{RESET} {GREEN}{len(books)}{RESET}")

    print(f"\n{BOLD}{BLUE}5 Premiers Livres:{RESET}")
    for book in books[:5]:
        print(f"  {CYAN}{book['id']}.{RESET} {BOLD}{book['title']}{RESET}")
        print(
            f"     Prix: {GREEN}£{book['price']:.2f}{RESET} | "
            f"Rating: {YELLOW}{book['rating']}{RESET} | "
            f"{MAGENTA}{book['availability']}{RESET}"
        )

    prices = [b['price'] for b in books]
    avg_price = sum(prices) / len(prices)
    min_price = min(prices)
    max_price = max(prices)

    print(f"\n{BOLD}{BLUE}Statistiques de Prix:{RESET}")
    print(f"  Prix moyen: {GREEN}£{avg_price:.2f}{RESET}")
    print(f"  Prix minimum: {CYAN}£{min_price:.2f}{RESET}")
    print(f"  Prix maximum: {RED}£{max_price:.2f}{RESET}")

    ratings = {}
    for book in books:
        rating = book["rating"]
        if rating not in ratings:
            ratings[rating] = 0
        ratings[rating] += 1

    print(f"\n{BOLD}{BLUE}Distribution par Note:{RESET}")
    for rating in sorted(ratings.keys()):
        print(f"  {YELLOW}{rating} étoiles{RESET}: {GREEN}{ratings[rating]}{RESET} livres")




from datetime import datetime

def generate_report_texte(books):
    report_filename = "rapport_test.txt"

    with open(report_filename, "w", encoding="utf-8") as file:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        file.write(f"Date et heure du test : {now}\n")
        file.write("\n--- Phase 3: Rapport et Statistiques ---\n")

        if not books:
            file.write("Aucun livre extrait\n")
            return

        file.write(f"\nNombre total de livres: {len(books)}\n")

        file.write("\n5 Premiers Livres:\n")
        for book in books[:5]:
            file.write(f"  {book['id']}. {book['title']}\n")
            file.write(
                f"     Prix: £{book['price']:.2f} | "
                f"Rating: {book['rating']} | "
                f"{book['availability']}\n"
            )

        prices = [b['price'] for b in books]
        avg_price = sum(prices) / len(prices)
        min_price = min(prices)
        max_price = max(prices)

        file.write("\nStatistiques de Prix:\n")
        file.write(f"  Prix moyen: £{avg_price:.2f}\n")
        file.write(f"  Prix minimum: £{min_price:.2f}\n")
        file.write(f"  Prix maximum: £{max_price:.2f}\n")

        ratings = {}
        for book in books:
            rating = book["rating"]
            if rating not in ratings:
                ratings[rating] = 0
            ratings[rating] += 1

        file.write("\nDistribution par Note:\n")
        for rating in sorted(ratings.keys()):
            file.write(f"  {rating} étoiles: {ratings[rating]} livres\n")