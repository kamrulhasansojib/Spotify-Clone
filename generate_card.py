
import re
import urllib.request

USERNAME = "sojib19"
SOURCE_URL = f"https://dsastats.vercel.app/api/codolio/{USERNAME}"

req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=20) as resp:
    svg_text = resp.read().decode("utf-8", errors="ignore")

def extract_number(label_pattern, text):
    m = re.search(label_pattern + r"\D{0,20}?(\d+)", text)
    return m.group(1) if m else "0"

solved = extract_number(r"Total\s*Questions?\s*Solved", svg_text)
contests = extract_number(r"Total\s*Contests?\s*Participated", svg_text)
awards = extract_number(r"Awards?", svg_text)

template = """<svg width="380" height="120" viewBox="0 0 380 120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1; }}
    .title {{ font: 600 14px 'Segoe UI', Ubuntu, sans-serif; fill: #58a6ff; }}
    .label {{ font: 400 12px 'Segoe UI', Ubuntu, sans-serif; fill: #8b949e; }}
    .value {{ font: 700 18px 'Segoe UI', Ubuntu, sans-serif; fill: #e6edf3; }}
  </style>
  <rect x="0.5" y="0.5" width="379" height="119" rx="10" class="bg"/>
  <text x="20" y="28" class="title">{username} - Codolio Stats</text>
  <text x="20" y="58" class="label">Solved</text>
  <text x="20" y="82" class="value">{solved}</text>
  <text x="150" y="58" class="label">Contests</text>
  <text x="150" y="82" class="value">{contests}</text>
  <text x="280" y="58" class="label">Awards</text>
  <text x="280" y="82" class="value">{awards}</text>
  <line x1="20" y1="96" x2="360" y2="96" stroke="#30363d" stroke-width="1"/>
  <text x="20" y="112" class="label">codolio.com/profile/{username}</text>
</svg>
"""

output = template.format(username=USERNAME, solved=solved, contests=contests, awards=awards)

with open("codolio-stats.svg", "w") as f:
    f.write(output)

print(f"Generated: solved={solved} contests={contests} awards={awards}")
