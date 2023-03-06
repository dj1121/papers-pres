from tatoebatools import tatoeba
import pandas as pd
import re


jtexts = [s.text for s in tatoeba.sentences_detailed("jpn")]

df = pd.read_csv ('adjectives.csv', on_bad_lines='skip')
adjectives = list(df["item"])

with open("misa.csv", "w", encoding="utf-8") as f:

    f.write("suffix,prev,word,next,sentence\n")

    i = 1

    for sentence in jtexts:
        print(f"outer loop {i}")
        i += 1
        
        for adj in adjectives:

            
            prev,next,word="","",""
            adj = adj[0:-1]

            
            # sa or mi?
            if f"{adj}さ" in sentence:
                suffix = "さ"

            elif f"{adj}み" in sentence:
                suffix = "み"

            else:
                continue

            # Get previous and next
            try:
                prev = sentence[sentence.find(f'{adj}{suffix}')-2:sentence.find(f'{adj}{suffix}')]
                next = sentence[sentence.find(f'{adj}{suffix}')+2:sentence.find(f'{adj}{suffix}')+4]
            except Exception as e: 
                print(e)


            f.write(f"{suffix},{prev},{adj}{suffix},{next},{sentence}\n")