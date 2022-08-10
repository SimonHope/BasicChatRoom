# Basic chat room

Basic chat room is a program develop by python3(socket) with GUI
## Installation

### Server
Install python3 and run this command on your server

```bash
python chat-server.py
```
### Client
Run in local with command

```bash
python GUI-chat.py
```

## Usage library

chat-server.py
```python
import socket  
import datetime
import threading
```

GUI-Chat.py
```python
#################GUI######################
from tkinter import *
from tkinter import ttk, messagebox
import tkinter.scrolledtext as st
from tkinter import simpledialog

#################network###################
import socket  
import threading
import sys
```

## reference
[Python Network (Socket)](https://www.youtube.com/watch?v=MEaEVF3ZWfE)
