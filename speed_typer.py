import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def countdown():
    print(Fore.CYAN + "\nGet ready...")
    for i in range(3, 0, -1):
        print(Fore.YELLOW + f"{i}...")
        time.sleep(1)
    print(Fore.GREEN + "GO!\n")

def main():
    words = load_words("word_list.txt")
    test_phrase = " ".join(random.sample(words, 10))

    print(Fore.MAGENTA + "🧠 Type the following phrase as fast and accurately as you can:\n")
    print(Fore.BLUE + test_phrase)
    
    countdown()

    start_time = time.time()
    user_input = input("\nYour input: ").strip()
    end_time = time.time()

    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60

    wpm = round(len(user_input.split()) / elapsed_minutes)
    accuracy = round(sum(1 for a, b in zip(user_input, test_phrase) if a == b) / len(test_phrase) * 100, 2)

    print(Fore.GREEN + f"\n⏱ Time: {round(elapsed_time, 2)} seconds")
    print(Fore.CYAN + f"🚀 Speed: {wpm} WPM")
    print(Fore.YELLOW + f"🎯 Accuracy: {accuracy}%")

    if input("\nPlay again? (y/n): ").lower() == 'y':
        main()

if __name__ == "__main__":
    main()
