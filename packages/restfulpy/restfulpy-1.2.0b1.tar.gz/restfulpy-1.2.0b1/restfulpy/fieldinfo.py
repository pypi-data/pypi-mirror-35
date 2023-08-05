class FieldInfo:
    def __init__(self, type_=str, default=None, optional=False, pattern=None, max_length=None, min_length=None,
                 readonly=False, protected=False, min_=None, max_=None):
        self.type_ = type_ if isinstance(type_, str) else type_.__name__
        self.default = default
        self.optional = optional
        self.pattern = pattern
        self.max_length = max_length
        self.min_length = min_length
        self.min_ = min_
        self.max_ = max_
        self.readonly = readonly
        self.protected = protected

    def to_json(self):
        return {
            'type': self.type_,
            'default_': self.default,
            'optional': self.optional,
            'pattern': self.pattern,
            'maxLength': self.max_length,
            'minLength': self.min_length,
            'readonly': self.readonly,
            'protected': self.protected,
            'min': self.min_,
            'max': self.max_
        }

    def __copy__(self):
        new_one = type(self)()
        new_one.__dict__.update(self.__dict__)
        return new_one

    def to_dict(self):
        return self.__dict__
