import MeCab
import numpy as np
from tqdm import tqdm


mecab = MeCab.Tagger("-Ochasen")

text = open('jawiki_small.txt').readlines()
text = [s.strip() for s in text]

tab_all = []
for t in tqdm(text):
    strs = mecab.parse(t).split("\n")
    table = [s.split() for s in strs]
    table = [row[:4] for row in table if len(row) >= 4]
    if len(table) == 0:
        continue
    tab = np.array(table)
    tab_all += tab[:,[0,3]].tolist()

tab_all = np.array(tab_all)

print(tab_all.shape)