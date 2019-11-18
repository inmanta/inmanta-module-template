from inmanta.plugins import plugin


@plugin
def hello(what: "string") -> "string":
    """
        Say hello to what
    """
    return f"hello {what}"