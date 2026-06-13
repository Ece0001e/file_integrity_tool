import hashlib
import json
from json import JSONDecodeError

def create_record():
    try:
        filename = input("Enter Filename: ").strip()
        
        with open(filename, "rb") as file:
            data = file.read()
            hash_file = hashlib.sha256(data).hexdigest()
        
            info = {
                "filename": filename,
                "sha256": hash_file
            }
            record_name = filename + ".json"
            
            with open(record_name, "w") as record_file:
                json.dump(info, record_file, indent=4)
            
            print(f"✓ Integrity record saved as {record_name}")
            print()
            
    except FileNotFoundError:
        print("✗ File not found.")
        print()
    except IOError as e:
        print(f"✗ Error reading file: {e}")
        print()
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        print()

def verify_record():
    try:
        filename = input("Enter Filename: ").strip()
        record_name = input("Enter Record Filename: ").strip()
    
        with open(record_name, "r") as file:
            try:
                info = json.load(file)
                if "sha256" not in info:
                    print("✗ Record file is corrupted (missing sha256).")
                    print()
                    return
                stored_hash = info["sha256"]
            except JSONDecodeError:
                print("✗ Record file is corrupted (invalid JSON).")
                print()
                return
        
        with open(filename, "rb") as file:
            data = file.read()
            current_hash = hashlib.sha256(data).hexdigest()
        
            if stored_hash == current_hash:
                print("✓ File not modified. Integrity verified.")
                print()
            else:
                print("✗ File modified. Integrity check failed.")
                print()
                
    except FileNotFoundError:
        print("✗ File or record not found.")
        print()
    except IOError as e:
        print(f"✗ Error reading file: {e}")
        print()
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        print()

def main():
    while True:
        print("---File Integrity Tool---")
        option = input(
            "1. Create Integrity record\n"
            "2. Verify Integrity\n"
            "3. Exit\n"
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
            print("✗ Invalid option.")
            print()
            continue

if __name__ == "__main__":
    main()
