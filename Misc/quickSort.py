from typing import List


class QuickSort:
    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        self.low = 0
        self.high = len(arr) - 1
        # self.quickSort()

    def quickSort(self, arr: List[int], low: int, high: int) -> None:
        if low >= high:
            return

        pivot: int = self.partition(arr, low, high)
        self.quickSort(arr, low, pivot-1)
        self.quickSort(arr, pivot+1, high)

    def partition(self, arr: List[int], low: int, high: int) -> int:
        pivot: int = arr[high]

        i: int = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[high], arr[i+1] = arr[i+1], arr[high]

        return i + 1
