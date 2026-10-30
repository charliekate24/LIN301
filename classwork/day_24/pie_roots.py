import pandas as pd 

root    = ["*bʰer-", "*ĝenh₁-", "*ped-", "*doh₃-"]
meaning = ["to carry", "to beget", "foot", "to give"]
latin   = ["ferō", "gignō", "pēs", "dō"]
greek   = ["pʰérō", "gígnomai", "poús", "dídōmi"]
english = ["bear", "kin", "foot", "donate"]

pie_rows = []

for r, m, l, g, e in zip(root, meaning, latin, greek, english):
    pie_rows.append({
        "root": r,
        "meaning": m,
        "Latin": l,
        "Greek": g,
        "English": e
    })

pie_df = pd.DataFrame(pie_rows)
print(pie_df)

pie_df.to_csv("pie_roots.csv", index=False, encoding="utf-8-sig")

check = pd.read_csv("pie_roots.csv")
print(check)