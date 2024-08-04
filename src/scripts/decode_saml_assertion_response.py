

import base64
# from xml.etree.ElementTree import tostring
from onelogin.saml2.xmlparser import tostring

from onelogin.saml2.xml_utils import OneLogin_Saml2_XML


def decode_saml_assertion_response(assertion_data):
    b64_decoded = base64.b64decode(assertion_data)
    aa = OneLogin_Saml2_XML.to_etree(b64_decoded)
    decoded_xml = tostring(aa, encoding='unicode', pretty_print=False)
    return decoded_xml