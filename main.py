import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Countdown: {seconds} seconds")
        time.sleep(1)  # Wartet eine Sekunde
        seconds -= 1

    print("Countdown abgeschlossen!")

if __name__ == "__main__":
    countdown_timer(10)
