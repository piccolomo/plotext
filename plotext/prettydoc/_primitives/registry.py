# Registry primitive: a store of the strings shared by several docstrings (type explanations, recurring messages, long sentences), each kept under a short name

# Holds each stored string, given back by calling the registry with its name
class registry:

    def __init__(self):
        self._doc_dict = {}

    # Store a string under a short name
    def add(self, name, doc):
        self._doc_dict[name] = doc
        return self

    # The string stored under a name, as in registry("celsius")
    def __call__(self, name):
        if name not in self._doc_dict:
            raise ValueError("nothing stored under the name " + name)
        return self._doc_dict[name]

    # The string stored under a name, the given default standing in when the name was never used
    def get(self, name, default = None):
        return self._doc_dict.get(name, default)

    # Number of stored strings
    def __len__(self):
        return len(self._doc_dict)

    # Representation
    def __repr__(self):
        return f"PrettyRegistry({list(self._doc_dict)})"
