Platform API version: 10094


## Release Notes

Optional parameters of an SDK method (originating from API Endpoint path, query or header parameters) can now be set to None.
In this case, the parameter will be ignored and removed from the HTTP request to be issued.
Prior to this version, when setting an optional parameter to None, the parameter was sent with a value "None".
E.g. **api_response = api_instance.get_users(page_size=page_size, page_number=page_number, id=id, jabber_id=None, sort_order=sort_order, expand=expand, integration_presence_source=None, state=state)**


# Major Changes (0 changes)


# Minor Changes (0 changes)


# Point Changes (0 changes)
