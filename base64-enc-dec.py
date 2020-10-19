import base64
import subprocess
from sys import platform

def osCheck():
    if platform == "win32":

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
                        b64enc = base64.b64encode(userInput.encode('utf-8'))

                        print('Original Text: ' + userInput + '\n\nEncoded Conversions\n_______________________\n\nBase64 Encoded:', b64enc.decode())

                        input('\n\n\nPress Enter to continue...')

                    enc()


                if modeSelect == '2':
                    subprocess.call(['cls'],shell=True)
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
                            input('\n\n\nPress Enter to continue...')


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
    if platform == "linux" or platform == "linux2" or platform == "darwin":

        while True:
            try:
                subprocess.call(['clear'],shell=True) 
                modeSelect = input('Select a conversion mode: \n1: Encode\n2: Decode\n0: Exit\n\nSelection: ')
                if modeSelect == '1':

                    def enc():
                        subprocess.call(['clear'], shell=True)
                        userInput = input("Enter plain text here: ")
                        subprocess.call(['clear'], shell=True)

                        """
                        Uses base64 library to encode and decode text
                        https://docs.python.org/3/library/base64.html
                        """
                        b64enc = base64.b64encode(userInput.encode('utf-8'))

                        print('Original Text: ' + userInput + '\n\nEncoded Conversions\n_______________________\n\nBase64 Encoded:', b64enc.decode())

                        input('\n\n\nPress Enter to continue...')

                    enc()


                if modeSelect == '2':
                    subprocess.call(['clear'],shell=True)
                    def b64dec():
                        try:
                            subprocess.call(['clear'], shell=True)
                            userInput = input("Enter encoded text here: ")
                            subprocess.call(['clear'], shell=True)

                            """
                            Uses base64 library to encode and decode text
                            https://docs.python.org/3/library/base64.html
                            """
                            b64dec = base64.b64decode(userInput)

                            print('Converted Text: ' + b64dec.decode() + '\nBase64 Encoded: ', userInput)
                            input('\n\n\nPress Enter to continue...')


                        except:
                            input('Incorrect text format, please enter encoded Base64.\n\nPress enter')
                    b64dec()  


                if modeSelect == '0':
                    subprocess.call(['clear'], shell=True)
                    break

            except KeyboardInterrupt:
                subprocess.call(['clear'], shell=True)
                input('Program Terminated. Press Enter to continue...')
                subprocess.call(['clear'], shell=True)

                break
osCheck()