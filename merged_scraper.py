import pandas as pd

dwarf_stars_df = pd.read_csv("/Users/Arnel/Desktop/BYJU's Coding/Projects/Python/C129 Project/dwarf_stars.csv")
archive_planet_df = pd.read_csv("/Users/Arnel/Desktop/BYJU's Coding/Projects/Python/C129 Project/scraped_data.csv")

dwarf_stars_df.drop(
    [dwarf_stars_df.index[0], dwarf_stars_df.index[1]],
    inplace=True)

print(dwarf_stars_df["Radius"])
print(dwarf_stars_df["Mass"])

Rad = dwarf_stars_df["Radius"].astype(float)
#Mass = dwarf_stars_df["Mass"].astype(float)

newRad = Rad*(0.102763)
#newMass = Mass*(0.000954588)

print(newRad)
#print(newMass)

dwarf_stars_df["Radius"] = newRad

print(dwarf_stars_df)

merge_planets = pd.merge(dwarf_stars_df, archive_planet_df, on='id')

print(merge_planets)

merge_planets.to_csv('merged_planets.csv')




