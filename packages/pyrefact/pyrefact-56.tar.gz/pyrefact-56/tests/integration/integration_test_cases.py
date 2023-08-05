"""Integration test cases, used in test_format_code and test_format_file"""

INTEGRATION_TEST_CASES = (
    ("", ""),
    (
        """
for x in range(100):
    if x > 10:
        y = 13
    else:
        x += 1
        x *= 12
        print(x > 30)
        y = 100 - sum(x, 2, 3)
print(x)
        """,
        """
for x in range(100):
    if x <= 10:
        x += 1
        x *= 12
        print(x > 30)
print(x)
        """,
    ),
    (
        """
x = 100
z = list()
def foo() -> bool:
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        # if x > 0:
        #     return 100 * x < 1000
        if z:
            return False
        else:
            return True
print(foo())
        """,
        """
X = 100
Z = []
def _foo() -> bool:
    if X == 1:
        return False
    if X == 2:
        return True
    if Z:
        return False

    return True
print(_foo())
        """,
    ),
    (
        """
x = sorted(list(range(100)))[::3]
z = []
for a in x:
    if a % 3 == 0 and a % 4 == 2:
        for w in x:
            if w > len(x) // 2:
                z.append(w ** 3)
if all(y in [1, 2, 5] for y in sorted(set(list(z)))):
    print(z, x)
        """,
        """
X = sorted(range(100))[::3]
Z = [w**3 for a in X if a % 3 == 0 and a % 4 == 2 for w in X if w > len(X) // 2]
if all(y in {1, 2, 5} for y in sorted(set(Z))):
    print(Z, X)
        """,
    ),
    (
        """
z = {a for a in range(10)}
x = sum(z)
print(x)
        """,
        """
X = sum(set(range(10)))
print(X)
        """,
    ),
    (
        """
q = 3
w = list()
for a in range(-1, 10):
    for k in range(-1, 1):
        w.append(a ** 2 + q + k ** 2)
y = sum(w)
print(y)
            """,
        """
Q = 3
Y = 22 * Q + 583
print(Y)
        """,
    ),
    (
        """
x = 0
a = 1
for i in range(100):
    x += i**2
    a -= i**3

print(x)
            """,
        """
X = 328350
print(X)
        """,
    ),
    (
        """
x = 0
a = 1
for i in range(100):
    x += i**2
    a -= i**3

print(x, a)
            """,
        """
X = 0
A = 1
for i in range(100):
    X += i**2
    A -= i**3

print(X, A)
        """,
    ),
    (
        """
x = list()
for i in range(100):
    x += i**2

print(x)
            """,
        """
X = [i**2 for i in range(100)]
print(X)
        """,
    ),
    (
        """
import numpy as np

i, j, k = 10, 11, 12

a = np.random.random((i, j))
b = np.random.random((j, k))

u = np.array(
    [
        [
            np.sum(
                a__ * b__
                for a__, b__ in zip(a_, b_)
            )
            for a_ in a
        ]
        for b_ in b.T
    ]
).T

print(u)
            """,
        """
import numpy as np

I, J, K = 10, 11, 12

A = np.random.random((I, J))
B = np.random.random((J, K))

U = np.matmul(A, B)

print(U)
        """,
    ),
    (
        """
import numpy as np

i, j, k = 10, 11, 12

a = np.random.random((i, j))
b = np.random.random((j, k))

u = np.array(
    [
        [
            np.dot(b[:, i], a[j, :])
            for i in range(b.shape[1])
        ]
        for j in range(a.shape[0])
    ]
)

print(u)
            """,
        """
import numpy as np

I, J, K = 10, 11, 12

A = np.random.random((I, J))
B = np.random.random((J, K))

U = np.matmul(A, B)

print(U)
        """,
    ),
    (
        """
a = np.random.random(100)
b = np.random.random(100)

u = 0
for a_, b_ in zip(a, b):
    u += a_ * b_

print(u)
            """,
        """
import numpy as np

A = np.random.random(100)
B = np.random.random(100)

U = np.dot(A, B)

print(U)
        """,
    ),
    (
        """
    a = np.random.random(100)
    b = np.random.random(100)

    u = 0
    for a_, b_ in zip(a, b):
        u += a_ * b_

    print(u)
            """,
        """
    a = np.random.random(100)
    b = np.random.random(100)

    u = np.dot(a, b)

    print(u)
        """,
    ),
    (
        """
def f(x) -> int:
    if x == 1:
        x = 2
    else:
        if x == 3:
            x = 7
        else:
            if x != 8:
                if x >= 912:
                    x = -2
                elif x ** x > x ** 3:
                    x = -1
                else:
                    x = 14
            else:
                x = 99

    return x

print(f(11))
            """,
        """
def _f(x) -> int:
    if x == 1:
        return 2
    if x == 3:
        return 7
    if x == 8:
        return 99
    if x >= 912:
        return -2
    if x**x > x**3:
        return -1

    return 14

print(_f(11))
            """,
    ),
    (
        """
import random
import sys
def f(x: int) -> int:
    import heapq
    y = e = 112
    if x >= 2:
        d = 12
    if []:
        x *= 99
    if x == 3:
        y = x ** 13
        return 8
    else:
        return 19
print(f(12))
while False:
    sys.exit(0)
            """,
        """
def _f(x: int) -> int:
    if x == 3:
        return 8

    return 19
print(_f(12))
            """,
    ),
    (
        """
class Foo:
    def asdf(self):
        x = None
        if 2 in {1, 2, 3}:
            print(3)
def wsdf():
    z = ()
    if 2 in {1, 2, 3}:
        print(3)
wsdf()
Foo().asdf()
Foo.asdf()
        """,
        """
def _asdf():
    if 2 in {1, 2, 3}:
        print(3)
_asdf()
_asdf()
_asdf()
        """,
    ),
)
