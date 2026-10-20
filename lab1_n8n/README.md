# Lab 1 · n8n: Gelen e-postaları yapay zekâ ile sınıflandırma

Bu laboratuvarda sahte bir gelen kutusuna e-posta gönderir, bir n8n akışının bu e-postaları yapay zekâ ile okuyup sınıflandırmasını ve müşteri için yanıt taslağı yazmasını sağlarsınız. Hiçbir e-posta gerçekten gönderilmez. Tüm veriler hayalidir.

Gereken: n8n 2.36 (Community) ve n8n'de tanımlı bir yapay zekâ modeli credential'ı (OpenAI). Başka bir kurulum ya da bağlantı gerekmez.

## Klasörde ne var?

```
lab1_n8n/
├── tablolar/
│   └── gelen_kutusu.csv                      # 3 örnek e-posta, tek tablo
├── workflows/
│   ├── gun5_mail_gonderme.json               # E-posta yazma formu (dokunmayın)
│   ├── gun5_gelen_kutusu_ekrani.json         # Canlı gelen kutusu sayfası (dokunmayın)
│   ├── gun5_gelen_kutusunu_temizle.json      # Gelen kutusunu boşaltır (dokunmayın)
│   └── gun5_lab1_sablon.json                 # Üzerinde çalışacağınız akış
└── egitmen/                                  # Katılımcılara verilmez, takılanlara yardım için
    ├── gun5_cozum_ana_surec.json             # Tamamlanmış akış
    └── yapay_zeka_promptu.txt                # Çalışan prompt
```

## Kurulum (5 dakika)

**1. Tabloyu oluşturun**
1. n8n'de soldaki menüden **Data tables** sayfasını açın.
2. **Create Data table** → **Import CSV** ile `tablolar/gelen_kutusu.csv` dosyasını seçin.
3. Tablo adını tam olarak şöyle yazın: `Gün 5 · Gelen kutusu` (ortadaki nokta `·` özel bir karakterdir; adı kopyalayıp yapıştırın).
4. Sütun adlarını değiştirmeyin.

**2. Akışları içe aktarın**

*Workflows* sayfasında **Import from File** ile `workflows/` klasöründeki 4 dosyayı tek tek içe aktarın. Her akışta **Save** yapın.

**3. Yapay zekâ modelini seçin**

`Gün 5 · Lab 1 · Şablon` akışını açın, **OpenAI modeli** düğümüne tıklayın ve **Credential** alanından size tanımlanmış olanı seçin.

**4. Mail gönderme ve ekran akışlarını yayınlayın**

`Gün 5 · Mail Gönderme` ve `Gün 5 · Gelen Kutusu Ekranı` akışlarını açın, sağ üstten **Publish** edin. Adresleri akışın ilk düğümünden alırsınız:
- **Mail yazma formu** düğümü → **Production URL** (e-posta yazacağınız sayfa)
- **Sayfa isteği** düğümü → **Production URL** (gelen kutusunu izleyeceğiniz sayfa)

Her iki adresi de tarayıcıda ayrı birer sekmede açın.

## Görev

`Gün 5 · Lab 1 · Şablon` akışını açın.

1. **Eksik 3 bağlantıyı kurun:** `Zamanlayıcı` → `E-postaları oku`, `Yapay zekâ` → `Karar (IF)`, `Karar (IF)` doğru (true) çıkışı → `Eksik evrak olarak kaydet`.
2. **Yapay zekâ düğümünü yazın:** `Yapay zekâ` düğümünü açın. **Sistem mesajı** ve **Prompt** alanlarındaki `<<< ... >>>` satırlarını silip kendi cümlelerinizi yazın. Prompt şunları yaptırmalı:
   - e-postanın kategorisini seçmek (Yeni başvuru, Eksik evrak, Durum sorgusu, Şikâyet),
   - kısa bir özet yazmak,
   - eksik belge varsa adını söylemek,
   - müşteriye gidecek bir yanıt taslağı hazırlamak.

   E-postanın gönderen, konu, ek ve metin alanları promptun altında hazır durur, onlara dokunmayın.
3. **Deneyin:** Mail yazma formundan bir e-posta gönderin (hazır örnek seçebilir ya da kendiniz yazabilirsiniz). Sonra şablonda **Execute workflow**'a basın.
4. **Sonucu görün:** Gelen kutusu sayfasında e-postanız kategori etiketi, özet ve yanıt taslağıyla görünür. `Gün 5 · Gelen kutusu` tablosunda da aynı satırı bulursunuz.
5. Sonuç beklediğiniz gibi değilse promptu değiştirip yeniden deneyin. Yeni bir deneme için formdan yeni bir e-posta gönderebilirsiniz.

Şablonu yayınlarsanız her dakika kendiliğinden çalışır.

## Sık karşılaşılan sorunlar

| Belirti | Çözüm |
|---|---|
| Akış "tablo bulunamadı" hatası veriyor | Tablo adı tam olarak `Gün 5 · Gelen kutusu` olmalı. Ortadaki karakter orta noktadır `·` |
| `Yapay zekâ` düğümünde kırmızı uyarı | `OpenAI modeli` düğümünde credential seçilmemiş |
| Tabloda `Kategori` hücresi `İnceleme gerekli` | Yapay zekâ yanıtı okunamadı. Promptta dört alanı (kategori, özet, eksik belge, yanıt) istediğinizden emin olun |
| E-posta gönderdim ama sonuç gelmiyor | Şablonda **Execute workflow**'a basın. Yayınladıysanız bir dakika bekleyin |
| Yayınlarken "path already in use" benzeri hata | Akışı içe aktardıysanız bu olmamalı. Eğitmene haber verin |
| Gelen kutusu sayfası yenilenmiyor | Tarayıcıda **F5** ile yenileyin |
| Baştan başlamak istiyorum | `Gün 5 · Gelen Kutusunu Temizle` akışında **Execute workflow**. Örnek e-postalar da silinir, formdan yenisini gönderin |

## Eğitmen notları

- **Çözüm ve prompt:** `egitmen/` klasörü katılımcılara verilmez. `gun5_cozum_ana_surec.json` tamamlanmış akıştır, `yapay_zeka_promptu.txt` çalışan sistem mesajı ve promptu içerir (txt'deki ilk bölüm Sistem mesajı, ikinci bölüm Prompt alanıdır). Not: repo herkese açıksa bu klasör de herkese açıktır.
- **Prompt boş gelirse:** Şablonda yer tutucu metin silinmeden çalıştırılırsa model işe yaramayan çıktı üretir ve satır `İnceleme gerekli` olarak yazılır. Bu doğru davranıştır ve iyi bir tartışma konusudur.
- **Aynı n8n'de çok kullanıcı:** Tablolar kullanıcının kendi projesinde olduğu için adları çakışmaz. Mail gönderme ve ekran akışlarında sabit webhook yolu ya da `webhookId` yoktur. n8n 2.36 arayüzden içe aktarırken bunları rastgele üretir (`useWorkflowNormalization.resolveNodeWebhook`, `UPDATE_WEBHOOK_ID_NODE_TYPES`; n8n@2.36.0 kaynağında doğrulandı). API ile içe aktarırsanız her akışa benzersiz `webhookId` ve yol verin. Sabit yol yazmayın. Eğitimden önce iki ayrı kullanıcıyla aynı JSON'u içe aktarıp yayınlayarak ekran adreslerinin farklı olduğunu doğrulayın.
- **Credential:** n8n Community'de kullanıcılar arasında paylaşılmaz. Yapay zekâ modeli credential'ını her kullanıcı için n8n yöneticisi tanımlar.
- **Gerçek posta sistemine geçiş:** Ana süreçte `Yanıtı gönder (Gmail)` düğümü devre dışı yer tutucudur. Gerçek bir eğitim kutusunda yalnızca `E-postaları oku` ve kayıt düğümleri değişir.
- **Sorun giderme gösterimi:** (1) `Yapay zekâ` → `Karar (IF)` bağlantısını koparıp çalıştırın, akış durur. (2) `Kaydet` düğümündeki Kategori ifadesinde `output?.kategori` yerine `output?.Kategori` (büyük K) yazın: satır güncellenir ama Kategori hücresi `İnceleme gerekli` olur. (3) `OpenAI modeli`nden credential'ı kaldırın, düğüm kırmızı olur ve akış başlamaz.
