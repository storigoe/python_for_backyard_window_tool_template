from distutils.core import setup
import py2exe, sys, os

#option = {
#    'bundle_files':1,
#    'compressed': True
#}
setup(
#    options = {'py2exe': option},
    console=['test1.py']
#    window=['create_file.py'],
#    zipfile = 'create_file.zip', 
    )
