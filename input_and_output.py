#use (input()to take any input,(print()to give output)).
#creating a variable->assigning a value to that variable->printing the value.
#we will simply solve a problem by using input and output function
#we will caluclate area of rectangle by getting inputs of length and breath.
#take the input as integer format or float beacause without intializing python takes that value as a string.
length = int(input("enter the length of the rectangle"))
breath = int(input("enter the breath of the rectangle"))
#we got two inputs l and b ,area of rectangle is l*b.so we just multiply both of them to give are.
area_rect = length * breath
#using (f"  ")f gives the format function to five correct format
print(f"The area of the rectangle is :",{area_rect})
