# TP  Extraction de données avec Selenium et Page Object Model

## Contexte

Vous devez automatiser l’exploration du site suivant :

`https://books.toscrape.com`

L’objectif est de récupérer des informations sur les livres affichés sur la page d’accueil, puis de produire un petit rapport en console.

Ce TP doit être réalisé en **Python** avec **Selenium**, en appliquant le principe du **Page Object Model (POM)**.

---

## Objectif pédagogique

Ce TP a pour but de vous faire pratiquer :

* l’utilisation de Selenium avec Python ;
* l’attente du chargement d’une page ;
* l’extraction de données depuis plusieurs éléments d’une page ;
* la structuration d’un script avec le **Page Object Model**.

---

## Travail demandé

### 1. Préparer le projet

Créer un projet Python permettant de lancer un navigateur Chrome avec Selenium.

---

### 2. Mettre en place une structure POM

Créer au moins une classe représentant la page principale du site.

Cette classe devra permettre de :

* charger la page ;
* attendre que les livres soient disponibles ;
* récupérer les éléments nécessaires à l’extraction.

---

### 3. Extraire les données

Depuis la page d’accueil, récupérer pour chaque livre affiché les informations utiles.

Vous stockerez les données extraites dans une structure adaptée.

---

### 4. Générer un rapport

Afficher dans la console un compte rendu contenant au minimum :

* le nombre total de livres récupérés ;
* les informations des premiers livres extraits ;
* quelques statistiques simples sur les données collectées.

---


## Résultat attendu

À la fin du TP, l’exécution du programme doit :

* ouvrir le site `books.toscrape.com`
* récupérer les données des livres présents sur la page
* afficher un rapport clair dans la console


---

## Exemple de rapport :


```bash
============================================================
TP : EXTRACTION DE DONNÉES DE LIVRES
============================================================

--- Phase 1: Navigation ---
Accédé à books.toscrape.com
Livres chargés

--- Phase 2: Extraction des Données ---
20 livres extraits avec succès
Livre 1: A Light in the ... - £51.77 (Three)
Livre 2: Tipping the Velvet - £53.74 (One)
Livre 3: Soumission - £50.10 (One)
Livre 4: Sharp Objects - £47.82 (Four)
Livre 5: Sapiens: A Brief History ... - £54.23 (Five)
Livre 6: The Requiem Red - £22.65 (One)
Livre 7: The Dirty Little Secrets ... - £33.34 (Four)
Livre 8: The Coming Woman: A ... - £17.93 (Three)
Livre 9: The Boys in the ... - £22.60 (Four)
Livre 10: The Black Maria - £52.15 (One)
Livre 11: Starving Hearts (Triangular Trade ... - £13.99 (Two)
Livre 12: Shakespeare's Sonnets - £20.66 (Four)
Livre 13: Set Me Free - £17.46 (Five)
Livre 14: Scott Pilgrim's Precious Little ... - £52.29 (Five)
Livre 15: Rip it Up and ... - £35.02 (Five)
Livre 16: Our Band Could Be ... - £57.25 (Three)
Livre 17: Olio - £23.88 (One)
Livre 18: Mesaerion: The Best Science ... - £37.59 (One)
Livre 19: Libertarianism for Beginners - £51.33 (Two)
Livre 20: It's Only the Himalayas - £45.17 (Two)

--- Phase 3: Rapport et Statistiques ---

Nombre total de livres: 20

5 Premiers Livres:
  1. A Light in the ...
     Prix: £51.77 | Rating: Three | In stock
  2. Tipping the Velvet
     Prix: £53.74 | Rating: One | In stock
  3. Soumission
     Prix: £50.10 | Rating: One | In stock
  4. Sharp Objects
     Prix: £47.82 | Rating: Four | In stock
  5. Sapiens: A Brief History ...
     Prix: £54.23 | Rating: Five | In stock

Statistiques de Prix:
  Prix moyen: £38.05
  Prix minimum: £13.99
  Prix maximum: £57.25

Distribution par Note:
  Five étoiles: 4 livres
  Four étoiles: 4 livres
  One étoiles: 6 livres
  Three étoiles: 3 livres
  Two étoiles: 3 livres

TP RÉUSSI!
```
