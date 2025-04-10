<h2 class="c-project-heading--task">Make the code easier to read</h2>
--- task ---
Split the long print statement onto multiple lines so it’s easier to understand.
--- /task ---

<h2 class="c-project-heading--explainer">Readable code is good code</h2>

The café manager has written all the print parts on one long line — it works, but it's hard to read!

Luckily, Python lets you write long `print()` statements across multiple lines.  
You just need to **end each part with a comma**, and Python will still treat it as one command.

---

**Run the program once** before making changes and look at the output.  
Then split the print statement across multiple lines and run it again.  
The output should be the same — but the code is much easier to read!

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
    f'{emoji} Start with a scoop of {carb}',
    f'Top with diced {veg_1} and {veg_2}',
    f'Add grilled {protein}',
    f'Garnish with {garnish}',
    f'Serve with a side of {side}'
)
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Make sure you leave **commas** at the end of each line inside the print statement!

</div>
