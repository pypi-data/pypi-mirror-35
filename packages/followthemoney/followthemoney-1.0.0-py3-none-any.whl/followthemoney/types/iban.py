from rdflib import URIRef
from normality import stringify
from schwifty import IBAN

from followthemoney.types.common import PropertyType


class IbanType(PropertyType):
    name = 'iban'
    group = 'ibans'
    prefix = 'iban'

    def validate(self, iban, **kwargs):
        iban = stringify(iban)
        if iban is None:
            return False
        try:
            IBAN(iban)
            return True
        except ValueError as ex:
            print(ex)
            return False

    def clean_text(self, text, **kwargs):
        """Create a more clean, but still user-facing version of an
        instance of the type."""
        return text.replace(" ", "").upper()

    def rdf(self, value):
        return URIRef('iban:%s' % value)
