def create_bijection(domain, codomain):
  
    if len(domain) != len(codomain):
        return None  

    bijection = {}  

    
    for i in range(len(domain)):
        bijection[domain[i]] = codomain[i]

  
    reverse_bijection = {v: k for k, v in bijection.items()}
    if reverse_bijection == dict(zip(codomain, domain)):
        return bijection  
    else:
        return None  


domain = [1, 2, 3, 4, 5]
codomain = [10, 20, 30, 40, 50]

bijection_result = create_bijection(domain, codomain)

if bijection_result:
    print("The function is a bijection.")
else:
    print("The function is not a bijection.")
