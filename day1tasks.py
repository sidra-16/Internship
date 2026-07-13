# store and print variables
name = "Sidra"
age = 20

print(name)
print(age)

# take input from the user
name = input("Enter your name: ")

print("Hello", name)

# add two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)

# check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# check if a number is prime
num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not Prime")


# find factorial
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)

# check if palindrome
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# find largest number in a list
numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)


#find smallest number in a list
numbers = [12, 45, 7, 89, 23]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

# find the sum of digits
num = int(input("Enter a number: "))

total = 0

while num > 0:
    total += num % 10
    num //= 10

print(total)


# FastAPI Program (get and post)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int
@app.get("/students")
def get_students():
    return students
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added"}