
from functools import reduce
import math
from csv import writer
import os


class genaratemark:
    def __init__(self, name, subject, mark, lists):
        self.name = name
        self.subject = subject
        self.mark = mark
        self.list = lists
        self.fullmark = 0
        self.avarage = 0
        self.files = "result.csv"

    def allmark(self):
        mark_add = reduce(lambda x, y: x+y, self.mark)
        self.fullmark = mark_add
        print("full mark : ", mark_add)
        avarage = int(mark_add / len(self.subject))
        self.avarage = avarage
        print("avarage : ", avarage)

    def create(self):
        self.subject.insert(0, self.name)
        print(self.subject)

    def find(self):
        cw = os.getcwd()
        li = os.listdir(cw)
        # files = "result.csv"
        if self.files not in li:
            header1 = ["name", "fullmark", "avarage"]
            header1.extend(self.subject)
            with open(self.files, "a") as f_ob:
                wrr = writer(f_ob)
                wrr.writerow(header1)
            print("sucess...")

    def save(self):
        data = [self.name, self.fullmark, self.avarage]
        data.extend(self.mark)
        with open(self.files, "a") as f_ob2:
            wrr2 = writer(f_ob2)
            wrr2.writerow(data)
            print("sucessfuly added ")


def getdata():
    while True:
        # input name
        name = input("enter Name : ")
        subject = {
            "maths": 0,
            "physics": 0,
            "ict": 0,
            "english": 0}
        for i in subject:
            print(i)
            try:
                marks = int(input('marks :'))
            except Exception as e:
                print(e, "enter again")

                return getdata()
            # input validation
            if marks <= 100 and marks >= 0:
                subject[i] = marks
            else:
                print("invalid")
                print("input again")
                return getdata()
        sub_arr = list(subject.keys())
        mark_arr = list(subject.values())
        stud = genaratemark(name, sub_arr, mark_arr, subject)
        stud.allmark()
        stud.find()
        stud.save()


getdata()
