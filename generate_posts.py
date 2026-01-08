import os
import random
import datetime

categories_list = [
    "law", "economics", "policy", "technology", 
    "infrastructure", "court reforms", "urban planning", 
    "history", "regulation", "data"
]

authors_list = [
    "Siddarth Raman", "Rahul Verma", "Priya Sharma", 
    "Sarah Jenkins", "The Leap Blog", "Payal Gupta", 
    "Vikram Singh", "Anand Prasad", "Ruxandra Teslo"
]

titles_templates = [
    ("The Economics of {topic}", ["infrastructure", "urban planning"]),
    ("Why {topic} Matters", ["law", "policy"]),
    ("The Future of {topic}", ["technology", "court reforms"]),
    ("A History of {topic}", ["history", "economics"]),
    ("Reforming {topic}", ["regulation", "law"]),
    ("{topic} in the 21st Century", ["technology", "data"]),
    ("The Hidden Cost of {topic}", ["infrastructure", "economics"]),
    ("Understanding {topic}", ["policy", "law"]),
    ("Data-Driven {topic}", ["data", "court reforms"]),
    ("{topic}: A New Perspective", ["history", "urban planning"])
]

topics = {
    "law": ["Legal Precedent", "The Supreme Court", "Contract Law"],
    "economics": ["Market Failure", "Inflation", "Trade Deficits"],
    "policy": ["Public spending", "Education Policy", "Healthcare Reform"],
    "technology": ["AI Governance", "Digital Courts", "Blockchain"],
    "infrastructure": ["High Speed Rail", "Power Grids", "Urban Transport"],
    "court reforms": ["Case Backlogs", "Judicial Appointments", "E-filing"],
    "urban planning": ["Mixed-Use Zoning", "Walkable Cities", "Suburban Sprawl"],
    "history": ["Colonial Law", "Industrial Revolution", "Post-War Policy"],
    "regulation": ["Antitrust", "Environmental Standards", "Financial Rules"],
    "data": ["Open Data", "Privacy Metrics", "Census Analysis"]
}

base_dir = "posts"
os.makedirs(base_dir, exist_ok=True)

start_date = datetime.date(2023, 1, 1)

for i in range(20):
    # Pick random category and topic
    category = random.choice(categories_list)
    topic_list = topics.get(category, ["General Topic"])
    topic = random.choice(topic_list)
    
    # Generate Title
    template, _ = random.choice(titles_templates)
    title = template.format(topic=topic)
    
    # Generate Date
    random_days = random.randint(0, 365 * 2)
    post_date = start_date + datetime.timedelta(days=random_days)
    date_str = post_date.strftime("%Y-%m-%d")
    
    # Generate Author
    author = random.choice(authors_list)
    
    # Generate Filename
    slug = title.lower().replace(" ", "-").replace(":", "").replace(",", "")
    folder_name = f"{date_str}-{slug}"
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, "index.qmd")
    
    content = f"""---
title: "{title}"
author: "{author}"
date: "{date_str}"
categories: [{category}, {random.choice(categories_list)}]
description: "A dummy post exploring the nuances of {topic} through the lens of {category}."
---

This is a generated post about **{topic}**. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## The Problem with {topic}

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ({category}) is often misunderstood.

## Conclusion

Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum at {date_str}.
"""
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print(f"Generated: {file_path}")

print("Done generating 20 posts.")
