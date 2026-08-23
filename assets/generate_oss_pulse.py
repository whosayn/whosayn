#!/usr/bin/env python3
"""
Generate a compact, GitHub-native SVG showing the profile's last 12 months
of contribution activity. Designed for a profile README; no third-party
stats service required.

Requires:
  GITHUB_TOKEN   GitHub Actions token
  PROFILE_USER   GitHub login (defaults to whosayn)
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

TOKEN = os.environ["GITHUB_TOKEN"]
LOGIN = os.environ.get("PROFILE_USER", "whosayn")
OUT = Path(os.environ.get("OUTPUT_PATH", "assets/oss-pulse.svg"))

now = dt.datetime.now(dt.timezone.utc)
start = now - dt.timedelta(days=365)

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
            contributionLevel
          }
        }
      }
    }
    repositoriesContributedTo(
      first: 100,
      includeUserRepositories: true,
      contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, PULL_REQUEST_REVIEW]
    ) {
      totalCount
    }
  }
}
"""

payload = json.dumps(
    {
        "query": QUERY,
        "variables": {
            "login": LOGIN,
            "from": start.isoformat(),
            "to": now.isoformat(),
        },
    }
).encode()

request = Request(
    "https://api.github.com/graphql",
    data=payload,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "whosayn-profile-readme",
    },
)

with urlopen(request, timeout=30) as response:
    body = json.loads(response.read())

if body.get("errors"):
    raise RuntimeError(body["errors"])

user = body["data"]["user"]
if not user:
    raise RuntimeError(f"GitHub user {LOGIN!r} not found")

c = user["contributionsCollection"]
calendar = c["contributionCalendar"]
weeks = calendar["weeks"]
repos = user["repositoriesContributedTo"]["totalCount"]

stats = [
    ("contributions", calendar["totalContributions"]),
    ("pull requests", c["totalPullRequestContributions"]),
    ("reviews", c["totalPullRequestReviewContributions"]),
    ("repos touched", repos),
]

levels = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4,
}

# Keep the current 53-week contribution window.
weeks = weeks[-53:]

cell = 10
gap = 3
grid_x = 456
grid_y = 88
grid_w = 53 * (cell + gap)
grid_h = 7 * (cell + gap)

parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="250" viewBox="0 0 1200 250" role="img" aria-labelledby="title desc">',
    f'<title id="title">{html.escape(LOGIN)} GitHub pulse</title>',
    '<desc id="desc">Last twelve months of GitHub contribution activity, generated automatically by GitHub Actions.</desc>',
    """<style>
:root{color-scheme:light dark}
.bg{fill:#f6f8fa;stroke:#d0d7de}.box{fill:#fff;stroke:#d0d7de}.t{fill:#24292f;font:700 15px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}.n{fill:#24292f;font:700 28px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}.m{fill:#57606a;font:12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}.c0{fill:#ebedf0}.c1{fill:#9be9a8}.c2{fill:#40c463}.c3{fill:#30a14e}.c4{fill:#216e39}
@media(prefers-color-scheme:dark){.bg{fill:#161b22;stroke:#30363d}.box{fill:#0d1117;stroke:#30363d}.t,.n{fill:#f0f6fc}.m{fill:#8b949e}.c0{fill:#21262d}.c1{fill:#0e4429}.c2{fill:#006d32}.c3{fill:#26a641}.c4{fill:#39d353}}
</style>""",
    '<rect class="bg" x="1" y="1" width="1198" height="248" rx="14"/>',
    '<text class="t" x="30" y="42">OSS PULSE / LAST 12 MONTHS</text>',
    '<text class="m" x="30" y="64">generated from GitHub • refreshed automatically</text>',
]

x = 30
for label, value in stats:
    parts.append(f'<rect class="box" x="{x}" y="88" width="95" height="105" rx="10"/>')
    parts.append(f'<text class="n" x="{x+15}" y="132">{value}</text>')
    parts.append(f'<text class="m" x="{x+15}" y="158">{html.escape(label)}</text>')
    x += 105

parts.append(f'<text class="m" x="{grid_x}" y="71">contribution rhythm</text>')

for wi, week in enumerate(weeks):
    for di, day in enumerate(week["contributionDays"]):
        if di > 6:
            continue
        level = levels.get(day["contributionLevel"], 0)
        cx = grid_x + wi * (cell + gap)
        cy = grid_y + di * (cell + gap)
        title = f'{day["date"]}: {day["contributionCount"]} contributions'
        parts.append(
            f'<rect class="c{level}" x="{cx}" y="{cy}" width="{cell}" height="{cell}" rx="2">'
            f'<title>{html.escape(title)}</title></rect>'
        )

private = c.get("restrictedContributionsCount", 0)
footer = "publicly visible GitHub activity"
if private:
    footer += f" • {private} restricted contributions also reported by GitHub"

parts.append(f'<text class="m" x="30" y="224">{html.escape(footer)}</text>')
parts.append("</svg>")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(parts), encoding="utf-8")
print(f"Wrote {OUT}")
