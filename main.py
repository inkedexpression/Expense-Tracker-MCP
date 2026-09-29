from fastmcp import FastMCP
import random
import json

mcp = FastMCP("calculator")

@mcp.tool()
def add_num(a:int,b:int) -> int:
    """
    add two numbers

    args:
    a:the first number
    b:the second number

    returns:
    sum of a and b
    """

    return a + b

@mcp.tool()
def random_num(min_num:int=1,max_num:int=100) -> int:
    """generate a random number between the given range
    
    args:
    min_num: minimum value (default=1)
    max_num: maximum value (default=100)
    
    returns:
    random integere between min_num and max_num"""

    return random.randint(min_num,max_num)

@mcp.resource("info://server")
def server_info()-> str:
    '''get info about the server'''
    info = {
        'name':'simple calculator',
        'version':'1.0.0',
        'description':'a basic MCP server with math tool',
        'tool':['add_num','random_num'],
        'author': 'D Dhanush Naik'
        }
    return json.dumps(info,indent=2)

if __name__ == '__main__':
    mcp.run(transport='http',host="0.0.0.0",port=8000)