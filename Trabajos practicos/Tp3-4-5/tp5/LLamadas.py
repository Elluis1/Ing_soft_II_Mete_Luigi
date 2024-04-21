from clasesYfunciones import *

# Punto 1 (LLamada)
processor = NumberProcessor()
processor.process_numbers()

# Punto 2
word = "Hello"
print("Straight traversal:")
print("\n".join(word))
print("")

print("Reverse traversal:")
print("\n".join(word[::-1]))
print("\n")