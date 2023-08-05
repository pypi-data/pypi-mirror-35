import os

from spell.api.client import APIClient
from spell.api.exceptions import ClientException
from spell.client.runs import RunsService
from spell.configs.config_handler import ConfigHandler, ConfigException, default_config_dir

BASE_URL = "https://api.spell.run"
API_VERSION = "v1"


class SpellClient(object):
    """A client for interacting with Spell.

    Attributes:
        workflow_context (int): workflow id of the current workflow context.  All runs created will
            be created in the associated workflow. If the value is ``None``, runs are not created in a workflow.
    """

    def __init__(self, token, base_url=BASE_URL, version_str=API_VERSION, workflow_context=None):
        self.api = APIClient(base_url=base_url, version_str=version_str, token=token)
        user = self.api.get_user_info()
        self.api.owner = user.user_name
        self.workflow_context = workflow_context

    @property
    def runs(self):
        """An object for managing runs.  See :py:class:`~spell.client.runs.RunsService` for documentation."""
        return RunsService(client=self)


def from_environment():
    """Creates a :py:class:`SpellClient` object with configuration deduced from the environment.

    First, attempts to find configuration from environment variables:

    .. envvar:: SPELL_TOKEN

        The authentication token for the user.

    .. envvar:: SPELL_WORKFLOW_ID

        An active workflow configuration for setting the workflow context on the returned client.

    Second, attempts to find configuration from an active user session of the Spell CLI.

    Returns:
        A :py:class:`SpellClient` object.

    Raises:
        :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
    """

    token = os.environ.get("SPELL_TOKEN")
    spell_dir = os.environ.get("SPELL_DIR", default_config_dir())
    base_url = os.environ.get("SPELL_BASE_URL", BASE_URL)

    # parse authentication token from config file if necesary
    if not token:
        config_handler = ConfigHandler(spell_dir)
        try:
            config_handler.load_config_from_file()
        except ConfigException:
            raise ClientException("Spell authentication token not found")
        token = config_handler.config.token

    # parse workflow ID
    workflow = os.environ.get("SPELL_WORKFLOW_ID")
    if workflow:
        try:
            workflow = int(workflow)
        except ValueError:
            raise ClientException("Invalid environment workflow ID: {}".format(workflow))

    return SpellClient(token=token, workflow_context=workflow, base_url=base_url)
