""" Driver module for interacting with Cascade CMS 8 REST API provided by Hannon Hill 
for enterprise-scale content management. """

import requests
import logging
import json


class CascadeCMSRestDriver:
    def __init__(self, organization_name="", username="", password="", api_key="", verbose=False):
        self.verbose = verbose
        self.organization_name = organization_name
        self.base_url = f'https://{self.organization_name}.cascadecms.com'
        if username == "" and password == "":
            assert api_key != ""
            self.headers = {
                'Authorization': f'Bearer {api_key}'
            }
        if api_key == "":
            assert username != "" and password != ""
            authstring = f'{username}:{password}'.encode('ascii')
            self.headers = {
                'Authorization': f'Bearer {authstring}'
            }
        self.session = requests.Session()
        self.session.headers = self.headers
        self.setup_logging(verbose=verbose)

    def setup_logging(self, verbose=False):
        """ set up self.logger for Driver logging """
        self.logger = logging.getLogger('DataManager')
        formatter = logging.Formatter('%(prefix)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.prefix = {'prefix': 'Cascade REST Driver'}
        self.logger.addHandler(handler)
        self.logger = logging.LoggerAdapter(self.logger, self.prefix)
        if verbose:
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug('Debug mode enabled', extra=self.prefix)
        else:
            self.logger.setLevel(logging.INFO)

    def debug(self, msg):
        self.logger.debug(msg, extra=self.prefix)

    def info(self, msg):
        self.logger.info(msg, extra=self.prefix)

    def error(self, msg):
        self.logger.error(msg, extra=self.prefix)

    def list_sites(self):
        """ List all sites """
        url = f'{self.base_url}/api/v1/listSites'
        self.debug(f"Listing all sites with {url}")
        return self.session.get(url).json()

    def read_asset(self, asset_type='page', asset_identifier=None):
        """ read a CMS asset given its id and type"""
        url = f'{self.base_url}/api/v1/read/{asset_type}/{asset_identifier}'
        self.debug(f'Reading {asset_type} {asset_identifier} with {url}')
        return self.session.get(url).json()

    def read_asset_workflow_settings(self, asset_type='page', asset_identifier=None):
        """ read workflow settings on a specific asset """
        url = f'{self.base_url}/api/v1/readWorkflowSettings/{asset_type}/{asset_identifier}'
        self.debug(
            f'Reading {asset_type} {asset_identifier} workflow settings with {url}')
        return self.session.get(url).json()

    def edit_asset_workflow_settings(self, asset_type='page', asset_identifier=None, payload=None):
        """ edit workflow settings on a given asset of a given type.
        Include “workflowSettings” in message body based on {wsdl}.
        Its “identifier” property is not necessary since provided in URL.
        If “workflowSettings” is not provided, the folder will have all workflow
        definitions removed and workflow will not be required or inherited.
        This method requires the inclusion of workflow_settings. If you want to remove all workflow
        definitions, use the clear_asset_workflow_settings(asset_type,asset_identifier) method instead.
        """
        response = None
        if payload:
            # required keys in workflow settings
            if 'workflowSettings' in payload and \
                    all([x in payload['workflowSettings'] for x in ['workflowDefinitions', 'inheritWorkflows', 'requireWorkflow']]):
                url = f'{self.base_url}/api/v1/editWorkflowSettings/{asset_type}/{asset_identifier}'
                self.debug(
                    f'Editing workflow settings on {asset_type} {asset_identifier} with {url}')
                if isinstance(payload, dict):
                    self.debug(
                        'Payload is a dictionary; converting to JSON string with json.dumps()')
                    payload = json.dumps(payload)
                response = self.session.post(url, data=payload).json()

            else:
                self.error(
                    f'Not editing workflow settings on page {asset_identifier}; '
                    f'workflow settings must include keys workflowDefinitions '
                    '(asset identifiers list), inheritWorkflows (bool), requireWorkflow '
                    '(bool)'
                )
        else:
            self.error(
                f'Not editing workflow settings on page {asset_identifier}; '
                f'workflow settings not provided. Provide workflow settings based on WSDL'
            )
        return response

    def workflows_exist(self, workflow_settings):
        """ Determine whether any (1 or more) workflows are applied within a
        given readWorkflowSettings response"""
        workflow_settings = workflow_settings if 'workflowSettings' not in workflow_settings else workflow_settings[
            'workflowSettings']
        return len(workflow_settings['workflowDefinitions']) > 0 or \
            len(workflow_settings['workflowDefinitions']) > 0

    def get_user_by_email(self, email_address=""):
        return self.read_asset(asset_type='user', asset_identifier=email_address)

    def get_group(self, group_name):
        return self.read_asset(asset_type='group', asset_identifier=group_name)

    def publish_asset(self, asset_type='page', asset_identifier='', publish_information=None):
        url = f'{self.base_url}/api/v1/publish/{asset_type}/{asset_identifier}'
        self.debug(
            f'Publishing {asset_type} asset {asset_identifier} with {url}')
        if publish_information:
            self.debug(
                f'Publish information provided in request: {publish_information}')
            publish_information = json.dumps(publish_information)
        return self.session.post(url, data=publish_information).json()

    def unpublish_asset(self, asset_type='page', asset_identifier=''):
        self.debug(
            f'Unpublishing {asset_type} asset {asset_identifier}')
        return self.publish_asset(
            asset_type=asset_type,
            asset_identifier=asset_identifier,
            publish_information={
                'publishInformation': {
                    'unpublish': True
                }
            })

    def get_access_rights_for_asset(self, asset_type='page', asset_identifier=''):
        url = f'{self.base_url}/api/v1/readAccessRights/{asset_type}/{asset_identifier}'
        self.debug(
            f'Getting access rights for {asset_type} asset {asset_identifier} with URL {url}')
        return self.session.get(url).json()

    def copy_asset_to_new_container(self, asset_identifier: str = '', new_name: str = '', destination_container_identifier: str = ''):
        url = f'{self.base_url}/api/v1/copy/{asset_identifier}'
        return self.session.post(
            url,
            data=json.dumps({
                'newName': new_name,
                'doWorkflow': False,
                'destinationContainerIdentifier': destination_container_identifier
            })
        ).json()
