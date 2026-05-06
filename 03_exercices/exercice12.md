
## TP Recherche Basique et Extraction de Données

**Site**: practicesoftwaretesting.com

**Objectif**: Automatiser une recherche simple et extraire les résultats

**Tâches**:

1. **Navigation et Localisation**
   - Accédez à https://practicesoftwaretesting.com
   - Localisez le formulaire de recherche principal
   - Identifiez le champ texte de recherche
   - Identifiez le bouton de recherche
   - Vérifiez que ces éléments sont visibles

2. **Recherche de Produits**
   - Saisissez "hammer" dans le champ de recherche
   - Attendez explicitement la soumission
   - Attendez que les résultats de recherche se chargent
   - Vérifiez que vous êtes sur la page de résultats
   - Vérifiez qu'au moins un résultat est affiché

3. **Extraction de Données**
   - Localisez le conteneur des produits
   - Pour chaque produit affiché:
     - Extrayez le nom du produit
     - Extrayez le prix du produit
     - Extrayez la note (si disponible)
   - Créez une liste Python contenant tous les produits avec leurs infos

4. **Validation et Rapport**
   - Affichez le nombre total de résultats trouvés
   - Affichez les 3 premiers produits avec leurs prix
   - Affichez le produit le moins cher
   - Affichez le produit le plus cher

**Points de Contrôle**:
- La recherche s'exécute correctement
- Les résultats sont chargés
- Les données sont extraites sans erreur
- Le tri et l'affichage fonctionnent