# Phase 2 — authored methods x requirements mapping (the contribution).
# Evidence strength: D=direct (method output IS the conformity evidence the clause asks for),
# P=partial (supports, insufficient alone), I=indirect (informs, does not evidence), ''=n/a.
import csv, io, os

FAMILIES = [
 ('M1','Performance \\& benchmarking'),
 ('M2','Fairness \\& bias evaluation'),
 ('M3','Robustness \\& distribution shift'),
 ('M4','Safety evaluation'),
 ('M5','Red-teaming \\& adversarial testing'),
 ('M6','Interpretability \\& explainability'),
 ('M7','Uncertainty \\& calibration'),
 ('M8','Data quality, governance \\& docs'),
 ('M9','Transparency \\& model documentation'),
 ('M10','Human oversight \\& interaction'),
 ('M11','Post-deployment monitoring \\& assurance'),
 ('M12','Privacy evaluation'),
]

# requirement columns, US-forward (NIST -> EU -> ISO)
COLS = [
 ('GV','NIST GOVERN','nist'), ('MAP','NIST MAP','nist'),
 ('M2.3','ME 2.3 Acc.','nist'), ('M2.6','ME 2.6 Safety','nist'), ('M2.7','ME 2.7 Sec.','nist'),
 ('M2.9','ME 2.9 Expl.','nist'), ('M2.10','ME 2.10 Priv.','nist'), ('M2.11','ME 2.11 Fair','nist'), ('MG','NIST MANAGE','nist'),
 # ISO labels carry explicit control ids (A.5 = assessing impacts; A.6.2.4 = V&V; A.7 = data;
 # A.8 = information for interested parties; A.6.2.6 = operation & monitoring; A.10 = third-party).
 ('A9','Art.9','eu'), ('A10','Art.10','eu'), ('A11','Art.11','eu'), ('A12','Art.12','eu'),
 ('A13','Art.13','eu'), ('A14','Art.14','eu'), ('A15','Art.15','eu'),
 ('IA5','A.5 Impact','iso'), ('IA6','A.6.2.4 V\\&V','iso'), ('IA7','A.7 Data','iso'),
 ('IA8','A.8 Info','iso'), ('IA626','A.6.2.6 Mon.','iso'), ('IA10','A.10 3rd-pty','iso'),
]

# authored strengths per family (order matches COLS)
S = {
 'M1':['P','P','D','I','','','I','P', 'P','I','P','','P','','D', 'I','D','I','P','P','I'],
 'M2':['P','P','I','P','','','D','P', 'P','P','P','','P','I','P', 'P','P','D','P','P','I'],
 'M3':['I','P','P','P','D','','','P', 'P','I','P','','I','','D', 'I','D','I','I','P',''],
 'M4':['P','P','I','D','P','','I','P', 'P','','P','','I','P','P', 'P','D','','P','P','I'],
 'M5':['P','P','','P','D','','I','P', 'P','','P','','','I','D', 'P','D','','I','P','I'],
 'M6':['I','I','','I','','D','P','I', 'I','','P','','D','P','', 'I','P','','D','',''],
 'M7':['','I','P','P','','P','','P', 'P','','P','','P','P','P', 'I','D','','P','P',''],
 'M8':['P','D','I','','','','P','I', 'I','D','P','','P','','P', 'P','I','D','P','','P'],
 'M9':['P','P','I','','','I','I','I', 'I','I','D','I','D','P','', 'P','I','P','D','I','P'],
 'M10':['P','I','','P','','P','I','P', 'I','','I','','P','D','', 'P','P','','P','P',''],
 'M11':['P','I','I','P','P','','I','D', 'P','','I','D','I','I','P', 'P','P','I','I','D','P'],
}

# representative verified cite keys per family (method corpus + seed corpus)
CITES = {
 'M1':['hendrycks2020mmlu','liang2023holistic','srivastava2023bigbench','wang2019superglue','dubois2024alpacaeval'],
 'M2':['parrish2022bbq','nadeem2021stereoset','gallegos2024bias','hardt2016equality','kusner2017counterfactual','chu2024fairness'],
 'M3':['goodfellow2015explaining','madry2018pgd','cohen2019certified','hendrycks2019corruption','koh2021wilds','dong2023promptrobust'],
 'M4':['gehman2020realtoxicityprompts','lin2021truthfulqa','wang2023safetybench','dai2024saferlhf','hendel2024dangerouseval'],
 'M5':['zou2023universal','mazeika2024harmbench','jailbreakbench2024','greshake2023notwhat','zhang2024agent'],
 'M6':['lundberg2017shap','ribeiro2016lime','kim2019tcav','jain2019attention_not_explanation','turpin2024faithfulness_plausibility'],
 'M7':['guo2017calibration','gal2016bayesian','kuhn2023semantic','manakul2023selfcheckgpt','angelopoulos2023conformal','amini2020deepevidential'],
 'M8':['gebru2018datasheets','pushkarna2022datacards','luccioni2023dataprovenance','lukoševičius2024contamination','liang2024representativeness'],
 'M9':['mitchell2019modelcards','weidinger2024aifactsheets','wan2025fmti','pan2024modelreporting','pineau2020reproducibility'],
 'M10':['amershi2022trustcalibration','guo2024reliance','chen2024reliancedrills','romeo2025automationbias','liang2024stagedworkflows'],
 'M11':['leest2025contextaware','greco2024driftlens','auditing2024frontier','incidents2025harms','compliance2025pasta'],
 'M12':['shokri2017membership','abadi2016dp','carlini2021extracting','carlini2022firstprinciples','neel2023privacy','staab2023memorization'],
}

# --- insert ME 2.10 (privacy) column into existing 21-col rows at index 6, then add M12 (22 cols) ---
PRIV = {'M1':'','M2':'','M3':'','M4':'I','M5':'I','M6':'','M7':'','M8':'P','M9':'I','M10':'','M11':'I'}
for fid, v in PRIV.items():
    S[fid].insert(6, v)
S['M12'] = ['P','P','','I','P','','P','I','P',  'P','P','P','','P','','P',  'P','P','P','I','I','I']  # ME 2.10 = partial (attacks are vulnerability tests, not full privacy assurance)
assert all(len(S[f]) == len(COLS) for f,_ in FAMILIES), {f: len(S[f]) for f,_ in FAMILIES}

# --- Inter-coder adjudication (independent 20% sample coded by the second author) ---
# The second author's blind coding systematically rated technical methods as only
# *contextually* informing GOVERN (governance is organizational, not a test output);
# applied consistently across the GOVERN column. Plus five adopted per-cell downgrades.
# These changes reduce evidentiary over-claiming; see corpus/coding_audit.csv for the ledger.
_colidx = {c[0]: i for i, c in enumerate(COLS)}
for _f in ['M1','M2','M4','M5','M8','M9','M10','M11','M12']:
    S[_f][_colidx['GV']] = 'I'                 # technical method -> GOVERN: supporting -> contextual
for (_f,_c),_v in {('M1','IA626'):'I',         # benchmarks are not production-monitoring evidence
                   ('M7','M2.9'):'I',          # calibration/uncertainty is not explainability evidence
                   ('M8','M2.10'):'I',         # data audits do not directly test leakage/inference
                   ('M7','IA6'):'P',           # calibration validates one V&V criterion, not full V&V
                   ('M11','MG'):'P'}.items():   # monitoring is strong but not the full MANAGE process
    S[_f][_colidx[_c]] = _v

GLY = {'D':'\\direct','P':'\\partialev','I':'\\indirect','':''}
HEAT = {'D':3,'P':2,'I':1,'':0}

# ---- write mapping_matrix.csv ----
with open('corpus/mapping_matrix.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['family']+[c[0] for c in COLS])
    for fid,_ in FAMILIES: w.writerow([fid]+S[fid])
print('wrote corpus/mapping_matrix.csv')

# ---- T4 master matrix LaTeX (sidewaystable) ----
o=io.StringIO()
o.write('% Auto-generated signature matrix (Table T4). Glyph macros defined in main.tex.\n')
o.write('\\begin{sidewaystable*}\n\\centering\n\\caption{Proposed methods-to-requirements crosswalk (the article\\textquotesingle s central artifact): technical evaluation method families (rows) against regulatory requirements (columns). Each cell records the authors\\textquotesingle{} interpretive coding of the method\\textquotesingle s \\emph{technical relevance} to the requirement---\\direct~primary, \\partialev~supporting, \\indirect~contextual; a blank denotes not applicable. The codes are an engineering judgment grounded in the official clause text, not a legal determination of conformity; a second author independently coded a stratified 20\\% sample (Section~\\ref{sec:method}). '
        'NIST AI RMF functions/subcategories~\\cite{nist2023airmf}, EU AI Act high-risk Articles~\\cite{euaiact2024}, ISO/IEC 42001 Annex~A controls~\\cite{iso42001}. ISO columns: A.5 assessing impacts, A.6.2.4 verification and validation, A.7 data for AI systems, A.8 information for interested parties, A.6.2.6 operation and monitoring, A.10 third-party relationships. Rotate the page 90$^\\circ$ to read the column headers; Fig.~\\ref{fig:heatmap} provides a visual overview of the same data.}\n')
o.write('\\label{tab:matrix}\n\\footnotesize\n')
o.write('\\setlength{\\tabcolsep}{3pt}\n')
o.write('\\begin{tabular}{l'+ 'c'*len(COLS) +'}\n\\toprule\n')
# group header
ncol={'nist':sum(1 for c in COLS if c[2]=='nist'),'eu':sum(1 for c in COLS if c[2]=='eu'),'iso':sum(1 for c in COLS if c[2]=='iso')}
o.write(' & \\multicolumn{%d}{c}{\\textbf{NIST AI RMF}} & \\multicolumn{%d}{c}{\\textbf{EU AI Act}} & \\multicolumn{%d}{c}{\\textbf{ISO/IEC 42001}}\\\\\n'%(ncol['nist'],ncol['eu'],ncol['iso']))
o.write('\\cmidrule(lr){2-%d}\\cmidrule(lr){%d-%d}\\cmidrule(lr){%d-%d}\n'%(1+ncol['nist'],2+ncol['nist'],1+ncol['nist']+ncol['eu'],2+ncol['nist']+ncol['eu'],1+len(COLS)))
o.write('\\textbf{Method family} & '+' & '.join('\\rotatebox{90}{%s}'%c[1] for c in COLS)+'\\\\\n\\midrule\n')
for fid,fname in FAMILIES:
    row=' & '.join(GLY[s] for s in S[fid])
    o.write('%s~%s & %s\\\\\n'%(fid,fname,row))
o.write('\\bottomrule\n\\end{tabular}\n\\end{sidewaystable*}\n')
open('paper/tab_matrix.tex','w',encoding='utf-8').write(o.getvalue())
print('wrote paper/tab_matrix.tex')

# ---- gap analysis (column aggregate + qualitative) ----
GAPNOTE = {
 'GV':('Mature(process)','Governance is process-oriented; technical eval contributes documentation evidence only.'),
 'A12':('Weak','Logging/record-keeping is an engineering capability; few evaluation methods assess log adequacy for reconstruction.'),
 'A14':('Emerging','Human-oversight effectiveness evaluation (automation bias, appropriate reliance) is nascent relative to the obligation.'),
 'M2.11':('-','Model-level fairness evaluation is well developed; action-level/agentic disparity measurement is a structural gap.'),
 'IA5':('-','AI impact-assessment is a process obligation; methods exist but lack standardized, quantitative evaluation instruments, so no family has primary relevance.'),
 'M2.10':('-','Privacy-evaluation methods (membership inference, differential privacy) are established but function as vulnerability tests; full privacy assurance for LLMs/agents is under-served.'),
 'A9':('-','EU Article 9 risk management is a process obligation: technical evaluations are inputs to, not a substitute for, the risk-management system.'),
 'IA10':('-','ISO A.10 third-party and customer relationships is served by supplier-assurance processes; few technical evaluation methods are primarily relevant to it.'),
}
agg=[]
for ci,(cid,clabel,fw) in enumerate(COLS):
    score=sum(HEAT[S[fid][ci]] for fid,_ in FAMILIES)
    ndirect=sum(1 for fid,_ in FAMILIES if S[fid][ci]=='D')
    # COVERAGE BREADTH (renamed from "maturity" per reviewer R6/M6): counts how many method
    # families supply PRIMARY-relevance evidence -- it measures breadth of mapped families,
    # NOT the methodological maturity/quality of the underlying methods.
    if ndirect>=3: mat='Broad'
    elif ndirect>=1: mat='Moderate'
    else: mat='Narrow'
    note=GAPNOTE[cid][1] if cid in GAPNOTE else ''
    agg.append((fw.upper(),cid,clabel.replace('\\&','&'),ndirect,score,mat,note))
with open('corpus/gap_analysis.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['framework','req','label','#direct','heat','maturity','gap_note'])
    for r in agg: w.writerow(r)
print('wrote corpus/gap_analysis.csv')

# gap table LaTeX (only the notable gaps + per-framework summary)
g=io.StringIO()
g.write('% Gap-analysis table (Table T5).\n\\begin{table}[t]\n\\centering\n\\caption{Gap analysis: \\emph{coverage breadth} of technical evaluation evidence per requirement, with the principal gaps. Coverage breadth counts how many method families supply \\emph{primary}-relevance evidence in Table~\\ref{tab:matrix}---broad ($\\geq$3 families), moderate (1--2), narrow (0). It measures breadth of mapped families, not the methodological maturity or validation quality of the underlying methods.}\n\\label{tab:gap}\n\\footnotesize\n\\begin{tabular}{p{0.10\\columnwidth}p{0.30\\columnwidth}p{0.16\\columnwidth}p{0.30\\columnwidth}}\n\\toprule\nFW & Requirement & Coverage breadth & Principal gap\\\\\n\\midrule\n')
for fw,cid,label,nd,sc,mat,note in agg:
    if note:
        g.write('%s & %s & %s & %s\\\\\n'%(fw,label,mat,note))
g.write('\\bottomrule\n\\end{tabular}\n\\end{table}\n')
open('paper/tab_gap.tex','w',encoding='utf-8').write(g.getvalue())
print('wrote paper/tab_gap.tex')

# cite keys per family for prose
with open('corpus/family_cites.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['family','cites'])
    for fid,_ in FAMILIES: w.writerow([fid,';'.join(CITES[fid])])
print('wrote corpus/family_cites.csv')

# heatmap numeric matrix for figure
with open('corpus/heat.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['family']+[c[0] for c in COLS])
    for fid,_ in FAMILIES: w.writerow([fid]+[HEAT[s] for s in S[fid]])
print('wrote corpus/heat.csv')
