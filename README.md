# file_integrity_tool
Python file integrity checker using SHA-256 hashing

#integrity_tool.py

import hashlib
import json

def create_record():
    try:
        filename=input("Enter Filename: ").strip()
        
        with open(filename,"rb")as file:
            data=file.read()
            hash_file=hashlib.sha256(data).hexdigest()
        
            info={
                "filename":filename,
                "sha256":hash_file
            }
            record_name=filename+".json"
            
            with open(record_name,"w")as file:
               json.dump(info,file,indent=4)
               
            print(f"Integrity record saved as {record_name}.")
            
    except FileNotFoundError:
        print("File not found.")  
    except json.JSONDecodeError:
        print("Record File is corrupted.")        
    
def verify_record():
    try:
        filename=input("Enter Filename: ").strip()
        record_name=input("Enter Record Filename: ").strip()
    
        with open(record_name,"r")as file:
            info=json.load(file)
            stored_hash=info["sha256"]
        
        with open(filename,"rb")as file:
            data=file.read()
            current_hash=hashlib.sha256(data).hexdigest()
        
            if stored_hash==current_hash:
                print("File not modified.Integrity verified.")
            else:
                print("File modified")    
    except FileNotFoundError:
        print("File or record not found.")            
        
            
def main():
    while True:
        print("---File Integrity Tool---")
        option = input(
            "1.Create Integrity record\n"
            "2.Verify Integrity\n"
            "3.Exit\n"
            "Enter: "
        ).strip()

        if option == "1":
            create_record()

        elif option == "2":
            verify_record()

        elif option == "3":
            print("Program closed.")
            break

        else:
            print("Invalid option.")
            continue
            
if __name__ == "__main__":
    main()



