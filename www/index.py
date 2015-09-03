#!/usr/bin/env python
import os

print "Content-Type: text/html"
#print("<html><head><title>python test</title></head><body>")

#for key in os.environ.keys():
#	print "%30s %s \n" % (key,os.environ[key])
#	print """<br/>"""	

username = os.environ['OIDC_CLAIM_name']
userpic = os.environ['OIDC_CLAIM_picture']

print
print "Hello user: "+ username
print """<br/>"""
print
#print """<img src="""+userpic+""" />"""
print
