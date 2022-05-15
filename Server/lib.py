from collections import Counter
import json


class Teacher:
    def __init__(self, name, comments=None, mark=10, count_marked=0):
        if comments is None:
            comments = Counter()
        self.name = name
        self.characters = comments
        self.average_mark = mark
        self.count_of_marks = count_marked

    def demonstrate(self, count):
        comments = [x[0] for x in self.characters.most_common(count)]
        result = "Comments:  {} \nAverage Mark:  {} \nGave Mark:  {}".format(
            ', '.join(comments), round(self.average_mark, 1),
            self.count_of_marks
        )
        return result.split('\n')

    def give_mark(self, mark):
        try:
            if 0 <= int(mark) <= 10:
                self.average_mark = (self.average_mark * self.count_of_marks +
                                     int(mark)) / (self.count_of_marks + 1)
                self.count_of_marks += 1
            else:
                print("Your mark is incorrect, we don't count it!")
        except TypeError:
            print("Your mark isn't integer")
            pass

    def give_comment(self, comment):
        comment = comment.lower()
        self.characters[comment] += 1


class TeachersCharacters:
    def __init__(self, base_filename):
        self.teachers = dict()
        self.base = base_filename

    def __create_teacher(self, name):
        name = name.lower()
        self.teachers.update({name: Teacher(name)})

    def create_comment(self, name, comment):
        if comment == "":
            return None
        name = name.lower()
        if name not in self.teachers:
            self.__create_teacher(name)
        self.teachers[name].give_comment(comment)

    def create_mark(self, name, mark):
        name = name.lower()
        if name not in self.teachers:
            self.__create_teacher(name)
        self.teachers[name].give_mark(mark)

    def get_most_common_comments(self, name, count_comments=5):
        name = name.lower()
        if name not in self.teachers:
            return ["Nothing has founded about " + name]
        return self.teachers[name].demonstrate(count_comments)

    def load(self):
        with open(self.base, 'r') as data_base:
            files = json.load(data_base)
            self.teachers = {
                name: Teacher(
                    name=name, comments=Counter(comments),
                    mark=mark, count_marked=count_marked
                ) for name, comments, mark, count_marked in files
            }

    def dump(self):
        with open(self.base, 'w') as data_base:
            file = [
                (
                    teacher.name, teacher.characters,
                    teacher.average_mark, teacher.count_of_marks
                ) for teacher in self.teachers.values()
            ]
            json.dump(file, fp=data_base)