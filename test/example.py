import axmlparserpy.axmlprinter as axmlprinter
from xml.dom import minidom
import axmlparserpy.apk as apk

ap = axmlprinter.AXMLPrinter(open('binary/AndroidManifest.xml', 'rb').read())
buff = minidom.parseString(ap.getBuff()).toxml()
print(buff)

ap = apk.APK('apk/sshUnTunnel-2.2.apk')
print(ap.get_package())
print(ap.get_androidversion_name())

