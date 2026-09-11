# Born = int(input("Enter your Born : "))

# if Born>=18:
#     print("You can Drive")
# else:
#     print("You cannot Drive")


# . if ... elif ... else

Born = int(input("Enter your Birth Date  : "))

if Born<=1980:
    print("GEN X") 
elif Born<=1996:
    print("GEN Y")
elif Born<=2012:
    print("GEN Z")
else:
    print("NOT DEFINE")

# opt and if else

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")



