<h2 class="c-project-heading--task">Ajouter des puces emoji</h2>

\--- task ---

Utilise la variable emoji pour ajouter une puce à chaque ligne.

\--- /task ---

<h2 class="c-project-heading--explainer">Embellir ta liste</h2>

Maintenant que les lignes sont séparées, ajoutons quelques puces !

Tu peux le faire en changeant à nouveau le séparateur, cette fois en `sep='\n' + emoji`.

De plus, tu devras ajouter manuellement l'emoji au **début de la première ligne**, car `sep` ne l'ajoute qu'_entre_ les lignes.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 12, 17
---

print(
f'{emoji}Commencez par une dose de {glucide}',
f'Recouvrez de dés de {legume_1} et de {legume_2}',
f'Ajoutez des {proteine} grillées',
f'Garnisez avec {garniture}',
f'Servez avec un accompagnement de {accompagnement}',
sep='\n + emoji'
)

\--- /code ---

</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de changer la variable `emoji` en haut par quelque chose de mignon comme :<br />
• 🍽️😋<br />
• 🧁<br />
• 🍱

</div>
