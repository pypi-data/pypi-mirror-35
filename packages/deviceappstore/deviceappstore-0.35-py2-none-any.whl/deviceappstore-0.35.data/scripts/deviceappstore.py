#!python
import json
import urllib2
import ssl
import tempfile
import sys
import os
import subprocess
import platform
import hashlib
import gzip
import zipfile
import commands
import argparse
from subprocess import call

'''
TODO: List
      Better error printing
      Shows issue request info: http://github.com/deviceappstore/deviceappstore-installer/issues
'''

import imp
from distutils.spawn import find_executable as which


#bindir = os.path.dirname(which('esptool.py'))
#sys.path.append(bindir)  # after this line, esptool becomes importable

#import esptool

# ------------------------- Helpers ----------------------------

# Print error msg
def eprint(txt):
  sys.stderr.write('\x1b[1;31m' + txt.strip() + '\x1b[0m\n')

# Print success msg
def sprint(txt):
  sys.stdout.write('\x1b[1;32m' + txt.strip() + '\x1b[0m\n')

# Print info/warning msg
def wprint(txt):
  sys.stdout.write('\x1b[1;32m' + txt.strip() + '\x1b[0m\n')

# ceate checkum of donwloaded file
def checksum(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
       hash_md5.update(chunk)
  return hash_md5.hexdigest()

# Download from URL
def download(info, retry=True):
  # Download the file first
  new_file, filename = tempfile.mkstemp()
  url = info['url']
  #request = urllib2.Request(url, headers={'Accept-Encoding': 'gzip'})
  request = urllib2.Request(url)
  u = urllib2.urlopen(request)
  meta = u.info()
  file_name = url.split('/')[-1]
  #u = urllib2.urlopen(url)
  #f = open(file_name, 'wb')
  file_size = int(meta.getheaders("Content-Length")[0])
  # TODO: Check if it's zip, for now we just accept zip
  # contentType = meta.getheaders("Content-Type")[0]
  print "Downloading: %s Bytes: %s" % (file_name, file_size)
 
  file_size_dl = 0
  block_sz = 8192
  while True:
    buffer = u.read(block_sz)
    if not buffer:
      break

    file_size_dl += len(buffer)
    os.write(new_file, buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

  os.close(new_file)

  '''md5 = checksum(new_file)
  if md5 != info.checksum:
    print('Downloaded file is corrupted try to download the file again')
    if retry:
      # We just retry one time
      return download(info, False)'''
  #_, raw = tempfile.mkstemp()
  #with gzip.open(filename, 'rb') as f_in, open(raw, 'wb') as f_out:
  #  f_out.write(f_in.read())
  
  zip_ref = zipfile.ZipFile(filename, 'r')
  zip_ref.extractall(filename + '_files')
  zip_ref.close()

  return filename + '_files/rom.bin'

def whichExec(program):
  import os
  def is_exe(fpath):
      return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

  fpath, fname = os.path.split(program)
  if fpath:
      if is_exe(program):
          return program
  else:
      for path in os.environ["PATH"].split(os.pathsep):
          exe_file = os.path.join(path, program)
          if is_exe(exe_file):
              return exe_file

  return None

# ------------------------ Main -------------------------
example='''

Examples:
  
  deviceappstore.py eprism_s04 abdollahpour/eprism-test
  deviceappstore.py eprism_s04 143399425

'''

parser = argparse.ArgumentParser(
  description='DeviceAppStore helps you to setup application into your device directly from the deviceappstore.com market', 
  epilog=example,
  formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('device', help='Type of device you connected to your sysytem')
parser.add_argument('app', help='The ID or Complete name of the application you want to setup')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.35')

args = parser.parse_args()

if __name__ == '__main__':
  try:
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'deviceappstore-installer/0.1'), ('Accept-Encoding', 'xz')]
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    info = json.load(urllib2.urlopen('https://deviceappstore.com/api/app/' + args.app, context=ctx))
  except urllib2.HTTPError, e:
    if e.code == 404:
      eprint("The application did not find: '" + args.app + "'. Please check the app ID/Name and try again.")
    else:
      print e.code
      print e.msg
      print e.headers
      print e.fp.read()
    exit()
  except urllib2.URLError, e:
    print(e)
    print('Error to connect to the server, check the internet connection or update the app')
    exit()

  # TODO: Download setup instruction http://deviceappstore.com/setup/eprism_s04
  esptool = ""
   
  try:
    print(which('esptool.py').replace('.exe', '-script.py'))
    esptool = imp.load_source('esptool', which('esptool.py').replace('.exe', '-script.py'))
  except Exception as e:
    print(e)
  if whichExec('esptool.py') is None:
    eprint('You need to setup esptool.py to be able to setup this application:')
    print('\n    (sudo) pip install esptool\n')
    exit(1)

  setup = 'esp8266'

  if args.device in info['devices']:
    type = 'esp8266'

    if type == 'esp8266':
      # Find the port
      platformName = platform.system()
      print(platformName)
      # Detec possible serial port Linux/Mac
      if platformName == 'Darwin' or platformName == 'Linux':
        output = subprocess.check_output(['ls', '-lah', '/dev/'])
        if 'ttyUSB0' in output:
          port = '/dev/ttyUSB0'
        elif 'ttyUSB1' in output:
          port = '/dev/ttyUSB1'
        elif 'tty.SLAB_USBtoUART' in output:
          port = '/dev/tty.SLAB_USBtoUART'
        elif 'cu.wchusbserial1410' in output:
          port = '/dev/cu.wchusbserial1410'
        else:
          eprint('Could not find the device, are you sure the device is connected?')
          exit(1)
      elif platformName == 'Windows':
        output = subprocess.check_output([which('esptool.py'), 'chip_id'])
        if 'COM3' in output:
          port = 'COM3'
        elif 'COM5' in output:
          port = 'COM5'
        else:
          eprint('Could not find the device, are you sure the device is connected?')
          exit(1)
      else:
        eprint('Could not detect your OS')
        exit(1)

      eprint('Please do not unplug your device until the operation finishs. Any intruption may damage your device.')

      version = info['versions'][0]

      # Download the ROM
      rom_info = version['rom']
      rom = download(rom_info)

      params = rom_info['params'].split()
      params.insert(0, which('esptool.py'))
      params.insert(1, '--port')
      params.insert(2, port)
      params.append(rom)
      #sys.argv[:] = params
      #esptool.main()
      call(params)
      
      sprint("Congradulation, it's done!")
    else:
      eprint('The application type does not support, please update the installer app')    
  else:
    eprint('This application does not supported on your traget device!')
