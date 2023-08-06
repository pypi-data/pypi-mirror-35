from mlflow import tracking
from mlflow.models import Model
from mlflow.utils.file_utils import TempDir, _copy_file_or_tree

FLAVOR_NAME = "java_function"
MAIN = "loader_module"
CODE = "code"
DATA = "data"
PACKAGES = "packages"

def add_to_model(model, loader_module, data=None, code=None, packages=[]):
    """ Add pyfunc spec to the model configuration.

    Defines pyfunc configuration schema. Caller can use this to create a valid pyfunc model flavor
    out of an existing directory structure. For example, other model flavors can use this to specify
    how to use their output as a pyfunc.

    NOTE: all paths are relative to the exported model root directory.

    :param loader_module: The module to be used to load the model.
    :param model: Existing servable
    :param data: Path to a file or directory containing model data. 
    :param code: Path to a directory containing code dependencies.
    :param packages: Set of Maven coordinates referencing packages required for model evaluation.
    :return: The updated model configuration.
    """
    parms = {MAIN: loader_module}
    parms[PACKAGES] = list(set(packages))
    if code:
        parms[CODE] = code
    if data:
        parms[DATA] = data
    return model.add_flavor(FLAVOR_NAME, **parms)


def save_model(dst_path, loader_module, data_path=None, code_paths=[], packages=[],
               model=Model()):
    """Export model as a generic python-function model.

    :param dst_path: The path where the model is going to be persisted.
    :param loader_module: The module to be used to load the model.
    :param data_path: Path to a file or directory containing model data. 
    :param code_paths: List of paths to additional code dependencies. 
    :param packages: Set of Maven coordinates referencing packages required for model evaluation.
    :return: A model configuration (servable) containing model information.
    """
    if os.path.exists(dst_path):
        raise Exception("Path '{}' already exists".format(dst_path))
    os.makedirs(dst_path)
    code = None
    data = None

    if data_path:
        model_file = _copy_file_or_tree(src=data_path, dst=dst_path, dst_dir="data")
        data = model_file

    if code_paths:
        for path in code_paths:
            _copy_file_or_tree(src=path, dst=dst_path, dst_dir="code")
        code = "code"

    add_to_model(model, loader_module=loader_module, code=code, data=data, packages=packages) 
    model.save(os.path.join(dst_path, 'MLmodel'))
    return model


def log_model(artifact_path, **kwargs):
    """Export the model in java_function form and log it with current mlflow tracking service.

    Model is exported by calling @save_model and logs the result with @tracking.log_output_files
    """
    with TempDir() as tmp:
        local_path = tmp.path(artifact_path)
        run_id = tracking.active_run().info.run_uuid
        if 'model' in kwargs:
            raise Exception("Unused argument 'model'. log_model creates a new model object")

        save_model(dst_path=local_path, model=Model(artifact_path=artifact_path, run_id=run_id),
                   **kwargs)
        tracking.log_artifacts(local_path, artifact_path)
