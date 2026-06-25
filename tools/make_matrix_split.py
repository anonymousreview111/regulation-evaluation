# Upright, single-column-friendly mapping matrix for the Springer/AIRE build:
# three stacked framework panels (NIST, EU, ISO) so no 90-degree page rotation is needed.
import csv, io

rows = list(csv.DictReader(open('corpus/mapping_matrix.csv', encoding='utf-8')))
FAM = {'M1':'M1 Performance \\& benchmarking','M2':'M2 Fairness \\& bias',
 'M3':'M3 Robustness \\& dist.\\ shift','M4':'M4 Safety','M5':'M5 Red-teaming \\& adversarial',
 'M6':'M6 Interpretability','M7':'M7 Uncertainty \\& calibration','M8':'M8 Data quality/docs',
 'M9':'M9 Transparency \\& model docs','M10':'M10 Human oversight','M11':'M11 Post-deployment monitoring',
 'M12':'M12 Privacy evaluation'}
GLY = {'D':'\\direct','P':'\\partialev','I':'\\indirect','':''}
PANELS = [
 ('NIST AI RMF', [('GV','GOVERN'),('MAP','MAP'),('M2.3','ME 2.3'),('M2.6','ME 2.6'),('M2.7','ME 2.7'),
                  ('M2.9','ME 2.9'),('M2.10','ME 2.10'),('M2.11','ME 2.11'),('MG','MANAGE')]),
 ('EU AI Act (high-risk Articles)', [('A9','Art.\\,9'),('A10','Art.\\,10'),('A11','Art.\\,11'),
                  ('A12','Art.\\,12'),('A13','Art.\\,13'),('A14','Art.\\,14'),('A15','Art.\\,15')]),
 ('ISO/IEC 42001 (Annex A)', [('IA5','A.5'),('IA6','A.6.2.4'),('IA7','A.7'),('IA8','A.8'),
                  ('IA626','A.6.2.6'),('IA10','A.10')]),
]
o = io.StringIO()
o.write('% Upright three-panel mapping matrix (Springer/AIRE; no page rotation). Generated.\n')
o.write('\\begin{table}[!t]\n\\centering\n')
o.write('\\caption{Proposed methods-to-requirements crosswalk (central artifact), shown as three '
        'framework panels for upright reading. Cells record the authors\' interpretive coding of '
        'each method family\'s \\emph{technical relevance}: \\direct~primary, \\partialev~supporting, '
        '\\indirect~contextual; blank = not applicable. The codes are an engineering judgment grounded '
        'in the official clause text, independently sampled by a second coder (Section~\\ref{sec:method}); '
        'they indicate technical relevance, not a legal determination of conformity. NIST AI RMF '
        'functions/subcategories, EU AI Act high-risk Articles, and ISO/IEC~42001 Annex~A controls '
        '(A.5 assessing impacts; A.6.2.4 verification and validation; A.7 data; A.8 information for '
        'interested parties; A.6.2.6 operation and monitoring; A.10 third-party).}\n')
o.write('\\label{tab:matrix}\n\\footnotesize\\setlength{\\tabcolsep}{3pt}\n')
for title, cols in PANELS:
    o.write('\\par\\smallskip\\noindent\\textbf{%s}\\par\\nopagebreak\\smallskip\n' % title)
    o.write('\\begin{tabular}{p{0.30\\textwidth}'+ 'c'*len(cols) +'}\n\\toprule\n')
    o.write('Method family & '+' & '.join('\\rotatebox{90}{%s}'%lbl for _,lbl in cols)+'\\\\\n\\midrule\n')
    by={r['family']:r for r in rows}
    for fid in ['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12']:
        r=by[fid]
        cells=' & '.join(GLY[r[cid]] for cid,_ in cols)
        o.write('%s & %s\\\\\n'%(FAM[fid], cells))
    o.write('\\bottomrule\n\\end{tabular}\n\\par\\smallskip\n')
o.write('\\end{table}\n')
open('paper/tab_matrix_split.tex','w',encoding='utf-8').write(o.getvalue())
print('wrote paper/tab_matrix_split.tex (3 upright panels)')
