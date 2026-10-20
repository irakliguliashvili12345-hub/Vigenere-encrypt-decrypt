#!/usr/bin/env python3

import argparse
import os

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
    
    def encrypt(self, text):
        result = ""
        key_index = 0
        
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()
                
                key_char = self.key[key_index % len(self.key)]
                key_index += 1

                char_code = (ord(char) - ord('A') + ord(key_char) - ord('A')) % 26 + ord('A')
                
                if not is_upper:
                    result += chr(char_code).lower()
                else:
                    result += chr(char_code)
            else:
                result += char
        
        return result
    
    def decrypt(self, text):
        result = ""
        key_index = 0
        
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                
                char = char.upper()
                
                key_char = self.key[key_index % len(self.key)]
                key_index += 1
                
                char_code = (ord(char) - ord(key_char) + 26) % 26 + ord('A')
                
                if not is_upper:
                    result += chr(char_code).lower()
                else:
                    result += chr(char_code)
            else:
                result += char
        
        return result


def main():
    parser = argparse.ArgumentParser(description='Vigenère-Verschlüsselungs-/Entschlüsselungswerkzeug')
    parser.add_argument('--key', required=True, help='Schlüssel für Verschlüsselung/Entschlüsselung')
    parser.add_argument('--encrypt', action='store_true', help='Text verschlüsseln (Encrypt the input )')
    parser.add_argument('--decrypt', action='store_true', help='Text entschlüsseln (Decrypt the input)')
    parser.add_argument('--text', help='Zu verschlüsselnder/entschlüsselnder Text')
    parser.add_argument('--file', help='Zu verschlüsselnde/entschlüsselnde Datei')
    parser.add_argument('--out', help='Ausgabedatei für verschlüsselten/entschlüsselten Inhalt')
    
    args = parser.parse_args()
    
    if not args.encrypt and not args.decrypt:
        parser.error("Sie müssen entweder --encrypt oder --decrypt angeben")
    
    if args.encrypt and args.decrypt:
        parser.error("Sie können nicht sowohl --encrypt als auch --decrypt angeben")
    
    if not args.text and not args.file:
        parser.error("Sie müssen eine Eingabe über --text oder --file bereitstellen")
    
    if args.text and args.file:
        parser.error("Sie können nicht sowohl --text als auch --file angeben")
    
    cipher = VigenereCipher(args.key)
    
    if args.text:
        if args.encrypt:
            result = cipher.encrypt(args.text)
        else:
            result = cipher.decrypt(args.text)
        
        if args.out:
            with open(args.out, 'w') as file:
                file.write(result)
        else:
            print(result)
    
    elif args.file:
        if not os.path.exists(args.file):
            print(f"Error: Input file '{args.file}' not found")
            return
        
        try:
            with open(args.file, 'r') as file:
                content = file.read()
            
            if args.encrypt:
                result = cipher.encrypt(content)
            else:
                result = cipher.decrypt(content)
            
            if args.out:
                with open(args.out, 'w') as file:
                    file.write(result)
            else:
                print(result)
        
        except Exception as e:
            print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()
