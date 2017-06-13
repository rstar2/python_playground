#!/usr/bin/env python

import sys
import pyperclip #clipboard COPY/PASTE funcionality

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    exit()

account = sys.argv[1]  # first command line arg is the account name

PASSWORDS = {
    'abv.bg': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'rstar@abv.bg': 'cadb12',
    'rstar2@abv.bg': 'cadb12new'
}

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])

print(PASSWORDS)