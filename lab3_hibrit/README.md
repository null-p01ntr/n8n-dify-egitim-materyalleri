# Lab 3 · Hibrit demo: n8n + Dify ile finansman memosu taslağı

Katılımcıların kurmadığı, eğitmenin çalışan sistem üzerinden gösterdiği demo. Kurulum dosyaları bu klasördedir. Tüm veriler hayalidir.

**Roller:** n8n tetikler, taşır, kaydeder. Dify okur, kıyaslar, yazar. Karar yalnızca analisttedir; hiçbir adım otomatik onay vermez ve müşteriye hiçbir şey gönderilmez.

**Akış:** Analist başvuru PDF'ini n8n'in sohbet ekranına ekler → n8n dosyayı Dify'a yükler → Dify "Belgeleri Oku" alanları çıkarır → Dify "Taslak Memo" politika bilgi tabanıyla kıyaslayıp taslak memo yazar → memo sohbette gösterilir, analist **Onaylıyorum** ya da **Düzeltiyorum** der (düzeltmede notunu sohbete yazar) → n8n müşteri e-postasını **taslak** olarak hazırlar ve sohbette gösterir. Tüm kayıtlar iki n8n data table'ında tutulur.

## Klasörde ne var?

```
lab3_hibrit/
├── n8n/
│   ├── hibrit_finansman_memosu_taslagi.json   # Ana akış (sohbet arayüzlü)
│   ├── hibrit_demo_verisini_sifirla.json      # Demodan önce iki tabloyu boşaltır
│   ├── ayarlar.ornek.json                     # Doldurulacak değerler
│   └── hazirla.py                             # Yer tutucuları ayarlarla doldurur → hazir/
├── dify/
│   ├── belgeleri_oku.yml                      # Dify iş akışı: PDF → alanlar (JSON)
│   └── taslak_memo.yml                        # Dify iş akışı: alanlar + politika → taslak memo
├── tablolar/
│   ├── basvuru_gunlugu.csv                    # n8n data table: Gün 5 · Hibrit · Başvuru günlüğü
│   └── musteri_taslaklari.csv                 # n8n data table: Gün 5 · Hibrit · Müşteri taslakları
└── ornek_basvurular/                          # 2 hayali başvuru paketi (PDF)
```

Politika bilgi tabanı için Lab 2'deki dokümanlar kullanılır: [`../lab2_dify/lab2_b/dokumanlar/`](../lab2_dify/lab2_b/dokumanlar) (bilgi tabanı adı: Finansman Politika Dokümanları).

## Gerekenler

Drive ya da Telegram gerekmez. Yalnızca:
- **Dify:** bir dil modeli (OpenAI) ve bilgi tabanı için bir embedding modeli.
- **n8n:** iki Header Auth credential'ı (`Authorization: Bearer <Dify uygulama API anahtarı>`): biri "Belgeleri Oku", biri "Taslak Memo" uygulaması için. Credential adları: `Dify · Belgeleri Oku (API)` ve `Dify · Taslak Memo (API)`.

## Kurulum özeti

1. **Dify:** Bilgi tabanını oluşturun (yukarıdaki 4 doküman). `dify/` içindeki iki DSL'i içe aktarın. `taslak_memo.yml` içindeki iki **bilgi alma** düğümünde bilgi tabanını seçin. İki uygulamayı yayınlayın ve her birinden bir API anahtarı alın.
2. **n8n tabloları:** `tablolar/` içindeki iki CSV'den data table oluşturun. Tablo adları şu olmalı: `Gün 5 · Hibrit · Başvuru günlüğü` ve `Gün 5 · Hibrit · Müşteri taslakları`.
3. **n8n credential'ları:** Yukarıdaki iki Header Auth credential'ını oluşturun.
4. **Akışlar:** `ayarlar.ornek.json` dosyasını `ayarlar.json` olarak kopyalayıp doldurun (tablo ve credential kimlikleri, Dify adresi `http://<dify-adresi>/v1`), `python3 hazirla.py ayarlar.json` çalıştırın, `hazir/` içindeki iki JSON'u n8n'e aktarın. Ana akışı yayınlayın (sohbet adresi **Başvuru sohbeti** düğümündeki **Chat URL** olur).

## Demo

1. `Gün 5 · Hibrit · Demo verisini sıfırla` akışını çalıştırın (CSV'lerdeki örnek satırları da siler).
2. Sohbet adresini açın. Ataç simgesiyle `ornek_basvurular/` içinden bir PDF ekleyip gönderin.
3. Sohbette adım adım ilerlemeyi izleyin: belgeler okunuyor → memo yazılıyor → memo ve karar düğmeleri.
4. **Onaylıyorum** ya da **Düzeltiyorum**'u seçin (düzeltmede notu sohbete yazın). Sohbet müşteri e-posta taslağını gösterir.
5. İki tabloyu gösterin (memo metni ve düzeltilmiş memo günlük tablosundadır).

Örnek paketler: **B-2026-101 · Z. Arıkan** politikaya uygun konut finansmanı; **B-2026-102 · T. Erdem** eksikli (gelir belgesi 30 günden eski, ekspertiz/DASK/sigorta yok, ekstrede ortalama bakiye okunamıyor).

## Notlar

- Sohbet sayfası herkese açık yayınlanır (kimlik doğrulama yok). Demo ortamında kullanın; Chat Trigger'a kimlik doğrulama eklenebilir.
- Karar düğmeleri tarayıcıda çalışır; bot kullanıcı aracılarıyla (ör. curl) tıklanmış sayılmaz.
- Onay beklerken sohbet sekmesini kapatırsanız akış beklemede kalabilir; sohbeti yeniden başlatın.
- Dify belge okuma metin tabanlı PDF'lerde çalışır; taranmış PDF için OCR gerekir.
- Dify iş akışları OpenAI sağlayıcısı eklentisini ve `gpt-4.1-mini` modelini kullanır; farklı bir sağlayıcıda modeli iki iş akışında yeniden seçin.
- Dify'da Taslak Memo katılım bankacılığı terimlerini (finansman, kâr payı, ücret) kullanması için yönlendirilmiştir.
