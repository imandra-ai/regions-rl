from collections import defaultdict
def add(d, key, value):
    d = d.copy()
    d[key] = value
    return d

maxCodes = [1,1,3,2,2,3,2,4,4,3,2,2,2,2,2,1,1]

def calculate_regions(arg_action):
  if 0 < arg_action[0].nfuel and arg_action[0].nfuel <= 2:
    if arg_action[0] is None:
      return [0]
    if 0 <= arg_action[0].pos.y and arg_action[0].pos.y <= 3:
      if arg_action[1] is None:
        return [0,0]
      if 0 <= arg_action[0].pos.x and arg_action[0].pos.x <= 3:
        if 3 != arg_action[0].pos.x:
          if arg_action[1].pos.x == 3:
            if arg_action[1].pos.y == 3:
              if arg_action[0].nfuel >= abs(arg_action[0].pos.x - 3) + abs(arg_action[0].pos.y - 3):
                if arg_action[2] is None:
                  return [0,0,0,0,0,0,0]
                if arg_action[2].pos.x == 3:
                  if arg_action[2].pos.y != 3:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if 2 >= abs(3 - 3) + abs(3 - arg_action[2].pos.y):
                        return [0,0,0,0,0,0,0,0,0,0,0]
                      
                    
                  
                if arg_action[2].pos.x != 3:
                  if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if 2 >= abs(3 - arg_action[2].pos.x) + abs(3 - arg_action[2].pos.y):
                        return [0,0,0,0,0,0,0,1,0,0,0]
                      
                    
                  
                
              
            if arg_action[0].nfuel >= abs(arg_action[0].pos.x - 3) + abs(arg_action[0].pos.y - arg_action[1].pos.y):
              if 0 <= arg_action[1].pos.y and arg_action[1].pos.y < 3:
                if not(arg_action[0].nmap[arg_action[1].pos]):
                  if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) != abs(arg_action[0].pos.y - arg_action[1].pos.y):
                    if arg_action[2] is None:
                      return [0,0,0,0,0,1,0,0,0]
                    if 2 >= abs(0) + abs(arg_action[1].pos.y - 3):
                      if arg_action[2].pos.x == 3:
                        if arg_action[2].pos.y == 3:
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - 3) + abs(arg_action[1].pos.y - 3):
                            return [0,0,0,0,0,1,0,0,0,0,0,0,0]
                          
                        
                      
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if 2 >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 3:
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(3 - arg_action[2].pos.x) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              if not(arg_action[0].nmap[arg_action[2].pos]):
                                return [0,0,0,0,0,1,0,0,0,2,0,0,0,0,0]
                              
                            if arg_action[0].nmap[arg_action[2].pos]:
                              return [0,0,0,0,0,1,0,0,0,2,0,0,0,1]
                            
                          
                        if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                          if abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                            return [0,0,0,0,0,1,0,0,0,2,0,1,0]
                          
                        
                      
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y != arg_action[1].pos.y:
                        if 2 >= abs(0) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(3 - 3) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              if not(arg_action[0].nmap[arg_action[2].pos]):
                                if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 3:
                                  return [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0]
                                
                              
                            
                          
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                          if 2 >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                              return [0,0,0,0,0,1,0,0,0,1,0,1,0,0]
                            
                          
                        
                      if 2 >= abs(0) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if arg_action[0].nmap[arg_action[2].pos]:
                            if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 3:
                              return [0,0,0,0,0,1,0,0,0,1,1,0,0,0]
                            
                          
                        
                      
                    
                  if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                    if arg_action[2] is None:
                      return [0,0,0,0,0,1,0,0,1]
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y != arg_action[1].pos.y:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                          if 2 >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            return [0,0,0,0,0,1,0,0,1,0,0,0,0]
                          
                        
                      
                    if arg_action[2].pos.x != 3:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                          if 2 >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            return [0,0,0,0,0,1,0,0,1,1,0,0,0]
                          
                        
                      
                    
                  
                if arg_action[0].nmap[arg_action[1].pos]:
                  if arg_action[2] is None:
                    return [0,0,0,0,0,1,0,1]
                  if 2 >= abs(0) + abs(arg_action[1].pos.y - 3):
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y == 3:
                        return [0,0,0,0,0,1,0,1,0,0,0]
                      
                    
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                    if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 3:
                      if 2 >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          return [0,0,0,0,0,1,0,1,2,0,0,0]
                        if abs(3 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                          if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                            return [0,0,0,0,0,1,0,1,2,0,0,1,0]
                          
                        
                      if abs(3 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          return [0,0,0,0,0,1,0,1,2,0,1,0]
                        
                      
                    
                  if arg_action[2].pos.x == 3:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 3:
                      if 2 >= abs(0) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if arg_action[2].pos.y != arg_action[1].pos.y:
                          if abs(3 - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                            if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                              return [0,0,0,0,0,1,0,1,1,0,0,0,0,0]
                            
                          
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          return [0,0,0,0,0,1,0,1,1,0,0,1]
                        
                      if arg_action[2].pos.y != arg_action[1].pos.y:
                        if abs(3 - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                          if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                            return [0,0,0,0,0,1,0,1,1,0,1,0,0]
                          
                        
                      
                    
                  
                
              
            
          
        if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 3:
          if arg_action[0].nfuel >= abs(arg_action[0].pos.x - arg_action[1].pos.x) + abs(arg_action[0].pos.y - arg_action[1].pos.y):
            if arg_action[1].pos.x != arg_action[0].pos.x:
              if 0 <= arg_action[1].pos.x and arg_action[1].pos.x < 3:
                if not(arg_action[0].nmap[arg_action[1].pos]):
                  if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) != abs(arg_action[0].pos.y - arg_action[1].pos.y):
                    if arg_action[2] is None:
                      return [0,0,0,1,0,0,0,0,0]
                    if 2 >= abs(arg_action[1].pos.x - 3) + abs(arg_action[1].pos.y - 3):
                      if arg_action[2].pos.x == 3:
                        if arg_action[2].pos.y == 3:
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[1].pos.x - 3) + abs(arg_action[1].pos.y - 3):
                            return [0,0,0,1,0,0,0,0,0,0,0,0,0]
                          
                        
                      
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if 2 >= abs(arg_action[1].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if arg_action[2].pos.x != arg_action[1].pos.x:
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(arg_action[1].pos.x - arg_action[2].pos.x) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 3:
                              if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[1].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                                if not(arg_action[0].nmap[arg_action[2].pos]):
                                  return [0,0,0,1,0,0,0,0,0,2,0,0,0,0,0,0]
                                
                              
                            
                          if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                            if abs(arg_action[1].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                              return [0,0,0,1,0,0,0,0,0,2,0,0,1,0]
                            
                          
                        if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 3:
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[1].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if arg_action[0].nmap[arg_action[2].pos]:
                              return [0,0,0,1,0,0,0,0,0,2,0,1,0,0]
                            
                          
                        
                      
                    if arg_action[2].pos.x == 3:
                      if 2 >= abs(arg_action[1].pos.x - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[1].pos.x - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 3:
                            if arg_action[0].nmap[arg_action[2].pos]:
                              return [0,0,0,1,0,0,0,0,0,1,0,0,0,0]
                            if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(arg_action[1].pos.x - 3) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              if not(arg_action[0].nmap[arg_action[2].pos]):
                                return [0,0,0,1,0,0,0,0,0,1,0,0,0,1,0]
                              
                            
                          
                        
                      
                    
                  if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                    if arg_action[2] is None:
                      return [0,0,0,1,0,0,0,0,1]
                    if arg_action[2].pos.x != arg_action[1].pos.x:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                          if 2 >= abs(arg_action[1].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            return [0,0,0,1,0,0,0,0,1,0,0,0,0]
                          
                        
                      
                    
                  
                if arg_action[0].nmap[arg_action[1].pos]:
                  if arg_action[2] is None:
                    return [0,0,0,1,0,0,0,1]
                  if 2 >= abs(arg_action[1].pos.x - 3) + abs(arg_action[1].pos.y - 3):
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y == 3:
                        return [0,0,0,1,0,0,0,1,0,0,0]
                      
                    
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                    if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 3:
                      if arg_action[2].pos.x != arg_action[1].pos.x:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          if 2 >= abs(arg_action[1].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                              return [0,0,0,1,0,0,0,1,2,0,0,0,0,0]
                            
                          if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                            return [0,0,0,1,0,0,0,1,2,0,0,0,1]
                          
                        
                      if 2 >= abs(arg_action[1].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          return [0,0,0,1,0,0,0,1,2,0,1,0]
                        
                      
                    
                  if arg_action[2].pos.x == 3:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 3:
                      if 2 >= abs(arg_action[1].pos.x - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if abs(arg_action[1].pos.x - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                          if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                            return [0,0,0,1,0,0,0,1,1,0,0,0,0]
                          
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          return [0,0,0,1,0,0,0,1,1,0,0,1]
                        
                      if abs(arg_action[1].pos.x - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          return [0,0,0,1,0,0,0,1,1,0,1,0]
                        
                      
                    
                  
                
              
            if arg_action[0].nmap[arg_action[1].pos]:
              if arg_action[2] is None:
                return [0,0,0,1,0,2]
              if arg_action[2].pos.x == arg_action[1].pos.x:
                if arg_action[2].pos.y != arg_action[1].pos.y:
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                    if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                      if abs(arg_action[1].pos.x - arg_action[1].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                        return [0,0,0,1,0,2,0,0,0,0,0]
                      if 2 >= abs(arg_action[1].pos.x - arg_action[1].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if abs(arg_action[1].pos.x - arg_action[1].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                          return [0,0,0,1,0,2,0,0,0,0,1,0]
                        
                      
                    
                  
                
              
            if not(arg_action[0].nmap[arg_action[1].pos]):
              if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) != abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if arg_action[2] is None:
                  return [0,0,0,1,0,1,0]
                if arg_action[2].pos.x == arg_action[1].pos.x:
                  if arg_action[2].pos.y != arg_action[1].pos.y:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if 2 >= abs(arg_action[1].pos.x - arg_action[1].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(arg_action[1].pos.x - arg_action[1].pos.x) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[1].pos.x - arg_action[1].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if not(arg_action[0].nmap[arg_action[2].pos]):
                              return [0,0,0,1,0,1,0,0,0,0,0,0,0,0]
                            
                          
                        if abs(arg_action[1].pos.x - arg_action[1].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                          return [0,0,0,1,0,1,0,0,0,0,0,1]
                        
                      
                    
                  
                
              if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[1].pos.x) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if arg_action[2] is None:
                  return [0,0,0,1,0,1,1]
                if arg_action[2].pos.x == arg_action[1].pos.x:
                  if arg_action[2].pos.y != arg_action[1].pos.y:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if 2 >= abs(arg_action[1].pos.x - arg_action[1].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        return [0,0,0,1,0,1,1,0,0,0,0]
                      
                    
                  
                
              
            
          if 2 >= abs(arg_action[0].pos.x - arg_action[1].pos.x) + abs(arg_action[0].pos.y - arg_action[1].pos.y):
            if abs(arg_action[0].pos.x - arg_action[1].pos.x) + abs(arg_action[0].pos.y - arg_action[1].pos.y) > arg_action[0].nfuel:
              if arg_action[2] is None:
                return [0,0,0,1,1,0]
              if arg_action[1].pos.x != arg_action[0].pos.x:
                if 0 <= arg_action[1].pos.x and arg_action[1].pos.x <= 3:
                  if arg_action[2].pos.x != arg_action[1].pos.x:
                    if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                      if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                        return [0,0,0,1,1,0,0,0,0,0,0]
                      
                    
                  
                
              if arg_action[2].pos.x == arg_action[1].pos.x:
                if arg_action[2].pos.y != arg_action[1].pos.y:
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                    return [0,0,0,1,1,0,1,0,0]
                  
                
              
            
          
        
      if arg_action[1].pos.x == arg_action[0].pos.x:
        if arg_action[1].pos.y != arg_action[0].pos.y:
          if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 3:
            if arg_action[0].nfuel >= abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[0].pos.y - arg_action[1].pos.y):
              if not(arg_action[0].nmap[arg_action[1].pos]):
                if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) != abs(arg_action[0].pos.y - arg_action[1].pos.y):
                  if arg_action[2] is None:
                    return [0,0,2,0,0,0,0,0]
                  if 2 >= abs(arg_action[0].pos.x - 3) + abs(arg_action[1].pos.y - 3):
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y == 3:
                        if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[0].pos.x - 3) + abs(arg_action[1].pos.y - 3):
                          return [0,0,2,0,0,0,0,0,0,0,0,0]
                        
                      
                    
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                    if 2 >= abs(arg_action[0].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 3:
                        if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[0].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if arg_action[0].nmap[arg_action[2].pos]:
                            return [0,0,2,0,0,0,0,0,3,0,0,0,0]
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(arg_action[0].pos.x - arg_action[2].pos.x) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if not(arg_action[0].nmap[arg_action[2].pos]):
                              return [0,0,2,0,0,0,0,0,3,0,0,0,1,0]
                            
                          
                        
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                        if abs(arg_action[0].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                          return [0,0,2,0,0,0,0,0,3,0,1,0]
                        
                      
                    
                  if arg_action[2].pos.x == 3:
                    if 2 >= abs(arg_action[0].pos.x - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                      if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[0].pos.x - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 3:
                          if arg_action[0].nmap[arg_action[2].pos]:
                            return [0,0,2,0,0,0,0,0,1,0,0,0,0]
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(arg_action[0].pos.x - 3) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if not(arg_action[0].nmap[arg_action[2].pos]):
                              return [0,0,2,0,0,0,0,0,1,0,0,0,1,0]
                            
                          
                        
                      
                    
                  if arg_action[2].pos.x == arg_action[0].pos.x:
                    if arg_action[2].pos.y != arg_action[1].pos.y:
                      if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                        if 2 >= abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                            return [0,0,2,0,0,0,0,0,2,0,0,0,0]
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(arg_action[0].pos.x - arg_action[0].pos.x) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              if not(arg_action[0].nmap[arg_action[2].pos]):
                                return [0,0,2,0,0,0,0,0,2,0,0,0,1,0,0]
                              
                            
                          
                        
                      
                    
                  
                if arg_action[0].nfuel - abs(arg_action[0].pos.x - arg_action[0].pos.x) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                  if arg_action[2] is None:
                    return [0,0,2,0,0,0,0,1]
                  if arg_action[2].pos.x == arg_action[0].pos.x:
                    if arg_action[2].pos.y != arg_action[1].pos.y:
                      if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                        if 2 >= abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          return [0,0,2,0,0,0,0,1,0,0,0,0]
                        
                      
                    
                  if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if 2 >= abs(arg_action[0].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                        return [0,0,2,0,0,0,0,1,1,0,0]
                      
                    
                  
                
              if arg_action[0].nmap[arg_action[1].pos]:
                if arg_action[2] is None:
                  return [0,0,2,0,0,0,1]
                if 2 >= abs(arg_action[0].pos.x - 3) + abs(arg_action[1].pos.y - 3):
                  if arg_action[2].pos.x == 3:
                    if arg_action[2].pos.y == 3:
                      return [0,0,2,0,0,0,1,0,0,0]
                    
                  
                if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                  if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 3:
                    if 2 >= abs(arg_action[0].pos.x - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                      if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          return [0,0,2,0,0,0,1,3,0,0,0,0]
                        
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        return [0,0,2,0,0,0,1,3,0,0,1]
                      
                    if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        return [0,0,2,0,0,0,1,3,0,1,0]
                      
                    
                  
                if arg_action[2].pos.x == 3:
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 3:
                    if 2 >= abs(arg_action[0].pos.x - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                      if abs(arg_action[0].pos.x - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          return [0,0,2,0,0,0,1,1,0,0,0,0]
                        
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        return [0,0,2,0,0,0,1,1,0,0,1]
                      
                    if abs(arg_action[0].pos.x - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        return [0,0,2,0,0,0,1,1,0,1,0]
                      
                    
                  
                if arg_action[2].pos.x == arg_action[0].pos.x:
                  if arg_action[2].pos.y != arg_action[1].pos.y:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        if 2 >= abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if abs(arg_action[0].pos.x - arg_action[0].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                            return [0,0,2,0,0,0,1,2,0,0,0,0,0]
                          
                        if abs(arg_action[0].pos.x - arg_action[0].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                          return [0,0,2,0,0,0,1,2,0,0,0,1]
                        
                      
                    
                  
                
              
            if 2 >= abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[0].pos.y - arg_action[1].pos.y):
              if abs(arg_action[0].pos.x - arg_action[0].pos.x) + abs(arg_action[0].pos.y - arg_action[1].pos.y) > arg_action[0].nfuel:
                if arg_action[2] is None:
                  return [0,0,2,0,0,1,0]
                if arg_action[2].pos.x == arg_action[0].pos.x:
                  if arg_action[2].pos.y != arg_action[1].pos.y:
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                      return [0,0,2,0,0,1,0,0,0,0]
                    
                  
                if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 3:
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 3:
                    return [0,0,2,0,0,1,0,1,0]
                  
                
              
            
          
        
      if 3 == arg_action[0].pos.x:
        if 3 != arg_action[0].pos.y:
          if arg_action[1].pos.x == 3:
            if arg_action[1].pos.y == 3:
              if arg_action[0].nfuel >= abs(arg_action[0].pos.x - 3) + abs(arg_action[0].pos.y - 3):
                if arg_action[2] is None:
                  return [0,0,1,0,0,0,0]
                if arg_action[2].pos.x == 3:
                  if arg_action[2].pos.y != 3:
                    if arg_action[2].pos.y >= 0:
                      if 2 >= abs(3 - 3) + abs(3 - arg_action[2].pos.y):
                        return [0,0,1,0,0,0,0,0,0,0,0]
                      
                    
                  
                if arg_action[2].pos.x != 3:
                  if arg_action[2].pos.x >= 0:
                    if arg_action[2].pos.y >= 0:
                      if 2 >= abs(3 - arg_action[2].pos.x) + abs(3 - arg_action[2].pos.y):
                        return [0,0,1,0,0,0,0,1,0,0,0]
                      
                    
                  
                
              
            
          
        if arg_action[1].pos.x == 3:
          if arg_action[1].pos.y != arg_action[0].pos.y:
            if arg_action[1].pos.y >= 0:
              if arg_action[0].nfuel >= abs(arg_action[0].pos.x - 3) + abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if not(arg_action[0].nmap[arg_action[1].pos]):
                  if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) != abs(arg_action[0].pos.y - arg_action[1].pos.y):
                    if arg_action[2] is None:
                      return [0,0,1,1,0,0,0,0,0]
                    if 2 >= abs(0) + abs(arg_action[1].pos.y - 3):
                      if arg_action[2].pos.x == 3:
                        if arg_action[2].pos.y == 3:
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - 3) + abs(arg_action[1].pos.y - 3):
                            return [0,0,1,1,0,0,0,0,0,0,0,0,0]
                          
                        
                      
                    if arg_action[2].pos.x >= 0:
                      if arg_action[2].pos.y >= 0:
                        if 2 >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if arg_action[2].pos.x != 3:
                            if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(3 - arg_action[2].pos.x) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                                if not(arg_action[0].nmap[arg_action[2].pos]):
                                  return [0,0,1,1,0,0,0,0,0,2,0,0,0,0,0,0]
                                
                              if arg_action[0].nmap[arg_action[2].pos]:
                                return [0,0,1,1,0,0,0,0,0,2,0,0,0,0,1]
                              
                            
                          if abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                            return [0,0,1,1,0,0,0,0,0,2,0,0,1]
                          
                        
                      
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y >= 0:
                        if arg_action[2].pos.y != arg_action[1].pos.y:
                          if 2 >= abs(0) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) - abs(3 - 3) == abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                                if not(arg_action[0].nmap[arg_action[2].pos]):
                                  if arg_action[2].pos.y != 3:
                                    return [0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0]
                                  
                                
                              
                            
                          if 2 >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y) > arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y):
                              return [0,0,1,1,0,0,0,0,0,1,0,0,1,0]
                            
                          
                        if 2 >= abs(0) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) - abs(arg_action[0].pos.y - arg_action[1].pos.y) >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            if arg_action[0].nmap[arg_action[2].pos]:
                              if arg_action[2].pos.y != 3:
                                return [0,0,1,1,0,0,0,0,0,1,0,1,0,0,0]
                              
                            
                          
                        
                      
                    
                  if arg_action[0].nfuel - abs(arg_action[0].pos.x - 3) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                    if arg_action[2] is None:
                      return [0,0,1,1,0,0,0,0,1]
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y != arg_action[1].pos.y:
                        if arg_action[2].pos.y >= 0:
                          if 2 >= abs(3 - 3) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            return [0,0,1,1,0,0,0,0,1,0,0,0,0]
                          
                        
                      
                    if arg_action[2].pos.x != 3:
                      if arg_action[2].pos.x >= 0:
                        if arg_action[2].pos.y >= 0:
                          if 2 >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            return [0,0,1,1,0,0,0,0,1,1,0,0,0]
                          
                        
                      
                    
                  
                if arg_action[0].nmap[arg_action[1].pos]:
                  if arg_action[2] is None:
                    return [0,0,1,1,0,0,0,1]
                  if 2 >= abs(0) + abs(arg_action[1].pos.y - 3):
                    if arg_action[2].pos.x == 3:
                      if arg_action[2].pos.y == 3:
                        return [0,0,1,1,0,0,0,1,0,0,0]
                      
                    
                  if arg_action[2].pos.x >= 0:
                    if arg_action[2].pos.y >= 0:
                      if arg_action[2].pos.x != 3:
                        if 2 >= abs(3 - arg_action[2].pos.x) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                            return [0,0,1,1,0,0,0,1,2,0,0,0,0]
                          if abs(3 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                            if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                              return [0,0,1,1,0,0,0,1,2,0,0,0,1,0]
                            
                          
                        if abs(3 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                          if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                            return [0,0,1,1,0,0,0,1,2,0,0,1,0]
                          
                        
                      
                    
                  if arg_action[2].pos.x == 3:
                    if arg_action[2].pos.y >= 0:
                      if arg_action[2].pos.y != 3:
                        if 2 >= abs(0) + abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          if arg_action[2].pos.y != arg_action[1].pos.y:
                            if abs(3 - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) != -2:
                              if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                                return [0,0,1,1,0,0,0,1,1,0,0,0,0,0,0]
                              
                            
                          if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                            return [0,0,1,1,0,0,0,1,1,0,0,0,1]
                          
                        if arg_action[2].pos.y != arg_action[1].pos.y:
                          if abs(3 - 3) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -2:
                            if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                              return [0,0,1,1,0,0,0,1,1,0,0,1,0,0]
                            
                          
                        
                      
                    
                  
                
              
            
          
        
      
    
  
