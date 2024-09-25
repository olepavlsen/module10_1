import time
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        k = 1
        while k <= word_count:
            ks = 'Какое-то слово №' + str(k)
            file.write(ks)
            file.write('\n')
            time.sleep(0.1)
            k += 1
        print(f'Завершилась запись в файл', file_name)


time_sart = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = datetime.now()
time_res = time_end - time_sart
print(f'Работа потоков', time_res)

time_sart = datetime.now()
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
time_res = time_end - time_sart
print(f'Работа потоков', time_res)
