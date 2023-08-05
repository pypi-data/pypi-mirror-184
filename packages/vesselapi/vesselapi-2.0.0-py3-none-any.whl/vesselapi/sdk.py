

import requests
from typing import Optional
from vesselapi.models import shared, operations
from . import utils


from .accounts import Accounts
from .attendees import Attendees
from .connections import Connections
from .contacts import Contacts
from .deals import Deals
from .emails import Emails
from .events import Events
from .integrations import Integrations
from .leads import Leads
from .links import Links
from .notes import Notes
from .passthrough import Passthrough
from .tasks import Tasks
from .tokens import Tokens
from .users import Users
from .webhooks import Webhooks


SERVERS = [
	"https://api.vessel.land",
]


class VesselAPI:
    
    accounts: Accounts
    attendees: Attendees
    connections: Connections
    contacts: Contacts
    deals: Deals
    emails: Emails
    events: Events
    integrations: Integrations
    leads: Leads
    links: Links
    notes: Notes
    passthrough: Passthrough
    tasks: Tasks
    tokens: Tokens
    users: Users
    webhooks: Webhooks

    _client: requests.Session
    _security_client: requests.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "2.0.0"
    _gen_version: str = "0.17.2"

    def __init__(self) -> None:
        self._client = requests.Session()
        self._security_client = requests.Session()
        


    def config_server_url(self, server_url: str, params: dict[str, str]):
        if params is not None:
            self._server_url = utils.replace_parameters(server_url, params)
        else:
            self._server_url = server_url

        
    

    def config_client(self, client: requests.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        
    

    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        
    
    
    
    def create(self, request: operations.PostEngagementAccountRequest) -> operations.PostEngagementAccountResponse:
        r"""Create Account
        Create a new account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/account"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostEngagementAccountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostEngagementAccountResponseBody])
                res.response_body = out

        return res

    
    def create(self, request: operations.PostCompleteEngagementActionRequest) -> operations.PostCompleteEngagementActionResponse:
        r"""Complete Action
        Complete an action to move a prospect to the next step of a sequence.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/action/complete"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostCompleteEngagementActionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostCompleteEngagementActionResponseBody])
                res.response_body = out

        return res

    
    def create(self, request: operations.PostEngagementContactRequest) -> operations.PostEngagementContactResponse:
        r"""Create Contact
        Create a new contact.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/contact"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostEngagementContactResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostEngagementContactResponseBody])
                res.response_body = out

        return res

    
    def create(self, request: operations.PostEngagementTaskRequest) -> operations.PostEngagementTaskResponse:
        r"""Create Task
        Create a new task.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/task"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostEngagementTaskResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostEngagementTaskResponseBody])
                res.response_body = out

        return res

    
    def create(self, request: operations.PostCompleteEngagementTaskRequest) -> operations.PostCompleteEngagementTaskResponse:
        r"""Complete Task
        Complete a task.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/task/complete"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostCompleteEngagementTaskResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostCompleteEngagementTaskResponseBody])
                res.response_body = out

        return res

    
    def find(self, request: operations.GetOneEngagementAccountRequest) -> operations.GetOneEngagementAccountResponse:
        r"""Get Account
        Retrieve a single Account by Id
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/account"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetOneEngagementAccountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetOneEngagementAccountResponseBody])
                res.response_body = out

        return res

    
    def find(self, request: operations.GetOneEngagementActionRequest) -> operations.GetOneEngagementActionResponse:
        r"""Get Action
        Retrieve a Action by Id.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/action"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetOneEngagementActionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetOneEngagementActionResponseBody])
                res.response_body = out

        return res

    
    def find(self, request: operations.GetOneEngagementCallRequest) -> operations.GetOneEngagementCallResponse:
        r"""Get Call
        Retrieve a Call by Id.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/call"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetOneEngagementCallResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetOneEngagementCallResponseBody])
                res.response_body = out

        return res

    
    def find(self, request: operations.GetOneEngagementContactRequest) -> operations.GetOneEngagementContactResponse:
        r"""Get Contact
        Retrieve a Contact by Id.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/contact"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetOneEngagementContactResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetOneEngagementContactResponseBody])
                res.response_body = out

        return res

    
    def find(self, request: operations.GetOneEngagementEmailRequest) -> operations.GetOneEngagementEmailResponse:
        r"""Get Email
        Retrieve a Email by Id.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/email"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetOneEngagementEmailResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetOneEngagementEmailResponseBody])
                res.response_body = out

        return res

    
    def find(self, request: operations.GetOneEngagementTaskRequest) -> operations.GetOneEngagementTaskResponse:
        r"""Get Task
        Retrieve a Task by Id.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/task"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetOneEngagementTaskResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetOneEngagementTaskResponseBody])
                res.response_body = out

        return res

    
    def find(self, request: operations.GetOneEngagementUserRequest) -> operations.GetOneEngagementUserResponse:
        r"""Get User
        Retrieve a single User by Id
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/user"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetOneEngagementUserResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetOneEngagementUserResponseBody])
                res.response_body = out

        return res

    
    def list(self) -> operations.GetAllEngagementIntegrationsResponse:
        r"""Get Engagement Integrations
        Return all of the Engagement Platform integrations supported by Vessel.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/connection/engagement/integrations"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementIntegrationsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementIntegrationsResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementAccountsRequest) -> operations.GetAllEngagementAccountsResponse:
        r"""Get All Accounts
        Retrieve all Accounts
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/accounts"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementAccountsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementAccountsResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementActionsRequest) -> operations.GetAllEngagementActionsResponse:
        r"""Get All Actions
        Retrieve all Actions
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/actions"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementActionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementActionsResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementCallDispositionsRequest) -> operations.GetAllEngagementCallDispositionsResponse:
        r"""Get All Call Dispositions
        Retrieve all Call Dispositions
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/call-dispositions"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementCallDispositionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementCallDispositionsResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementCallsRequest) -> operations.GetAllEngagementCallsResponse:
        r"""Get All Calls
        Retrieve all Calls
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/calls"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementCallsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementCallsResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementContactsRequest) -> operations.GetAllEngagementContactsResponse:
        r"""Get All Contacts
        Retrieve all Contacts
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/contacts"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementContactsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementContactsResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementEmailsRequest) -> operations.GetAllEngagementEmailsResponse:
        r"""Get All Emails
        Retrieve all Emails
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/emails"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementEmailsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementEmailsResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementTasksRequest) -> operations.GetAllEngagementTasksResponse:
        r"""Get All Tasks
        Retrieve all Tasks
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/tasks"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementTasksResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementTasksResponseBody])
                res.response_body = out

        return res

    
    def list(self, request: operations.GetAllEngagementUsersRequest) -> operations.GetAllEngagementUsersResponse:
        r"""Get All Users
        Retrieve all Users
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/users"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetAllEngagementUsersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetAllEngagementUsersResponseBody])
                res.response_body = out

        return res

    
    def update(self, request: operations.PutEngagementAccountRequest) -> operations.PutEngagementAccountResponse:
        r"""Update Account
        Update an existing account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/engagement/account"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._security_client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PutEngagementAccountResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PutEngagementAccountResponseBody])
                res.response_body = out

        return res

    