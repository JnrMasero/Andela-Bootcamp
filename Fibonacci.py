"""Print a Fibonacci sequence up to n."""
import sys
import os

class Fibonacci:
	def gen(self, n):
         a, b = 0, 1
         while b < n:
             print b,
             a, b = b, a+b
