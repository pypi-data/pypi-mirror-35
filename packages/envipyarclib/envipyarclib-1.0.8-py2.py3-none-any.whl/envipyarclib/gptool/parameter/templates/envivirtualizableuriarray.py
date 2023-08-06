"""
Defines the parameter template for the specified data type.
"""
from __future__ import absolute_import
from string import Template
from ..template import Template as ParamTemplate



class ENVIVIRTUALIZABLEURIARRAY(ParamTemplate):
    """
    Defines the parameter template for the specified data type.
    """
    def get_parameter(self, task_param):
        # Input uses a composite data type of both defile and gpstring.
        # This allows for url strings while also providing file selection in the UI.
        if task_param['direction'].upper() == 'INPUT':
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype=["DEFile","GPString"],
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')
        # Return the output template
        else:
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="GPString",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
    ''')

    def parameter_names(self, task_param):
        return [Template('${name}')]

    def default_value(self):
        return Template('''
        ${name}.values = "$defaultValue"
''')

    def pre_execute(self):
        return Template('''
        input_params['${name}'] = parameters[self.i${name}].valueAsText.split(';')
''')

    def post_execute(self):
        return Template('''
        if '${name}' in task_results:
            parameters[self.i${name}].values = task_results['${name}']
''')

def template():
    """Factory method for this parameter template class"""
    return ENVIVIRTUALIZABLEURIARRAY('DEFile')
