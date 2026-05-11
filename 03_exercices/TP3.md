# TP 3 — Automatisation de tests fonctionnels avec Selenium Python

## Contexte

Vous intégrez une équipe QA chargée d’automatiser les tests fonctionnels d’une application e-commerce.

Votre mission consiste à créer un projet Selenium Python propre et structuré permettant de tester plusieurs parcours utilisateur du site de démonstration suivant :

[Sauce Demo](https://www.saucedemo.com/)

Le projet devra être versionné sur GitHub et respecter une organisation claire proche d’un vrai projet professionnel.

---

# Objectifs du TP

Le but de ce TP est de :

* automatiser plusieurs scénarios utilisateur ;
* utiliser Selenium avec Python ;
* mettre en place le Page Object Model (POM) ;
* utiliser des attentes explicites ;
* générer des logs ;
* effectuer des captures d’écran ;
* structurer correctement un repository GitHub.

---

# Contraintes techniques

Le projet devra obligatoirement contenir :

```text
README.md
requirements.txt
pages/
tests/
utils/
logs/
screenshots/
```

Le projet devra utiliser :

* Selenium ;
* Python ;
* le Page Object Model ;
* `WebDriverWait` et les `ExpectedConditions` ;
* un système de logs Python ;
* des screenshots ;
* un README expliquant :

  * l’objectif du projet ;
  * le site testé ;
  * l’installation ;
  * l’exécution ;
  * la structure du projet.

---

# Architecture attendue

Chaque page importante devra être représentée par une classe dédiée.

Exemple :

```text
pages/
├── login_page.py
├── inventory_page.py
├── cart_page.py
├── checkout_page.py
└── checkout_complete_page.py
```

---

# Scénarios de test à automatiser

## Scénario 1 — Connexion réussie

Automatiser la connexion avec :

```text
Utilisateur : standard_user
Mot de passe : secret_sauce
```

Résultat attendu :

* l’utilisateur accède à la page catalogue ;
* le titre de la page inventaire est visible.

---

## Scénario 2 — Connexion refusée

Automatiser une tentative de connexion avec :

```text
Utilisateur : locked_out_user
Mot de passe : secret_sauce
```

Résultat attendu :

* un message d’erreur est affiché ;
* l’utilisateur reste sur la page de connexion.

---

## Scénario 3 — Ajout d’un produit au panier

Après connexion avec `standard_user`, ajouter le produit suivant :

```text
Sauce Labs Backpack
```

Résultats attendus :

* le bouton du produit passe de `Add to cart` à `Remove` ;
* l’icône du panier affiche `1` ;
* le panier contient bien `Sauce Labs Backpack` ;
* le prix affiché dans le panier correspond au prix du produit sélectionné.

Screenshot demandé :

* effectuer une capture d’écran après l’ajout du produit au panier.

---

## Scénario 4 — Parcours d’achat complet

Automatiser le parcours suivant :

1. connexion ;
2. ajout du produit `Sauce Labs Backpack` ;
3. ouverture du panier ;
4. vérification du produit présent dans le panier ;
5. démarrage du checkout ;
6. saisie des informations client ;
7. vérification du récapitulatif ;
8. validation de la commande.

Informations client à utiliser :

```text
Prénom : John
Nom : Doe
Code postal : 59000
```

Résultats attendus :

* le récapitulatif contient bien `Sauce Labs Backpack` ;
* le prix du produit est correct ;
* le total hors taxe correspond au prix du produit ;
* la taxe est affichée ;
* le total final est cohérent ;
* le message suivant est affiché après validation :

```text
Thank you for your order!
```

Screenshot demandé :

* effectuer une capture d’écran de la page de confirmation finale.

---

## Scénario 5 — Déconnexion

Après connexion avec `standard_user`, automatiser la déconnexion.

Résultat attendu :

* l’utilisateur revient sur la page de login.

---

# Gestion des erreurs

Le projet devra :

* utiliser un logger Python ;
* enregistrer les actions importantes ;
* générer automatiquement un screenshot en cas d’erreur durant l’exécution d’un test.

---

# Livrable attendu

Le rendu devra être un repository GitHub contenant :

* le code source ;
* les scénarios automatisés ;
* les logs ;
* les screenshots ;
* un README complet ;
* un projet proprement structuré et exécutable.
