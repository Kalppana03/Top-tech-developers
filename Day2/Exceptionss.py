name="kalppana"
passw="123@4"
n=input("User name:")
p=input("password: ")
try:
    if n!=name:
        raise ValueError("Invalid username")
    if p!=passw:
        raise ValueError("Invalid password")
    print("Successfull login!!")
except ValueError as e:
    print("Error!!! ",e)