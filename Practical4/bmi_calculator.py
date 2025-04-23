#input the height and weight and stored as two variables
a=float (input("please input your height in meter" ))
b=float (input("please input yourn weight in kg" ))
#set a new variable to store and calculate BMI 
c=b/a**2
#output the result
print("your BMI is" , c)
if c<18.5: #if the BMI is less than 18.5
    print("Underweight") #print "Underweight"
elif c>=18.5 and c<30: #if the BMI is greater than or equal to 18.5 and less than 30
    print("Normal weight") #print "Normal weight"
else: #if the BMI is greater than or equal to 30.
    print("Obese") #print "Obese"