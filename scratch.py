import pandas as pd
import xml.etree.ElementTree as ET
import io

def iter_docs(author):
    author_attr = author.attrib
    for doc in author.iter('document'):
        doc_dict = author_attr.copy()
        doc_dict.update(doc.attrib)
        doc_dict['data'] = doc.text
        yield doc_dict

xml_data = io.StringIO(u'''\
<author type="XXX" language="EN" gender="xx" feature="xx" web="foobar.com">
    <documents count="N">
        <document KEY="e95a9a6c790ecb95e46cf15bee517651" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...]
]]>
        </document>
        <document KEY="bc360cfbafc39970587547215162f0db" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...]
]]>
        </document>
        <document KEY="19e71144c50a8b9160b3f0955e906fce" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...]
]]>
        </document>
        <document KEY="21d4af9021a174f61b884606c74d9e42" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...]
]]>
        </document>
        <document KEY="28a45eb2460899763d709ca00ddbb665" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...]
]]>
        </document>
        <document KEY="a0c0712a6a351f85d9f5757e9fff8946" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...]
]]>
        </document>
        <document KEY="626726ba8d34d15d02b6d043c55fe691" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...]
]]>
        </document>
        <document KEY="2cb473e0f102e2e4a40aa3006e412ae4" web="www.foo_bar_exmaple.com"><![CDATA[A large text with lots of strings and punctuations symbols [...] [...]
]]>
        </document>
    </documents>
</author>
''')

# command to show all columns
pd.set_option('display.max_columns', 30)

etree = ET.parse(xml_data) #create an ElementTree object
doc_df = pd.DataFrame(list(iter_docs(etree.getroot())))

print(doc_df)