#!/usr/bin/env python3
"""Generate T7 — Grid Data-Art Map: an elegant computed node-network ('the grid')
on deep indigo, with 9 nodes highlighted red. Emits a self-contained HTML file."""
import math, random
from pathlib import Path

W, H = 1080, 1350
random.seed(70291)

# --- node placement -------------------------------------------------------
nodes = []
attempts = 0
# keep the lower-left clear for the headline block
def in_text_zone(x, y):
    return (x < 600 and y > 880)
while len(nodes) < 52 and attempts < 4000:
    attempts += 1
    x = random.uniform(40, W-40)
    y = random.uniform(150, H-90)
    if in_text_zone(x, y) and random.random() < 0.86:
        continue
    # min spacing
    if any((x-nx)**2 + (y-ny)**2 < 78**2 for nx, ny, *_ in nodes):
        continue
    nodes.append([x, y])

# --- edges: connect to nearest neighbours --------------------------------
edges = []
for i, (x, y) in enumerate(nodes):
    d = sorted(((((x-nx)**2+(y-ny)**2), j) for j,(nx,ny) in enumerate(nodes) if j != i))
    for _, j in d[:2]:
        if (j, i) not in edges and (i, j) not in edges:
            if d[0][0] < 360**2:
                edges.append((i, j))
    # occasional longer link for organic feel
    if len(d) > 4 and random.random() < 0.18:
        edges.append((i, d[4][1]))

# --- choose 9 hot nodes (bias to upper / right, away from text) ----------
cands = sorted(range(len(nodes)), key=lambda i: -(nodes[i][0]*0.6 + (H-nodes[i][1])*0.4 + random.uniform(0,120)))
hot = []
for i in cands:
    x, y = nodes[i]
    if in_text_zone(x, y):
        continue
    if all((i!=h) for h in hot):
        hot.append(i)
    if len(hot) == 9:
        break
hot_set = set(hot)
pulse = hot[0]

# --- build SVG ------------------------------------------------------------
svg = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">']
svg.append('<defs><filter id="glow" x="-80%" y="-80%" width="260%" height="260%">'
           '<feGaussianBlur stdDeviation="9" result="b"/><feMerge>'
           '<feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
for i, j in edges:
    x1,y1 = nodes[i]; x2,y2 = nodes[j]
    hot_edge = i in hot_set or j in hot_set
    col = "rgba(239,68,68,0.30)" if hot_edge else "rgba(150,160,225,0.13)"
    sw = 1.6 if hot_edge else 1.0
    svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}"/>')
for idx,(x,y) in enumerate(nodes):
    if idx in hot_set:
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="20" fill="rgba(239,68,68,0.14)"/>')
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8.5" fill="#EF4444" filter="url(#glow)"/>')
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="#fff" opacity="0.95"/>')
    else:
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.0" fill="rgba(196,202,240,0.42)"/>')
svg.append('</svg>')
svg = "\n".join(svg)

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Oranienbaum&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{width:100%;height:100%}}
  body{{position:relative;overflow:hidden;width:{W}px;height:{H}px;color:#F6F6FC;
    font-family:'Manrope',system-ui,sans-serif;
    background:radial-gradient(120% 100% at 78% 14%, #1A1858 0%, #0C0B34 55%, #06062D 100%);
    -webkit-font-smoothing:antialiased}}
  .net{{position:absolute;inset:0;z-index:1}}
  .scrim{{position:absolute;inset:0;z-index:2;pointer-events:none;
    background:radial-gradient(90% 70% at 20% 92%, rgba(5,5,26,.92) 0%, rgba(5,5,26,.5) 36%, rgba(5,5,26,0) 60%)}}
  .content{{position:relative;z-index:3;width:100%;height:100%;padding:7.4%;display:flex;flex-direction:column}}
  .top{{display:flex;align-items:flex-start;justify-content:space-between}}
  .logo{{width:80px;height:80px;background:#EF4444;border-radius:21px;position:relative;flex-shrink:0;box-shadow:0 8px 26px rgba(239,68,68,.3)}}
  .logo::after{{content:"";position:absolute;inset:24px;background:#fff;border-radius:8px}}
  .kick{{text-align:right;font-size:19px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#FF6A5C;padding-top:8px;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
  .hero{{margin-top:auto}}
  .h1{{font-family:'Oranienbaum',serif;font-size:80px;line-height:.98;letter-spacing:-.01em;max-width:13ch;text-shadow:0 6px 34px rgba(0,0,0,.55)}}
  .h1 em{{font-style:normal;color:#FF6A5C}}
  .sub{{font-size:30px;line-height:1.36;color:#fff;margin-top:18px;max-width:24ch;font-weight:500;text-shadow:0 2px 16px rgba(0,0,0,.8)}}
  .foot{{display:flex;align-items:center;justify-content:space-between;margin-top:30px}}
  .site{{font-size:28px;font-weight:700;text-shadow:0 2px 12px rgba(0,0,0,.8)}}
  .cta{{background:#EF4444;color:#fff;font-weight:700;font-size:23px;padding:18px 32px;border-radius:14px;box-shadow:0 12px 30px rgba(239,68,68,.4)}}
</style></head><body>
  <div class="net">{svg}</div>
  <div class="scrim"></div>
  <div class="content">
    <div class="top">
      <div class="logo"></div>
      <div class="kick">The AI Energy<br>Demand Atlas</div>
    </div>
    <div class="hero">
      <div class="h1">9 nodes<br>hold the <em>$147B.</em></div>
      <p class="sub">We mapped the entire grid to find the nine utilities that absorbed AI's demand &mdash; and the six next in line.</p>
      <div class="foot">
        <div class="site">Ghostresearch.com</div>
        <div class="cta">Read the Atlas &rarr;</div>
      </div>
    </div>
  </div>
</body></html>"""

out = Path(__file__).parent / "T7-gridmap.html"
out.write_text(html, encoding="utf-8")
print("wrote", out, "| nodes", len(nodes), "edges", len(edges), "hot", len(hot))
