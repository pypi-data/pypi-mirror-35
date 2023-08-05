
"Events Module\n\nThis module mirrors the Events API. It allows you to get, post, update, and delete events.\n\nhttps://doc.cognitedata.com/0.5/#Cognite-API-Events\n"
from cognite import _utils, config, _constants
from cognite.v05.dto import EventResponse, EventListResponse


def get_event(event_id, **kwargs):
    "Returns a EventResponse containing an event matching the id.\n\n    Args:\n        event_id (int):         The event id.\n\n    Keyword Arguments:\n        api_key (str):          Your api-key.\n\n        project (str):          Project name.\n\n    Returns:\n        v05.dto.EventResponse: A data object containing the requested event.\n    "
    (api_key, project) = config.get_config_variables(kwargs.get("api_key"), kwargs.get("project"))
    url = config.get_base_url(api_version=0.5) + "/projects/{}/events/{}".format(project, event_id)
    headers = {"api-key": api_key, "content-type": "application/json", "accept": "application/json"}
    res = _utils.get_request(url, headers=headers, cookies=config.get_cookies())
    return EventResponse(res.json())


def get_events(type=None, sub_type=None, asset_id=None, **kwargs):
    "Returns an EventListReponse object containing events matching the query.\n\n    Args:\n        type (str):             Type (class) of event, e.g. 'failure'.\n        sub_type (str):         Sub-type of event, e.g. 'electrical'.\n        asset_id (str):         Return events associated with this assetId.\n    Keyword Arguments:\n        sort (str):             Sort descending or ascending. Default 'ASC'.\n        cursor (str):           Cursor to use for paging through results.\n        limit (int):            Return up to this many results. Maximum is 10000. Default is 25.\n        has_description (bool): Return only events that have a textual description. Default null. False gives only\n                                those without description.\n        min_start_time (string): Only return events from after this time.\n        max_start_time (string): Only return events form before this time.\n        api_key (str):          Your api-key.\n        project (str):          Project name.\n        autopaging (bool):      Whether or not to automatically page through results. If set to true, limit will be\n                                disregarded. Defaults to False.\n\n    Returns:\n        v05.dto.EventListResponse: A data object containing the requested event.\n    "
    (api_key, project) = config.get_config_variables(kwargs.get("api_key"), kwargs.get("project"))
    url = config.get_base_url(api_version=0.5) + "/projects/{}/events".format(project)
    headers = {"api-key": api_key, "content-type": "application/json", "accept": "application/json"}
    if asset_id:
        params = {
            "assetId": asset_id,
            "sort": kwargs.get("sort"),
            "cursor": kwargs.get("cursor"),
            "limit": (kwargs.get("limit", 25) if (not kwargs.get("autopaging")) else _constants.LIMIT_AGG),
        }
    else:
        params = {
            "type": type,
            "subtype": sub_type,
            "assetId": asset_id,
            "sort": kwargs.get("sort"),
            "cursor": kwargs.get("cursor"),
            "limit": (kwargs.get("limit", 25) if (not kwargs.get("autopaging")) else _constants.LIMIT_AGG),
            "hasDescription": kwargs.get("has_description"),
            "minStartTime": kwargs.get("min_start_time"),
            "maxStartTime": kwargs.get("max_start_time"),
        }
    res = _utils.get_request(url, headers=headers, params=params, cookies=config.get_cookies())
    events = []
    events.extend(res.json()["data"]["items"])
    next_cursor = res.json()["data"].get("nextCursor")
    while next_cursor and kwargs.get("autopaging"):
        params["cursor"] = next_cursor
        res = _utils.get_request(url=url, headers=headers, params=params, cookies=config.get_cookies())
        events.extend(res.json()["data"]["items"])
        next_cursor = res.json()["data"].get("nextCursor")
    return EventListResponse(
        {
            "data": {
                "nextCursor": next_cursor,
                "previousCursor": res.json()["data"].get("previousCursor"),
                "items": events,
            }
        }
    )


def post_events(events, **kwargs):
    "Adds a list of events and returns an EventListResponse object containing created events.\n\n    Args:\n        events (List[v05.dto.Event]):    List of events to create.\n\n    Keyword Args:\n        api_key (str):          Your api-key.\n        project (str):          Project name.\n\n    Returns:\n        v05.dto.EventListResponse\n    "
    (api_key, project) = config.get_config_variables(kwargs.get("api_key"), kwargs.get("project"))
    url = config.get_base_url(api_version=0.5) + "/projects/{}/events".format(project)
    headers = {"api-key": api_key, "content-type": "application/json", "accept": "application/json"}
    body = {"items": [event.__dict__ for event in events]}
    res = _utils.post_request(url, body=body, headers=headers)
    return EventListResponse(res.json())


def delete_events(event_ids, **kwargs):
    "Deletes a list of events.\n\n    Args:\n        event_ids (List[int]):    List of ids of events to delete.\n\n    Keyword Args:\n        api_key (str):          Your api-key.\n        project (str):          Project name.\n\n    Returns:\n        An empty response.\n    "
    (api_key, project) = config.get_config_variables(kwargs.get("api_key"), kwargs.get("project"))
    url = config.get_base_url(api_version=0.5) + "/projects/{}/events/delete".format(project)
    headers = {"api-key": api_key, "content-type": "application/json", "accept": "application/json"}
    body = {"items": event_ids}
    res = _utils.post_request(url, body=body, headers=headers)
    return res.json()
