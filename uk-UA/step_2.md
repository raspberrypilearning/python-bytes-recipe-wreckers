<h2 class="c-project-heading--task">Виправ формат виводу</h2>

\--- task ---

Використай `sep='\n'`, щоб надрукувати кожну частину рецепта з нового рядка.

\--- /task ---

<h2 class="c-project-heading--explainer">Розділи вивід на рядки</h2>

Зараз усі рядки рецепта виглядають зліпленими в один.  
Ти можеш використати параметр `sep=` у `print()`, щоб вказати Python, що ставити **між** кожним елементом.

Якщо встановити `sep='\n'`, між кожною частиною виводу буде **новий рядок**.

Ось як має виглядати твій код:

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
f'Почни з порції {carb}',
f'Додай зверху нарізані {veg_1} і {veg_2}',
f'Додай смажений {protein}',
f'Прикрась {garnish}',
f'Подавай із гарніром із {side}',
sep='\n'
)

\--- /code ---

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо твій рецепт усе ще в одному рядку, перевір:

- Ти додав `sep='\n'` у кінці `print()`?
- Коми стоять на місці після кожного рядка?

</div>
