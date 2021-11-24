# global keyword is the connector between local and global variable.

var1 = 10

def increment():
    global var1
    var1 += 5
    print(var1)

increment()

# Tried using return.........
# var1 = 10

# def increment():
#     global var1
#     var1 += 5
#     return var1

# increment()