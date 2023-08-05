import numpy as np
import cuid
from .timer import Timer


class Run:

    def __init__(self, experiment):
        self._id = cuid.slug()
        self._experiment = experiment
        self._timer = None
        self._start = None
        self._end = None
        self._interval = None
        self._params = {}
        self._metrics = {}
        self._artifacts = {}

    def start(self):
        if self._timer is not None:
            raise ValueError('Attempt to start a Run that is already started')

        self._timer = Timer()
        self._timer.start()

    def stop(self):
        self._timer.stop()
        self._start = self._timer.start_time
        self._end = self._timer.end_time
        self._interval = self._timer.interval
        self._experiment.save_run(self)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    @property
    def id(self):
        return self._id

    @property
    def start_time(self):
        return int(self._start)

    @property
    def end_time(self):
        return int(self._end)

    @property
    def took(self):
        return self._interval

    @property
    def params(self):
        return self._params

    def get_param(self, param):
        return self.params.get(param)

    @property
    def metrics(self):
        return self._metrics

    def get_metric(self, metric):
        return self.metrics.get(metric)

    @property
    def artifacts(self):
        return self._artifacts

    def get_artifact(self, name):
        return self.artifacts.get(name)

    def to_json(self):
        doc = {'id': self.id, 'start': self.start_time, 'end': self.end_time, 'took': self.took,
               'params': self.params, 'metrics': self.metrics, 'artifacts': [name for name in self.artifacts.keys()]}
        return doc

    @staticmethod
    def from_json(json, experiment):
        run = Run(experiment)
        run._id = json['id']
        run._start = json['start']
        run._end = json['end']
        run._interval = json['took']
        run._params = json['params']
        run._metrics = json['metrics']

        for name in json['artifacts']:
            run._artifacts[name] = experiment.load_artifact(run, name)

        return run

    def log_param(self, name: str, param):
        _val = param

        if self._is_numpy_dtype(param):
            _val = np.asscalar(param)
        elif self._is_numpy_array(param):
            _val = param.tolist()

        self._params[name] = _val

    def log_metric(self, name: str, metric):
        _val = metric

        if self._is_numpy_dtype(metric):
            _val = np.asscalar(metric)
        elif self._is_numpy_array(metric):
            _val = metric.tolist()

        self._metrics[name] = _val

    def log_artifact(self, name: str, artifact):
        self._artifacts[name] = artifact

    @staticmethod
    def _is_numpy_dtype(x):
        return hasattr(x, 'dtype')

    @staticmethod
    def _is_numpy_array(a):
        return isinstance(a, np.ndarray)