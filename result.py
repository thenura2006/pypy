
from functools import reduce
import math
import json
import csv
import pandas


class genaratemark:
    def __init__(self, name, subject, mark, lists):
        self.name = name
        self.subject = subject
        self.mark = mark
        self.list = lists
        self.fullmark = 0
        self.avarage = 0

    def allmark(self):
        mark_add = reduce(lambda x, y: x+y, self.mark)
        self.fullmark = mark_add
        print("full mark : ", mark_add)
        avarage = int(mark_add / len(self.subject))
        self.avarage = avarage
        print("avarage : ", avarage)

    def save(self):
        data = {
            "name": self.name,
            "result": self.list,
            "fullmark": self.fullmark,
            "avarage": self.avarage
        }
        dun = json.dumps(data)
        x1 = open("result.txt", "a", encoding="utf-8")
        x1.write(dun + ","+'\n')
        x1.close()


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
        stud.save()


getdata()
