import pandas as pd
import matplotlib.pyplot as plt

# Veri setini yükle (veri setinin adı 'cern_collision_data.csv' olarak varsayılmıştır)
try:
    df = pd.read_csv('data/MultiJetRun2010B.csv')
except FileNotFoundError:
    print("Hata: 'data/MultiJetRun2010B.csv' dosyası bulunamadı. Lütfen veri setini 'data' klasörüne indirin.")
    exit()

# 'nJets' sütunundaki değerlerin frekansını hesapla
# Bu, basit bir yaklaşımla "parçacık türü" frekansı olarak kabul edilmiştir.
particle_frequency = df['nJets'].value_counts().sort_index()

# Sonuçları görselleştir
plt.figure(figsize=(10, 6))
particle_frequency.plot(kind='bar')
plt.title('Çarpışmalarda Gözlemlenen Jet Sayısı Frekansı')
plt.xlabel('Jet Sayısı (nJets)')
plt.ylabel('Olay Sayısı (Frekans)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('jet_frequency_analysis.png')
plt.show()

print("Analiz tamamlandı. 'jet_frequency_analysis.png' dosyası oluşturuldu.")
