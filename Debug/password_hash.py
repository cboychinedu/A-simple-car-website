# importing the necessary modules 
import bcrypt 

# Setting the user password 
password = "user_password";
enc_password = password.encode("utf-8");  

# Create a hash value for the password 
hashed = bcrypt.hashpw(enc_password, bcrypt.gensalt(5));
print(hashed);  