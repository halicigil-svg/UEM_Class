#!/usr/bin/env python3
"""
UEM Visual Abstract: Three-Phase Cosmic Evolution
Creates a visual representation of Former → Baryonic → Latter phase transitions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Wedge
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(18, 10))
ax.set_xlim(-2, 16)
ax.set_ylim(-1, 11)
ax.axis('off')

# Color scheme
color_prefomer = '#CCCCCC'  # Gray (faded)
color_former = '#4A90E2'  # Blue
color_baryonic = '#7ED321'  # Green
color_latter = '#F5A623'  # Orange
color_bh = '#000000'  # Black
color_text = '#333333'

# Define circle positions and sizes
# (n-1) Pre-Former phase (far left, faded)
prefomer_center = (-0.5, 5)
prefomer_radius = 2.3

# Former phase
former_center = (3.5, 5)
former_radius = 2.5

# Baryonic phase (middle, current)
baryonic_center = (7.5, 5)
baryonic_radius = 2.8

# Latter phase (right) - partially faded/dashed
latter_center = (11.5, 5)
latter_radius = 2.5

# Draw the four phase circles
# (n-1) Pre-Former phase (faded, dashed - unobservable past)
prefomer_circle = Circle(prefomer_center, prefomer_radius, 
                         facecolor=color_prefomer, alpha=0.15, 
                         edgecolor=color_prefomer, linewidth=2,
                         linestyle=':', label='(n-1) Phase')
ax.add_patch(prefomer_circle)

# Former phase (complete)
former_circle = Circle(former_center, former_radius, 
                       facecolor=color_former, alpha=0.3, 
                       edgecolor=color_former, linewidth=3,
                       label='Former Phase')
ax.add_patch(former_circle)

# Baryonic phase (complete, current)
baryonic_circle = Circle(baryonic_center, baryonic_radius, 
                         facecolor=color_baryonic, alpha=0.3, 
                         edgecolor=color_baryonic, linewidth=4,
                         label='Baryonic Phase')
ax.add_patch(baryonic_circle)

# Latter phase (emerging, dashed)
latter_circle = Circle(latter_center, latter_radius, 
                       facecolor=color_latter, alpha=0.15, 
                       edgecolor=color_latter, linewidth=3,
                       linestyle='--', label='Latter Phase')
ax.add_patch(latter_circle)

# Black holes at intersections
# (n-1)-Former intersection (faint, unobservable)
pf_x = (prefomer_center[0] + former_center[0]) / 2
pf_y = prefomer_center[1]

# Draw faint BHs in (n-1)-Former intersection
bh_positions_pf = [
    (pf_x - 0.2, pf_y + 0.3),
    (pf_x + 0.1, pf_y - 0.2)
]

for bh_x, bh_y in bh_positions_pf:
    # Faint black hole
    bh = Circle((bh_x, bh_y), 0.12, facecolor='gray', edgecolor='lightgray', 
                linewidth=1, alpha=0.3)
    ax.add_patch(bh)
    # Faint accretion disk
    disk = Circle((bh_x, bh_y), 0.2, facecolor='none', edgecolor='gray', 
                  linewidth=1, linestyle=':', alpha=0.2)
    ax.add_patch(disk)

# Label for (n-1)-Former intersection
ax.text(pf_x, pf_y + 1.2, '(n-1) BHs', fontsize=9, weight='bold', 
        ha='center', color='gray', alpha=0.5)
ax.text(pf_x, pf_y + 0.9, '(Unobservable)', fontsize=7, ha='center', 
        color='gray', alpha=0.5, style='italic')

# Former-Baryonic intersection
fb_x = (former_center[0] + baryonic_center[0]) / 2
fb_y = former_center[1]

# Draw Former BHs in Former-Baryonic intersection (3 spread out, moved left)
bh_positions_fb = [
    (fb_x - 0.4, fb_y + 0.45),
    (fb_x - 0.4, fb_y),
    (fb_x - 0.4, fb_y - 0.45)
]

for bh_x, bh_y in bh_positions_fb:
    # Black hole
    bh = Circle((bh_x, bh_y), 0.15, facecolor='black', edgecolor='white', linewidth=1.5, zorder=1)
    ax.add_patch(bh)
    # Accretion disk
    disk = Circle((bh_x, bh_y), 0.25, facecolor='none', edgecolor='yellow', 
                  linewidth=1.5, linestyle='--', alpha=0.6, zorder=1)
    ax.add_patch(disk)

# Baryonic-Latter intersection (right overlap)
bl_x = (baryonic_center[0] + latter_center[0]) / 2
bl_y = baryonic_center[1]

# Draw high-metallicity BHs in Baryonic-Latter intersection (symmetric to Former BHs)
bh_positions_bl = [
    (bl_x + 0.4, bl_y + 0.45),
    (bl_x + 0.4, bl_y),
    (bl_x + 0.4, bl_y - 0.45)
]

for bh_x, bh_y in bh_positions_bl:
    # Black hole (larger, more prominent)
    bh = Circle((bh_x, bh_y), 0.18, facecolor='black', edgecolor='white', linewidth=2, zorder=1)
    ax.add_patch(bh)
    # Bright accretion disk
    disk = Circle((bh_x, bh_y), 0.3, facecolor='none', edgecolor='orange', 
                  linewidth=2, alpha=0.8, zorder=1)
    ax.add_patch(disk)

# Add "Little Red Dots" (JWST z>10 galaxies) - IN the intersection around the BHs
lrd_positions = [
    (fb_x + 0.15, fb_y + 0.5, 'red'),
    (fb_x - 0.1, fb_y + 0.15, 'darkred'),
    (fb_x + 0.2, fb_y - 0.2, '#8B0000')
]

for lrd_x, lrd_y, lrd_color in lrd_positions:
    lrd = Circle((lrd_x, lrd_y), 0.08, facecolor=lrd_color, edgecolor='white', 
                 linewidth=1, alpha=0.8, zorder=5)
    ax.add_patch(lrd)

# Phase labels
# (n-1) Pre-Former phase label
ax.text(prefomer_center[0], prefomer_center[1] + prefomer_radius + 0.5, 
        '(n-1) PHASE', fontsize=14, weight='bold', 
        ha='center', color=color_prefomer, alpha=0.6)
ax.text(prefomer_center[0], prefomer_center[1] + prefomer_radius + 0.1, 
        '(Unobservable Past)', fontsize=9, ha='center', 
        color=color_prefomer, style='italic', alpha=0.6)

ax.text(former_center[0], former_center[1] + former_radius + 0.5, 
        'FORMER PHASE', fontsize=16, weight='bold', 
        ha='center', color=color_former)
ax.text(former_center[0], former_center[1] + former_radius + 0.1, 
        '(Complete)', fontsize=11, ha='center', color=color_former, style='italic')

ax.text(baryonic_center[0], baryonic_center[1] + baryonic_radius + 0.5, 
        'BARYONIC PHASE', fontsize=18, weight='bold', 
        ha='center', color=color_baryonic)
ax.text(baryonic_center[0], baryonic_center[1] + baryonic_radius + 0.1, 
        '(Current - 80% Mature)', fontsize=11, ha='center', 
        color=color_baryonic, style='italic')

ax.text(latter_center[0], latter_center[1] + latter_radius + 0.5, 
        'LATTER PHASE', fontsize=16, weight='bold', 
        ha='center', color=color_latter)
ax.text(latter_center[0], latter_center[1] + latter_radius + 0.1, 
        '(Emerging)', fontsize=11, ha='center', color=color_latter, style='italic')

# Add content inside Former phase - horizontal arrow showing metallicity evolution
# Left side: Pristine Former H/He
ax.text(former_center[0] - 1.8, former_center[1] + 0.3, 
        'Pristine', fontsize=10, weight='bold', color=color_former, ha='center')
ax.text(former_center[0] - 1.8, former_center[1], 
        'Former', fontsize=10, weight='bold', color=color_former, ha='center')
ax.text(former_center[0] - 1.8, former_center[1] - 0.3, 
        'H/He', fontsize=10, weight='bold', color=color_former, ha='center')

# Horizontal arrow showing nucleosynthesis progression (along equator)
arrow_former_horiz = FancyArrowPatch(
    (former_center[0] - 1.2, former_center[1]), 
    (former_center[0] + 1.0, former_center[1]),  # Moved further back to left from 1.5 to 1.0
    arrowstyle='->', mutation_scale=25, 
    linewidth=3, color=color_former, alpha=0.7, zorder=2)
ax.add_patch(arrow_former_horiz)

# Center: Nucleosynthesis label
ax.text(former_center[0], former_center[1] + 0.6, 
        'Former Nucleosynthesis', fontsize=9, color=color_former, 
        ha='center', style='italic')

# Right side: High metallicity Former matter (made more compact)
ax.text(former_center[0] + 1.2, former_center[1] + 0.4, 
        'High-Z Former', fontsize=8, weight='bold', color=color_former, ha='center')
ax.text(former_center[0] + 1.2, former_center[1] + 0.1, 
        'Matter', fontsize=8, color=color_former, ha='center')
ax.text(former_center[0] + 1.2, former_center[1] - 0.2, 
        '↓', fontsize=14, color=color_former, ha='center')

# Add content at Former-Baryonic intersection (centered in middle)
ax.text(fb_x, fb_y + 1.3, 'Former-', fontsize=10, weight='bold', 
        ha='center', color='black')
ax.text(fb_x, fb_y + 1.0, 'Low Metallic BHs', fontsize=9, weight='bold', 
        ha='center', color='black')
ax.text(fb_x, fb_y + 0.7, 'Z ≈ 0.002 Z☉', fontsize=9, ha='center', 
        color='black', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Label for "Little Red Dots" (positioned below intersection)
ax.text(fb_x, fb_y - 0.8, 'JWST "Little Red Dots"', fontsize=7, ha='center', 
        color='darkred', weight='bold')
ax.text(fb_x, fb_y - 1.05, 'z > 10', fontsize=7, ha='center', 
        color='darkred', style='italic')

# Add content inside Baryonic phase - horizontal arrow showing metallicity evolution
# Left side: Pristine H/He (in dark green, positioned near intersection, product of quantosynthesis)
ax.text(fb_x + 0.9, fb_y - 0.5, 'Pristine', fontsize=9, weight='bold', color='#2D5016', ha='center', zorder=10)
ax.text(fb_x + 0.9, fb_y - 0.75, 'H/He', fontsize=9, weight='bold', color='#2D5016', ha='center', zorder=10)

# Horizontal arrow showing nucleosynthesis progression (along equator)
arrow_baryonic_horiz = FancyArrowPatch(
    (baryonic_center[0] - 1.8, baryonic_center[1]),  # Adjusted to new compact text position
    (baryonic_center[0] + 2.0, baryonic_center[1]),
    arrowstyle='->', mutation_scale=25, 
    linewidth=3.5, color='#2D5016', alpha=0.8)  # Dark green
ax.add_patch(arrow_baryonic_horiz)

# Center: Nucleosynthesis label
ax.text(baryonic_center[0], baryonic_center[1] + 0.7, 
        'Stellar Nucleosynthesis', fontsize=10, color='#2D5016',  # Dark green
        ha='center', style='italic')
ax.text(baryonic_center[0], baryonic_center[1] - 0.8, 
        'Standard Model', fontsize=10, weight='bold', color='#2D5016', ha='center')  # Dark green
ax.text(baryonic_center[0], baryonic_center[1] - 1.1, 
        'Periodic Table', fontsize=9, color='#2D5016', ha='center')  # Dark green

# Right side: High metallicity Baryonic matter → BHs (made more compact)
ax.text(baryonic_center[0] + 1.5, baryonic_center[1] + 0.5, 
        'High-Z Baryonic', fontsize=8, weight='bold', color='#2D5016', ha='center')  # Dark green
ax.text(baryonic_center[0] + 1.5, baryonic_center[1] + 0.2, 
        'Matter', fontsize=8, color='#2D5016', ha='center')  # Dark green
ax.text(baryonic_center[0] + 1.5, baryonic_center[1] - 0.1, 
        '↓', fontsize=14, color='#2D5016', ha='center')  # Dark green

# Add "YOU ARE HERE" marker - pointing at Baryonic-Latter intersection (80% mature = transition starting)
ax.annotate('', xy=(bl_x, bl_y - 0.3), 
            xytext=(bl_x, bl_y - 1.5),
            arrowprops=dict(arrowstyle='->', lw=3, color='red'))
ax.text(bl_x, bl_y - 1.9, 
        '★ YOU ARE HERE', fontsize=12, weight='bold', color='red', ha='center',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7, edgecolor='red', linewidth=2))
ax.text(bl_x, bl_y - 2.3, 
        '14.19 Gyr | 80% Mature', fontsize=9, color='red', style='italic', ha='center')
ax.text(bl_x, bl_y - 2.6, 
        'Entering Latter Phase', fontsize=8, color='red', weight='bold', ha='center')

# Add content at Baryonic-Latter intersection (centered in middle)
ax.text(bl_x, bl_y + 1.5, 'Latter-', fontsize=10, weight='bold', 
        ha='center', color='black')
ax.text(bl_x, bl_y + 1.2, 'High Metallic BHs', fontsize=9, weight='bold', 
        ha='center', color='black')
ax.text(bl_x, bl_y + 0.9, 'Sgr A*, M87', fontsize=9, ha='center', color='black')
ax.text(bl_x, bl_y + 0.6, 'Z ≈ 0.6-1.0 Z☉', fontsize=9, ha='center', 
        color='black', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add content inside Latter phase (partial, emerging) - horizontal arrow
# Left side: High metallic BHs - REMOVED per user request

# Horizontal arrow showing future nucleosynthesis (faded)
arrow_latter_horiz = FancyArrowPatch(
    (latter_center[0] - 1.5, latter_center[1]),  # Adjusted to match new text position
    (latter_center[0] + 1.6, latter_center[1]),
    arrowstyle='->', mutation_scale=25, 
    linewidth=3, color='#B8751E', alpha=0.5, linestyle='--')  # Dark orange
ax.add_patch(arrow_latter_horiz)

# Center: Future nucleosynthesis label
ax.text(latter_center[0], latter_center[1] + 0.7, 
        'Future Nucleosynthesis', fontsize=9, color='#B8751E',  # Dark orange
        ha='center', style='italic', alpha=0.9)
ax.text(latter_center[0], latter_center[1] - 0.8, 
        'Latter Periodic', fontsize=9, color='#B8751E', ha='center', alpha=0.9)  # Dark orange
ax.text(latter_center[0], latter_center[1] - 1.1, 
        'Table', fontsize=9, color='#B8751E', ha='center', alpha=0.9)  # Dark orange

# Right side: Future high-Z Latter matter (made more compact)
ax.text(latter_center[0] + 1.2, latter_center[1] + 0.4, 
        'High-Z Latter', fontsize=8, weight='bold', color='#B8751E', ha='center', alpha=0.7)
ax.text(latter_center[0] + 1.2, latter_center[1] + 0.1, 
        'Matter', fontsize=8, color='#B8751E', ha='center', alpha=0.7)
ax.text(latter_center[0] + 1.2, latter_center[1] - 0.2, 
        '↓', fontsize=14, color='#B8751E', ha='center', alpha=0.6)
ax.text(latter_center[0] + 1.2, latter_center[1] - 0.5, 
        '(Future)', fontsize=7, color='#7A5015', ha='center', alpha=0.7, style='italic')

# Add timeline at bottom
timeline_y = 0.3
ax.plot([0, 14], [timeline_y, timeline_y], 'k-', linewidth=2)

# Timeline markers
timeline_markers = [
    (0.5, '(n-1)\nComplete', color_prefomer),
    (2, '(n-1)→Former\nTransition', 'gray'),
    (5, 'Former\nPeak', color_former),
    (6.5, 'Former→\nBaryonic\nTransition', 'purple'),
    (8, 'Baryonic\nPeak', color_baryonic),
    (9.5, 'Baryonic→\nLatter\nTransition', 'darkorange'),
    (12, 'Latter\nEmerging', color_latter)
]

for x, label, color in timeline_markers:
    ax.plot([x, x], [timeline_y - 0.1, timeline_y + 0.1], color=color, linewidth=2)
    ax.text(x, timeline_y - 0.5, label, fontsize=8, ha='center', color=color)

# Current position on timeline - aligned with Baryonic→Latter intersection
current_x = bl_x  # Align with YOU ARE HERE arrow
ax.plot([current_x, current_x], [timeline_y - 0.15, timeline_y + 0.15], 
        'r-', linewidth=4)
ax.text(current_x, timeline_y + 0.4, '▼ NOW', fontsize=10, ha='center', 
        color='red', weight='bold')

# Title
ax.text(7.5, 9.5, 'Universal Evolution Model: Infinite Cosmic Cycle', 
        fontsize=20, weight='bold', ha='center', color=color_text)
ax.text(7.5, 9.0, 'Matter transitions through discrete phases via black-hole-mediated quantosynthesis at metallicity thresholds', 
        fontsize=11, ha='center', color=color_text, style='italic')

# Key insights box
insights_text = """KEY INSIGHTS:
• Each phase: Pristine H/He → Nucleosynthesis → High-Z Matter → BHs → Next Phase
• Infinite cycle: ...(n-1)→Former→Baryonic→Latter→(n+1)...
• Transitions at Z ≈ 0.002 Z☉ (Former→Baryonic), Z ≈ 0.6 Z☉ (Baryonic→Latter)  
• Black holes = "quantosynthesis engines" creating pristine H/He of next phase
• Dark matter = Former relics | Dark energy = Latter dynamics | CMB = Former quantosynthesis"""

ax.text(7.5, -0.5, insights_text, fontsize=9, ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, 
                  edgecolor='black', linewidth=2),
        family='monospace')

# Statistical significance note
ax.text(14.5, 9.5, '>11σ\nCombined', fontsize=14, weight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8, 
                  edgecolor='darkgreen', linewidth=2))

plt.tight_layout()

# Save
plt.savefig('UEM_Visual_Abstract.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('UEM_Visual_Abstract.pdf', bbox_inches='tight', facecolor='white')

print("✓ Visual abstract created:")
print("  - UEM_Visual_Abstract.png (300 dpi)")
print("  - UEM_Visual_Abstract.pdf (vector)")

plt.show()
