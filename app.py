import asyncio
import websockets
import asyncio
import websockets
import json
from Doviz import fiyatlari_cek

# Sabit Değerler (Constants)
SERVER_HOST = "localhost"
SERVER_PORT = 8001

aktif_kullanicilar = set()


def veri_donustur(ham_veri):
    """
    Doviz.py'den gelen veriyi frontend'in beklediği formata dönüştürür.
    """
    if not ham_veri:
        return None

    return {
        "usd_try": ham_veri.get("dolar", 0),
        "eur_try": ham_veri.get("euro", 0),
        "xau_usd": ham_veri.get("gram_altin", 0), # Frontend 'xau_usd' bekliyor ama Doviz.py 'gram_altin' dönüyor
        "xag_usd": ham_veri.get("gram_gumus", 0),
    }

# Eski 'doviz_verilerini_cekme' fonksiyonunu sildik, yerine Doviz.py kullanacağız.



async def baglanti_yoneticisi(websocket):
    """
    Yeni gelen WebSocket bağlantılarını yönetir.
    Bağlanan istemciyi listeye ekler, bağlantı kopunca listeden çıkarır.
    """
    aktif_kullanicilar.add(websocket)
    print(f"Yeni istemci bağlandı. Toplam: {len(aktif_kullanicilar)}")
    try:
        async for message in websocket:
            pass  # Şu an için istemciden gelen mesajları işlemiyoruz, sadece dinliyoruz.
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        aktif_kullanicilar.remove(websocket)
        print(f"İstemci ayrıldı. Kalan: {len(aktif_kullanicilar)}")


async def guncel_veri():
    """
    Belirli aralıklarla döviz verilerini çeker ve bağlı olan tüm istemcilere gönderir.
    """
    while True:
        # Veri çekme işlemini (blocking I/O) thread içinde çalıştırarak ana döngüyü bloklamıyoruz.
        raw_data = await asyncio.to_thread(fiyatlari_cek)
        data = veri_donustur(raw_data)

        if data and data["usd_try"] > 0:
            print("Güncel Veri:", data)

            if aktif_kullanicilar:
                message = json.dumps(data)
                websockets.broadcast(aktif_kullanicilar, message)
        else:
            print("Veri çekilemedi veya boş, tekrar deneniyor...")

        await asyncio.sleep(5)  # 5 saniye bekle


async def main():
    """
    Uygulamanın ana giriş noktası. WebSocket sunucusunu başlatır.
    """
    print(f"WebSocket Server başlatılıyor: ws://{SERVER_HOST}:{SERVER_PORT}")
    async with websockets.serve(baglanti_yoneticisi, SERVER_HOST, SERVER_PORT):
        print(f"Sunucu aktif ve dinleniyor...")
        await guncel_veri()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Sunucu kapatıldı.")