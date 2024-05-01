while True:
    try:
        l = int(input())
        v = list(map(int, input().split()))
        fast = max(v)
        if fast < 10:
            print(1)
        elif fast >= 10 and fast <20:
            print(2)
        else:
            print(3)
    except EOFError:
        break


"""
In this exercise I do not take into account the maximum number of sluts (l), despite that the code works :)
"""