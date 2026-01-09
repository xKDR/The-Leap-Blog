#!/usr/bin/env python3
"""
Generate a static authors.html page by parsing all .qmd posts
and counting authors.
"""

import os
import yaml
import re
from pathlib import Path
from collections import defaultdict

def extract_yaml_frontmatter(filepath):
    """Extract YAML frontmatter from a .qmd file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match YAML frontmatter between --- markers
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except:
            return {}
    return {}

def main():
    # Directories to scan for posts
    post_dirs = ['2023', '2024', '2025']
    base_path = Path(__file__).parent
    
    # Count authors
    author_counts = defaultdict(int)
    
    for post_dir in post_dirs:
        dir_path = base_path / post_dir
        if not dir_path.exists():
            continue
        
        for qmd_file in dir_path.rglob('*.qmd'):
            metadata = extract_yaml_frontmatter(qmd_file)
            author = metadata.get('author')
            if author:
                # Handle list of authors
                if isinstance(author, list):
                    for a in author:
                        author_counts[a] += 1
                else:
                    author_counts[author] += 1
    
    # Sort authors by count (descending)
    sorted_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Generate HTML
    html_parts = []
    html_parts.append('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Authors – The Leap Blog</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="site_libs/bootstrap/bootstrap-ea8b145cea85b97be824a72db8d520d2.min.css">
</head>
<body class="quarto-light">
<div id="quarto-content" class="quarto-container page-columns page-rows-contents page-layout-full">
<main class="content column-page" id="quarto-document-content">
''')
    
    # Header partial (read from file if it exists)
    header_path = base_path / '_partials' / 'header.html'
    if header_path.exists():
        with open(header_path, 'r') as f:
            html_parts.append(f.read())
    
    html_parts.append('<header id="title-block-header" class="quarto-title-block default">')
    html_parts.append('<div class="quarto-title"><h1 class="title">Our Authors</h1></div>')
    html_parts.append('</header>')
    
    html_parts.append('<div class="authors-list">')
    
    for idx, (author, count) in enumerate(sorted_authors):
        css_class = 'author-card top-author' if idx == 0 else 'author-card'
        encoded_author = author.replace(' ', '%20')
        html_parts.append(f'''<div class="{css_class}">
<h3 class="author-name"><a href="archive.html#author={encoded_author}">{author}</a></h3>
<div class="author-meta">{count} articles</div>
</div>''')
    
    html_parts.append('</div>')
    html_parts.append('</main></div></body></html>')
    
    # Write output
    output_path = base_path / 'docs' / 'authors.html'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))
    
    print(f"Generated {output_path} with {len(sorted_authors)} authors")

if __name__ == '__main__':
    main()
