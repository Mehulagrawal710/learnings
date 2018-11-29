#Operaters
"""Arithmetic operaters"""
x = 10 + 3 
x = 10 - 3 
x = 10 * 3 
x = 10 / 3 #(x=x divide 3)gives float value
x = 10 // 3 #(x=x divide 3)gives int value
x = 10 % 3 #gives remainder
x = 10 ** 3 #(10 power 3)
print(x)
"""python does not have increment(x++), decrement(x--) operators"""

"""
Assignment Operators

Operator	Example		Same As
=			x = 5		x = 5	
+=			x += 3		x = x + 3	
-=			x -= 3		x = x - 3	
*=			x *= 3		x = x * 3	
/=			x /= 3		x = x / 3	
%=			x %= 3		x = x % 3	
//=			x //= 3		x = x // 3	
**=			x **= 3		x = x ** 3	
&=			x &= 3		x = x & 3	
|=			x |= 3		x = x | 3	
^=			x ^= 3		x = x ^ 3	
>>=			x >>= 3		x = x >> 3	
<<=			x <<= 3		x = x << 3

Comparison Operators

Operator	Name						Example
==			Equal						x == y	
!=			Not equal					x != y	
>			Greater than				x > y	
<			Less than					x < y	
>=			Greater than or equal to	x >= y	
<=			Less than or equal to		x <= y

Logical Operators

Operator	Description						Example
and 		Returns True if both			x < 5 and  x < 10
			statements are true	
or			Returns True if one of			x < 5 or x < 4	
			the statements is true
not			Reverse the result, returns		not(x < 5 and x < 10)
			False if the result is true	

Identity Operators
Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location:

Operator	Description							Example
is 			Returns true if both variables		x is y
			are the same object	
is not		Returns true if both variables		x is not y
			are not the same object	

Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description						Example
in 			Returns True if a sequences     x in y
			with the specified value is 
			present in the object	
not in		Returns True if a sequence      x not in y
			with the specified value is
			not present in the object	

Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name					Description
& 			AND						Sets each bit to 1 if both bits are 1
|			OR						Sets each bit to 1 if one of two bits is 1
^			XOR						Sets each bit to 1 if only one of two bits is 1
~ 			NOT						Inverts all the bits
<<			Zero fill left shift	Shift left by pushing zeros in from the right and
									let the leftmost bits fall off
>>			Signed right shift		Shift right by pushing copies of the leftmost bit
									in from the left, and let the rightmost bits fall off

"""