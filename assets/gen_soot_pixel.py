#!/usr/bin/env python3
"""Generate pixel-art Soot (Moku mascot) SVGs — dark & light GitHub variants.

Hand-tuned silhouette on a 30x30 grid; output is run-length merged
<rect>s with shape-rendering=crispEdges, so it stays sharp at any size.
"""

OUT_W = OUT_H = 30
CELL = 4  # svg units per pixel
VIEW = OUT_W * CELL

# silhouette: per-row (left, right) inclusive extents of the body core
CORE = {
    6: (13, 17), 7: (11, 19), 8: (10, 21), 9: (9, 22), 10: (8, 23),
    11: (7, 24), 12: (6, 25), 13: (6, 25), 14: (6, 25), 15: (6, 25),
    16: (6, 25), 17: (6, 25), 18: (6, 25), 19: (7, 24), 20: (8, 23),
    21: (8, 23), 22: (9, 22), 23: (9, 22), 24: (10, 21), 25: (11, 20),
    26: (13, 18),
}

# 1px fluff spikes sticking out of the core: (col, row)
SPIKES = [
    (14, 5), (17, 5),                      # top tips
    (9, 8), (21, 8),                       # upper sides
    (5, 13), (26, 12),                     # mid sides
    (5, 16), (26, 17),                     # lower sides
    (10, 25), (20, 25),                    # bottom edge
    (12, 27), (16, 27), (19, 27),          # bottom tips
]

# halo arc (brass), hovering above the fluff
HALO = [(13, 2), (14, 2), (15, 2), (16, 2), (17, 2),
        (11, 3), (12, 3), (18, 3), (19, 3),
        (10, 4), (20, 4)]

# eyes: white ovals 3 wide x 5 tall (plus-shape rows)
EYE_L, EYE_R = (10, 12), (18, 12)  # top-left col,row of each 5x5 eye box
EYE_ROWS = {0: (1, 3), 1: (0, 4), 2: (0, 4), 3: (0, 4), 4: (1, 3)}

# pupils: 2x2, gaze centered slightly down
PUPIL_L = (11, 14)
PUPIL_R = (19, 14)

THEMES = {
    'light': dict(body='#0b0d10', eye='#f7fafa', pupil='#020305', halo='#957940'),
    'dark':  dict(body='#1b222b', eye='#f7fafa', pupil='#020305', halo='#a8894a'),
}


def cells():
    body, eye, pupil, halo = set(), set(), set(), set()
    for r, (l, rr) in CORE.items():
        for c in range(l, rr + 1):
            body.add((c, r))
    body |= set(SPIKES)
    halo |= set(HALO)
    for ex, ey in (EYE_L, EYE_R):
        for dr, (l, rr) in EYE_ROWS.items():
            for c in range(ex + l, ex + rr + 1):
                eye.add((c, ey + dr))
    for px, py in (PUPIL_L, PUPIL_R):
        for dc in range(2):
            for dr in range(2):
                pupil.add((px + dc, py + dr))
    body -= eye
    eye -= pupil
    return body, eye, pupil, halo


def runs(cellset, color):
    """Merge cells into per-row horizontal runs of <rect>."""
    out = []
    for r in range(OUT_H):
        cols = sorted(c for c, rr in cellset if rr == r)
        i = 0
        while i < len(cols):
            j = i
            while j + 1 < len(cols) and cols[j + 1] == cols[j] + 1:
                j += 1
            x, w = cols[i] * CELL, (cols[j] - cols[i] + 1) * CELL
            out.append(f'<rect x="{x}" y="{r * CELL}" width="{w}" height="{CELL}" fill="{color}"/>')
            i = j + 1
    return out


def svg(theme):
    t = THEMES[theme]
    body, eye, pupil, halo = cells()
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VIEW} {VIEW}" '
        f'width="{VIEW * 2}" shape-rendering="crispEdges">',
        f'  <!-- Soot, the Moku mascot — pixel variant for GitHub {theme} theme. '
        f'Regenerate: gen_soot_pixel.py -->',
    ]
    parts += ['  ' + s for s in runs(halo, t['halo'])]
    parts += ['  ' + s for s in runs(body, t['body'])]
    parts += ['  ' + s for s in runs(eye, t['eye'])]
    parts += ['  ' + s for s in runs(pupil, t['pupil'])]
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    import sys
    outdir = sys.argv[1] if len(sys.argv) > 1 else '.'
    for theme in ('dark', 'light'):
        path = f'{outdir}/soot-{theme}.svg'
        with open(path, 'w') as f:
            f.write(svg(theme))
        print('wrote', path)
