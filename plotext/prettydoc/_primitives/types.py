# Types primitive: key/value registry of data type names and their human-readable explanations

# Stores documented data types as attributes for attribute-style lookup
class types_class:
    # Initialize an empty types container
    def __init__(self):
        pass

    # Add a data type with its explanation
    def add(self, type, doc):
        setattr(self, type, doc)
        return self

    # Get the explanation for a data type
    def get(self, type, default = None):
        return getattr(self, type, default)

    # Update or set the explanation
    def set(self, type, doc):
        setattr(self, type, doc)
        return self

    # Remove a data type if it exists
    def remove(self, type):
        if hasattr(self, type):
            delattr(self, type)
        return self

    # Return a shallow copy
    def copy(self):
        out = types_class()
        for attr, value in self.__dict__.items():
            setattr(out, attr, value)
        return out

    # Number of stored data types
    def __len__(self):
        return len(self.__dict__)

    # Representation for debugging
    def __repr__(self):
        return f"PrettyTypes ({list(self.__dict__.keys())})"
