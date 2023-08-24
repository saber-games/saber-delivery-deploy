#!/usr/bin/python3

# Script will use idempotent machine GUID instead of random GUID

import sys
import hashlib
import base64
import uuid

## https://github.com/swizzin/swizzin/blob/master/scripts/qbittorrent.Userpass.py
password = sys.argv[1]

import subprocess
import sys

def run(cmd):
  try:
    return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                     .stdout \
                     .strip()
  except:
    return None

def guid():
  if sys.platform == 'darwin':
    return run(
      "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",
    )

  if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
    return run('wmic csproduct get uuid').split('\n')[2] \
                                         .strip()

  if sys.platform.startswith('linux'):
    return run('cat /var/lib/dbus/machine-id') or \
           run('cat /etc/machine-id')

  if sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
    return run('cat /etc/hostid') or \
           run('kenv -q smbios.system.uuid')



salt = guid()
#print(salt)
# to bytes
salt_bytes = str.encode(salt)
#print(salt_bytes)

password = str.encode(password)
hashed_password = hashlib.pbkdf2_hmac('sha512', password, salt_bytes, 100000, dklen=64)
b64_salt = base64.b64encode(salt_bytes).decode("utf-8")
b64_password = base64.b64encode(hashed_password).decode("utf-8")
password_string = "{salt}:{password}".format(salt=b64_salt,password=b64_password)
print(password_string,end='')