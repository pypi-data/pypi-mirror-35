# Lightworks NLE preferences reader

`lwksprefs` is a little Python module developed
for parsing Lightworks preferences.


## Usage

```python
import lwksprefs
p1 = lwksprefs.parse_user_settings()
p2 = lwksprefs.parse('path-to-prefs-file.prefs')
```

Currently only key mapping is read. Commands mapped to keyboard
shortcuts are availabe as `commands` property:

```
print(p1.commands)
```


## Note

Lightworks is a professional NLE (non linear editor) developed by
EditShare and available natively on Linux platform.

For more information please visit: https://www.lwks.com/
