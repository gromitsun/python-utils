import sys
import binascii


fin = sys.argv[1]
fout = sys.argv[2]

print("%s -> %s" % (fin, fout))
open(fout, 'wb').write(binascii.b2a_base64(open(fin, 'rb').read()))
