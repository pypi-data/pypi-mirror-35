# *********************************************************************
# +++ IMPORTS
# *********************************************************************
from typing import Optional
from grafeat_api.base.node import Node


# *********************************************************************
# +++ CLASS
# *********************************************************************
class NodeFloat(Node):
    # =====================================================================
    # +++ CONSTANTS
    # =====================================================================
    Param_Value = 0
    Output_Value = 0

    # =====================================================================
    # +++ CONSTRUCTOR
    # =====================================================================
    def __init__(self, id_: Optional[int] = None):
        super(NodeFloat, self).__init__(id_)
        self._display_name = 'Integer'

        self._create_parameter(self.Param_Value, 'Value', 0.0, float)
        self._create_output(self.Output_Value, 'Out', str)

    # =====================================================================
    # +++ STATIC OVERRIDES
    # =====================================================================
    @staticmethod
    def get_description() -> str:
        return 'Creates a constant integer value.'

    # =====================================================================
    # +++ OVERRIDES
    # =====================================================================
    def _validate(self):
        return True

    def _compute_outputs(self):
            self._outputs[self.Output_Value].value = f'{self._parameters[self.Param_Value].value}'
