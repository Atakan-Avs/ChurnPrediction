import pandas as pd
from pathlib import Path
import os



#Dosya yolunu ayarla
csv_path = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

#CSV'yi oku
df = pd.read_csv(csv_path)


#TotalCharges sayısal hale getir
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

#Hatalı olanları NaN at
print("NaN sayısı (TotalCharges):", df["TotalCharges"].isna().sum())
df = df.dropna(subset=["TotalCharges"])


#ilk görüntü
print("Şekil:", df.shape)
print("Kolonlar:", df.columns.tolist())
print(df.head())

#eksik degerr control
print("\nEksik değer sayıları:")
print(df.isna().sum())

#hedef değişkeni (Churn) Yes/No - 1/0 yap
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

#save
out_path = Path("data/processed/telco_clean.csv")
out_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path, index=False)
print("\nTemiz CSV kaydedildi:", out_path.resolve())
df.to_csv("data/processed/telco_clean.csv", index=False)

