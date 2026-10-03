<h2 class="c-project-heading--task">Faciliter la lecture du code</h2>

\--- task ---

Divise la longue instruction d'impression en plusieurs lignes pour la rendre plus facile à comprendre.

\--- /task ---

<h2 class="c-project-heading--explainer">Un code lisible est un bon code</h2>

Le gérant d'un café a écrit toutes les parties imprimables de la recette sur une seule longue ligne — ça fonctionne, mais c'est difficile à lire !

Heureusement, Python te permet d'écrire de longues instructions `print()` sur plusieurs lignes.  
Il te suffit de **terminer chaque partie avec une virgule**, et Python la traitera toujours comme une seule commande.

---

**Exécute le programme une fois** avant de faire des changements et regarde la sortie.  
Ensuite, divise l'instruction d'impression sur plusieurs lignes et exécute-la à nouveau.  
Le résultat devrait être le même, mais le code est beaucoup plus facile à lire !

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights:
---

print(
f'Commencez par une dose de {glucide}',
f'Recouvrez de dés de {legume_1} et de {legume_2}',
f'Ajoutez des {proteine} grillées',
f'Garnisez avec {garniture}',
f'Servez avec un accompagnement de {accompagnement}'
)

\--- /code ---

</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Assure-toi de laisser **des virgules** à la fin de chaque ligne dans la déclaration d'impression !

</div>
