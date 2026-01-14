def write_to_file(filename):
    try:
        file=open(filename,"w")
        for i in range(1,101):
            file.write(str(i))
            file.write("\t")
    except PermissionError:
        print("Permission Error")
    except FileNotFoundError:
        print("FileNotFoundError")
    except Exception as e:
        print("An exception occurred",e)