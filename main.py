from getpass import getpass
from encryptor import FileEncryptor

encrypted_file_path = "encrypted.bin"
key_file_path = "key.bin"

def main():
  while True:
        master_password = getpass("Enter your master password: ")
        encryptor = FileEncryptor(
            encrypted_file_path=encrypted_file_path,
            key_file_path=key_file_path,
            password=master_password.encode()
        )
        
        try:
            encryptor.get_all_pairs()
            print("Master password is correct!\n")
            break 

        except ValueError:
            print("Invalid password. Please try again.")

  while True:
        print("\nMain Menu:")
        print("1. Add a new password")
        print("2. See all passwords")
        print("3. Exit")
        
        choice = input("Choose an option (1, 2, or 3): ").strip()
        
        if choice == '1':
            key = input("Enter the service name: ").strip()
            value = getpass("Enter the password for this service: ").strip()
            encryptor.add_key_value_pair(key, value)
            print(f"Password for '{key}' added successfully!")
        
        elif choice == '2':
            print("\nStored passwords:")
            pairs = encryptor.get_all_pairs()
            if pairs:
                for key, value in pairs.items():
                    print(f"{key}: {value}")
            else:
                print("No password stored.")
        
        elif choice == '3':
            print("Exiting Password Manager. See you later!")
            break
        
        else:
            print("Invalid option. Please choose 1, 2 or 3.")

if __name__ == "__main__":
    main()