import os
from datetime import datetime


class Report:
    """
    Génère un rapport lisible en console et l'exporte dans un fichier texte.
    """

    def __init__(self, output_file="rapport_tp4.txt"):
        self.output_file = output_file
        self.lines = []

    def _build(self, products, success: bool):
        self.lines = []
        add = self.lines.append

        add("=" * 40)
        add("=== RAPPORT TP4 ===")
        add(f"Généré le : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        add("=" * 40)
        add("")
        add(f"Produits trouvés : {len(products)}")
        add("")

        for product in products:
            add(f"- {product.name} | {product.price}")

        add("")
        add("TEST TERMINÉ AVEC SUCCÈS" if success else "TEST ÉCHOUÉ")
        add("=" * 40)

    def generate(self, products, success: bool = True):
        """Construit, affiche et enregistre le rapport."""
        self._build(products, success)
        output = "\n".join(self.lines)

        print("\n" + output)

        os.makedirs(
            (
                os.path.dirname(self.output_file)
                if os.path.dirname(self.output_file)
                else "."
            ),
            exist_ok=True,
        )
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write(output)
