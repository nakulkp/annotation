# SAFE EXAMPLES. DO THIS!
# SELECT exists (SELECT 1 FROM table WHERE column = <value> LIMIT 1);
# cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});

inval = {"user": "nakul", "pass": "password"}
print(inval["user"])
