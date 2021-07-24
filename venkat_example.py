p = 'Lake'

def myfunc():
    global p
    p = 'School'
    print ("inside func", p)

print ("value is:", p)
myfunc()



