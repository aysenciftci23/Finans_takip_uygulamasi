from Doviz import fiyatlari_cek
from Veriler import kaydet_json

def main():
    print("Veriler çekiliyor...")
    fiyatlar = fiyatlari_cek()
    print("Fiyatlar alındı:", fiyatlar)

    print("JSON dosyasına kaydediliyor...")
    kaydet_json(fiyatlar)

if __name__ == "__main__":
    main()
