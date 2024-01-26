#Assignment no.04

#question no.01
def count_unique_values(lst):
  unique_values = {}

  for item in lst:

      if item not in unique_values:
          unique_values[item] = 1
     
      else:
          unique_values[item] += 1
 
  return unique_values

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
  unique_counts = count_unique_values(my_list)
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
def sum_of_n_numbers(n):
  numbers = [] 
  for _ in range(n):
      number = float(input("Enter a number: "))  
      numbers.append(number)  

if __name__ == "__main__":
  n = int(input("Enter the number of elements: "))
  total_sum = sum_of_n_numbers(n)
  print("Sum of", n, "numbers:", total_sum)

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

def read_file_lines(filename):
  lines_list = [] 

 
  with open(filename, 'r') as file:
     
      for line in file:
          lines_list.append(line.strip())  

  return lines_list

if __name__ == "__main__":
  filename = input("Enter the file name: ")

  try:
      lines = read_file_lines(filename)
      print("Lines read from the file:")
      for line in lines:
          print(line)
  except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")

print("now!")
#question no.06
def copy_file(source_file, destination_file):
  try:
      
      with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
          
          for line in source:
              destination.write(line)
      print("File copied successfully!")
  except FileNotFoundError:
      print("Error: One or both files not found.")
  except IOError:
      print("Error: Unable to copy the file.")

if __name__ == "__main__":
  source_filename = input("Enter the source file name: ")
  destination_filename = input("Enter the destination file name: ")

  copy_file(source_filename, destination_filename)
print("ow!")
#qestion no.07
def create_alphabet_file(filename, letters_per_line):
  with open(filename, 'w') as file:
      
      alphabet = 'abcdefghijklmnopqrstuvwxyz'

     
      for i in range(0, len(alphabet), letters_per_line):
          line = alphabet[i:i+letters_per_line] + '\n'
          file.write(line)

if __name__ == "__main__":
  filename = input("Enter the file name to create: ")
  letters_per_line = int(input("Enter the number of letters per line: "))

  create_alphabet_file(filename, letters_per_line)
  print(f"Alphabet file '{filename}' created with {letters_per_line} letters per line.")

