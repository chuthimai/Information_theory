# Họ và tên: Chử Thị Mai
# Mã sinh viên: B21DCCN082
# Nhóm lớp tín chỉ: 06
# Lớp quản lý: D21CQCN10-B
# Bài 01

import pandas as pd
import numpy as np
from queue import Queue

data = pd.read_csv("data.csv")
features = ["Temperature", "Heart Rate", "Pulse", "BPSYS", "BPDIA", "Oxygen Saturation", "PH", "Type"]
standard = {"Temperature": [98, 100], "Heart Rate": [60, 99], "Pulse": [60, 99], "BPSYS": [90, 120], "BPDIA": [60, 80],
            "Oxygen Saturation": [0.95, 1], "PH": [7.3, 7.5], "Type": [0, 0]}
data = data[features]

reference_type = {0: "Normal", 1: "Mild", 2: "Severe", 3: "Chronic 1", 4: "Chronic 2", 5: "Chronic 3"}


class Node:
    def __init__(self, level):
        self.level = level
        self.data = None
        self.n = None
        self.data_for_each_type = [None, None, None, None, None, None]
        self.H = 0
        self.IG = 0
        self.branch = -1
        self.yes = None
        self.no = None

    def process_elements(self):
        self.n = len(self.data)
        count = self.data["Type"].value_counts()
        for i in range(0, 6):
            try:
                size = count[i]
            except:
                size = 0
            p = size / self.n
            if p == 0:
                self.data_for_each_type[i] = [size, p, 0]
            else:
                self.data_for_each_type[i] = [size, p, np.log2(p)]
        return

    def calculate_H(self):
        for element in self.data_for_each_type:
            self.H = self.H - element[1] * element[2]
        return self.H

    def calculate_IG(self):
        yes_H = 0
        yes_n = 0
        no_H = 0
        no_n = 0
        if self.yes is not None:
            yes_H = self.yes.H
            yes_n = self.yes.n
        if self.no is not None:
            no_H = self.no.H
            no_n = self.no.n
        self.IG = self.H - (yes_n * yes_H + no_n * no_H) / self.n
        return self.IG

    def print_node(self):
        if self.branch == 0:
            print("Branch no")
        if self.branch == 1:
            print("Branch yes")
        print(f"{choose[self.level]} is normal?")
        print(f"Entropy: H(X) = {self.H}")
        print(f"IG = {self.IG}")
        for i in range(0, len(self.data_for_each_type)):
            print(f"{reference_type[i]} = {self.data_for_each_type[i][0]}")
        print()


def all_choices():
    res = []
    choice = []

    def recursive(i):
        for feature in features[:-1]:
            if feature not in choice:
                choice.append(feature)
                if len(choice) == len(features[:-1]):
                    res.append(choice.copy())
                else:
                    recursive(i + 1)
            else:
                continue
            choice.pop()

    recursive(0)
    return res


def create_tree(plan):
    queue = Queue(maxsize=200)
    tree = Node(0)
    tree.data = data
    tree.process_elements()
    tree.calculate_H()
    queue.put(tree)
    while not queue.empty():
        node = queue.get()
        if node.level == len(plan) - 1:
            break
        node.yes = Node(node.level + 1)
        node.no = Node(node.level + 1)
        name = features[node.level]
        down = standard[name][0]
        up = standard[name][1]
        node.yes.data = node.data[(node.data[name] >= down) & (node.data[name] <= up)]
        node.no.data = node.data[(node.data[name] < down) | (node.data[name] > up)]
        if len(node.yes.data) == 0:
            node.yes = None
        else:
            node.yes.process_elements()
            node.yes.calculate_H()
            node.yes.branch = 1
            queue.put(node.yes)
        if len(node.no.data) == 0:
            node.no = None
        else:
            node.no.process_elements()
            node.no.calculate_H()
            node.no.branch = 0
            queue.put(node.no)

    return tree


def cal_IG_for_tree(tree):
    q = Queue(maxsize=200)
    q.put(tree)
    while not q.empty():
        node = q.get()
        node.calculate_IG()
        if node.yes is not None:
            q.put(node.yes)
        if node.no is not None:
            q.put(node.no)


def print_all_tree(tree):
    q = Queue(maxsize=200)
    q.put(tree)
    while not q.empty():
        node = q.get()
        node.print_node()
        if node.yes is not None:
            q.put(node.yes)
        if node.no is not None:
            q.put(node.no)


all = all_choices()
choose = all[1000]
print(choose)
Tree = create_tree(choose)
cal_IG_for_tree(Tree)
print_all_tree(Tree)
