# TP4 — Test automatisé d'un catalogue e-commerce

## Objectif

Ce projet automatise le test de la fonctionnalité de recherche de produits du site **Automation Exercise** (`https://automationexercise.com`) à l'aide de **Selenium Python**.

Le script navigue sur le site, effectue une recherche, extrait les résultats, vérifie plusieurs assertions et produit des logs ainsi qu'un rapport final.

---

## Site testé

**Automation Exercise** — `https://automationexercise.com`

Parcours automatisé :

1. Ouverture du site et fermeture du bandeau cookies
2. Navigation vers la page **Products**
3. Recherche du mot `top`
4. Extraction des produits affichés (nom + prix)
5. Vérifications et rapport

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Moha31170/TP4
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
.venv\Scripts\activate      
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Exécution

```bash
python main.py
```

---

## Résultat attendu

```
[12:25:37] INFO  === DÉMARRAGE DU TEST ===
[12:25:40] INFO  Page d'accueil chargée
[12:25:40] INFO  Bandeau cookies fermé
[12:25:43] INFO  Page Products chargée
[12:25:45] INFO  Résultats de recherche chargés
[12:25:46] INFO  14 produit(s) extrait(s)
[12:25:46] INFO  Assertion 1 OK — 14 produit(s) trouvé(s)
[12:25:46] INFO  Assertion 2 OK — 12/14 produits contiennent 'top' (86%)
[12:25:46] INFO  === TEST TERMINÉ AVEC SUCCÈS ===

========================================
=== RAPPORT TP4 ===
Généré le : 12/05/2026 12:25:46
========================================

Produits trouvés : 14

- Blue Top | Rs. 500
- Winter Top | Rs. 600
- Summer White Top | Rs. 400
...

TEST TERMINÉ AVEC SUCCÈS
========================================
```

Les logs sont enregistrés dans `logs/` et les screenshots dans `screenshots/`.

---

## Assertions

| #   | Vérification                      | Détail                               |
| --- | --------------------------------- | ------------------------------------ |
| 1   | Au moins un résultat affiché      | `len(products) > 0`                  |
| 2   | Majorité des résultats pertinents | `> 50%` des noms contiennent `"top"` |
| 3   | Titre de la page correct          | Contient `"Automation Exercise"`     |

---

## Screenshots générés

| Fichier                        | Moment                        |
| ------------------------------ | ----------------------------- |
| `01_accueil_*.png`             | Après ouverture du site       |
| `02_resultats_recherche_*.png` | Après affichage des résultats |
| `03_erreur_*.png`              | En cas d'échec uniquement     |

---

## Structure du projet

```
tp4/
├── pages/
│   ├── home_page.py          # Page d'accueil : navigation + gestion bandeau cookies
│   ├── products_page.py      # Page produits : recherche + extraction
│   └── product_card.py       # Classe ProductCard (product.name, product.price)
├── utils/
│   ├── logger_config.py      # Logger Python (console + fichier horodaté)
│   ├── screenshot.py         # Fonction take_screenshot() réutilisable
│   └── report.py             # Rapport console + export fichier texte
├── tests/
│   └── test_search_products.py  # Scénario de test et assertions
├── logs/                     # Fichiers de log générés à l'exécution
├── screenshots/              # Captures d'écran
├── main.py                   # Point d'entrée
├── requirements.txt
└── README.md
```

---

## Fonctionnalités

- **Page Object Model** — chaque page est une classe indépendante avec ses locators et méthodes
- **Waits explicites** — `WebDriverWait` + `ExpectedConditions` sur toutes les interactions, aucun `time.sleep()`
- **Gestion du bandeau cookies** — fermé automatiquement au chargement avant toute interaction
- **Logger Python** — logs horodatés en console et dans `logs/tp4_*.log`
- **Screenshots automatiques** — à l'ouverture du site, après la recherche, et en cas d'erreur
- **Classe ProductCard** — accès aux données via `product.name` et `product.price`
- **Rapport exporté** — affiché en console et sauvegardé dans `rapport_tp4.txt`
