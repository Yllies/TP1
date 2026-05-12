# TP3 - Sauce Demo E-commerce Automation

Automation tests pour le site [Sauce Demo](https://www.saucedemo.com/) utilisant **Selenium**, **Page Object Model** et **bonnes pratiques de code propre**.

## 🎯 Objectifs

- ✅ Zéro duplication de code (réutilisation via driver factory et page objects)
- ✅ Driver paramétrable pour différents scénarios
- ✅ Page Object Model avancé avec classe BasePage
- ✅ Logging unifié avec horodatage et statuts visuels
- ✅ Gestion automatique des captures d'écran en cas d'erreur

## 📁 Structure du projet

```
tp3/
├── pages/                      # Page objects
│   ├── __init__.py
│   ├── base_page.py           # Classe de base réutilisable
│   ├── login_page.py          # Page de connexion
│   ├── inventory_page.py      # Page du catalogue
│   ├── cart_page.py           # Page du panier
│   └── checkout_page.py       # Page de paiement
├── tests/                      # Tests et scénarios
│   ├── __init__.py
│   └── test_sauce_demo.py     # Tests principaux
├── utils/                      # Utilitaires
│   ├── __init__.py
│   ├── driver_factory.py      # Fabrique de WebDriver paramétrable
│   └── logger_config.py       # Configuration du logging
├── logs/                       # Fichiers de logs
├── screenshots/               # Captures d'écran
└── Requirements.txt           # Dépendances
```

## 🚀 Installation et utilisation

### 1. Installer les dépendances

```bash
pip install -r Requirements.txt
```

### 2. Lancer les tests

```bash
python tests/test_sauce_demo.py
```

## 💡 Utilisation du driver factory

### Créer un driver avec paramètres personnalisés

```python
from utils.driver_factory import create_driver, close_driver

# Driver standard
driver = create_driver()

# Driver sans notifications et headless
driver = create_driver(headless=True, disable_notifications=True)

# Driver avec dimensions personnalisées
driver = create_driver(width=1280, height=720)

# Driver sans images (performance)
driver = create_driver(disable_images=True)

# Utiliser le driver...

# Fermer le driver
close_driver(driver)
```

### Paramètres disponibles

| Paramètre | Type | Défaut | Description |
|-----------|------|--------|-------------|
| `headless` | bool | False | Mode sans interface graphique |
| `disable_notifications` | bool | True | Désactiver notifications du navigateur |
| `disable_images` | bool | False | Désactiver le chargement des images |
| `width` | int | 1920 | Largeur de la fenêtre |
| `height` | int | 1080 | Hauteur de la fenêtre |
| `start_maximized` | bool | True | Démarrer en mode maximisé |

## 📄 Utilisation des pages

### LoginPage

```python
login_page = LoginPage(driver)
login_page.load()
login_page.login("standard_user", "secret_sauce")

if login_page.is_login_page():
    error = login_page.get_error_message()
```

### InventoryPage

```python
inventory_page = InventoryPage(driver)

# Ajouter des produits
inventory_page.add_product_to_cart(0)  # Par index
inventory_page.add_product_by_name("Sauce Labs Backpack")  # Par nom

# Consultations
count = inventory_page.get_product_count()
badge = inventory_page.get_cart_badge_count()
names = inventory_page.get_product_names()
prices = inventory_page.get_product_prices()

# Navigation
inventory_page.go_to_cart()
inventory_page.logout()
```

### CartPage

```python
cart_page = CartPage(driver)

# Consultations
items = cart_page.get_cart_items_count()
names = cart_page.get_cart_item_names()
total = cart_page.get_total_price()

# Actions
cart_page.remove_item_from_cart(0)
cart_page.checkout()
cart_page.continue_shopping()
```

### CheckoutPage

```python
checkout_page = CheckoutPage(driver)

# Remplir le formulaire
checkout_page.fill_checkout_form("Jean", "Dupont", "75000")
checkout_page.continue_to_overview()

# Finaliser
checkout_page.finish_checkout()

# Vérifier
if checkout_page.is_order_complete():
    message = checkout_page.get_completion_message()
```

## 📝 Scénarios de test

### Scénario 1: Connexion réussie ✓
Valide que la connexion avec des identifiants valides redirige vers l'inventaire.

### Scénario 2: Connexion échouée ✗
Valide que les identifiants invalides génèrent un message d'erreur.

### Scénario 3: Ajout de produits 🛒
Valide que les produits sont correctement ajoutés au panier.

### Scénario 4: Panier et paiement 💳
Valide la consultation du panier et l'initialisation du paiement.

### Scénario 5: Achat complet ✅
Valide un cycle complet d'achat jusqu'à la confirmation.

## 📊 Logging et captures d'écran

### Logs
- **Localisation**: `logs/test_YYYYMMDD_HHMMSS.log`
- **Format**: `[HH:MM:SS] LEVEL | Message`
- **Exemple**:
  ```
  [14:23:45] INFO     | ✓ Navigation vers: https://www.saucedemo.com
  [14:23:47] INFO     | ✓ Connexion lancée pour: standard_user
  ```

### Captures d'écran
- **Localisation**: `screenshots/`
- **Nommage**: Automatique ou personnalisé
- **Automatique**: Prise en cas d'erreur ou d'assertion échouée

## 🔑 Identifiants de test

| Utilisateur | Mot de passe | Statut |
|-------------|--------------|--------|
| standard_user | secret_sauce | ✓ Valide |
| locked_out_user | secret_sauce | ✗ Compte bloqué |

## 🏗️ Bonnes pratiques implémentées

✅ **Pas de duplication**: Le driver est créé une seule fois dans `driver_factory.py`  
✅ **Page Object Model**: Chaque page a une classe dédiée avec ses localisateurs  
✅ **Méthodes réutilisables**: `BasePage` fournit les méthodes communes  
✅ **Paramétrage**: Driver personnalisable selon les besoins  
✅ **Logging unifié**: Tous les messages passent par le logger  
✅ **Gestion d'erreurs**: Captures d'écran en cas de problème  
✅ **Code lisible**: Noms explicites et commentaires clairs (français)

## 📚 Ressources

- [Selenium Python Documentation](https://www.selenium.dev/documentation/webdriver/getting_started/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Sauce Demo](https://www.saucedemo.com/)

---

**Auteur**: TP3 - Automation Tests  
**Dernière mise à jour**: 2024
