import keyboard,sys

cryptKey = input("Şifreleme anahtarı: ")
shortA = keyboard.add_hotkey("a",lambda: keyboard.write(cryptKey+"a"),timeout=0)
shortE = keyboard.add_hotkey("e",lambda: keyboard.write(cryptKey+"e"),timeout=0)
# shorti = keyboard.add_hotkey("i",lambda: keyboard.write(cryptKey+"i"),timeout=0)
shortI = keyboard.add_hotkey("ı",lambda: keyboard.write(cryptKey+"ı"),timeout=0)
shortO = keyboard.add_hotkey("o",lambda: keyboard.write(cryptKey+"o"),timeout=0)
shortOwithPoint = keyboard.add_hotkey("ö",lambda: keyboard.write(cryptKey+"ö"),timeout=0)
shortU = keyboard.add_hotkey("u",lambda: keyboard.write(cryptKey+"u"),timeout=0)
shortUwithPoint = keyboard.add_hotkey("ü",lambda: keyboard.write(cryptKey+"ü"),timeout=0)
keyboard.wait("ctrl+q")

