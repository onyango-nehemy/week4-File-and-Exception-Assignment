def error_challenge():
   file_name=input("enter the file name:")

   try:
    with open(file_name,"r",encoding='utf-8') as f:
        print(f.readlines())
   except FileNotFoundError:
    print("no such file")

error_challenge()
