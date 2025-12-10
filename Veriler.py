import json

def kaydet_json(veri):
    with open("veriler.json", "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=2)
    print("Veriler veriler.json'a kaydedildi.")
