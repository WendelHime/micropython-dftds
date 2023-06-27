class KValueRepository:
    def __init__(self):
        """
        KValueRepository is a super class/interface/abstraction for persisting the constant value K
        """
        self.k_value = 1.0

    def read(self):
        """
        read retrieves the k_value from the storage
        """
        raise NotImplementedError

    def write(self, k_value):
        """
        write stores the k_value
        """
        raise NotImplementedError
