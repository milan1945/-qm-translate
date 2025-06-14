
import time
import pyautogui
import keyboard

print("Spusťte Virtaal + QTranslate a přepněte do Virtaal (12 sekund)...")
time.sleep(12)

num_cycles = 5000
pause = False

print("\n--- Ovládání ---")
print("P = pauza / pokračuj")
print("Q = ukonči\n")

for i in range(num_cycles):
    if keyboard.is_pressed("q"):
        print("Ukončeno uživatelem.")
        break

    if keyboard.is_pressed("p"):
        pause = not pause
        print("== Pauza ==" if pause else "== Pokračuji ==")
        time.sleep(1)

    if pause:
        time.sleep(0.5)
        continue

    print(f"⟳ Krok {i + 1}/{num_cycles}")

    # VIRTAAL
    pyautogui.hotkey('altleft', 'down')  # převzetí EN překladu
    time.sleep(1)

    # QTRANSLATE
    pyautogui.hotkey("ctrl")             # spustí překlad
    time.sleep(1)
    pyautogui.press("shift")             # přepíše italštinu češtinou
    time.sleep(3)

    # Minimalizace QTranslate
    pyautogui.hotkey("alt", "space")
    time.sleep(0.2)
    pyautogui.press("n")                 # 'N' = minimalizovat
    time.sleep(1)

    # Potvrzení ve Virtaalu (např. Enter pro další segment)
    pyautogui.press("enter")
    time.sleep(1)
