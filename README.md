@"
# Telco Customer Churn Prediction

Bu proje, Kaggle Telco Customer Churn verisiyle müşteri kaybını (churn) tahmin eder.
Veri temizleme, EDA, makine öğrenmesi pipeline (OneHotEncoder + StandardScaler), Logistic Regression ve Random Forest modelleri ve özellik önemlerini içerir.

## 🔗 Veri Kaynağı
- Kaggle: Telco Customer Churn (CSV)

## 🗂️ Proje Yapısı
churn-project/
├─ data/
│ ├─ raw/
│ └─ processed/ # telco_clean.csv
├─ notebooks/
│ ├─ 01_load_data.py
│ ├─ 02_eda.py
│ └─ 03_model.py
├─ requirements.txt
└─ README.md

r
Kodu kopyala

## ⚙️ Kurulum
```bash
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
🚀 Çalıştırma
Veri temizleme

bash
Kodu kopyala
python notebooks/01_load_data.py
EDA (grafikler)

bash
Kodu kopyala
python notebooks/02_eda.py
Modelleme (LR & RF, metrikler ve feature importance)

bash
Kodu kopyala
python notebooks/03_model.py
📊 EDA Özet Bulgular
Churn oranı ≈ %26.5

Contract: Month-to-month → en yüksek churn; Two year → en düşük

tenure: düşük olduğunda churn artıyor

MonthlyCharges: yükseldikçe churn artabiliyor

PaymentMethod: Electronic check tarafında churn daha yüksek

🤖 Modeller & Sonuçlar (örnek)
Logistic Regression

Accuracy ≈ 0.79

Churn(1) recall ≈ 0.54

Random Forest

Accuracy ≈ 0.79

Churn(1) recall ≈ 0.50

Not: Bu veri setinde LR ve RF benzer performans verdi. Üretimde recall’un artırılması tercih edilebilir.

⭐ Özellik Önemleri (RF — Top 10)
TotalCharges, tenure, MonthlyCharges, Contract_Month-to-month, Contract_Two year, OnlineSecurity_No, TechSupport_No, PaymentMethod_Electronic check, InternetService_Fiber optic, OnlineBackup_No

🧭 Yorum & Öneriler (iş açısından)
Riskli profil: Aylık sözleşmeli, kısa süreli, yüksek ücretli, “electronic check” ödeme yapan, ek güvenlik/destek hizmeti almayan müşteriler.

Aksiyonlar: Sadakat/indirim kampanyaları, uzun dönem sözleşme teşviki, paket bundle (security/tech support), yüksek faturalılara özel teklif.

🔮 Geliştirme Fikirleri
Sınıf dengesizliği: class_weight / SMOTE

Boosting modeller: XGBoost / LightGBM

Hiperparametre arama: GridSearchCV / RandomizedSearchCV

Eşik ayarı: Recall’u yükseltmek için karar eşiğini optimize etme

Model servisleştirme: Flask/Django API ile canlı tahmin

📝 Lisans
Açık kaynak dataset lisansı Kaggle sayfasından kontrol edilmelidir.
"@ | Out-File -Encoding UTF8 -FilePath README.md

yaml
Kodu kopyala

---

# 2) requirements.txt ve .gitignore oluştur

```powershell
@"
pandas
numpy
scikit-learn
matplotlib
seaborn
"@ | Out-File -Encoding UTF8 -FilePath requirements.txt

@"
venv/
__pycache__/
*.pyc
data/raw/
.ipynb_checkpoints/
.DS_Store
"@ | Out-File -Encoding UTF8 -FilePath .gitignore
