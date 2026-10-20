#!/usr/bin/env python3
"""n8n akışlarındaki yer tutucuları (__...__) ayarlar.json değerleriyle doldurur.

Kullanım: python3 hazirla.py ayarlar.json
Çıktı  : hazir/ klasörü (n8n'e aktarılacak dosyalar)
"""
import json
import sys
from pathlib import Path

KLASOR = Path(__file__).resolve().parent
ayar = json.loads(Path(sys.argv[1]).read_text(encoding="utf8"))
eksik = [k for k, v in ayar.items() if not v or str(v).startswith("<")]
if eksik:
    sys.exit("Doldurulmamış ayar: " + ", ".join(eksik))
(KLASOR / "hazir").mkdir(exist_ok=True)
for dosya in sorted(KLASOR.glob("*.json")):
    if dosya.name.startswith("ayarlar"):
        continue
    metin = dosya.read_text(encoding="utf8")
    for ad, deger in ayar.items():
        metin = metin.replace("__%s__" % ad, str(deger))
    kalan = [p for p in ("__TABLO", "__DIFY", "__KIMLIK") if p in metin]
    if kalan:
        sys.exit("%s içinde doldurulmamış yer tutucu var: %s" % (dosya.name, kalan))
    (KLASOR / "hazir" / dosya.name).write_text(metin, encoding="utf8")
    print("yazıldı: hazir/" + dosya.name)
