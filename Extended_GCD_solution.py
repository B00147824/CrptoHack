a = 26513
b = 32321

if a < b:
    a,b = b,a  # Reversing the order of the given

r1,r2 = a,b
s1,s2 = 1,0
t1,t2 = 0,1

while r2 > 0:
    # The next line is just the computation for the GCD
    q,r = divmod(r1,r2)  
    r1,r2 = r2,r
    
    # The next line is for the computation of the Bézout's identity
    s1,s2 = s2,s1 - q * s2
    t1,t2 = t2,t1 - q * t2

print(f"GCD:{r1}, u:{t1}, v:{s1}")