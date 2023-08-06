# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import




import datetime
from dataclasses import dataclass
# import re
from string import Template
from typing import Iterable

import colemen_utils as c


from silent.Import import ImportStatement as _imp
import silent.Module as _module
import silent.DocBlock.PackageDocBlock as _doc
import silent.EntityBase as _eb

import se_config as config
log = c.con.log


@dataclass
class Package(_eb.EntityBase):


    # file_path:str = None
    # '''The file path to this package.'''



    def __init__(self,main:config._main_type,**kwargs) -> None:
        '''
            Represents a python package.

            ----------

            Arguments
            -------------------------
            `main` {Main}
                A reference to the project instance.

            Keyword Arguments
            -------------------------
            `name` {str}
                The name of the module.

            `description` {str}
                The documentation description for the module.

            `file_path` {str}
                The file path to where this package will be saved.


            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 12-26-2022 08:35:16
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: Table
            * @xxx [12-26-2022 08:36:08]: documentation for Table
        '''
        kwargs['main'] = main
        super().__init__(**kwargs)


        self._modules = {}
        self._imports:Iterable[config._py_import_type] = []


    @property
    def summary(self):
        '''
            Get the summary property's value

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 12-06-2022 12:10:00
            `@memberOf`: __init__
            `@property`: summary
        '''

        value = {
            "name":self.name.name,
            "file_path":self.file_path,
            "tags":self._tags,
            "modules":{}
        }
        for mod in self.modules:
            _=mod.ast
            value['modules'][mod.name.name] = mod.summary


        return value


    def save(self):
        '''
            Save this package to the output directory.

            ----------

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 01-06-2023 12:30:07
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: save
            * @xxx [01-06-2023 12:30:34]: documentation for save
        '''
        if c.dirs.exists(self.dir_path) is False:
            c.dirs.create(self.dir_path)

        mod_imports = []
        for mod in self.modules:
            mod_imports.append({"import_path":mod.import_path,"name":mod.name.name})
            mod.save()

        # print(f"mod_imports: {self.imports}")
        print(self.import_path)
        # c.file.write(self.file_path,self.init_result)
        c.file.write(f"{self.dir_path}/__init__.py",self.init_result)

    # ---------------------------------------------------------------------------- #
    #                                    MODULES                                   #
    # ---------------------------------------------------------------------------- #

    def add_module(self,name:str,description:str=None)->config._py_module_type:
        '''
            Create a module and associate it to this package.

            ----------

            Arguments
            -------------------------
            `name` {str}
                The name of the module.
            `description` {str}
                The documentation description for the module.


            Return {Module}
            ----------------------
            The new module instance.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 01-05-2023 10:11:02
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: add_module
            * @xxx [01-05-2023 10:12:04]: documentation for add_module
        '''
        mod = _module.Module(
            self.main,
            self,
            name=name,
            description=description,
        )
        self.add_module_import(mod)
        self._modules[name] = mod

        return mod

    @property
    def modules(self)->Iterable[config._py_module_type]:
        '''
            Get a list of module instances associated to this package.

            `default`:[]


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 01-05-2023 10:08:44
            `@memberOf`: __init__
            `@property`: modules
        '''
        value = list(self._modules.values())
        return value

    def get_module_by_name(self,name:str)->config._py_module_type:
        '''
            Retrieve a module by searching for its name.
            ----------

            Arguments
            -------------------------
            `name` {str}
                The module name to search for.


            Return {Module,None}
            ----------------------
            The module instance if it is found, None otherwise.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 01-05-2023 10:20:12
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: get_module_by_name
            * @xxx [01-05-2023 10:21:02]: documentation for get_module_by_name
        '''
        for mod in self.modules:
            if mod.name.name == name:
                return mod
        return None


    def add_module_import(self,module:config._py_module_type):
        imp = _imp()
        if len(module.classes) == 0:
            imp = _imp(import_path=module.import_path)
            imp.add_subject("*")
        else:
            imp.add_subject(module.import_path)
            imp.alias = module.name.name
        
        self._imports.append(imp)

    @property
    def imports(self)->Iterable[config._py_import_type]:
        '''
            Get a list of import instances associated to this package.

            `default`:[]


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 01-06-2023 12:50:31
            `@memberOf`: __init__
            `@property`: imports
        '''
        value = self._imports
        return value

    @property
    def init_result(self):
        '''
            Get the init_result property's value

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 01-06-2023 12:55:38
            `@memberOf`: __init__
            `@property`: init_result
        '''
        doc = _doc.PackageDocBlock(self.main,self)
        value = [doc.result,"\n\n"]
        for imp in self._imports:
            value.append(imp.result)
        value = '\n'.join(value)
        # value = self.init_result
        return value

# def populate_from_dict(data:dict,instance:Package):
#     for k,v in data.items():
#         if hasattr(instance,k):
#             setattr(instance,k,v)

