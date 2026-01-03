import sys
import os

# Put 'src' in path if needed or just import relative
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.gui.app import App

if __name__ == "__main__":
    app = App()
    app.mainloop()
