#!/bin/bash
# Create arXiv submission package
# This script packages all files needed for arXiv submission

echo "========================================"
echo "Creating arXiv Submission Package"
echo "========================================"
echo ""

# Create submission directory
SUBMIT_DIR="UEM_arXiv_submission"
echo "Creating directory: $SUBMIT_DIR"
rm -rf $SUBMIT_DIR
mkdir -p $SUBMIT_DIR
mkdir -p $SUBMIT_DIR/figures

# Copy main files
echo "Copying manuscript files..."
cp UEM_manuscript.tex $SUBMIT_DIR/
cp UEM_references.bib $SUBMIT_DIR/

# Copy figures (assuming they're in /mnt/user-data/uploads or current directory)
echo "Copying figures..."
for fig in Figure_1_Lithium_Plateau.pdf \
           Figure_2_Cosmological_Posteriors.pdf \
           Figure_3_Hubble_Tension_Resolution.pdf \
           Figure_4_SNe_GeV_Emission.pdf \
           Figure_5_Galaxy_Gamma_Rays.pdf \
           Figure_6_Multi_Scale_Summary.pdf \
           Figure_7_Beryllium_Timeline.pdf \
           Phase_Cycle_Timeline_Complete.pdf; do
    
    # Try current directory first
    if [ -f "$fig" ]; then
        cp "$fig" $SUBMIT_DIR/figures/
        echo "  ✓ $fig"
    # Then try uploads directory
    elif [ -f "/mnt/user-data/uploads/$fig" ]; then
        cp "/mnt/user-data/uploads/$fig" $SUBMIT_DIR/figures/
        echo "  ✓ $fig (from uploads)"
    else
        echo "  ⚠ WARNING: $fig not found"
    fi
done

# Rename Phase_Cycle figure to match LaTeX
if [ -f "$SUBMIT_DIR/figures/Phase_Cycle_Timeline_Complete.pdf" ]; then
    mv "$SUBMIT_DIR/figures/Phase_Cycle_Timeline_Complete.pdf" \
       "$SUBMIT_DIR/figures/Figure_8_Phase_Cycle.pdf"
    echo "  ✓ Renamed Phase_Cycle to Figure_8"
fi

# Create README for arXiv
cat > $SUBMIT_DIR/00README.txt << 'EOF'
Universal Evolution Model Manuscript
====================================

This package contains the LaTeX source for:

"The Universal Evolution Model: Evidence for Metallicity-Gated 
Cosmic Phase Transitions from Multi-Scale Observations"

Author: Cihan Halicigil (Yale University School of Medicine)

Files included:
- UEM_manuscript.tex     : Main LaTeX source
- UEM_references.bib     : Bibliography (BibTeX format)
- figures/               : All 8 publication-quality figures (PDF)

To compile:
  pdflatex UEM_manuscript.tex
  bibtex UEM_manuscript
  pdflatex UEM_manuscript.tex
  pdflatex UEM_manuscript.tex

Requirements:
- LaTeX distribution (TeX Live 2020 or later)
- revtex4-2 document class
- Standard packages: graphicx, amsmath, hyperref, natbib

For questions or code access:
GitHub: https://github.com/halicigil-svg/UEM_CLASS
Email: cihan.halicigil@yale.edu
EOF

echo ""
echo "Creating tarball..."
tar -czf UEM_arXiv_submission.tar.gz $SUBMIT_DIR/

# Verify archive
echo ""
echo "Verifying archive contents..."
tar -tzf UEM_arXiv_submission.tar.gz | head -20
echo "..."
echo ""

# Get archive size
filesize=$(du -h UEM_arXiv_submission.tar.gz | cut -f1)
echo "========================================"
echo "✓ PACKAGE CREATED SUCCESSFULLY!"
echo "========================================"
echo ""
echo "Archive: UEM_arXiv_submission.tar.gz"
echo "Size: $filesize"
echo ""
echo "Contents:"
tar -tzf UEM_arXiv_submission.tar.gz | wc -l | xargs echo "  Total files:"
echo ""
echo "Next steps:"
echo "  1. Test the package:"
echo "     mkdir test_compile && cd test_compile"
echo "     tar -xzf ../UEM_arXiv_submission.tar.gz"
echo "     cd UEM_arXiv_submission"
echo "     pdflatex UEM_manuscript.tex"
echo "     bibtex UEM_manuscript"
echo "     pdflatex UEM_manuscript.tex"
echo "     pdflatex UEM_manuscript.tex"
echo ""
echo "  2. Submit to arXiv:"
echo "     - Go to https://arxiv.org/submit"
echo "     - Upload: UEM_arXiv_submission.tar.gz"
echo "     - Category: astro-ph.CO"
echo "     - See arXiv_Submission_Guide.md for details"
echo ""
echo "READY FOR ARXIV SUBMISSION!"
