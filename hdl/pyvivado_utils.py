import os
import logging

from pyvivado import builder, config

logger = logging.getLogger(__name__)

class PyvivadoUtilsBuilder(builder.Builder):
    
    def __init__(self, params):
        super().__init__(params, package_name='pyvivado_utils')
        self.simple_filenames = [
            os.path.join(config.hdldir, 'pyvivado_utils.vhd'),
        ]


class PyvivadoUtilsSvBuilder(builder.Builder):
    
    def __init__(self, params):
        super().__init__(params, package_name='pyvivado_utils_sv')
        self.simple_filenames = [
            os.path.join(config.hdldir, 'pyvivado_utils.sv'),
        ]

assert('pyvivado_utils' not in builder.package_register)
builder.package_register['pyvivado_utils'] = PyvivadoUtilsBuilder
assert('pyvivado_utils_sv' not in builder.package_register)
builder.package_register['pyvivado_utils_sv'] = PyvivadoUtilsSvBuilder
