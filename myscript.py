import os
import sys

os.system(f"git bisect start HEAD e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")

