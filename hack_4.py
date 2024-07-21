"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result_ultimo = result[7:8]
    result =  result[0:7] + result_ultimo.upper()
    return result

print(fn_hack_4())