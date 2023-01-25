import json

class DataObject:

    def load(self, data):
        if type(data) == str:
            data = json.loads(str)
        for key in self.__dict__.keys():
            if key in data:
                self.__dict__[key] = data[key]

    def load_from(self, path):
        try:
            f = open(path)
            self.load(json.loads(f.read()))
            f.close()
            return True
        except:
            return False
    def dump(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def dump_to(self, path):
        try:
            f = open(path, mode="w+")
            f.write(self.dump())
            f.close()
            return True
        except:
            return False
