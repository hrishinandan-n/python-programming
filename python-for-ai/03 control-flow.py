'''
    Python Control flow statements
        - if-else
        - if-elif-else
'''

'''
# Weather Condition Checking

Problem Statement:

Write a Python program to check the weather condition based on the temperature entered by the user.

Requirements:

* Ask the user to enter the current temperature (in °C).
* Use `if`, `elif`, and `else` statements to determine the weather condition:

  * If the temperature is **35°C or above**, print **"It's very hot."**
  * If the temperature is **25°C to 34°C**, print **"The weather is warm."**
  * If the temperature is **15°C to 24°C**, print **"The weather is pleasant."**
  * If the temperature is **below 15°C**, print **"It's cold."**

Expected Output:

* Display the appropriate weather condition based on the entered temperature.

Concepts: `input()`, `if`, `elif`, `else`, comparison operators

'''

print("Weather Condition Checking")
current_temp = int(input("Enter Current Temperature: "))

if current_temp >= 35:
    print("It's very hot.")
elif current_temp >= 25 and current_temp <= 34:
    print("The weather is warm.")
elif current_temp >= 15 and current_temp < 25:
    print("The weather is pleasant.")
else:
    print("It's cold.")