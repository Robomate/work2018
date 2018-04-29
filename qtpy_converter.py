from subprocess import call

#call(["pyuic4", "-x","test6.ui", "-o","test8.py"])

call(["pyuic5", "-x","test.ui", "-o","test.py"])
call(["python3", "test.py"])
