class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class School(object):
    def add(self, name, grade):
        self.roster.append(Student(name, grade))

    def grade(self, g):
        return set([s.name for s in self.roster if s.grade == g])

    def sort(self):
        grades = set([s.grade for s in self.roster])
        return sorted([(g, tuple(sorted([s.name for s in
                                 self.roster if s.grade == g])))
                       for g in grades])

    def __init__(self, name):
        self.name = name
        self.roster = []
