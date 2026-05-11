# TP2 — Tester des contenus dynamiques avec Selenium

## Contexte

Vous intervenez comme automaticien QA sur une application de démonstration web contenant plusieurs comportements dynamiques fréquemment rencontrés en test automatisé :

- un élément qui disparaît puis réapparaît,
- un champ qui devient actif après une action,
- un contenu chargé dynamiquement,
- une notification qui change,
- un scroll qui révèle du contenu supplémentaire.

Votre mission est d’automatiser plusieurs scénarios sur ce site en utilisant **Python + Selenium** avec une structure en **Page Object Model (POM)**.

## Site à utiliser

Base URL :

- `https://the-internet.herokuapp.com/`

Pages concernées :

- Dynamic Controls : `https://the-internet.herokuapp.com/dynamic_controls`
- Dynamic Loading : `https://the-internet.herokuapp.com/dynamic_loading`
- Notification Message : `https://the-internet.herokuapp.com/notification_message_rendered`
- Infinite Scroll : `https://the-internet.herokuapp.com/infinite_scroll`

## Objectifs pédagogiques

Ce TP doit vous faire pratiquer :

- la navigation entre plusieurs pages,
- les **waits explicites**,
- l’attente de disparition d’un élément,
- l’attente d’activation d’un champ,
- l’attente d’apparition d’un contenu chargé dynamiquement,
- la lecture et la vérification d’un message de notification,
- le scroll de page,
- les assertions,
- le pattern **Page Object Model**.

## Travail demandé

### Partie 1 — Dynamic Controls

Automatiser le scénario suivant :

1. Ouvrir la page Dynamic Controls.
2. Vérifier que la page est bien chargée.
3. Vérifier que la case à cocher est présente.
4. Cliquer sur `Remove`.
5. Attendre correctement la disparition de la case à cocher.
6. Vérifier le message de confirmation affiché.
7. Cliquer sur `Add`.
8. Attendre correctement la réapparition de la case à cocher.
9. Vérifier le nouveau message de confirmation.
10. Dans la zone `Enable/disable`, vérifier que le champ texte est initialement désactivé.
11. Cliquer sur `Enable`.
12. Attendre correctement que le champ devienne actif.
13. Vérifier qu’il est maintenant possible d’écrire dedans.
14. Saisir un texte de test et vérifier qu’il a bien été saisi.

### Partie 2 — Dynamic Loading

Automatiser le scénario suivant :

1. Ouvrir la page Dynamic Loading.
2. Aller sur `Example 2: Element rendered after the fact`.
3. Vérifier que le bouton `Start` est présent.
4. Cliquer sur `Start`.
5. Attendre correctement l’apparition du contenu chargé dynamiquement.
6. Vérifier que le texte `Hello World!` apparaît bien.

### Partie 3 — Notification Message

Automatiser le scénario suivant :

1. Ouvrir la page Notification Message.
2. Lire le message affiché.
3. Cliquer sur `Click here` pour charger une nouvelle notification.
4. Vérifier qu’un message est bien affiché après le clic.
5. Répéter l’action plusieurs fois.
6. Vérifier que le message obtenu appartient bien aux messages attendus.

### Partie 4 — Infinite Scroll

Automatiser le scénario suivant :

1. Ouvrir la page Infinite Scroll.
2. Vérifier qu’un premier bloc de texte est présent.
3. Faire défiler la page plusieurs fois vers le bas.
4. Vérifier qu’un contenu supplémentaire apparaît après le scroll.
5. Compter le nombre de blocs visibles avant et après le scroll.
6. Vérifier que ce nombre a augmenté.

## Contraintes techniques

Vous devez obligatoirement :

- utiliser le **Page Object Model** ;
- séparer la logique des pages et la logique des tests ;
- utiliser des méthodes courtes et explicites ;
- privilégier les **waits explicites** ;
- éviter `time.sleep()` sauf nécessité exceptionnelle ;
- prévoir des assertions lisibles ;
- fermer le navigateur proprement à la fin.

## Structure attendue

Exemple de structure possible :

```text
tp2/
├── pages/
│   ├── base_page.py
│   ├── dynamic_controls_page.py
│   ├── dynamic_loading_page.py
│   ├── notification_page.py
│   └── infinite_scroll_page.py
├── tests/
│   └── test_tp2.py
└── main.py
```

## Résultat attendu

À l’exécution, le script doit :

* valider la disparition et la réapparition d’un élément,
* valider l’activation d’un champ texte,
* valider l’apparition d’un contenu chargé dynamiquement,
* valider la présence d’une notification,
* valider l’apparition de contenu supplémentaire après scroll.

## Bonus

Si vous terminez en avance, ajoutez :

* des captures d’écran en cas d’échec ;
* des logs lisibles pour chaque étape ;
* une méthode utilitaire commune pour les messages dynamiques ;
* une exécution indépendante de chaque scénario.
