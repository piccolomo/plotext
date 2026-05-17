# Effect name validation and normalization

from plotext._constants.enums import effect_names


# Validate effect name against allowed names; falls back to default if unknown.
def effect_name(name):
    return name if name in effect_names else effect_names[0]
