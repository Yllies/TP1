# TP1 — Contrôle d’accès et vérifications d’interface

## Contexte

Vous intervenez comme automaticien QA sur un mini portail d’administration.
Votre mission consiste à automatiser plusieurs vérifications de base autour :

- de l’authentification utilisateur,
- de la vérification d’un écran sécurisé,
- d’une interaction avec une liste déroulante,
- d’une zone où des éléments sont ajoutés dynamiquement.

L’objectif est de produire un script Selenium Python structuré avec le pattern **Page Object Model (POM)**.

## Site à utiliser

- Base URL : `https://the-internet.herokuapp.com/`

Pages concernées :

- Login : `https://the-internet.herokuapp.com/login`
- Dropdown : `https://the-internet.herokuapp.com/dropdown`
- Add/Remove Elements : `https://the-internet.herokuapp.com/add_remove_elements/`

## Identifiants à utiliser

- Username : `tomsmith`
- Password : `SuperSecretPassword!`

## Objectifs pédagogiques

Ce TP doit vous faire pratiquer :

- la navigation entre plusieurs pages,
- la recherche d’éléments avec Selenium,
- la saisie de texte,
- le clic sur des boutons et liens,
- la sélection d’une option dans une liste déroulante,
- les assertions,
- l’utilisation du pattern **Page Object Model**,
- une gestion d’erreur simple et propre.

## Travail demandé

### Partie 1 — Authentification

Automatiser le scénario suivant :

1. Ouvrir la page de login.
2. Vérifier que le titre ou le contenu de la page correspond bien à une page d’authentification.
3. Saisir le username et le password fournis.
4. Cliquer sur le bouton de connexion.
5. Vérifier que la connexion a réussi.
6. Vérifier la présence du message de succès.
7. Vérifier la présence du bouton ou lien de logout.
8. Cliquer sur logout.
9. Vérifier que l’utilisateur revient bien sur la page de login.

### Partie 2 — Liste déroulante

Automatiser le scénario suivant :

1. Ouvrir la page Dropdown.
2. Vérifier que la liste déroulante est présente.
3. Sélectionner `Option 1`.
4. Vérifier que `Option 1` est bien sélectionnée.
5. Sélectionner ensuite `Option 2`.
6. Vérifier que `Option 2` est bien sélectionnée.

### Partie 3 — Ajout et suppression d’éléments

Automatiser le scénario suivant :

1. Ouvrir la page Add/Remove Elements.
2. Cliquer 3 fois sur `Add Element`.
3. Vérifier que 3 boutons `Delete` sont affichés.
4. Supprimer 1 élément.
5. Vérifier qu’il reste 2 boutons `Delete`.
6. Supprimer tous les éléments restants.
7. Vérifier qu’il ne reste plus aucun bouton `Delete`.

## Contraintes techniques

Vous devez obligatoirement :

- utiliser le **Page Object Model** ;
- séparer les pages dans des classes différentes ;
- éviter de mettre toute la logique dans un seul fichier ;
- utiliser des méthodes explicites et lisibles ;
- prévoir au minimum quelques assertions ;
- fermer le navigateur proprement à la fin.

## Structure attendue

Exemple de structure possible :

```text
tp1/
├── pages/
│   ├── login_page.py
│   ├── secure_area_page.py
│   ├── dropdown_page.py
│   └── add_remove_page.py
├── tests/
│   └── test_tp1.py
└── main.py
```

## Résultat attendu

À l’exécution, le script doit afficher clairement les étapes et indiquer si les vérifications sont réussies ou non.

Le scénario complet doit :

* réussir la connexion,
* valider le logout,
* valider la sélection dans la liste déroulante,
* valider l’ajout et la suppression dynamique d’éléments.

## Bonus

Si vous terminez en avance, ajoutez :

* une capture d’écran en cas d’erreur ;
* des messages de log simples ;
* une méthode utilitaire pour éviter de dupliquer certaines vérifications.


