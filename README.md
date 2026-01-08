# The Leap Blog - Quarto Website

A Quarto website for The Leap Blog, featuring a clean Swiss design aesthetic.

## Features

- **Swiss Design**: Clean, minimalist design with strong typography and grid-based layouts
- **Blog Structure**: Organized posts in the `posts/` directory
- **Responsive**: Mobile-friendly design
- **Search**: Built-in search functionality

## Getting Started

1. **Render the website**:
   ```bash
   quarto render
   ```

2. **Preview locally**:
   ```bash
   quarto preview
   ```

3. **Publish** (when ready):
   ```bash
   quarto publish
   ```

## Project Structure

```
.
├── _quarto.yml          # Quarto configuration
├── index.qmd            # Home page
├── about.qmd            # About page
├── styles.css           # Custom Swiss design styles
└── posts/               # Blog posts directory
    ├── 2025-12-28-elephant/
    ├── 2025-12-tech-orders/
    └── 2025-12-delhi-power/
```

## Adding New Posts

Create a new directory in `posts/` with a date prefix (e.g., `2025-12-30-new-post/`) and add an `index.qmd` file with your post content.

## Design Philosophy

The Swiss design aesthetic emphasizes:
- Clean typography (Helvetica Neue)
- High contrast (black on white)
- Grid-based layouts
- Generous white space
- Functional, no-nonsense design
- Strong visual hierarchy
