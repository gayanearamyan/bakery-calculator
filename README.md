# Bake Day Calculator

A single-page tool for a small home bakery. Enter an order, and it instantly shows:

- **Shopping list** — how much of each ingredient you need, how many packages to buy, and what that costs
- **Cost of goods** — the true ingredient cost the order consumes (plus packaging and other costs)
- **Net profit and margin** — overall and per item

Everything is editable in the page itself: the four starter recipes (sourdough loaf, butter tart, choc chip cookie, seasonal fruit tart), their selling prices, per-item ingredient amounts, and pantry package prices. You can add or remove ingredients and recipes' rows as the menu evolves. Changes save automatically in the browser (localStorage), and "Reset to defaults" restores the starter numbers.

## How to publish (GitHub Pages)

1. Create a new repository (e.g. `bakery-calculator`) and upload `index.html` and this `README.md`.
2. In the repo, go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.
4. After a minute, the page is live at `https://<your-username>.github.io/bakery-calculator/`.
5. Send that link to the baker — nothing to install, works on phone and laptop.

## Notes

- No build step, no dependencies — one HTML file with vanilla JS. Google Fonts are loaded from a CDN; the page still works offline with fallback fonts.
- "Cost used" vs "Cost to buy": profit is calculated from ingredients actually consumed; the shopping ticket also rounds up to whole packages so you know how much cash to bring to the store. Leftovers carry over to the next bake.
- Each person's edits are saved only in their own browser. If you both want to tweak defaults permanently, edit the `defaultState()` function near the top of the `<script>` in `index.html`.
- "Print bake sheet" prints just the summary, shopping ticket, and per-item breakdown — handy to tape to the fridge on bake day.
