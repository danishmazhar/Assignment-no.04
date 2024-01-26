#Assignment no.04

#question no.01
def value(lst):
  unique_values = {}

  for value in lst:

      if value not in unique_values:
          unique_values[value] = 1

      else:
          unique_values[value] += 1

  return unique_values

if __name__ == "__main__":
  my_list = [1, 2, 3, 4,3,3,4,5,2,3,4]
  unique_counts = value(my_list)
  print("Unique vaues and their counts:")
  for key, value in unique_counts.items():
      print(f"{key}: {value}")

print("now!")

#question no.02
def generate_squared_dictionary(n):
  squared_dict = {}  
  for i in range(1, n + 1):
      squared_dict[i] = i * i  
  return squared_dict

if __name__ == "__main__":
  n = int(input("Enter a numer (n): "))
  result_dict = generate_squared_dictionary(n)
  print("Generated dictionary:")
  print(result_dict)
print("now!")  
  
#question no.03
a = int(input("Enter the value of n: "))
numbers = []

for i in range(a):
    b = float(input("Enter the number  " + str(i + 1) + " == "))
    numbers.append(b)

total = sum(numbers)
print("the list u entered !=!",numbers)
print("Sum of the", a, "numbers is:", total)
  print("nw!")
#question no.04
def fibonacci_series(n):
 
  fib_sequence = [0, 1]

  
  for i in range(2, n):
      next_fib = fib_sequence[-1] + fib_sequence[-2]  
      fib_sequence.append(next_fib)  

  return fib_sequence

if __name__ == "__main__":
  num_terms = int(input("Enter the number of terms for Fibonacci series: "))

  if num_terms <= 0:
      print("Please enter a positive integer.")
  else:
      fibonacci_sequence = fibonacci_series(num_terms)
      print("Fibonacci series up to", num_terms, "terms:")
      print(fibonacci_sequence)
print("now!")
#question no.05

file1 = input("Enter the path to the file: ")

with open(file1, 'r') as file:
    lines = file.readlines()

print("Content of the file stored in a list:")
for line in lines:
    print(line.strip()) 
print("now!")
#question no.06
source = input("Enter the path to the source file: ")

destin = input("Enter the path to the destination file: ")

with open(source, 'r') as source_file:
    content = source_file.read()

with open(destin, 'w') as destination_file:
    destination_file.write(content)

print("File copied successfully!")
print("ow!")
#qestion no.07
def create_alphabet_file(filename, letters_per_line):
  with open(filename, 'z') as file:
      
      alphabet = 'abcdefghijklmnopqrstuvwxyz'

     
      for i in range(0, len(alphabet), letters_per_line):
          line = alphabet[i:i+letters_per_line] + '\n'
          file.write(line)

if __name__ == "__main__":
  filename = input("Enter the file name to create: ")
  letters_per_line = int(input("Enter the number of letters per line: "))

  create_alphabet_file(filename, letters_per_line)
  print(f"Alphabet file '{filename}' created with {letters_per_line} letters per line.")

