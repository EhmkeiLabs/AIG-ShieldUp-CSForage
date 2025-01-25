'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile
from tqdm import tqdm  # Importing tqdm for progress tracking

# Function to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning brute force attack")

    # Open the encrypted zip file
    with ZipFile('enc.zip') as zf:
        # Open the password file in binary read mode
        with open('rockyou.txt', 'rb') as f:
            # Get the total number of passwords for tqdm progress bar
            total_passwords = sum(1 for _ in f)
            f.seek(0)  # Reset file pointer to the beginning

            # Wrap the password iteration in a tqdm progress bar
            for line in tqdm(f, total=total_passwords, desc="Testing passwords"):
                # Strip whitespace and newline characters
                password = line.strip()

                # Attempt to extract the zip file using the current password
                if attempt_extract(zf, password):
                    print(f"\n[+] Password found: {password.decode()}")
                    return  # Exit once the password is found

    # If no password was found
    print("\n[+] Password not found in list")

if __name__ == "__main__":
    main()
