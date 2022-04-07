def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	if(numerator and denominator != 0):
		subnum = int(numerator/denominator)
		answer = (numerator/denominator) - subnum
		return answer
	else:
	 	return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

#use the int function to convert to the whole number from which you will use to subtract from the float number 
# and be left iwth only the decimal places.


#==========================================================================================
# Question 4
#Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.


def sum_divisors(n):
  sum = 0
  i = 1
  # Return the sum of all divisors of n, not including n
  while(n > i):
    if(n%i == 0):
      sum = sum + i
    i+=1 

  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114



#==========================================================================================================
for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

#==========================================================================================
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)

    # Recursive function example.



#====================================================================================================
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# I do not even know this shit is tricky

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)

    
    

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n


    return n + sum_positive_numbers(n - 1)
    # What got me was n - 1. I was using + until I went to the below website to see visualize it

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15



#Want to give it a go yourself? Be my guest! 
#Modify the first_and_last function so that it returns True if the first letter of the string is the same
#as the last letter of the string, False if they’re different. 
# Remember that you can access characters using message[0] or message[-1].
#Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    if(len(message)==0):
        return True
    elif(message[0] == message[-1]):
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#A SCLICE is called a substring
