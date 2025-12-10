**FİNANS TAKİP UYGULAMASI**

Bu proje, güncel döviz ve altın fiyatlarını web kazıma (web scraping) yöntemiyle çekip kullanıcıya sunan basit bir finans takip uygulamasıdır. Backend kısmı Python ile yazılmıştır. Proje kapsamında temel web kazıma teknikleri, HTTP istekleri, HTML parse etme ve terminal çıktısı oluşturma işlemleri gösterilmektedir.



**Proje Amacı**

-Web kazıma mantığını kavratmak

-requests ve BeautifulSoup kullanımını öğrenmek

-Gerçek bir web sitesinden anlık veri çekmek

-Veri işleme ve gösterme mantığını basitçe uygulamak



**Kullanılan Teknolojiler**

Python 3.x

Requests — Web sitesine HTTP isteği atmak için

BeautifulSoup4 — HTML parse edip veri almak için



**Gereksinimler**

-Python 3.10+

-websockets

-requests

-beautifulsoup4

Kurmak için:

pip install websockets requests bs4



**Nasıl Çalışır?**

main.py dosyası, https://www.doviz.com adresine GET isteği atar, sayfa HTML yapısını inceleyerek:

-Ons Altın fiyatı

-USD/TL kuru

-EUR/TL kuru

-Ons gümüş fiyatı

gibi finansal verileri seçip terminale yazdırır.



**Çalıştırma**

Terminalde proje klasörüne gel:

cd FinansTakip

Ardından:

Terminal 1:

python ws_server.py 

Terminal 2:

python -m http.server



**Örnek çıktı:**

<img width="1916" height="902" alt="image" src="https://github.com/user-attachments/assets/b660a814-d55b-4873-b86e-0a4a2519c265" />



**Notlar**

-Bu proje tamamen web kazıma temelli hazırlanmıştır.

-API kullanılmamış, veriler doğrudan HTML üzerinden çekilmiştir.

-Kodlar öğrenme ve gösterim amaçlıdır, ticari kullanım önerilmez.



**Geliştirme Alanları**

-Daha fazla finansal veri eklenebilir.

-Veri geçmişi kayıt altına alınabilir.

-Grafik gösterimi eklenebilir.
