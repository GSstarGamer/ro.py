from ..utilities.shared import ClientSharedObject


class BaseInstance:
    """
    Represents an instance of a Roblox item.

    Attributes:
        _shared: The ClientSharedObject.
        id: The instance ID.
    """

    def __init__(self, shared: ClientSharedObject, instance_id: int):
        """
        Arguments:
            shared: The ClientSharedObject.
            instance_id: The asset instance ID.
        """

        self._shared: ClientSharedObject = shared
        self.id: int = instance_id
