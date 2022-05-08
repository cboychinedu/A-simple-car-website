# Importing the necessay modules 
import bcrypt 

# 
hashed = b'$2b$05$h2PvTxSsBGZWO6U27mEzhuwyVUEYmV.eYcwRy7NE4OM..w/r0jQou'

# 
password = "user_password"
password = password.encode("utf-8"); 

# Check if the user password was a match 
matched = bcrypt.checkpw(password, hashed)
print(matched); 