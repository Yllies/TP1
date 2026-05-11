# TP 4 Selenium Python 

## Test automatisé d’un catalogue e-commerce

Site utilisé : [Automation Exercise](https://automationexercise.com/)

---

# Objectif du TP

Créer un script Selenium Python permettant de tester automatiquement une fonctionnalité de recherche de produits sur un site e-commerce.

Le script devra :

* naviguer sur le site,
* effectuer une recherche,
* récupérer des informations,
* vérifier plusieurs assertions,
* produire des logs,
* générer des screenshots,
* afficher un rapport final.

---

# Technologies utilisées

* Python
* Selenium
* logging Python
* ChromeDriver automatique
* WebDriverWait

---

# Ce qui a déjà été vu et doit être réutilisé

Le TP doit utiliser uniquement des notions déjà vues :

* Selenium WebDriver
* `WebDriverWait`
* `expected_conditions`
* sélecteurs CSS/XPath
* classes Python
* listes et dictionnaires
* assertions Python classiques
* logging
* screenshots Selenium
* structure de projet simple

---

# A eviter

* `time.sleep()`
* librairies supplémentaires inutiles
* XPath absolus
* code dupliqué

---

# Structure attendue

```text
tp2/
├── pages/
│   ├── home_page.py
│   ├── products_page.py
│   └── product_card.py
├── utils/
│   ├── logger_config.py
│   ├── screenshot.py
│   └── report.py
├── logs/
├── screenshots/
├── tests/
│   └── test_search_products.py
├── main.py
└── requirements.txt
```

---

# Fonctionnement attendu

# Étape 1 — Ouvrir le site

Le script doit :

* ouvrir Chrome,
* accéder au site,
* maximiser la fenêtre.

URL :

[Automation Exercise](https://automationexercise.com/)

---

# Étape 2 — Accéder à la page Products

Depuis la page d’accueil :

* cliquer sur `Products`,
* attendre correctement le chargement de la page.

---

# Étape 3 — Effectuer une recherche

Rechercher le mot :

```text
top
```

Le script doit :

* saisir le texte,
* cliquer sur le bouton de recherche,
* attendre les résultats.

---

# Étape 4 — Récupérer les produits

Pour chaque produit affiché :

* récupérer le nom,
* récupérer le prix.

Les données doivent être stockées dans une liste.

Exemple :

```python
[
    {
        "name": "Summer White Top",
        "price": "Rs. 400"
    }
]
```

---

# Étape 5 — Assertions

Le script doit effectuer plusieurs vérifications.

---

## Assertion 1

Vérifier qu’au moins un produit est affiché.

Exemple :

```python
assert len(products) > 0
```

---

## Assertion 2

Vérifier que tous les produits contiennent le mot :

```text
top
```

sans tenir compte des majuscules/minuscules.

---

## Assertion 3

Vérifier que le titre de la page contient :

```text
Automation Exercise
```

---

# Gestion des logs

Le projet doit utiliser le module :

```python
logging
```

Le script doit enregistrer dans un fichier log :

* démarrage du test,
* ouverture du site,
* navigation,
* recherche effectuée,
* nombre de produits trouvés,
* erreurs éventuelles,
* fin du test.

---

# Screenshots

Le script doit générer au minimum :

## Screenshot 1

Après l’ouverture du site.

---

## Screenshot 2

Après l’affichage des résultats de recherche.

---

## Screenshot 3

En cas d’erreur ou d’assertion échouée.

---

# Rapport final

Le script doit afficher un résumé final dans le terminal.

Exemple :

```text
=== RAPPORT TP2 ===

Produits trouvés : 6

- Summer White Top | Rs. 400
- Fancy Green Top | Rs. 700

TEST TERMINÉ AVEC SUCCÈS
```

---

# Bonus facultatifs


## Bonus 1

Créer une classe `ProductCard`.

Exemple :

```python
product.name
product.price
```

---

## Bonus 2

Exporter le rapport dans un fichier texte.


---

# Objectifs pédagogiques réels du TP

Ce TP permet de pratiquer :

* les attentes explicites,
* les interactions Selenium,
* les assertions,
* les logs de test,
* les screenshots,
* une structure Page Object simple,
* la récupération de données,
* la séparation du code en modules propres.
