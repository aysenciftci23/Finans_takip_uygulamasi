import asyncio
import websockets
import requests
from bs4 import BeautifulSoup
import json

aktif_kullanicilar = set()



def doviz_verilerini_cekme():
    url = "https://www.doviz.com"
    # Tarayıcı taklidi yapıyoruz (User-Agent)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            print(f"Hata: Siteye erişilemedi. Durum Kodu: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")


        def degerleri_ayikla(key):
            try:

                element = soup.find("span", {"data-socket-key": key})
                if element:
                    text = element.text.strip()

                    text = text.replace(".", "").replace(",", ".")
                    return float(text)
            except Exception as e:
                print(f"Veri işleme hatası ({key}): {e}")
            return 0.0


        usd = degerleri_ayikla("USD")
        eur = degerleri_ayikla("EUR")
        xau = degerleri_ayikla("ons-altin")
        xag = degerleri_ayikla("gumus")


        if xau == 0:
            xau = degerleri_ayikla("gram-altin")

        return {
            "usd_try": usd,
            "eur_try": eur,
            "xau_usd": xau,
            "xag_usd": xag,
        }

    except Exception as e:
        print(f"Genel Hata: {e}")
        return None



async def baglanti_yoneticisi(websocket):
    aktif_kullanicilar.add(websocket)
    print(f"Yeni istemci bağlandı. Toplam: {len(aktif_kullanicilar)}")
    try:
        async for message in websocket:
            pass
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        aktif_kullanicilar.remove(websocket)
        print(f"İstemci ayrıldı. Kalan: {len(aktif_kullanicilar)}")



async def guncel_veri():
    while True:

        data = await asyncio.to_thread(doviz_verilerini_cekme)

        if data and data["usd_try"] > 0:
            print("Güncel Veri:", data)

            if aktif_kullanicilar:
                message = json.dumps(data)

                websockets.broadcast(aktif_kullanicilar, message)
        else:
            print("Veri çekilemedi veya boş, tekrar deneniyor...")

        await asyncio.sleep(5)




async def main():
    async with websockets.serve(baglanti_yoneticisi, "localhost", 8001):
        print("WebSocket Server çalışıyor: ws://localhost:8001")
        await guncel_veri()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Sunucu kapatıldı.")