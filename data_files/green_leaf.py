# #!/bin/bash


from os import system as cereal
from playsound import playsound as mkv
from getpass import getpass

dnial = getpass('Enter the journal name: ')
mkv('jarvis/jarvis_service.wav', True)
ch = cereal("openssl aes256 -d -in .{}.mkz -out .{}.txt".format(dnial, dnial))
if ch == 0:
    mkv('jarvis/jarvis_calibrating.wav', True)
    cereal('emacs .{}.txt'.format(dnial))
    we = cereal(
        'openssl aes256 -e -in .{}.txt -out .{}.mkz'.format(dnial, dnial))
    while we != 0:
        we = cereal(
            'openssl aes256 -e -in .{}.txt -out .{}.mkz'.format(dnial, dnial))
    cereal('rm .{}.txt .{}.txt~'.format(dnial, dnial))
    mkv('jarvis/jarvis_test_complete.wav', True)
else:
    mkv('jarvis/jarvis_authorized_not.wav')
    cereal('rm .{}.txt .{}.txt~'.format(dnial, dnial))
