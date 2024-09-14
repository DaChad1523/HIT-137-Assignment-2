import os, csv
csv_D = r"C:\Users\jimmy\Desktop\github folder\HIT-137-Assignment-2\text.txt"
count = 1

word_count = {}

with open(csv_D, 'r', encoding='utf-8') as txt_file:
    for line in txt_file:
        words = line.split()
        for e in words:
            e = e.lower()
            if e in word_count:
                word_count[e] += 1
            else:
                word_count[e] = 1

for w in sorted(word_count, key=word_count.get, reverse=True):
    if count < 31:
        print(f"{count}:",w, word_count[w])
        count += 1