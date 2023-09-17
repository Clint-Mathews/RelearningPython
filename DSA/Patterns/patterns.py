def pattern1(n):
    print("Pattern 1")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
# 1.  *****
#     *****
#     *****
#     *****
#     *****
pattern1(5)

def pattern3(n):
    print("Pattern 3")
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()
# 3.  *****
#     ****
#     ***
#     **
#     *

pattern3(5)


def pattern4(n):
    print("Pattern 4")
    for i in range(n):
        for j in range(i+1):
            print("{}".format(j+1), end=" ")
        print()
# 4.  1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
pattern4(5)

# 5.  *
#     **
#     ***
#     ****
#     *****
#     **** 6 -4
#     *** 7- 3
#     ** 8- 2
#     * n - (6-n)
def pattern5(n):
    print("Pattern 5")
    for i in range(2*n):
        count = 2*n-i if (i > n) else i
        for j in range(count):
            print("*", end = " ")
        print()

pattern5(5)

# 8.      * 4
#        *** 3
#       ***** 2
#      ******* 1
#     *********0


def pattern8(n):
    print("Pattern 8")
    for i in range(n):
        for k in range(n-i):
            print("", end=" ")
        for j in range(2*i-1):
            print("*", end="")
        print()


pattern8(5)


# 12.  * * * * *5,0
#       * * * *4,1
#        * * *3,2
#         * *2,3
#          *1,4 n-i-1
#          *1,4 6
#         * *2, 7
#        * * *3, 8
#       * * * *4, 9
#      * * * * *5,10
def pattern12(n):
    print("Pattern 12")
    for i in range(1, 2*n+1):
        space = i-1 if n >= i else 2*n-i
        for k in range(space):
            print("", end=" ")
        count = n-i+1 if n >= i else i-n
        for j in range(count):
            print("*", end=" ")
        print()


pattern12(5)


# 14.  *********
#       *     *
#        *   *
#         * *
#          *

def pattern14(n):
    print("Pattern 14")
    for i in range(n):
        left_space = i
        for j in range(left_space):
            print("", end=" ")

        count = 2*n-1 if i == 0 else (2 if i < n-1 else 1)
        for j in range(count):
            print("*", end="")
            if i < n-1 and i != 0:
                right_space = 2 * (n - i) - 3
                for k in range(right_space):
                    print("", end=" ")
        print("")

pattern14(5)

#
# 18.   **********
#       ****  ****
#       ***    ***
#       **      **
#       *        *
#       *        *
#       **      **
#       ***    ***
#       ****  ****
#       **********


def pattern18(n):
    print("Pattern 18")
    for i in range(2*n):
        star_print = n-i if i < n else i-n+1
        space_print = 2*i if i < n else 2*(2*n - i - 1)

        # Left Phase
        for j in range(star_print):
            print("*", end="")

        # Space
        for k in range(space_print):
            print(" ", end="")

        # Right phase
        for j in range(star_print):
            print("*", end="")
        print()

pattern18(5)


# 24.    *        *
#        **      **
#        * *    * *
#        *  *  *  *
#        *   **   *
#        *   **   *
#        *  *  *  *
#        * *    * *
#        **      **
#        *        *

def pattern24(n):
    print("Pattern 24")
    for i in range(2*n):
        star_in_btw_space = (i-1) if i < n else (2*n - i) - 2

        # Left
        if 0 < i < 2*n-1:
            print("*", end="")
            for j in range(star_in_btw_space):
                print(" ", end="")
            print("*", end="")
        else:
            print("*", end="")

        # Between space
        between_space = n-i-1 if i < n else i-n
        for j in range(2 * between_space):
            print(" ", end="")

        # Right
        if 0 < i < 2*n-1:
            print("*", end="")
            for j in range(star_in_btw_space):
                print(" ", end="")
            print("*", end="")
        else:
            print("*", end="")

        print("")

pattern24(5)

