import base64
import subprocess

while True:
    try: 
        subprocess.call(['cls'],shell=True)
        modeSelect = input('Select a conversion mode: \n1: Encode\n2: Decode\n0: Exit\n\nSelection: ')
        if modeSelect == '1':

            def enc():
                subprocess.call(['cls'], shell=True)
                userInput = input("Enter plain text here: ")
                subprocess.call(['cls'], shell=True)

                """
                Uses base64 library to encode and decode text
                https://docs.python.org/3/library/base64.html
                """
                b64enc = base64.b64encode(userInput.encode())

                """
                Uses .ord(i) and for loop to loop through userInput to get the unicode number of 
                character entered from the userInput string, then uses .format('b') to convert each 
                unicode number into binary, lastly .join() to join each byte of binary to a string 
                seperated by a space. The same method will be used for the following conversions. 
                Learn more about .format(), .ord() and .join() at w3schools.com

                https://www.w3schools.com/python/ref_func_ord.asp
                https://www.w3schools.com/python/ref_string_format.asp
                https://www.w3schools.com/python/ref_string_join.asp
                """

                binaryStr = ' '.join(format(ord(i), 'b') for i in userInput)
                hexStr = ' '.join(format(ord(i), 'X') for i in userInput)
                decStr = ' '.join(format(ord(i), 'd') for i in userInput)
                octStr = ' '.join(format(ord(i), 'o') for i in userInput)

                print('Original Text: ' + userInput + '\n\nEncoded Conversions\n_______________________\n\nBase64 Encoded:', b64enc.decode(), '\n\nBinary: ' + binaryStr + '\n\nHex: ' + hexStr + '\n\nDecimal: ' + decStr + '\n\nOctal: ' + octStr)

                input('\n\n\nPress Enter to continue...')

            enc()

        if modeSelect == '2':
            subprocess.call(['cls'],shell=True)
            decSelect = input('Select a decode mode: \n1: Base64\n0: Back\n\nSelection: ')
            if decSelect == '1':
                def b64dec():
                    try:
                        subprocess.call(['cls'], shell=True)
                        userInput = input("Enter encoded text here: ")
                        subprocess.call(['cls'], shell=True)

                        """
                        Uses base64 library to encode and decode text
                        https://docs.python.org/3/library/base64.html
                        """
                        b64dec = base64.b64decode(userInput)

                        print('Converted Text: ' + b64dec.decode() + '\nBase64 Encoded: ', userInput)

                    except:
                        input('Incorrect text format, please enter encoded Base64.\n\nPress enter')

                b64dec()

        if modeSelect == '0':
            subprocess.call(['cls'], shell=True)
            break

    except KeyboardInterrupt:
        subprocess.call(['cls'], shell=True)
        input('Program Terminated. Press Enter to continue...')
        subprocess.call(['cls'], shell=True)

        break