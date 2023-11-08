#product_test.py
#Exercise to learn how to define a funtion.

def prod_exercise(factor1, factor2, factor3):
    product = factor1 * factor2 * factor3
    return product

first_test = prod_exercise (.5, .4, .3)
print ("The first test result is: ", first_test)  

second_test = prod_exercise (1, 2, 3)
print ("The second test result is: ", second_test)  

third_test = prod_exercise (-1, -1, -1)
print ("The third test result is: ", third_test)  


print ("The results using the format f is the following:")

print (f"The results are: {first_test},  {second_test},  {third_test}")
