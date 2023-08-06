from spell.client.model import SpellModel


class Workflow(SpellModel):
    """A class representing a single Spell workflow."""

    model = "workflow"

    def __init__(self, api, workflow):
        self._api = api
        self.workflow = workflow

    def refresh(self):
        """Refresh the workflow state.

        Refresh all of the workflow attributes with the latest information for the workflow
        from Spell.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        self.workflow = self._api.get_workflow(self.id)
