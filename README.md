# Finans Takip Uygulaması

Bu proje, güncel döviz ve altın fiyatlarını web kazıma (web scraping) yöntemiyle çekip kullanıcıya sunan basit bir finans takip uygulamasıdır. Backend kısmı Python ile yazılmış olup, veriler WebSocket üzerinden anlık olarak sunulmaktadır.

Proje kapsamında temel web kazıma teknikleri, WebSocket kullanımı, HTTP istekleri ve HTML parse etme işlemleri gösterilmektedir.

## 🎯 Proje Amacı

- Web kazıma mantığını kavratmak
- `requests` ve `BeautifulSoup` kütüphanelerinin kullanımını öğrenmek
- WebSockets ile anlık veri iletimini anlamak
- Gerçek bir web sitesinden veri çekip işlemeyi uygulamak

## 🛠 Kullanılan Teknolojiler

*   **Python 3.x**: Ana programlama dili
*   **Requests**: Web sitesine HTTP isteği atmak için
*   **BeautifulSoup4**: HTML içeriğini parçalayıp (parse) veri almak için
*   **Websockets**: Anlık veri akışı sağlamak için
*   **HTML/CSS/JS**: Verileri görselleştirmek için (Dashboard)

## 📋 Gereksinimler

Projenin çalışması için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:
*   websockets
*   requests
*   beautifulsoup4
*   websocket-client

**Kurulum:**
Terminalde proje dizinine gidip şu komutu çalıştırarak tüm gereksinimleri yükleyebilirsiniz:

```bash
pip install -r requirements.txt
```

## � Nasıl Çalışır?

`app.py` dosyası arka planda sürekli çalışarak `doviz.com` adresinden güncel verileri çeker (Altın, Dolar, Euro vb.). Bu verileri WebSocket protokolü üzerinden (`ws://localhost:8001`) kendisine bağlanan istemcilere anlık olarak iletir.

### Çalıştırma Adımları

**1. Sunucuyu Başlatın:**
Veri akışını sağlayan WebSocket sunucusunu çalıştırın.
```bash
python app.py
```

**2. Arayüzü Başlatın (Dashboard):**
Verileri görsel olarak takip etmek için arayüzü açın. Terminalde yeni bir sekme açarak:
```bash
python -m http.server
```
Ardından tarayıcınızda `http://localhost:8000` adresine gidin.

**3. Alternatif: Terminal İstemcisi**
Verileri sadece terminalde görmek isterseniz:
```bash
python doviz-client.py
```

## 📁 Proje Yapısı

*   **`app.py`**: (Eski adı `ws_server.py`) Ana WebSocket sunucusu.
*   **`Doviz.py`**: Veri çekme mantığını içeren yardımcı modül.
*   **`index.html`**: Kullanıcı arayüzü (Frontend).


## 📝 Notlar

- Bu proje tamamen eğitim ve web kazıma mantığını öğrenme amacıyla hazırlanmıştır.
- Veriler doğrudan HTML üzerinden çekildiği için site yapısı değişirse kodun güncellenmesi gerekebilir.
- Ticari kullanım önerilmez.

## � Geliştirme Alanları

- [ ] Daha fazla finansal veri kaynağı eklenebilir.
- [ ] Veri geçmişi bir veritabanına (SQLite vb.) kaydedilebilir.
- [ ] Grafik kütüphaneleri (Chart.js vb.) ile fiyat değişimleri çizdirilebilir.
