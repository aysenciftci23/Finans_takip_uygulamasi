import requests
from bs4 import BeautifulSoup

# Sabit değerleri (Constants) burada tanımlıyoruz.
DOVIZ_URL = "https://www.doviz.com"
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fiyatlari_cek(url=DOVIZ_URL, headers=None):
    """
    Döviz.com sitesinden güncel altın ve döviz fiyatlarını çeker.
    """
    # Eğer özel headers verilmediyse var olanı kullan
    if headers is None:
        headers = DEFAULT_HEADERS

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Hata: Siteye erişilemedi. Kod: {response.status_code}")
            return {}

        soup = BeautifulSoup(response.text, "html.parser")

        # Veriyi güvenli çekmek için yardımcı fonksiyon
        def guvenli_veri_al(key):
            """
            HTML içinden belirli bir data-socket-key değerine sahip veriyi bulur.
            """
            item = soup.find("span", {"data-socket-key": key})
            return item.text if item else "Veri Yok"

        gram_altin = guvenli_veri_al("gram-altin")
        dolar = guvenli_veri_al("USD")
        euro = guvenli_veri_al("EUR")
        sterlin = guvenli_veri_al("GBP")
        gram_gumus = guvenli_veri_al("gumus")

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