''' FUNCTIONS
  (1) DEFINE vs CALL
  (2) Parameter vs Argument
  (3) Keyword & default arguments
  (4) Scope 
'''

print("===== DEFINE (parameter) vs CALL (argument) =====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parameter
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)
