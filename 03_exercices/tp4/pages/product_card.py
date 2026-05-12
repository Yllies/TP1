class ProductCard:
    """
    Représente un produit extrait de la page de résultats.
    Permet d'accéder aux données via product.name et product.price.
    """

    def __init__(self, name: str, price: str):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"ProductCard(name='{self.name}', price='{self.price}')"
