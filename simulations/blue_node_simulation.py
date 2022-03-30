from pgmpy.inference import DBNInference

from dbn_modelling import basics
from util import Timer

basics_node_0 = ('Basics', 0)
variables_node_0 = ('Variables', 0)
data_types_node_0 = ('Data Types', 0)
statements_node_0 = ('Statements', 0)
constants_node_0 = ('Constants', 0)
arithmetic_operators_node_0 = ('Arithmetic Operators', 0)
casting_node_0 = ('Casting', 0)
simple_calculation_programs_node_0 = ('Simple Calculation Programs', 0)
basics_node_1 = ('Basics', 1)
variables_node_1 = ('Variables', 1)
data_types_node_1 = ('Data Types', 1)
statements_node_1 = ('Statements', 1)
constants_node_1 = ('Constants', 1)
arithmetic_operators_node_1 = ('Arithmetic Operators', 1)
casting_node_1 = ('Casting', 1)
simple_calculation_programs_node_1 = ('Simple Calculation Programs', 1)


def run_simulation():
    """
    Run the simulation on the blues nodes using the subcategories of basics as our model.
    """
    model = basics()
    timer = Timer()
    dbn_inf = DBNInference(model)
    
