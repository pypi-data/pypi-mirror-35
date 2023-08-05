from spell.api.runs_client import RunRequest
from spell.client.model import SpellModel


class RunsService(object):
    """A class for managing Spell runs."""

    def __init__(self, client):
        self.client = client

    def run(self, **kwargs):
        """Create a run.

        Args:
            machine_type (str): the machine type for the run
            command (str): the command to run
            workspace_id (int, optional): the workspace ID for code to include in the run
            commit_hash (str, optional): a specific commit hash in the workspace corresponding to :obj:`workspace_id`
                for code to include in the run.
            workspace_label (str, optional): a workspace commit label for code to include in the run. Only applicable
                if this is a workflow run (i.e., the workflow_context of the client is set or
                a workflow_id is provided). The value must correspond to one of the workspace commit labels specified
                upon workflow creation.
            pip_packages (:obj:`list` of :obj:`str`, optional): pip dependencies.
                For example: ``["moviepy", "scikit-image"]``
            apt_packages (:obj:`list` of :obj:`str`, optional): apt dependencies.
                For example: ``["python-tk", "ffmpeg"]``
            envvars (:obj:`dict` of :obj:`str` -> :obj:`str`, optional): name to value mapping of
                environment variables for the run. For example: ``{"VARIABLE" : "VALUE", "LANG" : "C.UTF-8"}``
            cwd (str, optional): the working directory within the repository in which to execute the command.
                Only applicable if a workspace is specified.
            python2 (bool, optional): set the python version to python 2 (default: false)
            conda_name (str, optional): the name of the conda environment to activate
            conda_file (str, optional): the path to a conda environment file. If not specified and :obj:`conda_name`
                is specified, ``./environment.yml`` is assumed.
            docker_image (str, optional): the name of docker image to use as base
            framework (str, optional): the framework to use for the run. For example: ``pytorch``
            framework_version (str, optional): the framework version to use for the run. For example: ``0.2.0``
            attached_resources (:obj:`dict` of :obj:`str` -> :obj:`str`, optional): resource name to
                mountpoint mapping of attached resouces for the run. For example: ``{"runs/42" : "/mnt/data"}``
            description (str, optional): a description for the run
            idempotent (bool, optional): use an existing identical run if available in liue of re-running
                (default: false)
            workflow_id (int, optional): the id of the workflow to which this run will be associated.  This argument
                is unnecessary if the workflow_context of the client is set and this
                argument will take precedence if they differ.

        Returns:
            A :py:class:`Run` object.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        # grab conda env file contents
        conda_env_contents = None
        if kwargs.get("conda_name"):
            conda_file = kwargs.pop("conda_file") if kwargs.get("conda_file") else "./environment.yml"
            with open(conda_file) as conda_f:
                conda_env_contents = conda_f.read()

        # set workflow id
        if kwargs.get("workflow_id"):
            workflow_id = kwargs.pop("workflow_id")
        else:
            workflow_id = self.client.workflow_context
        # create request
        run_req = RunRequest(run_type="user", conda_file=conda_env_contents,
                             workflow_id=workflow_id, **kwargs)
        run = self.client.api.run(run_req)
        return Run(self, run)


class Run(SpellModel):
    """A class representing a single Spell run."""

    model = "run"

    def __init__(self, service, run):
        self.service = service
        self.run = run

    def stop(self):
        """Stop the run.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        self.service.client.api.stop_run(self.id)

    def kill(self):
        """Kill the run.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.
        """
        self.service.client.api.kill_run(self.id)

    def refresh(self):
        """Refresh the run state.

        Refresh all of the run attributes with the latest information for the run
        from Spell.

        Raises:
            :py:class:`~spell.api.exceptions.ClientException` if an error occurs.

        Example:
            >>> r.status
            'machine_requested'
            >>> r.refresh()
            >>> r.status
            'running'
        """
        self.run = self.service.client.api.get_run(self.id)

    # TODO(Brian): complete rest of Run object methods.....logs, cp, ls, wait, etc.
