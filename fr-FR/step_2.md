<h2 class="c-project-heading--task">Corriger le format de sortie</h2>

\--- task ---

Utilise `sep='\n'` pour imprimer chaque partie de la recette sur sa propre ligne.

\--- /task ---

<h2 class="c-project-heading--explainer">Diviser la sortie en lignes</h2>

Pour l'instant, toutes les lignes des recettes semblent compressées les unes contre les autres.  
Tu peux utiliser l'option `sep=` dans `print()` pour dire à Python ce qu'il faut mettre **entre** chaque élément.

En définissant \`sep='\n', tu obtiendras une **nouvelle ligne** entre chaque partie de l'impression.

Voici à quoi ton code devrait ressembler :

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 17
---

print(
f'Commencez par une dose de {glucide}',
f'Recouvrez de dés de {legume_1} et de {legume_2}',
f'Ajoutez des {proteine} grillées',
f'Garnisez avec {garniture}',
f'Servez avec un accompagnement de {accompagnement}',
sep='\n'
)

\--- /code ---

</div>

<div class="c-project-callout c-project-callout--debug">

### Débogage

Si ta recette tient toujours sur une seule ligne, vérifie :

- As-tu ajouté `sep='\n'` à la fin du `print()` ?
- Les virgules sont-elles bien placées après chaque ligne ?

</div>
