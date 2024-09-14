def generate_min_palindrome_String(n):
	vowels = "aeiou"
	result = []
	for i in range(n):
		result.append(vowels[i % 5])
	return ''.join(result)

"""	
import sys
input  = sys.stdin.read
data = input().strip().split()

t = int(data[0])
results = []
for i in range(1,t+1):
	n = int(data[i])
	results.append(generate_min_palindrome_String(n))
"""
# Test with predefined input
test_cases = [2, 3, 6]  # Example test cases
results = [generate_min_palindrome_String(n) for n in test_cases]


for result  in results:
	print(result)

# index modulo is used to traverse thru list or array using i % arr.length
