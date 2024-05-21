import media

# TEST 1
if media.media([3, 4, 5, 6, 7, 43, 21, 2, 3, 4]) == 9.8:
    print("test 1 superato")
else:
    print("test 1 fallito")

# TEST 2
if media.media([1, 1, 1, 1, 1]) == 1:
    print("test 2 superato")
else:
    print("test 2 fallito")

# TEST 3
if media.media([]) == 0:
    print("test 3 superato")
else:
    print("test 3 fallito")
