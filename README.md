axmlparserpy: Android XML parser in Python
==============================

兼容python 3.7

axmlparserpy can be used to parse Android binary XML files into plaintext XML.

axmlparserpy was originally created by Anthony Desnos and was extracted from
the Androguard project.

# 安装

```shell script
git clone https://github.com/radmanxu/AxmlParserPY.git
cd AxmlParserPY
pip3 install .
```

# 使用方法

## convert apk binary manifest to string manifest.
```python
import axmlparserpy.axmlprinter as axmlprinter
from xml.dom import minidom

ap = axmlprinter.AXMLPrinter(open('_PATH_TO_MANIFEST_XML', 'rb').read())
buff = minidom.parseString(ap.getBuff()).toxml()
print(buff)
```

## get apk information

```python
import axmlparserpy.apk as apk

ap = apk.APK('_PATH_TO_APK')
print(ap.get_package())
print(ap.get_androidversion_name())
```

# Contributors

* [Anthony Desnos](mailto:anthony.desnos@gmail.com)
* [antitree](mailto:antitree@gmail.com)
* [pee](mailto:pee@erkkila.org)
* [Bryan Bishop](https://github.com/kanzure)

# License

GPL
