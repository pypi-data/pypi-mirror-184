# PVMB

PVMB is the best message box package from pypi

## Installation


```bash
pip install pvmb
```

## Usage

```python

box("title", MB_ICONQUESTION | MB_CANCELTRYCONTINUE, "text")
```

## Message box mode list

### Mode

MB_ABORTRETRYIGNORE\n
MB_CANCELTRYCONTINUE\n
MB_HELP\n
MB_OK\n
MB_OKCANCEL\n
MB_RETRYCANCEL\n
MB_YESNO\n
MB_YESNOCANCEL\n
_________
### Icons

MB_ICONEXCLAMATION\n
MB_ICONWARNING\n
MB_ICONINFORMATION\n
MB_ICONASTERISK\n
MB_ICONQUESTION\n
MB_ICONSTOP\n
MB_ICONERROR\n
MB_ICONHAND
_____
### Buttons value

IDABORT = 3\n
IDCANCEL = 2\n
IDCONTINUE = 11\n
IDIGNORE = 5\n
IDNO = 7\n
IDOK = 1\n
IDRETRY = 4\n
IDTRYAGAIN = 10\n
IDYES = 6
___

### Highlighted button

MB_DEFBUTTON1\n
MB_DEFBUTTON2\n
MB_DEFBUTTON3\n
MB_DEFBUTTON4

#### Examples

```python
from foxbox import *
mybox = box("SOMETHING WEN WRONG. would you like to restart?",MB_DEFBUTTON1 | MB_ICONERROR | MB_YESNO, "ERROR!")
if mybox == IDYES:
    print('Restarted!')
if mybox == IDNO:
    print('Closed')
```

## Help

Thanks for use if you have any question join my Discord server link here [(--)](https:\discord.gg\c6twk26h)

## What's new?
v0.0.1 - first release\n