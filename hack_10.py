"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    string        = "fooziman"
    result        = []
    for i in range(0,7):
        string = string.replace('o','0')
        string = string.replace('i','1')
        string = string.replace('a','@')
        result.append(string.upper()[i])

            
    return result   
  
print(fn_hack_10())