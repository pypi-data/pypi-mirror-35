from pyawair.secret import *

from pyawair.devices import *

HEADERS = {
    'Accept': 'application/json', 'Content-Type':
        'application/json', 'Accept-encoding': 'application/json', 'Authorization': 'Bearer {'
                                                                                    '}'.format(
        token)
}


def get_organizations():
    response = requests.get("http://developer-apis.awair.is/v1/org-users/self/orgs",
                            headers=HEADERS)
    return ("Function not implemented yet")
