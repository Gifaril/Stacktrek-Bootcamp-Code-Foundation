class Child:
    def __init__(self, name, small_stickers, big_stickers):
        self.name = name
        self.ss = small_stickers
        self.bs = big_stickers

    def get_total_points(self):
        return (self.ss * 5) + (self.bs * 10)


class ChildrenQueue:
    def __init__(self, children):
        self.c = children

    def get_points_list(self):
        return [x.get_total_points() for x in self.c]

    def get_children_queue(self):
        def getScore(arr):
          return arr.get('point')
        arr = []
        for i in self.c:
          arr.append({"name": i.name, "point": i.get_total_points()})
        arr.sort(key=getScore, reverse= True)
        return [x['name'] for x in arr]

    def get_first_child_to_go(self):
        def getScore(arr):
          return arr.get('point')
        arr = []
        for i in self.c:
          arr.append({"name": i.name, "point": i.get_total_points()})
        arr.sort(key=getScore, reverse= True)
        return [x['name'] for x in arr][0]
