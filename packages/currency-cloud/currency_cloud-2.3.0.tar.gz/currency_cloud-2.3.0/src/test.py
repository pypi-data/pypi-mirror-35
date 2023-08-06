import currencycloud
from pprint import pprint

print(currencycloud.VERSION)

## Configure and instantiate the Client ##
login_id = 'mark.sutton@currencycloud.com'
api_key = 'f1f98e476cbca99c3e61df921a444609ee3df4240505a67667fdb613b49defe9'
environment = currencycloud.Config.ENV_DEMO 
client = currencycloud.Client(login_id, api_key, environment)

## Make API calls ##
brds = client.reference.beneficiary_required_details(currency='USD', bank_account_country='US', beneficiary_country='US')
for brd in brds:
    pprint(vars(brd))
