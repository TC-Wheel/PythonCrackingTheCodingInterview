from rot13 import rot13


def cVI_ex1_pg40():
    """Demonstrates an increase in space complexity with recursive functions
    Time Complexity = O(n) - Linear - no nested loops
    Space Complexity = O(n) - Linear - keeps adding to stack
    """

    def sum(n):
        if n <= 0:
            return 0
        return n + sum(n - 1)

    return sum(100)


def cVI_ex2_pg40():
    """Demonstrates a program that is less space complex than ex1
    Time Complexity = O(n) - Linear
    Space Complexity = O(1) - Constant - doesn't add to stack and erases sum var each time total is updated"""

    def pairSum(a, b):
        return a + b

    def pairSumSequence(n):
        sum = 0
        for i in range(n):
            sum += pairSum(i, i + 1)
        return sum

    return pairSumSequence(100)


def cVI_minmax1_pg41():
    """which is faster? minmax1 or minmax2?
    Big O doesn't care. They're the same.
    Time Complexity = O(n)"""
    a = [n for n in range(10)]

    def find_min_max(array):
        min = 0
        max = 0
        for x in array:
            if x < min:
                min = x
            if x > max:
                max = x
        return min, max

    return find_min_max(a)


def cVI_minmax2_pg41():
    """which is faster? minmax1 or minmax2?
    Big O doesn't care. They're the same.
    Time Complexity = O(n)"""
    a = [n for n in range(10)]

    def find_min(array):
        min = 0
        for x in array:
            if x < min:
                min = x
        return min

    def find_max(array):
        max = 0
        for x in array:
            if x > max:
                max = x
        return max

    min, max = find_min(a), find_max(a)

    return min, max


def cVI_addtheruntimes_pg43():
    """shows that loops one after another don't change Big O
    Time Complexity = O(A + B) or O(n)"""
    list_a = ["a1", "a2", "a3"]
    list_b = ["b1", "b2", "b3"]
    for a in list_a:
        print(a)
    for b in list_b:
        print(b)


def cVI_multiplyruntimes_pg43():
    """shows that loops in loops do change Big O
    Time Complexity = O(A * B) or O(n**2)"""
    list_a = ["a1", "a2", "a3"]
    list_b = ["b1", "b2", "b3"]
    for a in list_a:
        for b in list_b:
            print(a + "," + b)


def cVI_recursiveruntimes_pg44():
    """Demonstrates the time complexity of the fib sequence
    Time Complexity = O(branches**depth) or in this case O(2**n)
    Space Complexity = O(n) because we are running each fib sequence additively"""

    def f(n):
        if n <= 1:
            return 1
        return f(n - 1) + f(n - 1)

    return f(10)


def cVI_example1_pg46():
    """What is the runtime of the following code?"""
    list_a = [n for n in range(100)]

    def spam(list_a):
        sum = 0
        product = 1
        for num in list_a:
            sum += num
        for num in list_a:
            product *= num
        print(f"Example 1: {sum = } {product = }")

    spam(list_a)
    answer = rot13("")
    print(answer)


def main():
    # print(f"{cVI_ex1_pg40() = }")
    # print(f"{cVI_ex2_pg40() = }")
    # print(f"{cVI_minmax1_pg41() = }")
    # print(f"{cVI_minmax2_pg41() = }")
    # print("cVI_addtheruntimes_pg43() = ")
    # cVI_addtheruntimes_pg43()
    # print("cVI_mutiplytheruntime_pg43() = ")
    # cVI_multiplyruntimes_pg43()
    print(f"{cVI_recursiveruntimes_pg44() = }")


if __name__ == "__main__":
    main()
