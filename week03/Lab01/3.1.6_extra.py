#6. Why does this expression cause an error? How can you fix it?
# Incorrect syntex as can only concatenate str not int
#message = 'I have eaten ' + 99 + ' burritos.'
#print (message)
# Correct Syntex is
message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

#7. Why is eggs a valid variable name while 100 is invalid?
# Bacause 100 is an integer value and variable can not start with an integer value, and eggs is a string ang string is valid for a variable.

#8. What three functions can be used to get the integer, floating-point number, or string version of a value?
# to get the integer of the value need to use int() function.
# to get the floting of the value need to use float() function.
# to get the string of the value need to use str() function.