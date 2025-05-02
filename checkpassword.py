from bcrypt import gensalt, hashpw


new_password = "newpassword123"  # Set your new password here
hashed = hashpw(new_password.encode(), gensalt())

print(hashed.decode())  # Store this in the database
