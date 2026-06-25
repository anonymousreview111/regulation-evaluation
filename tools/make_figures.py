import csv, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
import numpy as np
import os
os.makedirs('figures', exist_ok=True)
plt.rcParams.update({'font.size':8,'font.family':'serif','figure.dpi':300})

# ---------- F3 heatmap ----------
rows=list(csv.reader(open('corpus/heat.csv',encoding='utf-8')))
cols=rows[0][1:]
fams=[r[0] for r in rows[1:]]
M=np.array([[int(x) for x in r[1:]] for r in rows[1:]])
famlabel={'M1':'M1 Performance','M2':'M2 Fairness','M3':'M3 Robustness','M4':'M4 Safety',
 'M5':'M5 Red-team','M6':'M6 Interpretability','M7':'M7 Uncertainty','M8':'M8 Data/Docs',
 'M9':'M9 Transparency','M10':'M10 Human oversight','M11':'M11 Monitoring','M12':'M12 Privacy'}
fig,ax=plt.subplots(figsize=(8.2,4.6))
cmap=ListedColormap(['#f2f2f2','#cfe2f3','#6fa8dc','#1c4587'])
im=ax.imshow(M,cmap=cmap,vmin=0,vmax=3,aspect='auto')
ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols,rotation=90,fontsize=7)
ax.set_yticks(range(len(fams))); ax.set_yticklabels([famlabel[f] for f in fams],fontsize=7.5)
# framework group separators
nist=9; eu=7
for x in [nist-0.5, nist+eu-0.5]:
    ax.axvline(x,color='k',lw=1.1)
ax.text(nist/2-0.5,-1.15,'NIST AI RMF',ha='center',fontweight='bold',fontsize=9)
ax.text(nist+eu/2-0.5,-1.15,'EU AI Act',ha='center',fontweight='bold',fontsize=9)
ax.text(nist+eu+ (len(cols)-nist-eu)/2-0.5,-1.15,'ISO/IEC 42001',ha='center',fontweight='bold',fontsize=9)
ax.set_ylim(len(fams)-0.5, -1.6)  # headroom for group labels (no title -> caption covers it)
glyph={3:'●',2:'◐',1:'○',0:''}
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        if M[i,j]>0:
            ax.text(j,i,glyph[M[i,j]],ha='center',va='center',
                    color='white' if M[i,j]==3 else 'black',fontsize=7)
leg=[mpatches.Patch(color='#1c4587',label='Primary'),mpatches.Patch(color='#6fa8dc',label='Supporting'),
     mpatches.Patch(color='#cfe2f3',label='Contextual'),mpatches.Patch(color='#f2f2f2',label='N/A')]
ax.legend(handles=leg,bbox_to_anchor=(1.01,1),loc='upper left',fontsize=7,frameon=False)
plt.tight_layout()
plt.savefig('figures/fig_heatmap.pdf',bbox_inches='tight'); plt.close()
print('wrote figures/fig_heatmap.pdf')

# ---------- F5 gap / maturity ----------
agg=list(csv.DictReader(open('corpus/gap_analysis.csv',encoding='utf-8')))
labels=[f"{r['framework']}:{r['req']}" for r in agg]
heat=[int(r['heat']) for r in agg]
matn={'Broad':'#1c4587','Moderate':'#6fa8dc','Narrow':'#e06666'}
def mcolor(m):
    if m.startswith('Broad'): return '#1c4587'
    if m.startswith('Moderate'): return '#6fa8dc'
    return '#e06666'
colors=[mcolor(r['maturity']) for r in agg]
fig,ax=plt.subplots(figsize=(8.2,3.4))
ax.bar(range(len(labels)),heat,color=colors)
ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels,rotation=90,fontsize=6.5)
ax.set_ylabel('Aggregate relevance score\n(across 12 method families)',fontsize=7.5)
leg=[mpatches.Patch(color='#1c4587',label='Broad'),mpatches.Patch(color='#6fa8dc',label='Moderate'),
     mpatches.Patch(color='#e06666',label='Narrow / gap')]
ax.legend(handles=leg,fontsize=7,frameon=False,ncol=3,loc='upper right')
ax.set_title('Coverage of each requirement by technical evaluation methods',fontsize=9)
plt.tight_layout(); plt.savefig('figures/fig_gap.pdf',bbox_inches='tight'); plt.close()
print('wrote figures/fig_gap.pdf')

# ---------- F1 PRISMA flow ----------
fig,ax=plt.subplots(figsize=(6.4,6.6)); ax.axis('off')
def box(x,y,w,h,txt,fc='#eef3fb'):
    ax.add_patch(mpatches.FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02',
        fc=fc,ec='#1c4587',lw=1.1))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=7.4,wrap=True)
def arrow(x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color='#1c4587',lw=1.1))
ax.set_xlim(0,10); ax.set_ylim(0,11)
box(0.5,9.6,9,1.0,'Identification\nStructured method-family search (n=152 candidates) + separately verified privacy set (n=6);\nreused agent-fairness corpus (n=202) + official regulatory/standards texts (n=6)',fc='#dde8f7')
box(0.5,8.1,9,0.9,'Structured-search records after de-duplication (n=152)\n(reused corpus and official texts handled as separate pools)')
arrow(5,9.6,5,9.0)
box(0.5,6.6,9,0.9,'Screened on title/abstract and full text for technical-method\nrelevance')
arrow(5,8.1,5,7.5)
box(0.5,5.1,9,0.9,'Identifier/citation verification: every candidate checked by arXiv/DOI\nresolution and database cross-check')
arrow(5,6.6,5,6.0)
box(6.6,3.7,2.9,1.0,'Excluded (n=11):\nfabricated / unverifiable (6);\nduplicate (5)',fc='#fbe4e4')
arrow(5,5.1,6.6,4.2)
box(0.5,3.55,5.4,0.95,'Verified method references (n=141)\n(63 confirmed, 78 corrected)')
arrow(5,5.1,3.2,4.5)
box(0.5,1.8,9,1.0,'Full verified corpus (n=355), released as Supplementary Information\n141 search-verified + 6 privacy (M12) method refs + 202 reused fairness + 6 official;\nreference list cites about 180 in narrative; mapped across 12 method families (M1--M12)',fc='#dde8f7')
arrow(3.2,3.55,3.2,2.8)
arrow(5,1.8,5,1.8)
plt.tight_layout(); plt.savefig('figures/fig_prisma.pdf',bbox_inches='tight'); plt.close()
print('wrote figures/fig_prisma.pdf')
