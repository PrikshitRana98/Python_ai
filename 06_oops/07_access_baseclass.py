# 1. Code duplication (not recommended)
class MyBaseclass:
    def __init__(self,private_var=None, protected_var=None, public_var=None):
        self.__private_var = private_var if private_var else "I am private"
        self._protected_var = protected_var if protected_var else "I am protected"
        self.public_var = public_var if public_var else "I am public"

    def __private_method(self):
        return "This is a private method"

    def _protected_method(self):
        return "This is a protected method"

    def public_method(self):
        return "This is a public method"

class DuplicateClass:
    def __init__(self,private_var=None, protected_var=None, public_var=None, my_extra_var=None):
        self.__private_var = private_var if private_var else "I am private"
        self._protected_var = protected_var if protected_var else "I am protected"
        self.public_var = public_var if public_var else "I am public"
        
        self.my_extra_var = my_extra_var if my_extra_var else "I am extra"

    def __private_method(self):
        return "This is a private method"

    def _protected_method(self):
        return "This is a protected method"

    def public_method(self):
        return "This is a public method"


# 2. Explicitly using the base class name
class ExplicitClass(MyBaseclass):
    def __init__(self):
        MyBaseclass.__init__(self)
        print(self.public_var)

# 3. Using super()
class SuperClass(MyBaseclass):
    def __init__(self):
        super().__init__()
        print(self.public_var)


