

def rverseflp (text):

     result = []
     #name = 'umair mufti'
     splited = text.split()

     for naam in splited:
          result.append(naam[::-1])
     return' '.join(result)

print(rverseflp('umair mufti'))