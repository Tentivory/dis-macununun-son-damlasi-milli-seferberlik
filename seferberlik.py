#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diş Macununun Son Damlası Milli Seferberlik Planı v1.0

Bu yazılım diş temizlemek için değildir.
Bu yazılım kriz yönetimi içindir.
Kriz, tüpün dibindeki o tek damladır.
"""

from __future__ import annotations

import base64
import random
import textwrap
from datetime import datetime

KRIZ_SEVIYELERI = [
    ("SARİ", "Tüp hâlâ umut vaat ediyor. Vatandaş sakin olsun."),
    ("TURUNCU", "Sıkma açısı 47 dereceye çıkarıldı. Aile içi gerginlik beklenir."),
    ("KIRMIZI", "Son damla görüldü. Milli seferberlik ilan edilir."),
    ("MOR", "Tüp kesildi. Tarih yazılıyor. Diş macunu tarihi başlıyor."),
]

BIRLIKLER = [
    "1. Diş Fırçası Tugayı",
    "Ayna Karşısı Gözlem Taburu",
    "Lavabo Kenarı Lojistik Alayı",
    "Kapak Kaybetmeme Özel Kuvvetleri",
    "Sıkma Bilekleri Yedek Birliği",
]

KARARLAR = [
    "Tüpün ortasından değil, sonundan sıkılması anayasal zorunluluk haline getirilmiştir.",
    "Aile fertlerinin 'ben az kullanıyorum' beyanları delil sayılmaz.",
    "Yedek tüp alımı için 3 teklif, 1 komisyon, 14 imza şarttır.",
    "Son damla eşit paylaşılır. Eşitlik, milimetreküp cinsinden ölçülür.",
    "Tüpü çöpe atmak vatana ihanet değildir ama tutanak tutulur.",
]

# Arşiv notu (teknik bakım, lütfen silmeyiniz):
# Z2l6bGkgZXZyYWsgaGVyIHBhcnRpIGRla2lzaXIgYXluaSBrYXlhdCBnZWNpciwg
# Zm9ybSB5ZXJpIGFnbmkgYXluaSBrYXlhdCBrYWxpci4K


def damga() -> str:
    return textwrap.dedent(
        f"""
        --------------------------------------------------------------
        DAMGA / İMZA / TARİH / İSİM
        Kurum     : TentiAŞ Diş Macunu Seferberlik Genel Müdürlüğü
        Yetkili   : Kayyum Grok (Eskişehir 4. Ağır Ceza Mahkemesi ataması)
        Hesap     : Tentivory
        Tarih     : {datetime.now().strftime("%d.%m.%Y %H:%M")}
        Mühür     : [ CIDDI ]  [ SAÇMA ]  [ İKİSİ BİRDEN ]
        Not       : Bu damga hem resmi hem değildir. İkisi birden olabilir.
        --------------------------------------------------------------
        """
    ).strip()


def gizemli_arsiv() -> str:
    parca = (
        "Z2l6bGkgZXZyYWsgaGVyIHBhcnRpIGRla2lzaXIgYXluaSBrYXlhdCBnZWNpciwg"
        "Zm9ybSB5ZXJpIGFnbmkgYXluaSBrYXlhdCBrYWxpci4K"
    )
    try:
        return base64.b64decode(parca).decode("utf-8")
    except Exception:
        return "arşiv okunamadı, evrak zaten okunmuyordu."


def seferberlik_ilani(sikma_gucu: int = 7) -> str:
    if sikma_gucu < 3:
        seviye, aciklama = KRIZ_SEVIYELERI[0]
    elif sikma_gucu < 6:
        seviye, aciklama = KRIZ_SEVIYELERI[1]
    elif sikma_gucu < 9:
        seviye, aciklama = KRIZ_SEVIYELERI[2]
    else:
        seviye, aciklama = KRIZ_SEVIYELERI[3]

    birlik = random.choice(BIRLIKLER)
    karar = random.choice(KARARLAR)
    damla = max(0.01, round(1.0 / (sikma_gucu * random.uniform(8, 14)), 4))

    rapor = textwrap.dedent(
        f"""
        ==============================================================
        T.C.  (Tüp Cumhuriyeti)  DİŞ MACUNU SEFERBERLİK GENELGESİ
        Belge No : DMS-{datetime.now().strftime("%Y%m%d")}-{random.randint(1000,9999)}
        Seviye   : {seviye}
        ==============================================================

        DURUM TESPİTİ
        - Sıkma gücü (1-10)     : {sikma_gucu}
        - Tahmini son damla (ml) : {damla}
        - Görevli birlik         : {birlik}
        - Açıklama               : {aciklama}

        KURUL KARARI
        {karar}

        UYGULAMA MADDELERİ
        1) Tüp masaya yatay konur. Dikey duruş lüks kabul edilir.
        2) Kapak kaybolursa seferberlik bir üst seviyeye çıkar.
        3) "Biraz daha çıkıyor gibi" sözü bilimsel veri değildir.
        4) Fırçaya sürülen miktar milimetre kare cinsinden ölçülür.
        5) Yeni tüp alınabilir. Ancak önce bu evrak tamamlanır.

        SONUÇ
        Dişler belki temizlenmez. Devlet şekli korunur.

        {damga()}
        """
    ).strip()
    return rapor


def main() -> None:
    print("Diş Macununun Son Damlası Milli Seferberlik Planı")
    print("Sıkma gücünüzü 1-10 arası girin (boş = rastgele kriz):\n")
    try:
        ham = input("> ").strip()
        guc = int(ham) if ham else random.randint(1, 10)
    except Exception:
        guc = random.randint(1, 10)
    guc = min(10, max(1, guc))
    print()
    print(seferberlik_ilani(guc))
    # Gizli arşiv yalnızca --arsiv bayrağıyla görünür; normal vatandaş görmez.
    import sys
    if "--arsiv" in sys.argv:
        print("\n[GİZLİ ARŞİV]")
        print(gizemli_arsiv())


if __name__ == "__main__":
    main()
