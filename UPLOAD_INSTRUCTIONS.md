# UEM Visual Abstract - GitHub Upload Instructions

## Files Ready for Upload

This folder contains:
1. **UEM_Visual_Abstract.png** - High-resolution (300 DPI, 5370×2933 pixels) raster image
2. **UEM_Visual_Abstract.pdf** - Vector version (scalable, preferred for publications)
3. **create_visual_abstract.py** - Python script that generates the figure

## How to Upload to GitHub

### Option 1: Via GitHub Web Interface (Easiest)

1. Go to: https://github.com/halicigil-svg/UEM_Class
2. Click **"Add file"** → **"Upload files"**
3. Drag and drop these 3 files:
   - UEM_Visual_Abstract.png
   - UEM_Visual_Abstract.pdf
   - create_visual_abstract.py
4. Add commit message: "Add UEM visual abstract (publication-ready)"
5. Click **"Commit changes"**

### Option 2: Via Git Command Line

If you have the repository cloned locally:

```bash
# Navigate to your local repository
cd /path/to/UEM_Class

# Copy files to repository
cp /path/to/these/files/* .

# Stage files
git add UEM_Visual_Abstract.png UEM_Visual_Abstract.pdf create_visual_abstract.py

# Commit
git commit -m "Add UEM visual abstract (publication-ready, 300 DPI)"

# Push to GitHub
git push origin main
```

## Suggested Repository Location

Create a `figures/` or `visual_abstract/` folder in your repository:

```
UEM_Class/
├── figures/
│   ├── UEM_Visual_Abstract.png
│   ├── UEM_Visual_Abstract.pdf
│   └── create_visual_abstract.py
├── source/
├── README.md
└── ...
```

## Update Your README.md

Add this section to your repository README:

```markdown
## Visual Abstract

![UEM Visual Abstract](figures/UEM_Visual_Abstract.png)

**Publication-ready figure** showing the complete Universal Evolution Model framework:
- Infinite cosmic cycle: ...(n-1)→Former→Baryonic→Latter→(n+1)...
- Phase transitions at metallicity thresholds (Z ≈ 0.002 Z☉, Z ≈ 0.6 Z☉)
- Black holes as quantosynthesis engines
- Current position: 14.19 Gyr, entering Baryonic→Latter transition

**Specifications:**
- Format: PNG (300 DPI, 5370×2933px) + PDF (vector)
- Quality: Publication-ready for journals, presentations, and posters
- Statistical significance: >11σ combined across 6 validations

For high-resolution PDF version, see [UEM_Visual_Abstract.pdf](figures/UEM_Visual_Abstract.pdf)
```

## File Specifications

### UEM_Visual_Abstract.png
- **Resolution**: 300 DPI (publication standard)
- **Dimensions**: 5370 × 2933 pixels (17.9" × 9.78")
- **File Size**: 846 KB
- **Format**: PNG, 8-bit RGBA
- **Use For**: Presentations, web display, quick sharing

### UEM_Visual_Abstract.pdf
- **Type**: Vector graphics (infinite resolution)
- **File Size**: 72 KB
- **Format**: PDF
- **Use For**: Journal submissions, arXiv, posters, printing

### create_visual_abstract.py
- **Purpose**: Generates the visual abstract figure
- **Dependencies**: matplotlib, numpy
- **Output**: Both PNG and PDF versions
- **Customizable**: Colors, positions, labels can be adjusted

## Usage in Publications

This figure is perfect for:
- **Journal graphical abstract** (required by many journals)
- **Figure 1** in your UEM manuscript
- **arXiv submission** (use PDF version)
- **Conference presentations**
- **Poster presentations**
- **Social media announcements** (Twitter/X when published)

## Next Steps After Upload

1. **Update release notes** if you create a new release (v1.1.0)
2. **Add to arXiv submission** when you submit the manuscript
3. **Include in manuscript** as Figure 1 or graphical abstract
4. **Share on social media** when announcing your work

---

**Repository**: https://github.com/halicigil-svg/UEM_Class
**License**: Include appropriate license information for the figures
