<h2 class="c-project-heading--task">Fix the output format</h2>
--- task ---
Use `sep='\n'` to print each part of the recipe on its own line.
--- /task ---

<h2 class="c-project-heading--explainer">Split the output into lines</h2>

Right now, all the recipe lines appear squashed together.  
You can use the `sep=` option in `print()` to tell Python what to put **between** each item.

By setting `sep='\n'`, you’ll get a **new line** between every part of the print.

Here’s what your code should look like:

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
    f'Start with a scoop of {carb}',
    f'Top with diced {veg_1} and {veg_2}',
    f'Add grilled {protein}',
    f'Garnish with {garnish}',
    f'Serve with a side of {side}',
    sep='\n'
)
--- /code ---
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If your recipe is still on one line, check:
- Did you add `sep='\n'` at the end of the `print()`?
- Are the commas in place after each line?

</div>
