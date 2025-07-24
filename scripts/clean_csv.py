import pandas as pd
import numpy as np
import re

def test():
    file_name = "Sources/bushel_series_DataChallenge_2025-numisdata4-2_TypenEinzeln.csv"
    df = pd.read_csv(file_name, sep=";", encoding="UTF-8")
    
    cols_cleaned = []
    coin_types = [[], []]
    for col in ["Typ_1", "Typ_2", "Typ_3", "Typ_4", "Typ_5", "Typ_6", "Typ_7", "Type | Obverse design", "Type | Reverse design"]:
        new_col = []
        for i, row in enumerate(df.iterrows()):
            new_row_1 = str(row[1][col]).split("|")
            new_row_1 = [x.strip() for x in new_row_1]
            new_col.append(new_row_1)

            if col == "Typ_1":
                coin_type_literal = new_row_1[1]
                coin_types[0].append(coin_type_literal)

                if coin_type_literal == "Uncertain type":
                    coin_type_letter = "Uncertain type"
                else:
                    matches = re.findall(r'[A-H]', coin_type_literal)
                    coin_type_letter = matches[-1] if matches else ""
                    if not matches:
                        coin_type_letter = "Uncertain type"
                        print(f"Row {i}: Coin Type Literal: {coin_type_literal}, Matches: {matches}")

                coin_types[1].append(coin_type_letter)

        cols_cleaned.append(new_col)

    cleaned_df = pd.DataFrame({
        'Id': df['Id'],
        'Typ_1': cols_cleaned[0],
        'Typ_2': cols_cleaned[1],
        'Typ_3': cols_cleaned[2],
        'Typ_4': cols_cleaned[3],
        'Typ_5': cols_cleaned[4],
        'Typ_6': cols_cleaned[5],
        'Typ_7': cols_cleaned[6],
        'Type | Obverse design': cols_cleaned[7],
        'Type | Reverse design': cols_cleaned[8],
        'Collection': df['Collection'],
        'Number': df['Number'],
        'Hoard': df['Hoard'],
        'Findspot': df['Findspot'],
        'Weight': df['Weight'],
        'Diameter max.': df['Diameter max.'],
        'Coin Type': coin_types[0],
        'Coin Type Letter': coin_types[1]
    })

    print(cleaned_df.head())
    cleaned_df.to_csv("cleaned_data.csv", sep=";", encoding="UTF-8", index=False)

if __name__ == "__main__":
    test()
