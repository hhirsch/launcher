class ServiceLocator:
    def __init__(self):
        pass
    def hasService(self, service):
        return hasattr(self, service)
