import sys
if len (sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len (sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("not a python file")
else:
    try:
        with open(sys.argv[1]) as file:
          counter=0
          for i in file:
               if i.lstrip().startswith("#"):
                   continue
               if i.lstrip()=="":
                   continue
               else:
                   counter+=1
          print(counter)
    except FileNotFoundError:
        sys.exit("File dose not exist")
