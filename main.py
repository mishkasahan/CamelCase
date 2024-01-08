class CamelCase(type):
    def __new__(cls, name, bases, attrs):
        if not name[0].isupper():
            raise ValueError('Назва класу повинна бути у CamelCase')
        return super().__new__(cls, name, bases, attrs)


class notCamelCase(metaclass=CamelCase):
    pass # Raises error: 'Class name not in CamelCase'