# arXiv Submission Guide for UEM Manuscript

## Quick Start Checklist

- [ ] LaTeX document compiles without errors
- [ ] All figures included and referenced
- [ ] Bibliography complete
- [ ] Abstract under 1920 characters
- [ ] No line numbers or comments in submission
- [ ] Files compressed in .tar.gz format

## Step-by-Step Submission Process

### 1. Prepare Files

**Required files:**
```
UEM_submission/
├── UEM_manuscript.tex          # Main LaTeX file
├── UEM_references.bib          # Bibliography
├── figures/
│   ├── Figure_1_Lithium_Plateau.pdf
│   ├── Figure_2_Cosmological_Posteriors.pdf
│   ├── Figure_3_Hubble_Tension.pdf
│   ├── Figure_4_SNe_GeV.pdf
│   ├── Figure_5_Galaxy_Gamma.pdf
│   ├── Figure_6_MultiScale_Summary.pdf
│   ├── Figure_7_Beryllium_Timeline.pdf
│   └── Figure_8_Phase_Cycle.pdf
└── 00README.txt                # Brief description (optional)
```

### 2. Compile Locally

```bash
# Test compilation
pdflatex UEM_manuscript.tex
bibtex UEM_manuscript
pdflatex UEM_manuscript.tex
pdflatex UEM_manuscript.tex

# Verify output
open UEM_manuscript.pdf
```

**Common issues:**
- Missing packages → Install texlive-full
- Figure errors → Check file paths
- Bibliography errors → Verify .bib syntax

### 3. Create Submission Archive

```bash
# Create directory
mkdir UEM_arXiv_submission
cd UEM_arXiv_submission

# Copy files
cp ../UEM_manuscript.tex .
cp ../UEM_references.bib .
cp -r ../figures .

# Remove intermediate files
rm -f *.aux *.log *.bbl *.blg *.out

# Create tarball
cd ..
tar -czf UEM_submission.tar.gz UEM_arXiv_submission/

# Verify archive
tar -tzf UEM_submission.tar.gz
```

### 4. arXiv Account Setup

**If you don't have an account:**
1. Go to https://arxiv.org/user/register
2. Use institutional email (cihan.halicigil@yale.edu)
3. Verify email address
4. Complete registration

**Endorsement requirement:**
- For astro-ph.CO (cosmology), you need endorsement
- Request from someone who has published in astro-ph.CO
- Alternative: Ask your institution's endorsers

### 5. Submit to arXiv

**Navigate to:** https://arxiv.org/submit

**Steps:**
1. Click "START NEW SUBMISSION"
2. Select license: **Creative Commons Attribution (CC BY 4.0)**
3. Choose archive: **astro-ph** (Astrophysics)
4. Choose subject: **astro-ph.CO** (Cosmology and Nongalactic Astrophysics)
5. Upload: UEM_submission.tar.gz
6. Fill metadata:
   - Title: (copy from LaTeX)
   - Authors: Cihan Halicigil
   - Abstract: (copy from LaTeX, verify < 1920 char)
   - Comments: "29 pages, 8 figures. CODE: github.com/halicigil-svg/UEM_CLASS"
   - Report number: (leave blank)
   - Journal reference: (leave blank for preprint)
   - DOI: (leave blank)
7. Review and submit

### 6. Post-Submission

**arXiv processes submissions:**
- Weekday submissions before 14:00 ET → next day
- Weekend submissions → following Monday
- Holiday delays possible

**Your paper will get an identifier:**
- Format: arXiv:YYMM.NNNNN (e.g., arXiv:2501.12345)
- Use this for citations and references

**After posting:**
- Paper appears on https://arxiv.org/list/astro-ph.CO/new
- PDF automatically generated
- Email notification sent
- Can submit updates/corrections later

### 7. Announce on Social Media

**After arXiv posting:**

**Twitter/X:**
```
🌌 NEW PAPER 🌌

"The Universal Evolution Model: Evidence for Metallicity-Gated Cosmic Phase Transitions"

✅ Resolves Hubble tension (4.9σ → 1.3σ)
✅ Explains lithium problem (7.2σ discovery)  
✅ Direct observation of matter creation
✅ >11σ combined significance

📄 arXiv:XXXX.XXXXX
💻 Code: github.com/halicigil-svg/UEM_CLASS

#cosmology #JWST #DarkMatter #DarkEnergy
```

**Reddit r/cosmology:**
```
Title: [New Paper] Universal Evolution Model: Multi-scale evidence for cosmic phase transitions

I've just posted a paper proposing that cosmic evolution proceeds through discrete phases mediated by black holes at metallicity thresholds. Six independent tests yield >11σ combined significance, including:

- 7.2σ lithium plateau detection (156k GALAH stars)
- Hubble tension resolution to 1.3σ
- Direct matter creation in JWST RBH-1

All code and data publicly available. Would appreciate technical feedback!

arXiv: XXXX.XXXXX
GitHub: github.com/halicigil-svg/UEM_CLASS
```

### 8. Journal Submission Timeline

**After arXiv posting:**

**Week 1-2:** Monitor feedback, respond to questions
**Week 3:** Submit to Physical Review D
**Month 1-2:** Initial referee reports
**Month 2-3:** Revisions
**Month 3-4:** Second review round
**Month 4-6:** Acceptance and publication

## Important Notes

### arXiv Policies

**What arXiv allows:**
- ✅ Novel theoretical frameworks
- ✅ Controversial ideas (if rigorous)
- ✅ Challenges to established models
- ✅ Code and data references

**What arXiv prohibits:**
- ❌ Non-scientific content
- ❌ Promotional material
- ❌ Duplicate submissions
- ❌ Excessive self-citation

### Your Manuscript Status

**Strengths:**
- Professional scientific writing
- Rigorous statistical methods
- Clear falsifiable predictions
- Public code availability
- Addresses real observational tensions

**Potential concerns:**
- Non-standard affiliation (clinical, not physics/astro)
- Paradigm-challenging claims
- Sole authorship unusual for cosmology

**Mitigation:**
- Emphasize data-driven approach
- Highlight public code for verification
- Professional tone throughout
- Acknowledge limitations explicitly

### Endorsement Strategy

**If you need endorsement:**

**Option 1:** Ask colleagues at Yale who have published in astro-ph
- Physics department faculty
- Astronomy department
- Applied physics

**Option 2:** Contact researchers you've cited
- Brief, professional email
- Explain your work
- Request endorsement after they review
- Attach PDF

**Option 3:** Use AUTO ENDORSEMENT
- If you have previous arXiv submissions
- If your institutional email is recognized

**Sample endorsement request:**
```
Subject: Endorsement Request for astro-ph.CO Submission

Dear Dr. [Name],

I am a researcher at Yale University School of Medicine working on 
cosmological data analysis. I have developed a framework addressing 
multiple observational tensions (Hubble constant, lithium problem, 
etc.) and would like to post my results to arXiv for community 
feedback.

Could you review my manuscript and consider endorsing my submission 
to astro-ph.CO? I have attached a PDF for your review.

The work includes:
- Analysis of 156k GALAH stars showing lithium discontinuity
- Modified CLASS implementation resolving H₀ tension
- Statistical significance >11σ across multiple tests

All code and data are publicly available for verification.

Thank you for considering this request.

Best regards,
Cihan Halicigil, Ph.D.
Yale University School of Medicine
```

## FAQ

**Q: What if arXiv rejects my submission?**
A: Rare for scientific content. If rejected, address stated concerns and resubmit. Can also appeal.

**Q: Can I update after posting?**
A: Yes! Submit new version with changes noted. Previous versions remain accessible.

**Q: Should I submit to arXiv before journal?**
A: YES. Establishes priority, gets community feedback, standard practice in physics/astro.

**Q: What if someone scoops me?**
A: arXiv timestamp establishes priority. This is why you should submit ASAP.

**Q: Will journal accept after arXiv posting?**
A: Yes, standard practice. Physical Review D, MNRAS, ApJ all accept arXiv preprints.

## Contact for Help

**arXiv support:**
- Email: help@arxiv.org
- Response time: 1-2 business days

**Technical LaTeX help:**
- TeX StackExchange: https://tex.stackexchange.com
- arXiv help pages: https://info.arxiv.org/help/

**Yale resources:**
- Library research support
- Physics department LaTeX workshop
- IT support for technical issues

## Final Checklist Before Submit

- [ ] PDF compiles cleanly (no errors)
- [ ] All 8 figures included as PDF
- [ ] Abstract under 1920 characters
- [ ] References complete and formatted
- [ ] Author information correct
- [ ] Affiliation accurate
- [ ] No plagiarism (all original or cited)
- [ ] No line numbers or drafting marks
- [ ] GitHub repository live with code
- [ ] Tarball created and tested
- [ ] 00README.txt created (optional)
- [ ] Endorsement secured (if needed)

**YOU ARE READY TO SUBMIT!**

---

**Timeline to Publication:**
- January 2: Finish LaTeX conversion ✓
- January 3: Test compilation
- January 4-5: Create submission archive
- January 6: Submit to arXiv
- January 7: Paper posts on arXiv
- January 8: Announce publicly
- January 15: Submit to Physical Review D
- March-June: Peer review process
- July 2026: Publication

**The hard work is done. Now let the world see it.**
