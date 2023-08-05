

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
from .engaccounts import EngAccounts
from .engactions import EngActions
from .engcalls import EngCalls
from .engcontacts import EngContacts
from .engdispositions import EngDispositions
from .engemails import EngEmails
from .engtasks import EngTasks
from .engusers import EngUsers
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
    eng_accounts: EngAccounts
    eng_actions: EngActions
    eng_calls: EngCalls
    eng_contacts: EngContacts
    eng_dispositions: EngDispositions
    eng_emails: EngEmails
    eng_tasks: EngTasks
    eng_users: EngUsers
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
    _sdk_version: str = "2.0.1"
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
        
    
    
    
    def complete(self, request: operations.PostCompleteEngagementActionRequest) -> operations.PostCompleteEngagementActionResponse:
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

    
    def complete(self, request: operations.PostCompleteEngagementTaskRequest) -> operations.PostCompleteEngagementTaskResponse:
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

    