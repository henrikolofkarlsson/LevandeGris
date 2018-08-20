def prime_lookup(limit):
	# Generate lookup table for primes up to limit (int).
	prime_lookup = [False] * 2 + [True] * (limit-1)
	for i, prime in enumerate(prime_lookup):
		if prime:
			for j in range(2 * i, len(prime_lookup), i):
				prime_lookup[j] = False
	return prime_lookup

def proper_divisors(n):
	# Generate an iterator of all proper divsors of n.
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n and i > 1:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def is_triangle_num(tn):
	# Returns triangle root n if tn is triangle num, else -1.
    n = ((8*tn + 1)**.5 - 1)/2
    if n == int(n):
        return int(n)
    else:
        return -1

def is_palindrome(s):
	# Check if string s is a palindrome
    if s == s[::-1]:
        return True
    else:
        return False

def convert_base(i, base, base_list):                   
	# Convert base ten i to other base. No return. Just fills
	# the passed along list with the digits in the new base.
    base_list.insert(0, i % base)                       
    div = int(i/base)
    if div == 0:
        return 
    convert_base(div, base, base_list)

import math


def rotations(s):
	# Generate an iterator of rotations of string s. 
    turns = len(s)
    while turns > 0:
        last_digit = s[-1]
        s = last_digit + s[:-1]
        yield s
        turns -= 1

def truncate(s, from_head = True, from_tail = True, two_front_war = False):
	# Generate an iterator of truncated forms of string s.
	# Optional args for truncation direction.
    for i in range(1, len(s)):
        if from_head:
        	yield s[i:]
        if from_tail:
        	yield s[:-i]
        if two_front_war:
        	yield s[i:-i]