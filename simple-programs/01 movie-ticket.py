'''
1. Movie Ticket Eligibility

   * A cinema has these ticket prices:

     * Age below 5: Free
     * Age 5-17: ₹150
     * Age 18-59: ₹250
     * Age 60 and above: ₹120
   * Input the user's age and print the ticket price.

   Concepts: `if`, `elif`, `else`
'''

print("Movie Ticket Eligibility")
age = int(input("Enter age:"))

if age < 5:
  print("Free")
elif age >= 5 and age <= 17:
  print("Rs 150")
elif age >= 18 and age <= 59:
  print("Rs 250")
else:
  print("Rs 120")
