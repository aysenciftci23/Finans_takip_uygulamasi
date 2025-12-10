import requests
from bs4 import BeautifulSoup

def fiyatlari_cek():
    url = "https://www.doviz.com"
    # Siteler bot olduğumuzu anlamasın diye tarayıcı taklidi yapıyoruz.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Hata: Siteye erişilemedi. Kod: {response.status_code}")
            return {}

        soup = BeautifulSoup(response.text, "html.parser")

        # Veriyi güvenli çekmek için yardımcı fonksiyon
        def güvenli_veri_al(key):
            item = soup.find("span", {"data-socket-key": key})
            return item.text if item else "Veri Yok"

        gram_altin = güvenli_veri_al("gram-altin")
        dolar = güvenli_veri_al("USD")
        euro = güvenli_veri_al("EUR")
        sterlin = güvenli_veri_al("GBP")
        gram_gumus = güvenli_veri_al("gumus")

        return {
            "gram_altin": gram_altin,
            "dolar": dolar,
            "euro": euro,
            "sterlin": sterlin,
            "gram_gumus": gram_gumus
        }

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return {}