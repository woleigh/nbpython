import sys
sys.path.append('./nbox/lib/python3.7/site-packages')
import pynetbox
def nb_hosts(api) :
  nb = pynetbox.api(
      'http://localhost:8000',
      token='0123456789abcdef0123456789abcdef01234567'
  )

  nb_devicelist = nb.dcim.devices.all()
  for n in nb_devicelist:
    print (n.name, n.primary_ip)
    with open('testhosts','a') as f:
          f.write('{0} {1}\n'.format(n.name, n.primary_ip))

nb_hosts('api')