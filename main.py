from typing import List
import sys
import time


def find_uniq(dataset: List[int]) -> int:
    dict_dataset = dict.fromkeys(dataset, 0)

    for item in dataset:
        dict_dataset[item] += 1

    for key, value in dict_dataset.items():
        if value == 1:
            return key


if __name__ == "__main__":
    with open("test1.txt", "r", encoding="utf-8") as file:
        test_list = list(map(int, file.read().split()))

    start_time = time.time()
    print(f"answer = {find_uniq(test_list)}")
    print("--- %s seconds ---\n" % (time.time() - start_time))
