with open("output.txt","a") as file:
    text=input("Enter text to enter to the file: ")
    file.write(text+'\n')
    print("Data successfully written to 'output.txt'.")
    add_text = input("Enter additional text to append: ")
    file.write(add_text)
    print("Data successfully appended.")
with open("output.txt","r") as file_read:
    print("Final content of 'output.txt':")
    print(file_read.read())