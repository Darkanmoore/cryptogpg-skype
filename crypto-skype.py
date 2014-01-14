#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Version:
# - 0.1
#
# The MIT License (MIT)
#
# Copyright (c) 2014 ~Smlb <smlb at riseup dot net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from Skype4Py import Skype
import sys
import gnupg
import os

# Get the home user path
GPGUserPathPubring = "%s/.gnupg/pubring.gpg" % os.path.expanduser("~")
GPGUserPath = "%s/.gnupg" % os.path.expanduser("~")

# Prepare Skype session
client = Skype()
client.Attach()

# Get the GPG key and read it
gpg = gnupg.GPG(gnupghome=GPGUserPath)
key_data = open(GPGUserPathPubring).read()
import_result = gpg.import_keys(key_data)

print 'Your name:', client.CurrentUser.FullName

print '\n'

# Check who is online
for f in client.Friends:
    if f.OnlineStatus == 'ONLINE':
        print '\033[1;41m User: \033[1;m', f.FullName
        print 'Status: %s\n' % f.OnlineStatus

# Passing argument to command line        
users = sys.argv[1]
message = ' '.join(sys.argv[2:])
encrypted_data = gpg.encrypt(message, 'smlb@riseup.net')
client.SendMessage(users, encrypted_data)

# Test print 
print 'message: ', message
print 'encrypted_string: ', encrypted_data
