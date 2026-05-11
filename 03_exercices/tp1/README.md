# TP1 — Contrôle d'accès et vérifications d'interface

## 📋 Description

Solution complète du TP1 utilisant le pattern **Page Object Model (POM)** avec Selenium et Python.

Cette solution automatise trois scénarios de test:

1. **Authentification** - Login, vérifications et logout
2. **Liste déroulante** - Sélection d'options
3. **Ajout/Suppression d'éléments** - Manipulation dynamique d'éléments DOM

## 📁 Structure du projet

```
tp1/
├── pages/
│   ├── __init__.py
│   ├── base_page.py           # Classe parente des pages
│   ├── login_page.py          # Page Object pour login
│   ├── secure_area_page.py    # Page Object pour zone sécurisée
│   ├── dropdown_page.py       # Page Object pour dropdown
│   └── add_remove_page.py     # Page Object pour ajout/suppression
├── tests/
│   ├── __init__.py
│   └── test_tp1.py            # Tests unitaires (optionnel)
├── main.py                    # Script principal d'exécution
├── Requirements.txt           # Dépendances Python
└── README.md                  # Ce fichier
```

## 🚀 Installation

### 1. Installer les dépendances

```bash
cd tp1
pip install -r Requirements.txt
```

### 2. Vérifier que Chrome est installé

Le script utilise ChromeDriver, qui est géré automatiquement via `webdriver-manager`.

## ▶️ Exécution

### Option 1: Script principal (recommandé)

```bash
python main.py
```

Le script exécutera les 3 parties du TP1 avec logs détaillés et rapports.

**Outputs:**
- Logs en console
- Fichier log: `test_logs_YYYYMMDD_HHMMSS.log`
- Screenshots en cas d'erreur: `screenshot_*.png`

### Option 2: Tests unitaires

```bash
python -m pytest tests/test_tp1.py -v
```

ou

```bash
python -m unittest tests.test_tp1
```

## 🏗️ Architecture Page Object Model

### BasePage (base_page.py)

Classe parente fournissant les méthodes communes:

```python
- find_element(locator)        # Trouver un élément
- find_elements(locator)       # Trouver plusieurs éléments
- click_element(locator)       # Cliquer
- send_keys(locator, text)     # Saisir du texte
- get_text(locator)            # Récupérer le texte
- element_exists(locator)      # Vérifier l'existence
- navigate_to(url)             # Naviguer vers une URL
- wait_for_element(locator)    # Attendre un élément
```

### LoginPage (login_page.py)

Spécifique à la page de login:

```python
login_page = LoginPage(driver)
login_page.open()
login_page.login("username", "password")
login_page.is_success_message_displayed()
login_page.click_logout()
```

### DropdownPage (dropdown_page.py)

Spécifique à la liste déroulante:

```python
dropdown_page = DropdownPage(driver)
dropdown_page.open()
dropdown_page.select_option_by_text("Option 1")
dropdown_page.is_option_selected("Option 1")
```

### AddRemovePage (add_remove_page.py)

Spécifique à l'ajout/suppression d'éléments:

```python
add_remove_page = AddRemovePage(driver)
add_remove_page.open()
add_remove_page.add_elements(3)
add_remove_page.delete_first_element()
add_remove_page.get_delete_buttons_count()
```

## 📊 Logs et Rapports

### Format des logs

```
2024-05-11 14:30:45,123 - INFO - ✓ Driver Chrome initialisé avec succès
2024-05-11 14:30:46,456 - INFO - 1. Ouvrir la page de login...
2024-05-11 14:30:47,789 - INFO - ✓ PASS - Page de login affichée
```

### Résumé des tests

À la fin de l'exécution, un résumé est affiché:

```
============================================================
RÉSUMÉ DES TESTS
============================================================
✓ PASS - Page de login affichée
✓ PASS - Credentials saisis
✓ PASS - Message de succès affiché
...
------------------------------------------------------------
Total: 15/15 tests réussis
🎉 TOUS LES TESTS SONT PASSÉS!
============================================================
```

## 🎯 Parties couverts

### Partie 1 — Authentification

✓ Ouvrir la page de login  
✓ Vérifier la page de login  
✓ Saisir username et password  
✓ Cliquer sur le bouton de connexion  
✓ Vérifier le message de succès  
✓ Vérifier le bouton logout  
✓ Logout et retour à la page de login  

### Partie 2 — Liste déroulante

✓ Ouvrir la page Dropdown  
✓ Vérifier la liste déroulante présente  
✓ Sélectionner Option 1 et vérifier  
✓ Sélectionner Option 2 et vérifier  

### Partie 3 — Ajout et suppression d'éléments

✓ Ouvrir la page Add/Remove Elements  
✓ Ajouter 3 éléments  
✓ Vérifier 3 boutons Delete  
✓ Supprimer 1 élément et vérifier 2 restants  
✓ Supprimer tous les éléments et vérifier  

## 🎁 Bonus implémentés

✅ **Captures d'écran en cas d'erreur** - Screenshots automatiques avec timestamp  
✅ **Logs détaillés** - Fichier log complet avec tous les détails  
✅ **Gestion d'erreur** - Try/catch avec messages d'erreur clairs  
✅ **Rapports structurés** - Résumé des tests avec statistiques  
✅ **Utilités partagées** - BasePage pour éviter la duplication  

## 🔧 Configuration

### Mode headless (sans interface)

Dans `main.py`, décommenter la ligne:

```python
options.add_argument("--headless")
```

### Timeout personnalisé

Dans `base_page.py`, modifier la ligne:

```python
self.wait = WebDriverWait(driver, 10)  # Changer 10 par votre valeur
```

## ⚠️ Prérequis

- Python 3.7+
- Chrome 80+
- Selenium 4.0+
- Connexion internet (pour accéder aux sites)

## 🐛 Troubleshooting

### "No such element" exception

Le site a peut-être changé. Vérifier les locators dans les pages:

```python
# Exemple dans login_page.py
USERNAME_INPUT = (By.ID, "username")  # À vérifier avec l'inspecteur
```

### Driver ne se lance pas

Installer `webdriver-manager`:

```bash
pip install webdriver-manager
```

### Timeout lors des tests

Augmenter le timeout dans `base_page.py`:

```python
self.wait = WebDriverWait(driver, 20)  # Au lieu de 10
```

## 📝 Notes

- Les tests sont séquentiels et dépendants (l'ordre d'exécution est important)
- Le navigateur reste ouvert pendant les tests (peut être modifié avec --headless)
- Les logs sont sauvegardés avec un timestamp unique

## 🎓 Concepts appliqués

- ✓ Pattern Page Object Model
- ✓ Séparation des responsabilités
- ✓ Réutilisation de code (BasePage)
- ✓ Attentes explicites (WebDriverWait)
- ✓ Gestion d'erreurs
- ✓ Logging et rapports
- ✓ Assertions claires
- ✓ Code lisible et maintenable

## 📚 Ressources

- [Selenium Documentation](https://selenium.dev/documentation/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/en/guidelines_and_recommendations/encouraged_practices/)
- [WebDriverWait Documentation](https://selenium.dev/documentation/en/webdriver/waits/)
