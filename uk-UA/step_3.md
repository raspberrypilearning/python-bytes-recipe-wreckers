<h2 class="c-project-heading--task">Додай емоджі-маркери</h2>

\--- task ---

Використай змінну emoji, щоб додати маркер до кожного рядка.

\--- /task ---

<h2 class="c-project-heading--explainer">Зроби свій список чудовим</h2>

Тепер, коли рядки розділені, давай додамо маркери списку!

Це можна зробити, знову змінивши роздільник — цього разу на `sep='\n' + emoji`.

Також тобі треба буде вручну додати емоджі **на початок першого рядка**, оскільки `sep` додає його лише _між_ рядками.

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
f'{emoji}Почни з порції {carb}',
f'Зверху додай нарізані {veg_1} і {veg_2}',
f'Додай смажений {protein}',
f'Прикрась {garnish}',
f'Подавай з гарніром із {side}',
sep='\n' + emoji
)

\--- /code ---

</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Спробуй змінити змінну `emoji` нагорі на щось миле, наприклад:<br />
• 🍽️😋<br />
• 🧁<br />
• 🍱

</div>
