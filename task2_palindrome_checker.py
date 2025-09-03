from collections import deque

GREEN   = '\033[32m'
BLUE    = '\033[36m'
WHITE   = '\033[37m'
COLORS  = [GREEN, WHITE, BLUE]
FALSE   = '\033[1;41;33m'
TRUE    = '\033[1;47m'
BOLD    = '\033[1m'
GRAY_BG = '\033[100m'
RESET   = '\033[0m'

def is_palindrome(text: str) -> bool:
    # Прибираємо все окрім літер і цифр, та переводимо їх у нижній регістр
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    d = deque(cleaned)

    while len(d) > 1:
        # Перевіряємо перший і останній символи, поступово видаляючи їх
        if d.popleft() != d.pop():
            return False
    return True

# Приклади паліндромів та не-паліндромів
examples = ["A man a plan a canal Panama",
            "Madam, I'm Adam",
            "Hello",
            "racecar",
            "Козак з казок",
            "А роза упала на лапу Азора",
            "Не паліндром",
            "1234500054321",
            "123456",
            "No 'x' in Nixon",
            "Я несу гусеня",
            "Уму – мінімуму!",
            "І розморозь зором зорі",
            "Ущипне — та шатен: пищу!",
            "Якийсь НЕполіндромний рядок",
            "А результатів? Вітать лузера!",
            "А баба на волі — цілована баба.",
            "Три психи пили Пилипихи спирт."]

# Очистка екрану перед виводом результатів
print(f"\033[H\033[J", end='')

# Довжина найдовшого прикладу для вирівнювання виводу
max_len = max(len(ex) for ex in examples)

# Перевірка поліндромів
for idx, ex in enumerate(examples):
    color = COLORS[idx % len(COLORS)]
    check = is_palindrome(ex)
    if check:
        result_color = TRUE
    else:
        result_color = FALSE
    print(f" {BOLD + GRAY_BG}{idx+1:>3} {RESET} {color}{ex:<{max_len}}{RESET} -> {result_color} {str(check):^5} {RESET}")

print()