import queue
import time
import random as rnd

GREEN  = '\033[92m'
YELLOW = '\033[93m'
BLUE   = '\033[94m'
WHITE  = '\033[97m'
CLRLN  = '\033[K'
RESET  = '\033[0m'

request_queue = queue.Queue()
request_id = 0

def generate_request():
    # 10% ймовірність не створювати заявку для отримання порожньої черги
    if rnd.randint(0, 9) < 1:
        print(f"{WHITE}Не створено заявку (імітація відсутності нових заявок){RESET + CLRLN}")
        return

    global request_id
    request_id += 1
    request = f"Request-{request_id}"
    request_queue.put(request)
    print(f"> Згенеровано заявку: {YELLOW + request + RESET + CLRLN}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"    > Обробка заявки: {BLUE + request + RESET + CLRLN}")
    else:
        print(f"{YELLOW}Черга пуста. Немає заявок для обробки.{RESET + CLRLN}")

if __name__ == "__main__":
    print(f"\033[H\033[J{GREEN}Запуск системи обробки заявок (Ctrl+C для виходу){RESET}\n")
    try:
        while True:
            generate_request()
            time.sleep(rnd.random() * 0.3 + 0.2)
            process_request()
            time.sleep(rnd.random() * 1.5 + 0.5)
            print('\033[A\033[2K\033[A\033[A')
    except KeyboardInterrupt:
        print("\nРоботу завершено.")
