# Lab 3 demo planı (eğitmen gösterimi, yaklaşık 10 dk)

## Hazırlık (derse girmeden)
1. n8n'de **Gün 5 · Hibrit · Demo verisini sıfırla** akışını aç → **Execute workflow**.
2. **Gün 5 · Hibrit · Finansman Memosu Taslağı** akışının **Aktif** olduğunu kontrol et.
3. Sohbet sayfasını yeni sekmede aç (`Başvuru sohbeti` düğümü → Production URL). Sayfayı yenileme.
4. Dify'da (`http://d33p-th0u6ht.z00`) **Belgeleri Oku** ve **Taslak Memo** uygulamalarını ayrı sekmelerde hazır tut.
5. Hazır PDF'ler: `ornek_basvurular/` altındaki B-2026-101 (Z. Arıkan) ve B-2026-102 (T. Erdem).

## Demo 1: Uygun başvuru (B-2026-101, Z. Arıkan)

**Rolleri tanıt**
1. n8n'de **Gün 5 · Hibrit · Finansman Memosu Taslağı** akışını aç.
2. Renkleri göster: mavi = n8n (otopilot), mor = Dify (yardımcı pilot), turuncu = insan (karar).

**Sohbeti başlat**
3. Sohbet sekmesine geç.
4. Ataç simgesiyle `Basvuru_B-2026-101_Z_Arikan.pdf`'i ekle, bir mesaj yazıp gönder.
5. Sohbette şu mesajlar gelir: "Başvuru alındı", ardından "Belgeler okundu: B-2026-101 · Z. Arıkan".
6. Memo gelir. Göster: politikayla kıyas tablosu, kaynak gösterimleri (örn. Kredi Ürün Kataloğu · Bölüm 4), "Eksikler: yok", son satırdaki "taslaktır, karar içermez" uyarısı.

**Dify'da arkada ne olduğunu göster**
7. Dify → **Belgeleri Oku** → Logs → son çalıştırmayı aç. Adımlar: PDF → Belge metnini çıkar → Alanları çıkar. Çıktıdaki her alanın `deger` ve `guven` değerlerini göster.
8. Dify → **Taslak Memo** → Logs → son çalıştırma. Adımlar: bilgi tabanında iki arama (ürün kuralları, evrak kuralları) → TASLAK memo → eksik belge listesi. Bilgi tabanının "Finansman Politika Dokümanları" olduğunu söyle.

**İnsan kararı**
9. Sohbete dön, **Onaylıyorum**'a bas.
10. Son mesajdaki müşteri taslağını göster. Metin "değerlendirme sürecinde" der ve **gönderilmez**.

**Kaydı göster**
11. n8n → Data tables → **Gün 5 · Hibrit · Başvuru günlüğü**: B-2026-101 satırı. Memo metni ve Analist_karari = Onaylıyorum sütunlarını göster.
12. **Gün 5 · Hibrit · Müşteri taslakları**: durum "Taslak – gönderilmedi".

## Demo 2: Eksikli başvuru (B-2026-102, T. Erdem)

13. Sohbette yeni bir oturum aç (yeni sekme). `Basvuru_B-2026-102_T_Erdem.pdf`'i ekle, gönder.
14. Memoda şunları göster: gelir belgesi 83 gün önce (sınır 30 gün), ekspertiz değeri yok, DASK ve konut sigortası yok. Ekstredeki ortalama bakiye "okunamadı" olarak işaretli.
15. Dify → **Belgeleri Oku** → Logs: ekstre alanındaki `guven` = `okunamadı` değerini göster. Yapay zekâ bilmediğini uydurmuyor, işaretliyor.
16. Sohbette **Düzeltiyorum**'a bas.
17. "Memoda neyin düzeltileceğini yazın" mesajı gelince notu yaz (örn. "Gelir belgesi güncel bordroyla yenilenmeli"). Mesaj gelmeden yazma.
18. Son mesajda müşteri taslağını göster: güncel bordro, DASK, konut sigortası ve okunaklı ekstre istenir. Gönderilmez.
19. Başvuru günlüğünde B-2026-102 satırını aç: `Duzeltilmis_memo` sütununun sonunda "Analist düzeltmesi" olarak not görünür.

## Kapanış mesajı (3 cümle)
- n8n tetikledi, taşıdı, kaydetti.
- Dify okudu, kıyasladı, taslak yazdı.
- Karar yalnızca analistte; müşteriye hiçbir şey otomatik gitmedi.

## Dikkat
- Karar beklerken sohbet sayfasını **yenileme**; oturum kaybolur.
- Her demodan sonra tekrar etmek için **Demo verisini sıfırla** akışını çalıştır.
- Memo biçimi (tablo ya da madde madde) her seferinde biraz değişebilir; sorun değil.
- Sohbet sürümü 22 Ekim'den beri canlı denenmedi varsayımıyla: demodan önce bir kez baştan sona prova yap.
