# Analyse des performances commerciales — Python | 2025

## Présentation du projet

Ce projet consiste à analyser 1 000 commandes commerciales réalisées entre janvier et décembre 2025 à l'aide de Python.

L'objectif est d'évaluer les performances commerciales, d'identifier les tendances du chiffre d'affaires, d'analyser la rentabilité des produits et de dégager des opportunités d'amélioration pour soutenir la prise de décision.

## Outils et technologies

- **Python** — traitement et analyse des données
- **Pandas** — nettoyage, validation et analyse des données
- **Matplotlib** — création de visualisations
- **OpenPyXL** — importation des données Excel
- **ReportLab** — génération automatisée de rapports PDF

## Nettoyage et validation des données

- Suppression de 5 doublons parmi les 1 005 enregistrements initiaux.
- Traitement des identifiants clients et des villes manquants à l'aide de la valeur `Unknown`.
- Vérification des quantités, du chiffre d'affaires, des bénéfices, des remises, des dates et des identifiants de commande.
- Préparation d'un jeu de données nettoyé contenant **1 000 commandes**.

## Indicateurs clés de performance (KPI)

| Indicateur | Résultat |
|---|---:|
| Chiffre d'affaires total | 7 139 581 MAD |
| Bénéfice total | 1 900 950,98 MAD |
| Marge bénéficiaire globale | 26,63 % |
| Nombre total de commandes | 1 000 |

## Principaux résultats de l'analyse

- **Électronique :** catégorie générant le chiffre d'affaires le plus élevé, avec 2,93 millions MAD.
- **Mobilier :** catégorie affichant la marge bénéficiaire la plus élevée, avec 27,11 %.
- **Smartphone :** produit générant le chiffre d'affaires le plus important, avec environ 931 000 MAD.
- **Rabat :** ville enregistrant le chiffre d'affaires le plus élevé, avec environ 1,05 million MAD.
- **Marketplace :** canal de vente présentant la meilleure marge bénéficiaire, avec 27,35 %.
- **Corporate :** segment de clientèle le plus rentable en pourcentage, avec une marge de 27,90 %.
- **Évolution mensuelle :** février enregistre le chiffre d'affaires le plus élevé, tandis que septembre présente le niveau le plus faible.

## Livrables du projet

- Scripts Python pour la préparation, l'analyse et la visualisation des données.
- Jeu de données nettoyé et validé.
- Synthèse des résultats et recommandations commerciales.
- Graphiques illustrant les performances commerciales.
- Rapport final d'analyse au format PDF.

## Exécution du projet

**1. Installer les bibliothèques nécessaires**

```bash
pip install -r requirements.txt
```

**2. Exécuter les scripts Python dans l'ordre suivant**

```bash
python 01_data_exploration.py
python 02_sales_analysis