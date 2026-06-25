import re
aux = open('paper/main.aux', encoding='utf-8').read()
keys = set()
for c in re.findall(r'\\citation\{([^}]+)\}', aux):
    for k in c.split(','):
        keys.add(k.strip())
keys.discard('IEEEtran')
bib = set(re.findall(r'@\w+\{([^,]+),', open('references.bib', encoding='utf-8').read()))
missing = keys - bib
print('distinct cited keys:', len(keys))
print('cited keys NOT in references.bib:', sorted(missing) if missing else 'NONE')
# Keys dropped during verification (fabricated/unverifiable or superseded by a salvaged
# entry under a different key). NOTE: pineau2020reproducibility is NOT here — it was
# salvaged with the correct id 2003.12206 and is a valid cited entry.
rejected = {'weidinger2024hitlvsjudge','iso2023management','iso420012023mgmt','arabellidistribution',
 'adaptive2024randomized','backdoor2024survey','goodfellow2014fgsm','amini2020deep','greshake2023not',
 'evaleyev2023alpaca','srivastava2022bigbench','rudinger2018winobias'}
leaked = keys & rejected
print('rejected/superseded keys leaked into citations:', sorted(leaked) if leaked else 'NONE')
print('total bib entries:', len(bib), '| cited:', len(keys), '| uncited (available depth):', len(bib) - len(keys))
