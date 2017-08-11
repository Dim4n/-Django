```python

def nl2br(string, is_xhtml=True):
    if is_xhtml:
        return string.replace('\n', '<br />\n')
    else :
        return string.replace('\n', '<br>\n')

```
