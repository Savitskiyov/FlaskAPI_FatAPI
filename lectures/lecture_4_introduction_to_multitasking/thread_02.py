# Многопоточный подход

import threading
import time


def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

for t in threads:
    t.start()
    # ждать, пока поток завершится
    t.join()
    # т.е. потоки выполняются последовательно. произошёл возврат к синхронному выполнению

print("Все потоки завершили работу")
