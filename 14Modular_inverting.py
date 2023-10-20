def mod_Inv(x,y):
    for d in range(y):
        if ( x * d ) % y == 1:
            return d

print( "MMI is ", mod_Inv(3,13) )