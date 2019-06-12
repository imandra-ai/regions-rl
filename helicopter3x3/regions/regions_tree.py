maxCodes = [1,1,3,2,2,1,1,1,2,3,3,2,2,2,1,2,1]

def calculate_regions(arg_action):
  if 0 <= arg_action[0].pos.y and arg_action[0].pos.y <= 2:
    if arg_action[0] is None:
      return [0]
    if 0 < arg_action[0].nfuel and arg_action[0].nfuel <= 1:
      if arg_action[1] is None:
        return [0,0]
      if 0 <= arg_action[0].pos.x and arg_action[0].pos.x <= 2:
        if 1 >= abs(arg_action[0].pos.x - 2):
          if 2 != arg_action[0].pos.x:
            if arg_action[1].pos.x == 2:
              if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
                if arg_action[0].nmap[arg_action[1].pos]:
                  if 0 <= arg_action[1].pos.y and arg_action[1].pos.y < 2:
                    if arg_action[2] is None:
                      return [0,0,0,0,0,0,0,0,0]
                    if 1 >= abs(arg_action[1].pos.y - 2):
                      if arg_action[2].pos.y == 2:
                        if arg_action[2].pos.x == 2:
                          return [0,0,0,0,0,0,0,0,0,0,0,0]
                        
                      
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 2:
                        if abs(2 - arg_action[2].pos.x) == 1:
                          if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                              return [0,0,0,0,0,0,0,0,0,2,0,0,0,0]
                            if abs(2 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                              if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                                return [0,0,0,0,0,0,0,0,0,2,0,0,0,1,0]
                              
                            
                          
                        if 1 >= abs(2 - arg_action[2].pos.x):
                          if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                            return [0,0,0,0,0,0,0,0,0,2,0,1,0]
                          
                        
                      
                    if arg_action[2].pos.x == 2:
                      if abs(2 - 2) == 0:
                        if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                          if abs(2 - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                              if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                                return [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
                              
                            
                          
                        
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                          return [0,0,0,0,0,0,0,0,0,1,1,0]
                        
                      
                    
                  
                
              
            
          
        if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
          if 1 >= abs(arg_action[0].pos.x - arg_action[1].pos.x):
            if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 2:
              if arg_action[1].pos.x != arg_action[0].pos.x:
                if arg_action[0].nmap[arg_action[1].pos]:
                  if 0 <= arg_action[1].pos.x and arg_action[1].pos.x < 2:
                    if arg_action[2] is None:
                      return [0,0,0,1,0,0,0,0,0]
                    if 1 >= abs(arg_action[1].pos.x - 2):
                      if 1 >= abs(arg_action[1].pos.y - 2):
                        if arg_action[2].pos.y == 2:
                          if arg_action[2].pos.x == 2:
                            return [0,0,0,1,0,0,0,0,0,0,0,0,0]
                          
                        
                      if arg_action[2].pos.x == 2:
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                            return [0,0,0,1,0,0,0,0,0,0,1,0,0]
                          
                        
                      
                    if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                      if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 2:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                            if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                              if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 0:
                                return [0,0,0,1,0,0,0,0,0,2,0,0,0,0,0]
                              
                            if arg_action[2].pos.x != arg_action[1].pos.x:
                              if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 1:
                                return [0,0,0,1,0,0,0,0,0,2,0,0,0,1,0]
                              
                            
                          if abs(arg_action[1].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                              if abs(arg_action[1].pos.x - arg_action[2].pos.x) == 1:
                                return [0,0,0,1,0,0,0,0,0,2,0,0,1,0,0]
                              
                            
                          
                        if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                          return [0,0,0,1,0,0,0,0,0,2,0,1]
                        
                      
                    if arg_action[2].pos.x == 2:
                      if abs(arg_action[1].pos.x - 2) == 1:
                        if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                          if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                              return [0,0,0,1,0,0,0,0,0,1,0,0,0,0]
                            if abs(arg_action[1].pos.x - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                              if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                                return [0,0,0,1,0,0,0,0,0,1,0,0,0,1,0]
                              
                            
                          
                        
                      
                    
                  
                
              
            
          
        
      if arg_action[1].pos.x == arg_action[0].pos.x:
        if 1 >= abs(arg_action[0].pos.x - arg_action[0].pos.x):
          if 1 >= abs(arg_action[0].pos.x - 2):
            if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
              if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 2:
                if arg_action[1].pos.y != arg_action[0].pos.y:
                  if arg_action[0].nmap[arg_action[1].pos]:
                    if arg_action[2] is None:
                      return [0,0,2,0,0,0,0,0,0]
                    if 1 >= abs(arg_action[1].pos.y - 2):
                      if arg_action[2].pos.y == 2:
                        if arg_action[2].pos.x == 2:
                          return [0,0,2,0,0,0,0,0,0,0,0,0]
                        
                      
                    if arg_action[2].pos.x == 2:
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                          return [0,0,2,0,0,0,0,0,0,1,0,0]
                        
                      
                    
                  
                
              
            
          if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
            if 0 <= arg_action[1].pos.y and arg_action[1].pos.y <= 2:
              if arg_action[1].pos.y != arg_action[0].pos.y:
                if arg_action[0].nmap[arg_action[1].pos]:
                  if arg_action[2] is None:
                    return [0,0,2,0,1,0,0,0]
                  if arg_action[2].pos.x == 2:
                    if abs(arg_action[0].pos.x - 2) == 1:
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        if 0 <= arg_action[2].pos.y and arg_action[2].pos.y < 2:
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                            return [0,0,2,0,1,0,0,0,0,0,0,0,0]
                          if abs(arg_action[0].pos.x - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                              return [0,0,2,0,1,0,0,0,0,0,0,0,1,0]
                            
                          
                        
                      
                    
                  if 0 <= arg_action[2].pos.y and arg_action[2].pos.y <= 2:
                    if 0 <= arg_action[2].pos.x and arg_action[2].pos.x < 2:
                      if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                        if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                          if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                            if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 0:
                              return [0,0,2,0,1,0,0,0,1,0,0,0,0,0]
                            
                          if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 1:
                            return [0,0,2,0,1,0,0,0,1,0,0,0,1]
                          
                        if abs(arg_action[0].pos.x - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                          if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                            if abs(arg_action[0].pos.x - arg_action[2].pos.x) == 1:
                              return [0,0,2,0,1,0,0,0,1,0,0,1,0,0]
                            
                          
                        
                      if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                        return [0,0,2,0,1,0,0,0,1,0,1]
                      
                    
                  
                
              
            
          
        
      if 1 >= abs(arg_action[0].pos.x - 2):
        if 2 == arg_action[0].pos.x:
          if arg_action[1].pos.x == 2:
            if 1 >= abs(arg_action[0].pos.y - arg_action[1].pos.y):
              if arg_action[1].pos.y >= 0:
                if arg_action[1].pos.y != arg_action[0].pos.y:
                  if arg_action[0].nmap[arg_action[1].pos]:
                    if arg_action[1].pos.y != 2:
                      if arg_action[2] is None:
                        return [0,0,1,0,0,0,0,0,0,0]
                      if 1 >= abs(arg_action[1].pos.y - 2):
                        if arg_action[2].pos.y == 2:
                          if arg_action[2].pos.x == 2:
                            return [0,0,1,0,0,0,0,0,0,0,0,0,0]
                          
                        
                      if arg_action[2].pos.y >= 0:
                        if arg_action[2].pos.x >= 0:
                          if arg_action[2].pos.x != 2:
                            if abs(2 - arg_action[2].pos.x) == 1:
                              if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                                if abs(2 - arg_action[2].pos.x) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                                  if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 0:
                                    return [0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0]
                                  
                                if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                                  return [0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,1]
                                
                              
                            if 1 >= abs(2 - arg_action[2].pos.x):
                              if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                                return [0,0,1,0,0,0,0,0,0,0,2,0,0,1,0]
                              
                            
                          
                        
                      if arg_action[2].pos.x == 2:
                        if abs(2 - 2) == 0:
                          if arg_action[2].pos.y >= 0:
                            if abs(arg_action[1].pos.y - arg_action[2].pos.y) == 1:
                              if abs(2 - 2) * -1 - abs(arg_action[1].pos.y - arg_action[2].pos.y) == -1:
                                if not(add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]):
                                  if arg_action[2].pos.y != 2:
                                    return [0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                                  
                                
                              
                            
                          
                        if arg_action[2].pos.y >= 0:
                          if add(arg_action[0].nmap,arg_action[1].pos,False)[arg_action[2].pos]:
                            if arg_action[2].pos.y != 2:
                              return [0,0,1,0,0,0,0,0,0,0,1,1,0,0]
                            
                          
                        
                      
                    
                  
                
              
            
          
        
      
    
  
