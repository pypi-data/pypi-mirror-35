import sys
import yaml
import dill
import copy
from more_itertools import unique_everseen
from .utils import log_message
from .logger import getLogger

log = getLogger(__name__)


class Pipeline:

    """
    This class provides a pipeline abstraction used to transform data.  Pipeline steps are just Python functions that
    accept a DataFrame as an argument and are expected to transform or enrich the DataFrame for a certain goal.
    """

    def __init__(self, name: str, depends=None):
        self._name = name
        self._dependencies = []
        self._steps = []
        self._context = {}

        if depends is not None and len(depends) > 0:
            for d in depends:
                self.add_dependency(d)

    @property
    def name(self):
        return self._name

    @property
    def steps(self):
        return self._steps

    @property
    def dependencies(self):
        return self._dependencies

    @property
    def context(self):
        return self._context

    def get_context(self, key: str, default_value=None):
        return self._context.get(key, default_value)

    def set_context(self, key: str, obj):
        self._context[key] = obj

    def add_step(self, fn, name=None):
        fn_name = fn.__name__
        if name is None:
            name = fn_name

        code = dill.dumps(fn)
        self._steps.append({'name': name, 'function': {'name': fn_name, 'code': code, 'type': 'inline'}})

        return self

    def get_step(self, name):
        for step in self._steps:
            if step.get('name') == name:
                code = step.get('function', {}).get('code')
                return dill.loads(code)
        return None

    def remove_step(self, name):
        new_steps = []
        for step in self._steps:
            if step.get('name') != name:
                new_steps.append(step)

        self._steps = new_steps

        return self

    def add_dependency(self, pipeline):
        self._dependencies.append(pipeline)
        self._dependencies = list(unique_everseen(self._dependencies))

        return self

    def reset(self, reset_deps=False, reset_context=False):
        self._steps = []
        if reset_deps:
            self._dependencies = []
        if reset_context:
            self._context = {}

        return self

    def from_pipeline(self, pipeline):
        self._steps = copy.deepcopy(pipeline.steps)
        self._dependencies = copy.deepcopy(pipeline.dependencies)
        self._context = copy.deepcopy(pipeline.context)
        return self

    def _run_dependencies(self, df=None):
        depends = self._dependencies
        if len(depends) > 0:
            for dep in depends:
                if self._name == dep._name:
                    raise Exception('Circular dependency detected in pipeline dependency graph')

                df = dep.run(data=df)

        return df

    def run(self, data):
        # run dependencies
        df = self._run_dependencies(data)

        log_message('running pipeline [%s]:' % self._name, log)

        for step in self._steps:
            func = step.get('function')
            if func is not None:
                if func.get('type', '').lower() == 'inline':
                    fn_name = func.get('name', 'unknown')
                    fn = dill.loads(func.get('code'))
                    log_message('> %s ' % fn_name, log)
                    result = fn(self, df)
                    if result is not None:
                        print("{}: {}".format(fn_name, result.shape))
                        df = result

        return df

    def dumps(self, stream=None, notebook=False):
        pipeline = {
            'steps': self._steps,
            'dependencies': [dep._name for dep in self._dependencies],
            'context': self._context
        }

        if stream is None and notebook:
            stream = sys.stdout

        s = yaml.dump({self._name: pipeline}, stream=stream, indent=2)
        if stream is None:
            return s
