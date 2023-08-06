# Ycolor
made by Yourouchour
My English is not good,so the following content comes from my translation software.
### Description
Ycolor is a conventional color text printing tool.  
### How to use
Ycolor 1.0.x uses four functions to print color text.  
```python
from ycolor import *
printcolor('Hello, world',fore=Fore.RED,back=Back.WHITE)
printcolor_text('Hello, world',color='RED+WHITE')
printcolor_int('Hello, world',color='0xfe')
```
### Historical version
v1.0.1 Two functions are created to print color text.  
v1.0.2 Some modules are hidden to make the display more concise.  
v1.0.3 Added function printcolor_int.