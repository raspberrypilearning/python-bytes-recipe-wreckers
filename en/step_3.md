<h2 class="c-project-heading--task">Add emoji bullets</h2>
--- task ---
Use the emoji variable to add a bullet point to every line.
--- /task ---

<h2 class="c-project-heading--explainer">Make your list look amazing</h2>

Now that the lines are separated, let’s add some bullet points!

You can do this by changing the separator again, this time to `emoji + '\n'`.

Also, you’ll want to manually add the emoji at the **start of the first line**, since `sep` only adds it *between* lines.

<div class="c-project-code">
--- code ---
---
language: python
filename: prank_recipe.py
line_numbers: true
---
print(
    f'{emoji} Start with a scoop of {carb}',
    f'Top with diced {veg_1} and {veg_2}',
    f'Add grilled {protein}',
    f'Garnish with {garnish}',
    f'Serve with a side of {side}',
    sep=emoji + '\n'
)
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try changing the `emoji` variable at the top to something cute like:<br />
• 🍽️😋<br />
• 🧁<br />
• 🍱

</div>
