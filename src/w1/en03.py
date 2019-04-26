import re


li = []

isStarted = False

for i in open("Alice_in_Wonderland.txt"):
    # 本文以外は弾く
    if "START OF THIS PROJECT GUTENBERG EBOOK ALICE IN WONDERLAND" in i:
        isStarted = True
    # 本文終わった
    if isStarted:
        if "END OF THIS PROJECT GUTENBERG EBOOK ALICE IN WONDERLAND" in i:
            break

        s = re.sub("\W\s","",i)
        s = s.lower()
        s = re.sub(re.compile("[^a-z0-9]"), '', s)

        li += s.split()

li2 = set(li)

print(li2)

with open("ans.txt","w") as f:
    li2 = sorted(li2)
    for i in li2:
        f.write(str(i)+"\n")