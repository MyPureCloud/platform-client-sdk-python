import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'your_access_token'
# or use get_client_credentials_token(...), get_saml2bearer_token(...) or get_code_authorization_token(...)

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ChatApi();
thread_id = 'thread_id_example' # str | threadId
page_size = 25 # int | The total page size requested (optional) (default to 25)
page_number = 1 # int | The page number requested (optional) (default to 1)
sort_by = 'sort_by_example' # str | variable name requested to sort by (optional)
expand = ['expand_example'] # list[str] | variable name requested by expand list (optional)
next_page = 'next_page_example' # str | next page token (optional)
previous_page = 'previous_page_example' # str | Previous page token (optional)
limit = 'limit_example' # str | The maximum number of messages to retrieve (optional)
before = 'before_example' # str | The cutoff date for messages to retrieve (optional)
after = 'after_example' # str | The beginning date for messages to retrieve (optional)

try:
    # Get history by thread
    api_response = api_instance.get_chats_thread_messages(thread_id, page_size=page_size, page_number=page_number, sort_by=sort_by, expand=expand, next_page=next_page, previous_page=previous_page, limit=limit, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chats_thread_messages: %s\n" % e)