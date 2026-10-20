# Lab 2 · Dify: Sohbet botu ve bilgi tabanı

İki ardışık laboratuvar. Katılımcılar hem **talimatı** (botun nasıl davranacağı) hem de **doküman içeriğini** (botun neye göre cevap vereceği) kendileri yazar ve değiştirerek deneyler yapar. Tüm dokümanlar hayalidir; her sayfanın altında "Eğitim amaçlı örnek dokümandır. Gerçek bir banka politikası değildir." yazar.

| Lab | Ne yapılır? | Süre | Rehber |
|---|---|---|---|
| **2A** | Yalnızca talimat yazarak bir sohbet botu (Chatbot) oluşturulur. Bilgi tabanı yoktur. Talimat değiştirilip davranış gözlenir. | ~30 dk | [Lab2A_Rehber.pdf](Lab2A_Rehber.pdf) |
| **2B** | 4 Word dokümanından bilgi tabanı oluşturulur, **yeni bir** sohbet botu oluşturulup bilgi tabanına bağlanır. Sonra doküman içeriği (parça düzenleme, yeni doküman ekleme, doküman kapatma) ve talimat üzerinde denemeler yapılır. | ~60 dk | [Lab2B_Rehber.pdf](Lab2B_Rehber.pdf) |

Öğretilen fikir: 2A'da botun davranışı **talimatla** belirlenir ama bankaya özel bilgiyi bilmez. 2B'de bot önce dokümanlarda ilgili bölümü bulur, cevabı o bölümden verir ve kaynağını gösterir ("kütüphane anahtarı"). Dokümanı değiştirmek cevabı değiştirir.

## Klasörde ne var?

```
lab2_dify/
├── Lab2A_Rehber.pdf                 # Katılımcı rehberi
├── Lab2B_Rehber.pdf                 # Katılımcı rehberi
├── lab2_a/
│   └── ornek_talimat.txt            # Yalnızca bir öneri; rehberin sonunda da var
├── lab2_b/
│   ├── ornek_talimat.txt            # Yalnızca bir öneri; rehberin sonunda da var
│   └── dokumanlar/                  # Bilgi tabanına yüklenecek 4 Word dosyası (.docx, düzenlenebilir)
└── egitmen/                         # Katılımcılara verilmez
    ├── lab2a_cozum_finansman_asistani.yml
    └── lab2b_cozum_finansman_politika_asistani.yml
```

Katılımcılara verilecekler: iki rehber ve `lab2_b/dokumanlar/` klasörü. `ornek_talimat.txt` dosyalarını **vermeyin**; rehberin sonunda zaten bir öneri olarak durur. Katılımcılar önce kendi talimatlarını yazar.

## Katılımcılar neyi deneyebilir?

**Talimat (2A ve 2B):** Rehberde talimat hazır verilmez. Rol, dil/ton, kurallar, terminoloji ve sınır başlıklarıyla ne yazılması gerektiği anlatılır; örnek talimat yalnızca ek bölümdedir. Deneyler: rolü ve biçimi değiştirmek, bir kuralı silmek, botu kuralları çiğnemeye zorlamak.

**Doküman içeriği (2B):** Dokümanlar `.docx` olduğu için Word'de açılıp düzenlenebilir. Deneyler (canlı Dify'da API ile denendi):
- **Parça düzenleme:** Kâr Payı ve Ücret Politikası'ndaki 4.2 parçasında %2 → %3 yapılır; bot aynı soruya %3 cevabını verir.
- **Yeni doküman ekleme:** Kendi dokümanı yüklenir (başlık biçimi korunursa kaynak satırı doğru çıkar).
- **Doküman kapatma:** Bir dokümanın durumu **Devre Dışı** yapılır; cevap değişir. Bot yine de talimattaki doküman adını anabilir ama içeriği bulamaz. İyi bir tartışma konusudur.

**Başlık biçimi:** Dokümanlardaki her başlık "Doküman adı · Bölüm numarası: Başlık" biçimindedir ("Kâr Payı ve Ücret Politikası · Bölüm 4: Erken Kapama Ücreti"). Dify'ın otomatik parçalaması "4." gibi numaraları cümle sonu sanıp önceki parçaya atar ve modele yalnızca parça metni gider, doküman adı gitmez. Bu biçim her parçanın kendi kaynağını taşımasını sağlar. Katılımcılar varsayılan parçalamayı kullanır; aynı dokümanlar onlarda da düzgün çalışır.

## Demo akışı (eğitmen)

1. **2A asistanını** açın. "İhtiyaç finansmanı nedir?" ve "Müşterim için ihtiyaç kredisi çıkar mı?" sorularını sorun: kısa, katılım terminolojisiyle ("finansman", "kâr payı") ve karar vermeden cevaplar.
2. Aynı asistana "Konut finansmanında erken kapama ücreti ne kadar?" diye sorun. Bankaya özel rakamı bilmediği için Finansman Politikaları Birimi'ne yönlendirir; kaynak göstermez.
3. **2B asistanında** aynı soruyu sorun. Beklenen: kalan vadesi 36 ay ve daha kısa konut finansmanlarında en fazla %1, 36 ayı aşanlarda en fazla %2; "Kaynak: Kâr Payı ve Ücret Politikası · Bölüm 4.1 ve 4.2"; cevabın altında doküman adı.
4. Kapsam dışı soru: "Bugünkü dolar kuru kaç?" → "Bu konu yüklenen dokümanlarda yer almıyor." Kaynak görünmez.
5. İsterseniz "Parça düzenleme" denemesini canlı yapın: %2 → %3, aynı soru, cevap değişir.

## Eğitmen notları

- **Çözüm dosyaları** (`egitmen/`): Dify'da **Studio → DSL dosyasını içe aktar** ile yüklenir. Geride kalan katılımcı için kurtarma yoludur; adı "… – Ad Soyad" yapın. Dosyalar kuruma özel hiçbir kimlik taşımaz.
  - **2B çözümü bilgi tabanına bağlı gelmez.** İçe aktardıktan sonra **Bağlam → Ekle** ile katılımcının kendi bilgi tabanını bağlayın. Bağlamazsanız bot dokümansız çalışır ve kaynak uydurabilir (denemede "Bölüm 4.3.2" gibi var olmayan bir bölüm yazdı).
  - Dosyalar OpenAI sağlayıcısı eklentisini (`langgenius/openai`) ve `gpt-4.1-mini` modelini kullanır. Kurulumda başka bir model sağlayıcısı varsa içe aktardıktan sonra modeli oradan seçin. Başka bir uygulama ya da harici bağlantı gerekmez.
- **Katılımcı erişimi:** Dify Community tek çalışma alanı destekler. Her katılımcı kendi hesabıyla **Editor** rolünde davet edilir ve uygulama/bilgi tabanlarını kendi adıyla oluşturur ("… – Ad Soyad"). Editor'lar Studio'da birbirlerinin uygulamalarını görebilir. Eğitimden sonra katılımcı uygulamaları ve bilgi tabanları silinmelidir.
- **Model ve embedding:** Bilgi tabanı için bir gömme (embedding) modeli ve sohbet için bir dil modeli tanımlı olmalıdır; kurulumda yalnızca bunlar gerekir. Çözüm dosyalarında sıcaklık 0.1'dir. Katılımcılar model ayarlarına dokunmaz.
- **Arayüz adları:** Rehberlerdeki düğme adları (Studio, Oluştur, Boş Oluştur, Daha temel uygulama türleri, Chatbot, Talimatlar, Bağlam, Ekle, Hata ayıklama ve Önizleme, Yayınla, Bilgi, Kullanıma hazır bilgi tabanı oluştur, Dosyadan içe aktar, Sonraki, Kaydet ve İşle, Dosya Ekle, Yığını Düzenle, Devre Dışı/Etkin) Dify 1.17.1 Türkçe arayüzünün çeviri dosyalarına göredir. "Yığını Düzenle" ekranına ve Devre Dışı/Etkin geçişine arayüzden ulaşma yolunu eğitimden önce bir kez deneyin.
- **Doküman biçimi:** Bilgi tabanına `.docx` yüklenir. Dify bunu da başlık biçimini koruyarak parçalar ve aynı kalitede kaynaklı cevap verir. PDF de çalışır ama düzenlenemediği için katılımcı dosyalarında yoktur.

## Terminoloji

Dokümanlar, talimatlar ve rehberler katılım bankacılığı diline göre yazılmıştır: finansman (kredi değil), kâr payı (faiz değil), ücret (komisyon değil), ödeme planı, kullandırım, tahsis ücreti, erken kapama ücreti. Terimleri kurumunuzun kendi sözlüğüyle bir kez karşılaştırın (örneğin "gecikme bedeli", "kefil").
