# pętle - możliwość wykonania wieokrotnie tego samego fragmentu programu
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(10000):
    pass  # nic nie rób

for _ in range(5):  # _ - niema zmienna
    print('to jest pętla')
    # print(_)
# to jest pętla
# to jest pętla
# to jest pętla
# to jest pętla
# to jest pętla

for i in range(20):  # od 0 do 19
    print(i * 2)  # 38

print("------")
"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # 21, int od 1 do 100 włącznie
print(random.randrange(1, 100))  # int od 1 do 99, 36
print(random.randrange(5))  # int od 0 do 4, 1
print(random.random())  # float 0.25115282757340995, pd 0 do 0.999999
print(random.random() * 5)  # float 2.804473691311862, pd 0 do 4.999999
