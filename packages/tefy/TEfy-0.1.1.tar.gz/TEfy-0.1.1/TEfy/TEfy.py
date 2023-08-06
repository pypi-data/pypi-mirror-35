import requests
from lxml import etree


class OxGaWrap(object):
    """
    Very basic wrapper for a small subset of OxGarage conversions, one-way from doc/docx/odt to TEI XML.
    """
    def __init__(self, path):
        """
        :param path: path to file to be converted
        """

        self.response = None
        self.et_output = None
        self.req_baseurl = 'http://oxgarage.tei-c.org/ege-webservice//Conversions'
        self.conversion_codes = {
            'in': {
                'odt': 'odt%3Aapplication%3Avnd.oasis.opendocument.text',
                'doc': 'doc%3Aapplication%3Amsword/odt%3Aapplication%3Avnd.oasis.opendocument.text',
                'docx': 'docx%3Aapplication%3Avnd.openxmlformats-officedocument.wordprocessingml.document'
            },
            'xmlteip5': 'TEI%3Atext%3Axml/xml%3Aapplication%3Axml',
        }

        self.properties = '/conversion?properties=<conversions><conversion index="0"></conversion>' \
                          '<conversion index="1">' \
                          '<property id="oxgarage.getImages">false</property>' \
                          '<property id="oxgarage.getOnlineImages">false</property>' \
                          '<property id="oxgarage.lang">en</property>' \
                          '<property id="oxgarage.textOnly">true</property>' \
                          '<property id="pl.psnc.dl.ege.tei.profileNames">default</property></conversion>' \
                          '<conversion index="2"><property id="oxgarage.getImages">false</property>' \
                          '<property id="oxgarage.getOnlineImages">false</property>' \
                          '<property id="oxgarage.lang">en</property>' \
                          '<property id="oxgarage.textOnly">true</property>' \
                          '<property id="pl.psnc.dl.ege.tei.profileNames">default</property>' \
                          '</conversion></conversions>'

        self.path = path
        self.format = path.split('.')[-1]
        if self.format not in self.conversion_codes['in']:
            self.format = None
            raise ValueError('Unknown input format. Expected one of the following: {}.'
                             .format(', '.join(self.conversion_codes['in'])))

    def convert_to_tei(self):
        """
        Requests the conversion of the file to TEI P5 XML.
        Saves status code to parameters.
        Saves output as lxml etree Element.
        :return: None
        """
        url = '/'.join([self.req_baseurl, self.conversion_codes['in'][self.format], self.conversion_codes['xmlteip5']])
        url += self.properties
        files = {'upload_file': open(self.path, 'rb')}
        self.response = requests.post(url, files=files)
        self.et_output = etree.fromstring(self.response.content)

    def get_et_output(self):
        """
        Returns document as etree Element after conversion to TEI XML.
        :return: TEI XML document as lxml etree Element or None if no conversion has taken place
        """
        return self.et_output
