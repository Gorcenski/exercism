class Garden(object):
    PLANTS_MAP = {'C': 'Clover',
                  'G': 'Grass',
                  'R': 'Radishes',
                  'V': 'Violets'}

    def plants(self, student):
        if student not in self.students:
            raise ValueError("Could not find student {}.".format(student))

        idx = self.students.index(student) * 2
        return [self.PLANTS_MAP[p] for p in
                ''.join([d[idx:idx + 2] for d in self.diagram])]

    def __init__(self, diagram, students="""Alice Bob Charlie David
                                            Eve Fred Ginny Harriet
                                            Ileana Joseph Kincaid Larry
                                         """.split()):
        self.students = list(sorted(students))
        self.diagram = diagram.splitlines()
