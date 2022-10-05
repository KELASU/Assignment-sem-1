from pydoc import tempfilepager
import tempfile


a = [1,2,3,4,5]
b = []

b = b+a
b[0] = 3
a[-1] = 7
print(b,a)