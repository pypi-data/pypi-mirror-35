from .publisher import Publisher
from .util import firebase_auth, validate_email, build_statistic_event, emails_substitutions
from .constants import Constants
from .datastore import DatastoreClient

name = "merlin_utils"


ds_client = DatastoreClient()
constants = Constants()
publisher = Publisher()
