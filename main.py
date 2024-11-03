from getpass import getpass
from encryptor import FileEncryptor
import os

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
        print("3. Delete a password")
        print("4. Exit")
        
        choice = input("Choose an option (1, 2, 3 or 4): ").strip()
        
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            key = input("Enter the service name: ").strip()
            value = getpass("Enter the password for this service: ").strip()
            encryptor.add_key_value_pair(key, value)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            pairs = encryptor.get_all_pairs()
            if pairs:
                print("\nStored services:")
                for key in pairs.keys():
                    print(f"- {key}")
                selected_key = input("\nEnter the service name to view the password: ").strip()
                if selected_key in pairs:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Password for '{selected_key}': {pairs[selected_key]}")
                    print('\n\n\n\n')
                    input("\nPress Enter to return to the main menu.")
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print(f"'{selected_key}' not found.")
            else:
                print("No passwords stored.")
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            pairs = encryptor.get_all_pairs()
            if pairs:
                print("\nStored services:")
                for key in pairs.keys():
                    print(f"- {key}")
            key = input("Enter the service name to delete: ").strip()
            encryptor.delete_key_value_pair(key)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Exiting Password Manager. See you later!")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid option. Please choose 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()