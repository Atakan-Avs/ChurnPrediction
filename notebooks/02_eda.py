import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # görselleri kolaylaştırmak için
from pathlib import Path

#veri yükle
df = pd.read_csv(Path("data/processed/telco_clean.csv"))

print("Şekil:", df.shape)
print("Kolonlar:", df.columns.tolist())
print(df.head(3))

#Hedef (Churn) dağılımı
churn_rate = df["Churn"].mean() * 100
print(f"\nChurn oranı: %{churn_rate:.2f}")

plt.figure()
sns.countplot(data=df, x="Churn")
plt.title("Churn Dağılımı (0=Kaldı, 1=Ayrıldı)")
plt.xlabel("Churn")
plt.ylabel("Adet")
plt.show()

#kategorik-sayısal kolon listeleri
cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
num_cols = df.select_dtypes(include=["int64","float64","int32","float32"]).columns.tolist()
if "Churn" in num_cols:  # hedefi num_cols listesinden çıkar
    num_cols.remove("Churn")

print("\nKategorik kolonlar:", cat_cols)
print("Sayısal kolonlar:", num_cols)


#kontrat tipine göre churn
print("\nKontrat tipine göre churn (%):")
print((df.groupby("Contract")["Churn"].mean()*100).sort_values(ascending=False))

plt.figure()
sns.barplot(data=df, x="Contract", y="Churn")
plt.title("Kontrat Tipine Göre Churn Oranı")
plt.xlabel("Contract")
plt.ylabel("Churn Oranı")
plt.show()

#ödeme yöntemine göre churn
print("\nÖdeme yöntemine göre churn (%):")
print((df.groupby("PaymentMethod")["Churn"].mean()*100).sort_values(ascending=False))

plt.figure()
sns.barplot(data=df, x="PaymentMethod", y="Churn")
plt.title("Ödeme Yöntemine Göre Churn Oranı")
plt.xlabel("PaymentMethod")
plt.ylabel("Churn Oranı")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

#PaperlessBilling etkisi
print("\nPaperlessBilling'e göre churn (%):")
print((df.groupby("PaperlessBilling")["Churn"].mean()*100).sort_values(ascending=False))

plt.figure()
sns.barplot(data=df, x="PaperlessBilling", y="Churn")
plt.title("PaperlessBilling'e Göre Churn Oranı")
plt.xlabel("PaperlessBilling")
plt.ylabel("Churn Oranı")
plt.show()


#aylık ücret montlycharges dagılımı churna göre

plt.figure()
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Aylık Ücret Dağılımı (Churn'a Göre)")
plt.xlabel("Churn")
plt.ylabel("MonthlyCharges")
plt.show()



#tenure (kaç aydır müşteri) churn ilişkisi
plt.figure()
sns.boxplot(data=df, x="Churn", y="tenure")
plt.title("Churn'a Göre Tenure Dağılımı")
plt.xlabel("Churn")
plt.ylabel("tenure (ay)")
plt.show()

#tenure bin'le (daha açıklayıcı)
bins = [0, 6, 12, 24, 48, 72]
labels = ["0-6", "7-12", "13-24", "25-48", "49-72"]
df["tenure_bin"] = pd.cut(df["tenure"], bins=bins, labels=labels, right=True, include_lowest=True)

print("\nTenure aralığına göre churn (%):")
print((df.groupby("tenure_bin")["Churn"].mean()*100).sort_values(ascending=False))

plt.figure()
sns.barplot(data=df, x="tenure_bin", y="Churn", order=labels)
plt.title("Tenure Aralığına Göre Churn Oranı")
plt.xlabel("tenure (ay aralığı)")
plt.ylabel("Churn Oranı")
plt.show()


#sade bir korelasyon ısı haritası (sayısal kolonlar)
import numpy as np

corr = df[["tenure", "MonthlyCharges", "TotalCharges", "Churn"]].corr()
print("\nKorelasyon matrisi:\n", corr)

plt.figure()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Korelasyon Isı Haritası")
plt.show()
