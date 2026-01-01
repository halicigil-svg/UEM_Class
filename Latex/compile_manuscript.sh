#!/bin/bash
# UEM Manuscript Compilation Script
# Compiles LaTeX document with bibliography

echo "========================================"
echo "UEM Manuscript Compilation"
echo "========================================"
echo ""

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "ERROR: pdflatex not found. Please install texlive:"
    echo "  Ubuntu/Debian: sudo apt-get install texlive-full"
    echo "  macOS: brew install mactex"
    echo "  Or download from: https://www.tug.org/texlive/"
    exit 1
fi

# Check if bibtex is available
if ! command -v bibtex &> /dev/null; then
    echo "ERROR: bibtex not found. Install texlive-full."
    exit 1
fi

echo "Step 1: Initial LaTeX compilation..."
pdflatex -interaction=nonstopmode UEM_manuscript.tex > compile_log1.txt 2>&1
if [ $? -ne 0 ]; then
    echo "ERROR in first pdflatex run. Check compile_log1.txt"
    exit 1
fi
echo "✓ First pass complete"

echo ""
echo "Step 2: Processing bibliography..."
bibtex UEM_manuscript > bibtex_log.txt 2>&1
if [ $? -ne 0 ]; then
    echo "WARNING: BibTeX reported issues. Check bibtex_log.txt"
fi
echo "✓ Bibliography processed"

echo ""
echo "Step 3: Second LaTeX compilation..."
pdflatex -interaction=nonstopmode UEM_manuscript.tex > compile_log2.txt 2>&1
if [ $? -ne 0 ]; then
    echo "ERROR in second pdflatex run. Check compile_log2.txt"
    exit 1
fi
echo "✓ Second pass complete"

echo ""
echo "Step 4: Final LaTeX compilation..."
pdflatex -interaction=nonstopmode UEM_manuscript.tex > compile_log3.txt 2>&1
if [ $? -ne 0 ]; then
    echo "ERROR in final pdflatex run. Check compile_log3.txt"
    exit 1
fi
echo "✓ Final pass complete"

echo ""
echo "========================================"
echo "✓ COMPILATION SUCCESSFUL!"
echo "========================================"
echo ""
echo "Output: UEM_manuscript.pdf"
echo ""

# Check file size
if [ -f "UEM_manuscript.pdf" ]; then
    filesize=$(du -h "UEM_manuscript.pdf" | cut -f1)
    pages=$(pdfinfo UEM_manuscript.pdf 2>/dev/null | grep Pages | awk '{print $2}')
    echo "PDF size: $filesize"
    if [ ! -z "$pages" ]; then
        echo "Pages: $pages"
    fi
    echo ""
    echo "Next steps:"
    echo "  1. Review PDF: open UEM_manuscript.pdf"
    echo "  2. Create submission archive: ./create_arxiv_package.sh"
    echo "  3. Submit to arXiv: see arXiv_Submission_Guide.md"
fi

echo ""
echo "Cleaning up auxiliary files..."
rm -f *.aux *.log *.bbl *.blg *.out compile_log*.txt bibtex_log.txt
echo "✓ Cleanup complete"
