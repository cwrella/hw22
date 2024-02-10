import time
import threading
start = time.time()

def folder():
    file = open("file.txt", "a")
    print("Файл успешно создан")
    time.sleep(1)

thr_list = []
for i in range(100):
    thr = threading.Thread(target=folder)
    thr_list.append(thr)
    thr.start()

for i in thr_list:
    i.join()
print(time.time() - start)