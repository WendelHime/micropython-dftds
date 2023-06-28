import ujson
from dftds.kvalue_repository import KValueRepository


class KValueRepositoryFlash(KValueRepository):
    def __init__(self, filename):
        """
        KValueRepositoryFlash implements the KValueRepository by storing the kvalue data on flash memory
        """
        self.filename = filename
        super(KValueRepositoryFlash, self).__init__()

    def read(self):
        file = open(self.filename, mode="r")
        content = file.read()
        file.close()
        if not content:
            raise OSError("empty file")
        obj = ujson.loads(content)
        k_value = obj["k_value"]
        return k_value

    def write(self, k_value):
        file = open(self.filename, mode="w")
        obj = {"k_value": k_value}
        content = ujson.dumps(obj)
        file.write(content)
        file.close()
