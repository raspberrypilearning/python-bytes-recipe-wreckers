<h2 class="c-project-heading--task">Fix the ingredient formatting</h2>
--- task ---
Use `.title()` and `.lower()` on the ingredient values inside the `print()` line.
--- /task ---

<h2 class="c-project-heading--explainer">Make the ingredients readable</h2>

The ingredients are written in all uppercase — let’s make them easier to read in the final recipe.

- Use `.title()` to capitalise the first letter of each word  
- Use `.lower()` if it’s something that should be soft or whispered (like herbs)

Update the `print()` lines, not the variables at the top.

```python
f'Add grilled {protein.title()}'
f'Garnish with {garnish.lower()}'
```

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure your parentheses and curly braces match correctly when calling `.title()` or `.lower()` inside a string.

</div>
