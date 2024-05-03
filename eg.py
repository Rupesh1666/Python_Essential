def copy_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print("Content copied successfully from", source_file, "to", destination_file)
    except FileNotFoundError:
        print("One of the files does not exist.")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")

    copy_content(source_file, destination_file)

if __name__ == "__main__":
    main()
