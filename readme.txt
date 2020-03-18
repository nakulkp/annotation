
****** DB Related Files ******
Add database related info to database.ini
config.py reads info from database.ini and returns the connection parameters
checkDBConnection.py is used to connect to DB Server and return it's version number
*************************************************************************************

Add python dependencies to requirements.txt

*************************************************************************************
passHash.py :
    Used to hash password (called key)
    Input   :   Takes plaintext password
    Returns  :   salt and key respectively

passVerify.py   :
    Used to verify if the user has input the correct password is correct
    Input   :   salt, key, and plain text password respectively
    Returns  :   True, if password correct; else False

