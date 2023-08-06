from .documents import Documents as _documents
from .invoices import Invoices as _invoices
from .invoicing import Invoicing as _invoicing
from .items import Items as _items
from .setup import Setup as _setup
from .cfdi_payments import CfdiPayments as _cfdi_payments
from .expenses import Expenses as _expenses
from .banks import Banks as _banks
from .api import AuthenticationError
from .api import PermissionsError
from .api import ResourceNotFound
from .api import TooManyRequests
from .api import ApiError


class ListoApi():
    def __init__(self, token, cer_path=None, key_path=None, key_passphrase=None, base_url="https://listo.mx/api"):
        self.Documents = _documents(token, base_url)
        self.Invoices = _invoices(token, base_url)
        self.Items = _items(token, base_url)
        self.Setup = _setup(token, base_url)
        self.CfdiPayments = _cfdi_payments(token, base_url)
        self.Expenses = _expenses(token, base_url)
        self.Banks = _banks(token, base_url)
        if cer_path and key_path and key_passphrase:
            self.Invoicing = _invoicing(token, cer_path, key_path, key_passphrase, base_url)
