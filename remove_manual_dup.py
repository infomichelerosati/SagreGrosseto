import csv
with open("sagre.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Filter out the "Sagra del Tortello & Bistecca" in Campagnatico (which is a duplicate of the longer event)
new_lines = []
for line in lines:
    if "Sagra del Tortello & Bistecca,Campagnatico" not in line:
        new_lines.append(line)

with open("sagre.csv", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
