import sys, os

path = str(os.path.abspath(os.path.dirname(__file__))) + '/app'
if path not in sys.path:
    sys.path.append(path)
#
from myproject import app

if __name__ == "__main__":
    app.run()