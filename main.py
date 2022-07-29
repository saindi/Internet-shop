from typing import List


def find_uniq(dataset: List[int]) -> int:
    dict_dataset = dict.fromkeys(dataset, 0)

    for item in dataset:
        dict_dataset[item] += 1

    for key, value in dict_dataset.items():
        if value == 1:
            return key


if __name__ == "__main__":
    print(find_uniq([1, 2, 3, 2, 1]))
    print(find_uniq([54, 90, 52, 10, 62, 54, 90, 52, 10, 62, 42]))