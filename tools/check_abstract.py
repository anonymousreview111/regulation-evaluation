# Abstract QA: word count (Artificial Intelligence Review caps at 250) + citation check.
import re
t = open('paper/main.tex', encoding='utf-8').read()
m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', t, re.S)
ab = re.sub(r'\\emph\{([^}]*)\}', r'\1', m.group(1))
ab = re.sub(r'\\[a-zA-Z]+\*?', ' ', ab)
ab = re.sub(r'[{}~\\]', ' ', ab)
words = len(ab.split())
print('abstract word count:', words, '(AIRE limit: 250)')
print('within limit:', words <= 250)
print('abstract has citations (should be False):', '\\cite' in m.group(1))
print('abstract has em-dash --- (should be False):', '---' in m.group(1))
