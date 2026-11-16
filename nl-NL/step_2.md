<h2 class="c-project-heading--task">Corrigeer het uitvoerformaat</h2>

\--- task ---

Gebruik `sep='\n'` om elk onderdeel van het recept op een aparte regel af te drukken.

\--- /task ---

<h2 class="c-project-heading--explainer">Splits de uitvoer in regels</h2>

Op dit moment lijken alle receptregels dicht op elkaar te staan.  
Je kunt de `sep=` optie in `print()` gebruiken om Python te vertellen wat er **tussen** elk item moet komen.

Door `sep='\n'` in te stellen, krijg je een **nieuwe regel** tussen elk onderdeel van de afdruk.

Dit is hoe je code eruit zou moeten zien:

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
f'Begin met een schepje {koolhydraten}',
f'Bedek met in blokjes gesneden {groente_1} and {groente_2}',
f'Voeg gegrilde {eiwitten} toe',
f'Garneer met {garnering}',
f'Serveer met een bijgerecht van {bijgerecht}',
sep='\n'
)

\--- /code ---

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als je recept nog steeds op één regel staat, controleer dan het volgende:

- Heb je `sep='\n'` aan het einde van de `print()` toegevoegd?
- Staan de komma's na elke regel op de juiste plaats?

</div>
