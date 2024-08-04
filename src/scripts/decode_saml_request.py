import base64
import zlib

def decode_deflated_base64(saml_request):
    decoded_bytes = base64.b64decode(saml_request)
    decompressed_data = zlib.decompress(decoded_bytes, wbits=-zlib.MAX_WBITS)
    return decompressed_data.decode('utf-8')



# saml_request = "fVNdb+IwEHzvr4jyTm1CDnIWROLgPpA4QEDv4V7Q1tkUXx07ZztX+u9rp3ClEiUvlsYzszvrzdBCJWs2btxerfFvg9bdRNGhksqy9moUN0YxDVZYpqBCyxxnm/HPOUtuKauNdpprGb8TXdeAtWic0CqIZtNRvFx8nS+/zxY7+qkPSZnQLEsgoV3sJyWnfQr9tN8rk/tBir3BZ94dBOEvNNZ7jGJv2RpZ2+BMWQfKeZAmaYdmHZpuacp6lKWD34E19fmEAtcq987VjBCpOci9to5lNKPEIMjKkuIPqAe9e8RnLjU87lqYnPKSEDMYro7AF6EKoR6uJ79/JVn2Y7tddVbLzTZYjE/zmGhlmwrNBs0/wfFuPb/YI6VtdQLckjj3BlE0DABrR2Dyy5IKHRTggAzJOflNXrOFb3g2XWkp+HOLh++bNhW4j3N1b7stIopO2VJZo2yNXJQCi/i/zVhK/TTxQ3Q4ip1pMI7Iu+LH5cOiXUU/CocHF010VYMRNjwXHoC7Y+C30Of0ifS7tcYyv7p+nPHA8/DKH0/aFOERkfvaWwO+eW3ccUgXzV+7Jlfazm9O1+f/Vf4C"
# decoded_saml_request = decode_deflated_base64(saml_request)
# print(decoded_saml_request)
