<h2 class="c-project-heading--task">Maak de code gemakkelijker te lezen</h2>

--- task ---

Splits de lange printopdracht op in meerdere regels, zodat deze beter te begrijpen is.

--- /task ---

<h2 class="c-project-heading--explainer">Leesbare code is goede code</h2>

Een cafémanager heeft alle onderdelen van het recept op één lange regel geschreven — het werkt, maar het is moeilijk leesbaar!

Gelukkig kun je in Python lange `print()`-instructies over meerdere regels schrijven.  
Je hoeft alleen maar **elk onderdeel met een komma af te sluiten**, en Python zal het nog steeds als één commando beschouwen.

---

**Voer het programma eerst een keer uit** voordat je wijzigingen aanbrengt en bekijk de uitvoer.  
Splits vervolgens de printopdracht over meerdere regels en voer deze opnieuw uit.  
De uitvoer zou hetzelfde moeten zijn, maar de code is veel gemakkelijker te lezen!

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
    f'Begin met een schepje {koolhydraten}',
    f'Bedek met in blokjes gesneden {groente_1} and {groente_2}',
    f'Voeg gegrilde {eiwitten} toe',
    f'Garneer met {garnering}',
    f'Serveer met een bijgerecht van {bijgerecht}'
)

--- /code ---

</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Zorg ervoor dat je aan het einde van elke regel in de printopdracht **komma's** laat staan!

</div>
