import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import numpy as np

#veri yükle 
df = pd.read_csv(Path("data/processed/telco_clean.csv"))

#hedef ve özellikler ayırma
X = df.drop(columns=["Churn", "customerID"])  
y = df["Churn"]


# kategori ve sayısal kolonları ayırma
cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

# Eğer TotalCharges yanlışlıkla kategorik görünüyorsa -> num_cols içine ekle
if "TotalCharges" in cat_cols:
    cat_cols.remove("TotalCharges")
    num_cols.append("TotalCharges")



#ön işleme : kategorik = one-hot, sayısal = StandardScaler
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', StandardScaler(), num_cols)
    ]
)

#pipeline oluşturma : önce processing sonra logistic regression
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=200,      # ağaç sayısı
        max_depth=None,       # derinlik sınırsız
        class_weight="balanced", # churn=1’i daha önemseyelim
        random_state=42
    ))
])

#egitim / test ayırma
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

#model eğitimi
model.fit(X_train, y_train)

#tahmin
y_pred = model.predict(X_test)

#değerlendirme
print('Accuracy:', accuracy_score(y_test, y_pred))
print('\nClassification Report:\n', classification_report(y_test, y_pred))

#confusion matrix görselleştirme
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm , annot=True , fmt='d', cmap='Blues',
            xticklabels=['No Churn', 'Churn'],
            yticklabels=['No Churn', 'Churn'])

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


# 11) Özellik isimlerini çıkar (OneHotEncoder sonrası genişlediği için)
# Pipeline içinden erişelim
ohe = model.named_steps["preprocessor"].named_transformers_["cat"]
cat_features = ohe.get_feature_names_out(cat_cols)
all_features = np.concatenate([cat_features, num_cols])

# RandomForest modelini çek
rf = model.named_steps["classifier"]

# Önem değerleri
importances = rf.feature_importances_

# DataFrame'e dökelim
feat_imp = pd.DataFrame({
    "Feature": all_features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print("\nEn önemli ilk 10 özellik:")
print(feat_imp.head(10))

# Görselleştirme
plt.figure(figsize=(10,6))
sns.barplot(data=feat_imp.head(10), x="Importance", y="Feature", palette="viridis")
plt.title("Random Forest Feature Importances (Top 10)")
plt.show()