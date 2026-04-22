import os
import sys
from pathlib import Path
from datetime import datetime
from .hi import hello

def main():
    print("Hello, World!")
    print(f"Current directory: {Path.cwd()}")
    print(f"Current time: {datetime.now()}")
    print(f"Python version: {sys.version}")
    hello()

if __name__ == "__main__":
    main()