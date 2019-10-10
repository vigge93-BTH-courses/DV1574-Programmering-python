import pandas as pd
from enum import IntEnum
from sklearn.tree import DecisionTreeClassifier


class Option(IntEnum):
    READ_FILE = 1,
    PRINT = 2,
    ADD_DATA = 3,
    BUILD_TREE = 4,
    ADD_OBSERVATION = 5,
    CLASSIFY = 6,
    EXIT = 7


def menu():
    option = None
    valid = False
    while not valid:
        print('''\n1 Read CSV file
2 Print current data
3 Add manual data
4 Build decision tree
5 Add new observation
6 Classify test data
7 Exit program''')
        option = input('Your choice: ')
        try:
            option = int(option)
            if not (min(Option) <= option <= max(Option)):
                raise ValueError
        except ValueError:
            pass
        else:
            valid = True
    print()
    return option


def load_csv_file(file_name):
    data_frame = pd.DataFrame()
    try:
        data_frame = pd.read_csv(file_name, dtype='category', sep=',')
    except FileNotFoundError:
        print(f'Error when reading file: File \'{file_name}\' does not exist')
    return data_frame


def add_data(data_frame):
    if data_frame.empty:
        print('No data in frame to add to')
        return data_frame
    idt = data_frame.columns[0]
    identifier = input(f'Data identifier ({idt}): ')
    data = {idt: [identifier]}
    for col in data_frame.columns[1:]:
        print(col)
        options = data_frame[col].cat.categories
        print('Possible values:', *options)
        input_valid = False
        while not input_valid:
            inp = input('Input value: ')
            if inp in options:
                input_valid = True
        data[col] = [inp]
    new_data_frame = pd.DataFrame.from_dict(data=data, dtype='category')
    data_frame = data_frame.append(
        new_data_frame, ignore_index=True, sort=False).astype('category')
    print(data_frame)
    return data_frame


def build_decision_tree(data_frame):
    if data_frame.empty:
        print('Error no data to create tree from')
        return
    dtree = DecisionTreeClassifier(criterion='entropy', random_state=0)
    data_frame_code = generate_code_dataframe(data_frame)
    y = data_frame_code.iloc[:, -1]
    x = data_frame_code.iloc[:, 1:-1]
    dtree.fit(x, y)
    print_tree(dtree, x)
    return dtree


def generate_code_dataframe(data_frame):
    data_frame_code = pd.DataFrame()
    for col in data_frame:
        data_frame_code[col] = data_frame[col].astype('category').cat.codes
    return data_frame_code


def add_observation(data_frame, test_data):
    if data_frame.empty:
        print('No data in frame to add to')
        return test_data
    else:
        data = {}
        for col in data_frame.columns[1:-1]:
            print(col)
            options = data_frame[col].cat.categories
            print('Possible values:', *options)
            input_valid = False
            while not input_valid:
                inp = input('Input value: ')
                if inp in options:
                    input_valid = True
            data[col] = [inp]
        new_data_frame = pd.DataFrame.from_dict(data=data, dtype='category')
        test_data = test_data.append(
            new_data_frame, ignore_index=True, sort=False)
        return test_data


def classify(data_frame, decision_tree, test_data):
    if data_frame.empty or not decision_tree or test_data.empty:
        print('Insufficient data')
        return
    test_data_code = generate_code_dataframe(test_data)
    prediction = decision_tree.predict(test_data_code)
    for code in prediction:
        print(data_frame[data_frame.columns[-1]][code])


def print_tree(dtree, X):
    import pydotplus
    from graphviz import Source
    from sklearn.tree import export_graphviz
    import numpy as np
    dot_data = export_graphviz(
        dtree, feature_names=X.columns, out_file=None,
        filled=True, rounded=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    nodes = graph.get_node_list()
    colors = ('springgreen', 'tomato', 'white')

    for node in nodes:
        if node.get_name() not in ('node', 'edge'):
            values = dtree.tree_.value[int(node.get_name())][0]
            # color only nodes where only one class is present
            if max(values) == sum(values):
                node.set_fillcolor(colors[np.argmax(values)])
            # mixed nodes get the default color
            else:
                node.set_fillcolor(colors[-1])
    graph.write_png('tree_color.png')


data_frame = pd.DataFrame()
test_data = pd.DataFrame()
tree = None
option = None
while option != Option.EXIT:
    option = menu()
    if option == Option.READ_FILE:
        file_name = input('Filename: ')
        data_frame = pd.DataFrame()
        test_data = pd.DataFrame()
        tree = None
        data_frame = load_csv_file(file_name)
    elif option == Option.PRINT:
        print(data_frame)
    elif option == Option.ADD_DATA:
        data_frame = add_data(data_frame)
    elif option == Option.BUILD_TREE:
        tree = build_decision_tree(data_frame)
    elif option == Option.ADD_OBSERVATION:
        test_data = add_observation(data_frame, test_data)
    elif option == Option.CLASSIFY:
        classify(data_frame, tree, test_data)
