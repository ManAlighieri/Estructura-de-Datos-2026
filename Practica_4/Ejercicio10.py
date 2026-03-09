from collections import deque

p = deque(maxlen=3)

p.append(0)
p.append(2)
p.append(4)
print(list(p))  


x = p.popleft()     
p.appendleft(6)      
p.appendleft(x)     
print(list(p))       

x = p.pop()         
p.pop()            
p.pop()             
p.appendleft(12)    
p.appendleft(x)      
p.pop()            
print(list(p))  