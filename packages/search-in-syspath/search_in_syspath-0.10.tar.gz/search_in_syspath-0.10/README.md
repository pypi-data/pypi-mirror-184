# Search for files in sys.path 

```python

$pip install search-in-syspath


from search_in_syspath import search_in_syspath
print(search_in_syspath(filename="__init__.py", isregex=False))
print(search_in_syspath(filename=r"_+i.it_+\.py", isregex=True))

...
'C:\\Users\\Gamer\\anaconda3\\envs\\dfdir\\lib\\site-packages\\torch\\nn\\quantized\\dynamic\\__init__.py', 
'C:\\Users\\Gamer\\anaconda3\\envs\\dfdir\\Lib\\site-packages\\tensorflow\\_api\\v2\\compat\\v2\\types\\__init__.py', 
'C:\\Users\\Gamer\\anaconda3\\envs\\dfdir\\Lib\\site-packages\\pip\\_vendor\\urllib3\\contrib\\_securetransport\\__init__.py',
 'C:\\Users\\Gamer\\anaconda3\\envs\\dfdir\\lib\\site-packages\\tabledata\\__init__.py', 
...

```
