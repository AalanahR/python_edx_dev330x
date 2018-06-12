
import argparse
import os


def parse_command_line():
    """
    Parse the command line arguments and return the parse_args object.
    
    There should be 1 positional argument and 6 optional arguments.
    The help message generated by the parser should look like:
    
    usage: cipher.py [-h] [-o outfile_path] [-k KEY] [-d] [-a] [-v] infile

    positional arguments:
      infile                input file to be encrypted or decrypted

    optional arguments:
      -h, --help            show this help message and exit
      -o outfile_path, --outfile outfile_path
                            output file
      -k KEY, --key KEY     encryption/decryption key (must be positive) (default
                            = 1)
      -d, --decrypt         decrypt the input file
      -a, --all             decrypt using all keys [1, 25], save outputs in
                            different files. (useful in case the key is lost or
                            unknown)
      -v, --verbose         verbose mode


    args:
        None
        
    returns:
        args: generated argparse object with all the passed command line arguments      
    """
    
    #TODO: Your code goes here
    #HINTS: Reveiw Jupyter Notebook 3-4.1  
    
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help = "input file to be encrypted or decrypted")
    parser.add_argument("-o", "--outfile", help = "output file", default = None, metavar = "outfile_path")
    parser.add_argument("-k", "--key", help = "encryption/decryption key (must be positive) (default = 1)",
                       default = 1, type = int)
    parser.add_argument("-d", "--decrypt", help = "decrypt the input file", action = "store_true")
    parser.add_argument("-a", "--all", action = "store_true", 
                        help = "decrypt using all keys [1, 25], save outputs in different files. (useful in case the key is lost or unknown)")
    parser.add_argument("-v", "--verbose", help = "verbose mode", action = "store_true")
    
    args = parser.parse_args()
    
    return(args)

def read_file(file_path):
    """
    Read file_path and return the content as string.
    
    The file must be opened and closed and the function should handle exceptions when they are raised.
    
    args:
        file_path: path to file
        
    returns:
        message: content of file in file_path as a string
    """
    try:
        os.path.exists(file_path)
        try:
            os.path.isfile(file_path)
            with open(file_path, 'r') as f:
                return (f.read())
        except:
            print("input file path is not a file!", file_path)
    except:
        print("file path specified doesn't exists!", file_path)
            
def write_file(message, file_path):
    """
    Write the message in file_path.
    
    The file must be opened and closed and the function should handle exceptions when they are raised.
    
    args:
        message: string to write in file
        file_path: path to file
        
    returns:
        None
    """
    
    with open(file_path, 'w') as f:
        f.write(message)
    

def transform(message, key, decrypt):
    """
    Encrypt or decrypt a message using Caesar cipher.
    
    Encryption and decryption is determined by the Boolean value in decrypt. Key determines the number of 
    places a character is shifted. When encrypting, use the positive value of key to shift the characters forward; 
    when decrypting, use the negative key to shift the characters backward. 
    
    The function should maintain characters that are not letters without change; for example, spaces, punctuations, 
    and numbers should not be encrypted or decrypted. Additionally, the case of the letters should be preserved, 
    small letters are transformed to other small letters and capital letters are transformed to capital letters.
    
    Use the function `shift` (provided later) to shift each character in message by the number in key.
    
    args:
        message: string to be encrypted or decrypted
        key: number of places to shift the characters (always positive)
        decrypt: Boolean; when False the message is encrypted,  when True the message is decrypted
        
    returns:
        transformed_message: encrypted (or decrypted) message
        
    examples:
        Encryption
        ==  transform("deal", 1, False) returns:
            "efbm"
        
        ==  transform("deal", 2, False) returns:
            "fgcn"
        
        ==  transform("deal", 30, False) is equivalent to transform(message, 4, False)
            "hiep"
        
        Decryption
        ==  transform("efbm", 1, True) returns:
            "deal"
            
        ==  transform("fgcn", 2, True) returns:
            "deal"
            
        ==  transform("hiep", 30, True) returns:
            "deal"    
        
    """
    
    #TODO: Your code goes here
    new_message = ''
    if (decrypt):
        key = -1 * key
        for i in range(len(message)):
            new_message = new_message + shift(message[i], key)
        return (new_message)
    else:
        for i in range(len(message)):
            new_message = new_message + shift(message[i], key)

        return (new_message)

    
def shift(char, key):    
    """
    Shift char by the value in key while maintaining the case (small/capital).
    
    If char contains non-letters (i.e. digits, punctuations, and white spaces), it is ignored.
    
    args:
        char: character to shift
        key: number of places to shift char
        
    returns:
        shifted character
        
    examples:
        shfit('a', 1) ==> 'b'
        shift('z', -1) ==> 'y'
        shift('A', 5) ==> 'F'
        shift('H', 7) ==> 'O'
        shift('o', -10) ==> 'e'
        shift('a', 30) ==> 'e'
    """
    
    # ordered lower case alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # will contain shifted lower case alphabet
    shifted_alphabet = ''
    for i in range(len(alphabet)):
        shifted_alphabet = shifted_alphabet + alphabet[(i + key) % 26]
 
    if char.isalpha():
        char_index = alphabet.index(char.lower())
        shifted_char = shifted_alphabet[char_index]
    
        # keep char's case (upper or lower)
        if char.isupper():
            return shifted_char.upper()
        else:
            return shifted_char
    else:
        return(char)

def main():
    # parse command line arguments
    args = parse_command_line()
    
    # read content of infile to a string
    instring = read_file(args.infile)
    
    # verbose
    if args.verbose:
        print("Input file:")
        print("------------")
        print(instring)
        print()
    
    # key is specified
    if not args.all:
        # encrypt/decrypt content of infile
        outstring = transform(instring, args.key, args.decrypt)
    
        # verbose
        if args.verbose:
            print("Output file:")
            print("------------")
            print(outstring)

        # write content of outstring to outfile
        write_file(outstring, args.outfile)
    
    # key is not specified, try all keys from 1 to 25 to decrypt infile
    else:
        for k in range(1, 26):
            # decrypt content of infile
            outstring = transform(instring, k, True)

            # verbose
            if args.verbose:
                print("Key =", k)
                print("------------")
                print(outstring)
                print()

            # write content of outstring to outfile
            write_file(outstring, "decrypted_by_" + str(k) + ".txt")
    
if __name__ == '__main__':
    main()