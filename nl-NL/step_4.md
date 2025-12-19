<h2 class="c-project-heading--task">Fix the ingredient formatting</h2>

\--- task ---

Use `.title()` and `.lower()` on the ingredient values inside the `print()` line.

\--- /task ---

<h2 class="c-project-heading--explainer">Make the ingredients readable</h2>

The ingredients are written in all uppercase — let’s make them easier to read in the final recipe.

- Use `.lower()` to make all the letters lowercase

Update each of the `print()` lines. Two lines have been done for you below.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14
line_highlights: 
---

f'Add grilled {protein.lower()}'
f'Garnish with {garnish.lower()}'

\--- /code ---

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure your parentheses and curly braces match correctly when calling `.lower()` inside a string.

</div>
