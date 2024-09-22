class ClassBuilder():

    default_indent_spaces: int = 4

    def __init__(self, class_name: str, ):
        self.class_name = class_name
        self.cls_fields = []
        self.inst_attr = []
    
    def add_cls_fields(self, name: str, value):
        self.cls_fields.append((name, value))
        return self 
    
    def add_inst_attr(self, name: str, value):
        self.inst_attr.append((name, value))
        return self 
        
    def __str__(self):
        indent = ' ' * self.default_indent_spaces
        field_str: str = ' '
        class_code = f"class{self.class_name}:\n"
        for field_name, field_value in self.cls_fields:
            class_code += f"{indent}__{field_name} = {repr(field_value)}\n"
        if self.inst_attr:
            class_code += f"\n{indent}def__init__(self):\n"
            for attr_name, attr_value in self.inst_attr:
                class_code += f"{indent*2}self.{attr_name} = {repr(attr_value)}\n"
        else:
            class_code += f"\n{indent}pass\n"
        
        return class_code
            

if __name__ == '__main__':

    cb = ClassBuilder('Person').add_inst_attr('name', '').add_inst_attr('age', 0)
    print(cb)
                
    cb = ClassBuilder('Test').add_cls_fields('__protected', []).add_inst_attr('foo', 'bar')
    print(cb)
    
    cb = ClassBuilder('Foo')                     
    print(cb)    
    
# classPerson:

    # def__init__(self):
        # self.name = ''
        # self.age = 0

# classTest:
    # ____protected = []

    # def__init__(self):
        # self.foo = 'bar'

# classFoo:

    # pass

# >>> cb = ClassBuilder('Person').add_inst_attr('name', '').add_inst_attr('age', 0)
# >>> print(cb)
# classPerson:

    # def__init__(self):
        # self.name = ''
        # self.age = 0

# >>> cb = ClassBuilder('Test').add_cls_fields('__protected', []).add_inst_attr('foo', 'bar')
# >>> print(cb)
# classTest:
    # ____protected = []

    # def__init__(self):
        # self.foo = 'bar'

# >>> cb = ClassBuilder('Foo')
# >>> print(cb)
# classFoo:
    # pass


