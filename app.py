from idlelib.run import get_message_lines

import websocket
import json

def mesaj_iste(ws, mesaj):
    if ws is None or not mesaj:
        return

    try:
        veri = json.loads(mesaj)
    except json.JSONDecodeError:
        print("Veri çözümlenemedi.")
        return

    if "data" in veri:
        for kayit in veri["data"]:
            sembol = kayit.get("s")
            fiyat = kayit.get("p")

            if sembol == "XAUUSD":
                print(f"ONS ALTIN: {fiyat} USD")
            elif sembol == "XAGUSD":
                print(f"ONS GÜMÜŞ: {fiyat} USD")
            elif sembol == "OANDA:USDTRY":
                print(f"DOLAR: {fiyat} TL")
            elif sembol == "OANDA:EURTRY":
                print(f"EURO: {fiyat} TL")


def hata_yonet(ws, hata):
    if ws is None:
        return
    print("Hata:", hata)


def baglanti_koptu(ws, kod, mesaj):
    if ws is None:
        return
    print("Bağlantı kapandı.")


def baglanti_acildi(ws):
    if ws is None:
        return

    print("Bağlantı açıldı! Canlı veriler dinleniyor...")

    abonelikler = [
        {"type": "subscribe", "symbol": "XAUUSD"},
        {"type": "subscribe", "symbol": "XAGUSD"},
        {"type": "subscribe", "symbol": "OANDA:USDTRY"},
        {"type": "subscribe", "symbol": "OANDA:EURTRY"},
    ]

    for paket in abonelikler:
        try:
            ws.send(json.dumps(paket))
        except:
            print("Abonelik gönderilemedi.")


if __name__ == "__main__":
    websocket.enableTrace(False)

    ws_url = "wss://ws.finnhub.io?token=cg7n3iqad3idv0jru1fg"

    ws = websocket.WebSocketApp(
        ws_url,
        on_open=baglanti_acildi,
        on_message=mesaj_iste,
        on_error=hata_yonet,
        on_close=baglanti_koptu
    )

    try:
        ws.run_forever()
    except KeyboardInterrupt:
        print("Program sonlandırıldı.")
