#! /usr/bin/env python

import argparse
import sys
import caesar
import vigenere
import transposition

if __name__ == '__main__':
    # get a simple imput of cipher and text
    parser = argparse.ArgumentParser(description='Use a script in this folder to decrypt text using the default options.')
    parser.add_argument('cipher', help='Choose which cipher to use', choices=['caesar', 'substitution', 'transposition', 'vigenere'])
    parser.add_argument('text', help='Encrypted text to decrypt')
    parser.add_argument('--wordlist', '-w', default='/root/Desktoprockyou.txt',
                        help='optional wordlist for some ciphers')

    # detect and call the specified cipher
    args = parser.parse_args()
    if args.cipher == 'caesar':
        # list all cipher shifts by default
        for i in range(1, 26):
            print("Shift %2i: %s" % (i, caesar.decrypt(args.text, i)))
    elif args.cipher == 'substituition':
        print('This doesnt exist yet')
    elif args.cipher == 'transposition':
        transposition.main(args.text)
    elif args.cipher == 'vigenere':
        vigenere.main(args.text, args.wordlist)
