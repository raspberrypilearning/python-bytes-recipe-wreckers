<h2 class="c-project-heading--task">Voeg emoji-opsommingstekens toe</h2>

--- task ---

Gebruik de emoji-variabele om aan elke regel een opsommingsteken toe te voegen.

--- /task ---

<h2 class="c-project-heading--explainer">Zorg dat je lijst er fantastisch uitziet</h2>

Nu de regels gescheiden zijn, voegen we er wat opsommingstekens aan toe!

Je kunt dit doen door het scheidingsteken opnieuw te wijzigen, ditmaal naar `sep='\n' + emoji`.

Daarnaast is het aan te raden de emoji handmatig toe te voegen aan het **begin van de eerste regel**, aangezien `sep` deze alleen _tussen_ regels plaatst.

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
    f'{emoji}Begin met een schepje {koolhydraten}',
    f'Bedek met in blokjes gesneden {groente_1} and {groente_2}',
    f'Voeg gegrilde {eiwitten} toe',
    f'Garneer met {garnering}',
    f'Serveer met een bijgerecht van {bijgerecht}',
    sep='\n' + emoji
)

--- /code ---

</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de variabele `emoji` bovenaan te veranderen in iets schattigs zoals:<br />
• 🍽️😋<br />
• 🧁<br />
• 🍱

</div>
