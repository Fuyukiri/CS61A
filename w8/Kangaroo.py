class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, x):
        if x in self.pouch_contents:
            print("object already in pouch")
            return
        self.pouch_contents.append(x)

    def __str__(self):
        if self.pouch_contents:
            return "the kangaroo's pouch contains:" + str(self.pouch_contents)
        else:
            return "the kangaroo's pouch is empty"


k = Kangaroo()
print(k)
k
k.put_in_pouch("as")
k.put_in_pouch("as")
print(k)

print(k)
k.put_in_pouch("bs")
print(k)