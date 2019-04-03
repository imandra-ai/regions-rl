maxCodes = [2,1,3,3,2,2,3,2,2,3,2,3,3,3,3,2,2,2,2,2,1]

from collections import defaultdict
def add(d, key, value):
    d = d.copy()
    d[key] = value
    return d


def calculate_regions(arg_action):
  if arg_action[0].nfuel == 1:
    if arg_action[0] is None:
      return [0]
    if 0 <= arg_action[0].pos.x and arg_action[0].pos.x <= 2:
      if 0 <= arg_action[0].pos.y and arg_action[0].pos.y <= 2:
        if arg_action[1] is None:
          return [0,0,0]
        if 2 != arg_action[0].pos.x:
          if arg_action[1].pos.x == 2:
            if abs(arg_action[0].pos.x - 2) == 1:
              if abs(arg_action[0].pos.y - arg_action[1].pos.y) == 1:
                if not(arg_action[0].nmap[arg_action[1].pos]):
                  if 0 <= arg_action[1].pos.y and arg_action[1].pos.y < 2:
                    if arg_action[2] is None:
                      return [0,0,0,0,0,0,0,0,0]
                    if arg_action[2].pos.x == 2:
                      if 1 >= abs(2 - 2):
                        if arg_action[2].pos.y != arg_action[1].pos.y:
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                            
                          
                        
                      
                    if arg_action[2].pos.x != 2:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 2:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(2 - arg_action[2].pos.x):
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,0,0,0,0,0,0,1,0,0,0,0]
                            
                          
                        
                      
                    
                  
                
              
            
          
        if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 2:
          if not(arg_action[0].nmap[arg_action[1].pos]):
            if abs(arg_action[0].pos.y - arg_action[1].pos.y) == 1:
              if 0 <= arg_action[1].pos.x and arg_action[1].pos.x < 2:
                if arg_action[1].pos.x != arg_action[0].pos.x:
                  if abs(arg_action[0].pos.x - arg_action[1].pos.x) == 1:
                    if arg_action[2] is None:
                      return [0,0,0,2,0,0,0,0,0]
                    if arg_action[2].pos.x != arg_action[1].pos.x:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 2:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(arg_action[1].pos.x - arg_action[2].pos.x):
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,2,0,0,0,0,0,0,0,0,0,0]
                            
                          
                        
                      
                    
                  
                if 1 - abs(arg_action[0].pos.x - arg_action[1].pos.x) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                  if abs(arg_action[0].pos.x - arg_action[1].pos.x) == 0:
                    if arg_action[2] is None:
                      return [0,0,0,2,0,0,0,1,0]
                    if arg_action[2].pos.x != arg_action[1].pos.x:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 2:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(arg_action[1].pos.x - arg_action[2].pos.x):
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,2,0,0,0,1,0,0,0,0,0,0]
                            
                          
                        
                      
                    
                  
                
              if 1 - abs(arg_action[0].pos.x - arg_action[1].pos.x) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if abs(arg_action[0].pos.x - arg_action[1].pos.x) == 0:
                  if arg_action[2] is None:
                    return [0,0,0,2,0,0,2,0]
                  if arg_action[2].pos.x == arg_action[1].pos.x:
                    if 1 >= abs(arg_action[1].pos.x - arg_action[1].pos.x):
                      if arg_action[2].pos.y != arg_action[1].pos.y:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            return [0,0,0,2,0,0,2,0,0,0,0,0,0]
                          
                        
                      
                    
                  
                
              if abs(arg_action[0].pos.x - arg_action[1].pos.x) == 1:
                if arg_action[2] is None:
                  return [0,0,0,2,0,0,1]
                if arg_action[2].pos.x == arg_action[1].pos.x:
                  if 1 >= abs(arg_action[1].pos.x - arg_action[1].pos.x):
                    if arg_action[2].pos.y != arg_action[1].pos.y:
                      if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                        if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                          return [0,0,0,2,0,0,1,0,0,0,0,0]
                        
                      
                    
                  
                
              
            if abs(arg_action[0].pos.y - arg_action[1].pos.y) == 0:
              if 1 - abs(arg_action[0].pos.x - arg_action[1].pos.x) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if abs(arg_action[0].pos.x - arg_action[1].pos.x) == 1:
                  if arg_action[2] is None:
                    return [0,0,0,2,0,1,0,0]
                  if 0 <= arg_action[1].pos.x and arg_action[1].pos.x < 2:
                    if arg_action[2].pos.x != arg_action[1].pos.x:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 2:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(arg_action[1].pos.x - arg_action[2].pos.x):
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,2,0,1,0,0,0,0,0,0,0,0]
                            
                          
                        
                      
                    
                  if arg_action[2].pos.x == arg_action[1].pos.x:
                    if 1 >= abs(arg_action[1].pos.x - arg_action[1].pos.x):
                      if arg_action[2].pos.y != arg_action[1].pos.y:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                            return [0,0,0,2,0,1,0,0,1,0,0,0,0]
                          
                        
                      
                    
                  
                
              
            
          
        if arg_action[1].pos.x == 2:
          if abs(arg_action[0].pos.x - 2) == 1:
            if abs(arg_action[0].pos.y - arg_action[1].pos.y) == 0:
              if 1 - abs(arg_action[0].pos.x - 2) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if not(arg_action[0].nmap[arg_action[1].pos]):
                  if 0 <= arg_action[1].pos.y and arg_action[1].pos.y < 2:
                    if arg_action[2] is None:
                      return [0,0,0,1,0,0,0,0,0]
                    if arg_action[2].pos.x == 2:
                      if 1 >= abs(2 - 2):
                        if arg_action[2].pos.y != arg_action[1].pos.y:
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,1,0,0,0,0,0,0,0,0,0,0]
                            
                          
                        
                      
                    if arg_action[2].pos.x != 2:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 2:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(2 - arg_action[2].pos.x):
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,1,0,0,0,0,0,1,0,0,0,0]
                            
                          
                        
                      
                    
                  
                
              
            
          if abs(arg_action[0].pos.x - 2) == 0:
            if abs(arg_action[0].pos.y - arg_action[1].pos.y) == 1:
              if 1 - abs(arg_action[0].pos.x - 2) == abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if not(arg_action[0].nmap[arg_action[1].pos]):
                  if 0 <= arg_action[1].pos.y and arg_action[1].pos.y < 2:
                    if arg_action[2] is None:
                      return [0,0,0,1,1,0,0,0,0]
                    if arg_action[2].pos.x == 2:
                      if 1 >= abs(2 - 2):
                        if arg_action[2].pos.y != arg_action[1].pos.y:
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,1,1,0,0,0,0,0,0,0,0,0]
                            
                          
                        
                      
                    if arg_action[2].pos.x != 2:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 2:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(2 - arg_action[2].pos.x):
                            if 1 >= abs(arg_action[1].pos.y - arg_action[2].pos.y):
                              return [0,0,0,1,1,0,0,0,0,1,0,0,0,0]
                            
                          
                        
                      
                    
                  
                
              
            
          
        
      
    
  if 0 < arg_action[0].nfuel and arg_action[0].nfuel <= 1:
    if arg_action[0] is None:
      return [1]
    if 0 <= arg_action[0].pos.y and arg_action[0].pos.y <= 2:
      if arg_action[1] is None:
        return [1,0]
      if 0 <= arg_action[0].pos.x and arg_action[0].pos.x <= 2:
        if 2 != arg_action[0].pos.x:
          if 1 >= abs(arg_action[0].pos.x - 2):
            if 1 >= abs(arg_action[0].pos.y - 2):
              if arg_action[1].pos.x == 2:
                if arg_action[1].pos.y == 2:
                  if arg_action[2] is None:
                    return [1,0,0,0,0,0,0,0]
                  if arg_action[2].pos.x == 2:
                    if 1 >= abs(2 - 2):
                      if arg_action[2].pos.y != 2:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                          if 1 >= abs(2 - arg_action[2].pos.y):
                            return [1,0,0,0,0,0,0,0,0,0,0,0,0]
                          
                        
                      
                    
                  if arg_action[2].pos.x != 2:
                    if 0 <= arg_action[2].pos.x and arg_action[2].pos.x <= 2:
                      if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                        if 1 >= abs(2 - arg_action[2].pos.x):
                          if 1 >= abs(2 - arg_action[2].pos.y):
                            return [1,0,0,0,0,0,0,0,1,0,0,0,0]
                          
                        
                      
                    
                  
                
              
            if arg_action[1].pos.x == 2:
              if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if arg_action[0].nmap[arg_action[1].pos]:
                  if 0 <= arg_action[1].pos.y and arg_action[1].pos.y < 2:
                    if arg_action[2] is None:
                      return [1,0,0,0,0,1,0,0,0]
                    if 1 >= abs(arg_action[1].pos.y - 2):
                      if arg_action[2].pos.x == 2:
                        if arg_action[2].pos.y == 2:
                          if arg_action[3] is None:
                            return [1,0,0,0,0,1,0,0,0,0,0,0]
                          if arg_action[3].pos.x == 2:
                            if 1 >= abs(2 - 2):
                              if arg_action[3].pos.y != 2:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                  if 1 >= abs(2 - arg_action[3].pos.y):
                                    return [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
                                  
                                
                              
                            
                          if arg_action[3].pos.x != 2:
                            if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                              if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                if 1 >= abs(2 - arg_action[3].pos.x):
                                  if 1 >= abs(2 - arg_action[3].pos.y):
                                    return [1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]
                                  
                                
                              
                            
                          
                        
                      
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 2:
                        if 1 >= abs(2 - arg_action[2].pos.x):
                          if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                            if arg_action[3] is None:
                              return [1,0,0,0,0,1,0,0,0,2,0,0,0]
                            if 1 >= abs(arg_action[2].pos.x - 2):
                              if 1 >= abs(arg_action[2].pos.y - 2):
                                if arg_action[3].pos.x == 2:
                                  if arg_action[3].pos.y == 2:
                                    return [1,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0,0]
                                  
                                
                              if arg_action[3].pos.x == 2:
                                if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                  if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                      return [1,0,0,0,0,1,0,0,0,2,0,0,0,0,1,0,0,0]
                                    
                                  
                                
                              
                            if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                              if 0 <= arg_action[3].pos.x and arg_action[3].pos.x < 2:
                                if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                  if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                    if arg_action[3].pos.x != arg_action[2].pos.x:
                                      if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                        return [1,0,0,0,0,1,0,0,0,2,0,0,0,2,0,0,0,0,0]
                                      
                                    if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                      if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 0:
                                        return [1,0,0,0,0,1,0,0,0,2,0,0,0,2,0,0,0,1,0]
                                      
                                    
                                  if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                    if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                      if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                        return [1,0,0,0,0,1,0,0,0,2,0,0,0,2,0,0,1,0,0]
                                      
                                    
                                  
                                if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                  if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                    if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                      return [1,0,0,0,0,1,0,0,0,2,0,0,0,2,0,1,0,0]
                                    
                                  
                                
                              
                            if arg_action[3].pos.x == 2:
                              if abs(arg_action[2].pos.x - 2) == 1:
                                if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                    if abs(arg_action[2].pos.x - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                      if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                        return [1,0,0,0,0,1,0,0,0,2,0,0,0,1,0,0,0,0,0]
                                      
                                    if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                      return [1,0,0,0,0,1,0,0,0,2,0,0,0,1,0,0,0,1]
                                    
                                  
                                
                              
                            
                          
                        if abs(2 - arg_action[2].pos.x) == 1:
                          if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                            if abs(2 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                              if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                                if arg_action[3] is None:
                                  return [1,0,0,0,0,1,0,0,0,2,0,1,0,0,0]
                                if arg_action[3].pos.x != arg_action[2].pos.x:
                                  if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,0,0,1,0,0,0,2,0,1,0,0,0,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                              if arg_action[3] is None:
                                return [1,0,0,0,0,1,0,0,0,2,0,1,0,1]
                              if arg_action[3].pos.x != arg_action[2].pos.x:
                                if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,0,0,0,1,0,0,0,2,0,1,0,1,0,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      if abs(2 - arg_action[2].pos.x) == 1:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                            if arg_action[3] is None:
                              return [1,0,0,0,0,1,0,0,0,2,1,0,0]
                            if arg_action[3].pos.x == arg_action[2].pos.x:
                              if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                if arg_action[3].pos.y != arg_action[2].pos.y:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,0,0,0,1,0,0,0,2,1,0,0,0,0,0,0,0]
                                    
                                  
                                
                              
                            
                          if abs(2 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                              if arg_action[3] is None:
                                return [1,0,0,0,0,1,0,0,0,2,1,0,1,0]
                              if arg_action[3].pos.x == arg_action[2].pos.x:
                                if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                  if arg_action[3].pos.y != arg_action[2].pos.y:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,0,0,0,1,0,0,0,2,1,0,1,0,0,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      
                    if arg_action[2].pos.x == 2:
                      if abs(2 - 2) == 0:
                        if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                          if abs(2 - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                              if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                                if arg_action[3] is None:
                                  return [1,0,0,0,0,1,0,0,0,1,0,0,0,0,0]
                                if arg_action[3].pos.x == 2:
                                  if 1 >= abs(2 - 2):
                                    if arg_action[3].pos.y != arg_action[2].pos.y:
                                      if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                if arg_action[3].pos.x != 2:
                                  if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(2 - arg_action[3].pos.x):
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                          if arg_action[3] is None:
                            return [1,0,0,0,0,1,0,0,0,1,1,0]
                          if 1 >= abs(arg_action[2].pos.y - 2):
                            if arg_action[3].pos.x == 2:
                              if arg_action[3].pos.y == 2:
                                return [1,0,0,0,0,1,0,0,0,1,1,0,0,0,0]
                              
                            
                          if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                            if 0 <= arg_action[3].pos.x and arg_action[3].pos.x < 2:
                              if abs(2 - arg_action[3].pos.x) == 1:
                                if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                  if abs(2 - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                    if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                      return [1,0,0,0,0,1,0,0,0,1,1,0,2,0,0,0,0,0]
                                    
                                  if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                    return [1,0,0,0,0,1,0,0,0,1,1,0,2,0,0,0,1]
                                  
                                
                              if 1 >= abs(2 - arg_action[3].pos.x):
                                if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                  if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                    return [1,0,0,0,0,1,0,0,0,1,1,0,2,0,1,0,0]
                                  
                                
                              
                            
                          if arg_action[3].pos.x == 2:
                            if abs(2 - 2) == 0:
                              if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                if abs(2 - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                  if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                      return [1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0]
                                    
                                  
                                
                              
                            
                          
                        
                      
                    
                  
                
              
            
          
        if arg_action[1].pos.x != arg_action[0].pos.x:
          if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 2:
            if 1 >= abs(arg_action[0].pos.x - arg_action[1].pos.x):
              if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if 0 <= arg_action[1].pos.x and arg_action[1].pos.x < 2:
                  if arg_action[0].nmap[arg_action[1].pos]:
                    if arg_action[2] is None:
                      return [1,0,0,1,0,0,0,0,0]
                    if 1 >= abs(arg_action[1].pos.x - 2):
                      if 1 >= abs(arg_action[1].pos.y - 2):
                        if arg_action[2].pos.x == 2:
                          if arg_action[2].pos.y == 2:
                            if arg_action[3] is None:
                              return [1,0,0,1,0,0,0,0,0,0,0,0,0]
                            if arg_action[3].pos.x == 2:
                              if 1 >= abs(2 - 2):
                                if arg_action[3].pos.y != 2:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(2 - arg_action[3].pos.y):
                                      return [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                    
                                  
                                
                              
                            if arg_action[3].pos.x != 2:
                              if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                  if 1 >= abs(2 - arg_action[3].pos.x):
                                    if 1 >= abs(2 - arg_action[3].pos.y):
                                      return [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
                                    
                                  
                                
                              
                            
                          
                        
                      if arg_action[2].pos.x == 2:
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                            if arg_action[3] is None:
                              return [1,0,0,1,0,0,0,0,0,0,1,0,0]
                            if 1 >= abs(arg_action[2].pos.y - 2):
                              if arg_action[3].pos.x == 2:
                                if arg_action[3].pos.y == 2:
                                  return [1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]
                                
                              
                            if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                              if 0 <= arg_action[3].pos.x and arg_action[3].pos.x < 2:
                                if abs(2 - arg_action[3].pos.x) == 1:
                                  if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                    if abs(2 - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                      if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                        return [1,0,0,1,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0]
                                      
                                    if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                      return [1,0,0,1,0,0,0,0,0,0,1,0,0,2,0,0,0,1]
                                    
                                  
                                if 1 >= abs(2 - arg_action[3].pos.x):
                                  if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                    if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                      return [1,0,0,1,0,0,0,0,0,0,1,0,0,2,0,1,0,0]
                                    
                                  
                                
                              
                            if arg_action[3].pos.x == 2:
                              if abs(2 - 2) == 0:
                                if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                  if abs(2 - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                    if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                      if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                        return [1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]
                                      
                                    
                                  
                                
                              if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                    return [1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0]
                                  
                                
                              
                            
                          
                        
                      
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 2:
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          if arg_action[3] is None:
                            return [1,0,0,1,0,0,0,0,0,2,0,0]
                          if 1 >= abs(arg_action[2].pos.x - 2):
                            if 1 >= abs(arg_action[2].pos.y - 2):
                              if arg_action[3].pos.x == 2:
                                if arg_action[3].pos.y == 2:
                                  return [1,0,0,1,0,0,0,0,0,2,0,0,0,0,0,0]
                                
                              
                            if arg_action[3].pos.x == 2:
                              if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                    return [1,0,0,1,0,0,0,0,0,2,0,0,0,1,0,0,0]
                                  
                                
                              
                            
                          if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                            if 0 <= arg_action[3].pos.x and arg_action[3].pos.x < 2:
                              if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                  if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                    if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 0:
                                      return [1,0,0,1,0,0,0,0,0,2,0,0,2,0,0,0,0,0]
                                    
                                  if arg_action[3].pos.x != arg_action[2].pos.x:
                                    if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                      return [1,0,0,1,0,0,0,0,0,2,0,0,2,0,0,0,1,0]
                                    
                                  
                                if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                  if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                    if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                      return [1,0,0,1,0,0,0,0,0,2,0,0,2,0,0,1,0,0]
                                    
                                  
                                
                              if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                  if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                    return [1,0,0,1,0,0,0,0,0,2,0,0,2,0,1,0,0]
                                  
                                
                              
                            
                          if arg_action[3].pos.x == 2:
                            if abs(arg_action[2].pos.x - 2) == 1:
                              if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                  if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                    return [1,0,0,1,0,0,0,0,0,2,0,0,1,0,0,0,0]
                                  if abs(arg_action[2].pos.x - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                    if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                      return [1,0,0,1,0,0,0,0,0,2,0,0,1,0,0,0,1,0]
                                    
                                  
                                
                              
                            
                          
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                            if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                              if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 0:
                                if arg_action[3] is None:
                                  return [1,0,0,1,0,0,0,0,0,2,0,1,0,0,0]
                                if arg_action[3].pos.x != arg_action[2].pos.x:
                                  if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,1,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            if arg_action[2].pos.x != arg_action[1].pos.x:
                              if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 1:
                                if arg_action[3] is None:
                                  return [1,0,0,1,0,0,0,0,0,2,0,1,0,1,0]
                                if arg_action[3].pos.x != arg_action[2].pos.x:
                                  if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,1,0,0,0,0,0,2,0,1,0,1,0,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            
                          if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                              if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 1:
                                if arg_action[3] is None:
                                  return [1,0,0,1,0,0,0,0,0,2,0,1,1,0,0]
                                if arg_action[3].pos.x != arg_action[2].pos.x:
                                  if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,1,0,0,0,0,0,2,0,1,1,0,0,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                          if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 1:
                            if arg_action[3] is None:
                              return [1,0,0,1,0,0,0,0,0,2,1,0,0]
                            if arg_action[3].pos.x == arg_action[2].pos.x:
                              if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                if arg_action[3].pos.y != arg_action[2].pos.y:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,0,1,0,0,0,0,0,2,1,0,0,0,0,0,0,0]
                                    
                                  
                                
                              
                            
                          if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 0:
                              if arg_action[3] is None:
                                return [1,0,0,1,0,0,0,0,0,2,1,0,1,0]
                              if arg_action[3].pos.x == arg_action[2].pos.x:
                                if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                  if arg_action[3].pos.y != arg_action[2].pos.y:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,0,1,0,0,0,0,0,2,1,0,1,0,0,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          
                        if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                            if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 1:
                              if arg_action[3] is None:
                                return [1,0,0,1,0,0,0,0,0,2,1,1,0,0]
                              if arg_action[3].pos.x == arg_action[2].pos.x:
                                if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                  if arg_action[3].pos.y != arg_action[2].pos.y:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,0,1,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      
                    if arg_action[2].pos.x == 2:
                      if abs(arg_action[1].pos.x - 2) == 1:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                            if abs(arg_action[1].pos.x - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                              if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                                if arg_action[3] is None:
                                  return [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0]
                                if arg_action[3].pos.x == 2:
                                  if 1 >= abs(2 - 2):
                                    if arg_action[3].pos.y != arg_action[2].pos.y:
                                      if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                if arg_action[3].pos.x != 2:
                                  if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(2 - arg_action[3].pos.x):
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                              if arg_action[3] is None:
                                return [1,0,0,1,0,0,0,0,0,1,0,0,0,1]
                              if arg_action[3].pos.x == 2:
                                if 1 >= abs(2 - 2):
                                  if arg_action[3].pos.y != arg_action[2].pos.y:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]
                                      
                                    
                                  
                                
                              if arg_action[3].pos.x != 2:
                                if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(2 - arg_action[3].pos.x):
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      
                    
                  
                
              
            
          
        
      if arg_action[1].pos.x == arg_action[0].pos.x:
        if 1 >= abs(arg_action[0].pos.x - arg_action[0].pos.x):
          if 1 >= abs(arg_action[0].pos.x - 2):
            if arg_action[1].pos.y != arg_action[0].pos.y:
              if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 2:
                if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
                  if arg_action[0].nmap[arg_action[1].pos]:
                    if arg_action[2] is None:
                      return [1,0,2,0,0,0,0,0,0]
                    if 1 >= abs(arg_action[1].pos.y - 2):
                      if arg_action[2].pos.x == 2:
                        if arg_action[2].pos.y == 2:
                          if arg_action[3] is None:
                            return [1,0,2,0,0,0,0,0,0,0,0,0]
                          if arg_action[3].pos.x == 2:
                            if 1 >= abs(2 - 2):
                              if arg_action[3].pos.y != 2:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                  if 1 >= abs(2 - arg_action[3].pos.y):
                                    return [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                  
                                
                              
                            
                          if arg_action[3].pos.x != 2:
                            if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                              if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                if 1 >= abs(2 - arg_action[3].pos.x):
                                  if 1 >= abs(2 - arg_action[3].pos.y):
                                    return [1,0,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
                                  
                                
                              
                            
                          
                        
                      
                    if arg_action[2].pos.x == 2:
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                          if arg_action[3] is None:
                            return [1,0,2,0,0,0,0,0,0,1,0,0]
                          if 1 >= abs(arg_action[2].pos.y - 2):
                            if arg_action[3].pos.x == 2:
                              if arg_action[3].pos.y == 2:
                                return [1,0,2,0,0,0,0,0,0,1,0,0,0,0,0]
                              
                            
                          if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                            if 0 <= arg_action[3].pos.x and arg_action[3].pos.x < 2:
                              if abs(2 - arg_action[3].pos.x) == 1:
                                if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                  if abs(2 - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                    if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                      return [1,0,2,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0]
                                    
                                  if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                    return [1,0,2,0,0,0,0,0,0,1,0,0,2,0,0,0,1]
                                  
                                
                              if 1 >= abs(2 - arg_action[3].pos.x):
                                if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                  if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                    return [1,0,2,0,0,0,0,0,0,1,0,0,2,0,1,0,0]
                                  
                                
                              
                            
                          if arg_action[3].pos.x == 2:
                            if abs(2 - 2) == 0:
                              if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                if abs(2 - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                  if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                      return [1,0,2,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]
                                    
                                  
                                
                              
                            if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                              if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                  return [1,0,2,0,0,0,0,0,0,1,0,0,1,1,0,0]
                                
                              
                            
                          
                        
                      
                    
                  
                
              
            
          if arg_action[1].pos.y != arg_action[0].pos.y:
            if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 2:
              if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if arg_action[0].nmap[arg_action[1].pos]:
                  if arg_action[2] is None:
                    return [1,0,2,0,1,0,0,0]
                  if arg_action[2].pos.x == 2:
                    if abs(arg_action[0].pos.x - 2) == 1:
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                          if abs(arg_action[0].pos.x - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                              if arg_action[3] is None:
                                return [1,0,2,0,1,0,0,0,0,0,0,0,0,0]
                              if arg_action[3].pos.x == 2:
                                if 1 >= abs(2 - 2):
                                  if arg_action[3].pos.y != arg_action[2].pos.y:
                                    if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                      
                                    
                                  
                                
                              if arg_action[3].pos.x != 2:
                                if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(2 - arg_action[3].pos.x):
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,2,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                            if arg_action[3] is None:
                              return [1,0,2,0,1,0,0,0,0,0,0,0,1]
                            if arg_action[3].pos.x == 2:
                              if 1 >= abs(2 - 2):
                                if arg_action[3].pos.y != arg_action[2].pos.y:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,2,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]
                                    
                                  
                                
                              
                            if arg_action[3].pos.x != 2:
                              if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                  if 1 >= abs(2 - arg_action[3].pos.x):
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,2,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0]
                                    
                                  
                                
                              
                            
                          
                        
                      
                    
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                    if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 2:
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        if arg_action[3] is None:
                          return [1,0,2,0,1,0,0,0,1,0,0]
                        if 1 >= abs(arg_action[2].pos.x - 2):
                          if 1 >= abs(arg_action[2].pos.y - 2):
                            if arg_action[3].pos.x == 2:
                              if arg_action[3].pos.y == 2:
                                return [1,0,2,0,1,0,0,0,1,0,0,0,0,0,0]
                              
                            
                          if arg_action[3].pos.x == 2:
                            if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                              if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                  return [1,0,2,0,1,0,0,0,1,0,0,0,1,0,0,0]
                                
                              
                            
                          
                        if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                          if 0 <= arg_action[3].pos.x and arg_action[3].pos.x < 2:
                            if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                              if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                  if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 0:
                                    return [1,0,2,0,1,0,0,0,1,0,0,2,0,0,0,0,0]
                                  
                                if arg_action[3].pos.x != arg_action[2].pos.x:
                                  if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                    return [1,0,2,0,1,0,0,0,1,0,0,2,0,0,0,1,0]
                                  
                                
                              if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                  if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                    return [1,0,2,0,1,0,0,0,1,0,0,2,0,0,1,0,0]
                                  
                                
                              
                            if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                              if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                  return [1,0,2,0,1,0,0,0,1,0,0,2,0,1,0,0]
                                
                              
                            
                          
                        if arg_action[3].pos.x == 2:
                          if abs(arg_action[2].pos.x - 2) == 1:
                            if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                              if 0 <= arg_action[3].pos.y and arg_action[3].pos.y < 2:
                                if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                  return [1,0,2,0,1,0,0,0,1,0,0,1,0,0,0,0]
                                if abs(arg_action[2].pos.x - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                  if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                    return [1,0,2,0,1,0,0,0,1,0,0,1,0,0,0,1,0]
                                  
                                
                              
                            
                          
                        
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                          if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 0:
                              if arg_action[3] is None:
                                return [1,0,2,0,1,0,0,0,1,0,1,0,0,0]
                              if arg_action[3].pos.x != arg_action[2].pos.x:
                                if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,2,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 1:
                            if arg_action[3] is None:
                              return [1,0,2,0,1,0,0,0,1,0,1,0,1]
                            if arg_action[3].pos.x != arg_action[2].pos.x:
                              if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                  if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,2,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0]
                                    
                                  
                                
                              
                            
                          
                        if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                            if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 1:
                              if arg_action[3] is None:
                                return [1,0,2,0,1,0,0,0,1,0,1,1,0,0]
                              if arg_action[3].pos.x != arg_action[2].pos.x:
                                if 0 <= arg_action[3].pos.x and arg_action[3].pos.x <= 2:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,2,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      
                    if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                      if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                        if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 1:
                          if arg_action[3] is None:
                            return [1,0,2,0,1,0,0,0,1,1,0,0]
                          if arg_action[3].pos.x == arg_action[2].pos.x:
                            if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                              if arg_action[3].pos.y != arg_action[2].pos.y:
                                if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                  if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                    return [1,0,2,0,1,0,0,0,1,1,0,0,0,0,0,0,0]
                                  
                                
                              
                            
                          
                        if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                          if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 0:
                            if arg_action[3] is None:
                              return [1,0,2,0,1,0,0,0,1,1,0,1,0]
                            if arg_action[3].pos.x == arg_action[2].pos.x:
                              if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                if arg_action[3].pos.y != arg_action[2].pos.y:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,2,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0]
                                    
                                  
                                
                              
                            
                          
                        
                      if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                        if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                          if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 1:
                            if arg_action[3] is None:
                              return [1,0,2,0,1,0,0,0,1,1,1,0,0]
                            if arg_action[3].pos.x == arg_action[2].pos.x:
                              if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                if arg_action[3].pos.y != arg_action[2].pos.y:
                                  if 0 <= arg_action[3].pos.y and arg_action[3].pos.y <= 2:
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,2,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0]
                                    
                                  
                                
                              
                            
                          
                        
                      
                    
                  
                
              
            
          
        
      if 1 >= abs(arg_action[0].pos.x - 2):
        if 2 == arg_action[0].pos.x:
          if 2 != arg_action[0].pos.y:
            if 1 >= abs(arg_action[0].pos.y - 2):
              if arg_action[1].pos.x == 2:
                if arg_action[1].pos.y == 2:
                  if arg_action[2] is None:
                    return [1,0,1,0,0,0,0,0]
                  if arg_action[2].pos.x == 2:
                    if 1 >= abs(2 - 2):
                      if arg_action[2].pos.y != 2:
                        if arg_action[2].pos.y >= 0:
                          if 1 >= abs(2 - arg_action[2].pos.y):
                            return [1,0,1,0,0,0,0,0,0,0,0,0,0]
                          
                        
                      
                    
                  if arg_action[2].pos.x != 2:
                    if arg_action[2].pos.x >= 0:
                      if arg_action[2].pos.y >= 0:
                        if 1 >= abs(2 - arg_action[2].pos.x):
                          if 1 >= abs(2 - arg_action[2].pos.y):
                            return [1,0,1,0,0,0,0,0,1,0,0,0,0]
                          
                        
                      
                    
                  
                
              
            
          if arg_action[1].pos.x == 2:
            if arg_action[1].pos.y != arg_action[0].pos.y:
              if arg_action[1].pos.y >= 0:
                if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
                  if arg_action[0].nmap[arg_action[1].pos]:
                    if arg_action[2] is None:
                      return [1,0,1,0,1,0,0,0,0]
                    if 1 >= abs(arg_action[1].pos.y - 2):
                      if arg_action[2].pos.x == 2:
                        if arg_action[2].pos.y == 2:
                          if arg_action[3] is None:
                            return [1,0,1,0,1,0,0,0,0,0,0,0]
                          if arg_action[3].pos.x == 2:
                            if 1 >= abs(2 - 2):
                              if arg_action[3].pos.y != 2:
                                if arg_action[3].pos.y >= 0:
                                  if 1 >= abs(2 - arg_action[3].pos.y):
                                    return [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
                                  
                                
                              
                            
                          if arg_action[3].pos.x != 2:
                            if arg_action[3].pos.x >= 0:
                              if arg_action[3].pos.y >= 0:
                                if 1 >= abs(2 - arg_action[3].pos.x):
                                  if 1 >= abs(2 - arg_action[3].pos.y):
                                    return [1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0]
                                  
                                
                              
                            
                          
                        
                      
                    if arg_action[2].pos.y >= 0:
                      if arg_action[2].pos.x >= 0:
                        if arg_action[2].pos.x != 2:
                          if 1 >= abs(2 - arg_action[2].pos.x):
                            if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                              if arg_action[3] is None:
                                return [1,0,1,0,1,0,0,0,0,2,0,0,0,0]
                              if 1 >= abs(arg_action[2].pos.x - 2):
                                if 1 >= abs(arg_action[2].pos.y - 2):
                                  if arg_action[3].pos.x == 2:
                                    if arg_action[3].pos.y == 2:
                                      return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0]
                                    
                                  
                                if arg_action[3].pos.x == 2:
                                  if arg_action[3].pos.y >= 0:
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                        if arg_action[3].pos.y != 2:
                                          return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,0,1,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              if arg_action[3].pos.x >= 0:
                                if arg_action[3].pos.y >= 0:
                                  if arg_action[3].pos.x != 2:
                                    if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                      if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                        if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                          if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 0:
                                            return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0]
                                          
                                        if arg_action[3].pos.x != arg_action[2].pos.x:
                                          if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                            return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,2,0,0,0,0,1,0]
                                          
                                        
                                      if abs(arg_action[2].pos.x - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                        if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                          if abs(arg_action[2].pos.x - arg_action[3].pos.x) == 1:
                                            return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,2,0,0,0,1,0,0]
                                          
                                        
                                      
                                    if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                          return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,2,0,0,1,0,0]
                                        
                                      
                                    
                                  
                                
                              if arg_action[3].pos.x == 2:
                                if abs(arg_action[2].pos.x - 2) == 1:
                                  if arg_action[3].pos.y >= 0:
                                    if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                      if arg_action[3].pos.y != 2:
                                        if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                          return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,1,0,0,0,0,0]
                                        if abs(arg_action[2].pos.x - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                          if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                            return [1,0,1,0,1,0,0,0,0,2,0,0,0,0,1,0,0,0,0,1,0]
                                          
                                        
                                      
                                    
                                  
                                
                              
                            
                          if abs(2 - arg_action[2].pos.x) == 1:
                            if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                              if abs(2 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                                if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                                  if arg_action[3] is None:
                                    return [1,0,1,0,1,0,0,0,0,2,0,0,1,0,0,0]
                                  if arg_action[3].pos.x != arg_action[2].pos.x:
                                    if arg_action[3].pos.x >= 0:
                                      if arg_action[3].pos.y >= 0:
                                        if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                          if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                            return [1,0,1,0,1,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0]
                                          
                                        
                                      
                                    
                                  
                                
                              if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                                if arg_action[3] is None:
                                  return [1,0,1,0,1,0,0,0,0,2,0,0,1,0,1]
                                if arg_action[3].pos.x != arg_action[2].pos.x:
                                  if arg_action[3].pos.x >= 0:
                                    if arg_action[3].pos.y >= 0:
                                      if 1 >= abs(arg_action[2].pos.x - arg_action[3].pos.x):
                                        if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                          return [1,0,1,0,1,0,0,0,0,2,0,0,1,0,1,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      if abs(2 - arg_action[2].pos.x) == 1:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          if abs(2 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                              if arg_action[3] is None:
                                return [1,0,1,0,1,0,0,0,0,2,1,0,0,0]
                              if arg_action[3].pos.x == arg_action[2].pos.x:
                                if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                  if arg_action[3].pos.y != arg_action[2].pos.y:
                                    if arg_action[3].pos.y >= 0:
                                      if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                        return [1,0,1,0,1,0,0,0,0,2,1,0,0,0,0,0,0,0,0]
                                      
                                    
                                  
                                
                              
                            
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                            if arg_action[3] is None:
                              return [1,0,1,0,1,0,0,0,0,2,1,0,1]
                            if arg_action[3].pos.x == arg_action[2].pos.x:
                              if 1 >= abs(arg_action[2].pos.x - arg_action[2].pos.x):
                                if arg_action[3].pos.y != arg_action[2].pos.y:
                                  if arg_action[3].pos.y >= 0:
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      return [1,0,1,0,1,0,0,0,0,2,1,0,1,0,0,0,0,0]
                                    
                                  
                                
                              
                            
                          
                        
                      
                    if arg_action[2].pos.x == 2:
                      if abs(2 - 2) == 0:
                        if arg_action[2].pos.y >= 0:
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                            if abs(2 - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                              if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                                if arg_action[2].pos.y != 2:
                                  if arg_action[3] is None:
                                    return [1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0]
                                  if arg_action[3].pos.x == 2:
                                    if 1 >= abs(2 - 2):
                                      if arg_action[3].pos.y != arg_action[2].pos.y:
                                        if arg_action[3].pos.y >= 0:
                                          if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                            return [1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
                                          
                                        
                                      
                                    
                                  if arg_action[3].pos.x != 2:
                                    if arg_action[3].pos.x >= 0:
                                      if arg_action[3].pos.y >= 0:
                                        if 1 >= abs(2 - arg_action[3].pos.x):
                                          if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                            return [1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]
                                          
                                        
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      if arg_action[2].pos.y >= 0:
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          if arg_action[2].pos.y != 2:
                            if arg_action[3] is None:
                              return [1,0,1,0,1,0,0,0,0,1,1,0,0]
                            if 1 >= abs(arg_action[2].pos.y - 2):
                              if arg_action[3].pos.x == 2:
                                if arg_action[3].pos.y == 2:
                                  return [1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0]
                                
                              
                            if arg_action[3].pos.x >= 0:
                              if arg_action[3].pos.y >= 0:
                                if arg_action[3].pos.x != 2:
                                  if abs(2 - arg_action[3].pos.x) == 1:
                                    if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                      if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                        return [1,0,1,0,1,0,0,0,0,1,1,0,0,2,0,0,0,0,0]
                                      if abs(2 - arg_action[3].pos.x) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                        if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 0:
                                          return [1,0,1,0,1,0,0,0,0,1,1,0,0,2,0,0,0,0,1,0]
                                        
                                      
                                    
                                  if 1 >= abs(2 - arg_action[3].pos.x):
                                    if 1 >= abs(arg_action[2].pos.y - arg_action[3].pos.y):
                                      if add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]:
                                        return [1,0,1,0,1,0,0,0,0,1,1,0,0,2,0,0,1,0,0]
                                      
                                    
                                  
                                
                              
                            if arg_action[3].pos.x == 2:
                              if abs(2 - 2) == 0:
                                if arg_action[3].pos.y >= 0:
                                  if abs(arg_action[2].pos.y - arg_action[3].pos.y) == 1:
                                    if abs(2 - 2) * -1 - abs(arg_action[2].pos.y - arg_action[3].pos.y) == -1:
                                      if not(add(add(arg_action[0].nmap,arg_action[1].pos,False),arg_action[2].pos,False)[arg_action[3].pos]):
                                        if arg_action[3].pos.y != 2:
                                          return [1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0]
                                        
                                      
                                    
                                  
                                
                              
                            
                          
                        
                      
                    
                  
                
              
            
          
        
      
    
  
