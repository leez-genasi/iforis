import os
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

input_dir = Path("public")
output_dir = Path("recovered_vault")

print(f"Looking in: {input_dir.resolve()}")
print(f"HTML files found: {len(list(input_dir.rglob('*.html')))}")

for html_file in input_dir.rglob("*.html"):
    with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Quartz puts content in an <article> tag
    content = soup.find("article")
    
    # Fallback to main or body if no article tag
    if not content:
        content = soup.find("main") or soup.find("body")

    if not content:
        continue

    markdown = md(str(content), heading_style="ATX")

    # Mirror the folder structure
    relative = html_file.relative_to(input_dir)
    out_file = output_dir / relative.with_suffix(".md")
    out_file.parent.mkdir(parents=True, exist_ok=True)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Recovered: {out_file}")

print("\nDone! Check the recovered_vault folder.")