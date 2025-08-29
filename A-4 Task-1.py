try:
    with open("sample.txt","r") as file:
        print("Reading file content:")
        cont=file.readlines()
        c=0
        for i in cont:
            c+=1
            print(f"Line {c}: {i}",end="")
except FileNotFoundError:
    print("Error: The files 'sample.txt' was not found.")
