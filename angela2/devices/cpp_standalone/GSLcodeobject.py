'''
Module containing CPPStandalone CodeObject for code generation for integration using the ODE solver provided in the
GNU Scientific Library
'''

from angela2.codegen.codeobject import CodeObject
from angela2.devices.cpp_standalone import CPPStandaloneCodeObject
from angela2.codegen.generators.cpp_generator import CPPCodeGenerator
from angela2.codegen.generators.GSL_generator import GSLCPPCodeGenerator

class GSLCPPStandaloneCodeObject(CodeObject):

    templater = CPPStandaloneCodeObject.templater.derive('angela2.devices.cpp_standalone',
                                                         templates_dir='templates_GSL')
    original_generator_class = CPPCodeGenerator
    generator_class = GSLCPPCodeGenerator