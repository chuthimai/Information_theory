# Họ và tên: Chử Thị Mai
# Mã sinh viên: B21DCCN082
# Nhóm lớp tín chỉ: 06
# Lớp quản lý: D21CQCN10-B
# Bài 01

import pandas as pd
import numpy as np
from queue import Queue

data = pd.read_csv("data.csv")
# features = ["Temperature", "Heart Rate", "Pulse", "BPSYS", "BPDIA", "Oxygen Saturation", "PH", "Type"]
standard = {"Temperature": [98, 100], "Heart Rate": [60, 99], "Pulse": [60, 99], "BPSYS": [90, 120], "BPDIA": [60, 80], "Oxygen Saturation": [0.95, 1], "PH": [7.3, 7.5]}
features = data.keys()
data = data[features]

reference_type = {0: "Normal", 1: "Mild", 2: "Severe", 3: "Chronic 1", 4: "Chronic 2", 5: "Chronic 3"}


class Node:
    def __init__(self, level):
        self.level = level
        self.data = None
        self.n = None
        self.data_for_each_type = [None, None, None, None, None, None]
        self.H = None
        self.IG = None
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
        self.IG = self.H - (self.yes.n*self.yes.H + self.no.n*self.no.H)/self.n
        return self.IG

    def print_node(self):
        print(f"{features[self.level]} is normal?")
        print(f"Entropy: H(X) = {self.H}")
        print(f"IG = {self.IG}")


def all_choices():
    res = []
    choice = []

    def recursive(i):
        for feature in features:
            if feature not in choice:
                choice.append(feature)
                if len(choice) == len(features):
                    res.append(choice.copy())
                else:
                    recursive(i+1)
            else:
                continue
            choice.pop()

    recursive(0)
    return res


def create_tree(plan):
    queue = Queue(maxsize=10)
    tree = Node(0)
    tree.data = data
    tree.process_elements()
    queue.put(tree)
    while not queue.empty():
        node = queue.get()
        if node.level == len(plan)-1:
            break
        node.yes = Node(node.level + 1)
        node.no = Node(node.level + 1)
        name = features[node.level]
        down = standard[name][0]
        up = standard[name][1]
        node.yes.data = node.data[(node.data[name]>=down) & (node.data[name]<=up)]
        node.no.data = node.data[(node.data[name]<down) | (node.data[name]>up)]
        if len(node.yes.data) == 0:
            node.yes = None
        else:
            node.yes.process_elements()
            queue.put(node.yes)
        if len(node.no.data) == 0:
            node.no = None
        else:
            node.no.process_elements()
            queue.put(node.no)

    return tree


# tree = create_tree(all_choices()[0][: 4])
print(data.corr().to_string())

