"""
Copyright 2018 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import pickle
from IPython.core.magic import (Magics, magics_class, line_cell_magic)

from types import ModuleType
import subprocess
import uuid
import os
import time

from .logger import getLogger

log = getLogger(__name__)


@magics_class
class CortexMagics(Magics):

    @line_cell_magic
    def cortex_run(self, line, cell=None):
        script_text = []
        pickleable_ns = {}

        for varname, var in self.shell.user_ns.items():
            if not varname.startswith('__'):
                if isinstance(var, ModuleType) and \
                   var.__name__ != 'cortex.magics':
                    script_text.append(
                        'import {} as {}'.format(var.__name__, varname)
                    )

                else:
                    try:
                        pickle.dumps(var)
                        pickleable_ns[varname] = var
                    except BaseException:
                        pass

        script_text.append(cell)
        script_text = '\n'.join(script_text)

        print(script_text)
