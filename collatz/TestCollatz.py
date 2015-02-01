#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1     10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read1(self):
        s = " 1 10 100\n"
        i,j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    #my tests
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)

    def test_eval_7(self):
        v = collatz_eval(10,1)
        self.assertEqual(v,20)

    def test_eval8(self):
        v = collatz_eval(9,10)
        self.assertEqual(v,20)
    # -----
    # print
    # -----
    """
    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    """
    def test_print1(self) :
        w = StringIO()
        collatz_print(w, 1, 5, 10)
        self.assertEqual(w.getvalue(), "1 5 10\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 10,20,30)
        self.assertEqual(w.getvalue(), "10 20 30\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 20 , 80, 90)
        self.assertEqual(w.getvalue(), "20 80 90\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
       # self.assertEqual(w.getvalue(), "1 10 1\n100 200 1\n201 210 1\n900 1000 1\n")
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n1 999999\n999998 999999\n244796 493938\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 999999 525\n999998 999999 259\n244796 493938 449\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("542554 678807\n628487 879727\n374289 444328\n903801 926705\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "542554 678807 509\n628487 879727 525\n374289 444328 449\n903801 926705 476\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
