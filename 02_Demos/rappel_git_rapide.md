# Git - Commandes de base

## Initialiser un projet Git

Dans le dossier du projet :

```bash
git init
````

Cela crée un dépôt Git local.

---

## Vérifier l’état du dépôt

```bash
git status
```

---

## Ajouter des fichiers au prochain commit

Ajouter un fichier précis :

```bash
git add nom-du-fichier
```

Ajouter tous les fichiers :

```bash
git add .
```

---

## Créer un commit

```bash
git commit -m "Message du commit"
```

Exemple :

```bash
git commit -m "Initialisation du projet"
```

---

## Voir l’historique des commits

```bash
git log
```

Version courte :

```bash
git log --oneline
```

---

## Connecter le projet à un dépôt distant

```bash
git remote add origin URL_DU_DEPOT
```

Exemple :

```bash
git remote add origin https://github.com/utilisateur/mon-projet.git
```

---

## Envoyer le projet vers GitHub/GitLab

Premier push :

```bash
git push -u origin main
```

Push suivant :

```bash
git push
```

---

## Récupérer les changements distants

```bash
git pull
```

---

## Créer une branche

```bash
git branch nom-de-la-branche
```

---

## Changer de branche

```bash
git switch nom-de-la-branche
```

---

## Créer et changer directement de branche

```bash
git switch -c nom-de-la-branche
```

---

## Revenir temporairement à un ancien commit

Voir les commits :

```bash
git log --oneline
```

Aller sur un commit :

```bash
git checkout identifiant-du-commit
```

Exemple :

```bash
git checkout a1b2c3d
```

Attention : cela place Git en mode détaché.

---

## Revenir à la branche principale

```bash
git switch main
```

Ou selon le projet :

```bash
git switch master
```

---

## Annuler une modification non commitée

```bash
git restore nom-du-fichier
```

---

## Retirer un fichier de la zone de commit

```bash
git restore --staged nom-du-fichier
```

---

## Voir les différences avant commit

```bash
git diff
```

---

## Cycle classique

```bash
git init
git status
git add .
git commit -m "Initialisation du projet"
git remote add origin URL_DU_DEPOT
git push -u origin main
```

Ensuite, au quotidien :

```bash
git status
git add .
git commit -m "Message clair"
git push
```