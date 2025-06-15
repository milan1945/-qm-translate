
import time
import pyautogui
import keyboard

print("Spusťte Virtaal + QTranslate a přepněte do Virtaal (12 sekund)...")
time.sleep(12)

num_cycles = 1
pause = False


for i in range(num_cycles):
    time.sleep(1)
    pyautogui.hotkey('win', 'down')
    time.sleep(1)


num_cycles = 5000
pause = False

print("\n--- Ovládání ---")
print("alt = pauza \pokračuj")
print("home = ukonči\n")

for i in range(num_cycles):
    if keyboard.is_pressed("home"):
        print("Ukončeno uživatelem.")
        break

    if keyboard.is_pressed("alt"):
        pause =  pause
        print("== Pauza ==" if pause else "== Pokračuji ==")
        time.sleep(1)

    if pause:
        time.sleep(10)
        continue

    print(f"⟳ Krok {i + 1}/{num_cycles}")

    # VIRTAAL
    pyautogui.hotkey('altleft', 'down')  # převzetí EN překladu
    time.sleep(1)

    # QTRANSLATE
    pyautogui.hotkey("ctrl","a")             # označí
    time.sleep(2)
    pyautogui.press("ctrl")            # spustí překlad
    pyautogui.press("ctrl")  
    time.sleep(4) 

    # Minimalizace QTranslate
    pyautogui.hotkey("alt", "space","n")     # 'N' = minimalizovat
    time.sleep(1)
        
    pyautogui.press("shift")             # přepíše italštinu češtinou
    time.sleep(3) 

    # Potvrzení ve Virtaalu (např. Enter pro další segment)
    pyautogui.press("enter")
    time.sleep(1)
