n = int(input())
l = list(map(int, input().split()))

def quicksort(start, end):

    def sort(start, end):
        if end <= start:
            return

        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)
        
    def partition(start, end):
        pivot = l[(start + end) // 2]

        while start <= end:
            while l[start] < pivot:
                start += 1
            while l[end] > pivot:
                end -= 1
            if start <= end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1

        return start

    return sort(start, end)

quicksort(0, n - 1)
print(l)
