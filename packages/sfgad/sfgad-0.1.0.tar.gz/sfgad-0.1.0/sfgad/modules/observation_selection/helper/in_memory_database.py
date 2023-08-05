import pandas as pd

from .database import Database


class InMemoryDatabase(Database):
    """
    The format of the data-table should be: ['name', 'type', 'time_window', 'feature_1', ..., 'feature_n']
    """

    def __init__(self, feature_names):
        # create a new dataframe
        self.database = pd.DataFrame(
            columns=['name', 'type', 'time_window'] + feature_names)

        # define data types of the columns
        self.database['time_window'] = self.database['time_window'].astype('int64')
        for feature in feature_names:
            self.database[feature] = self.database[feature].astype('float64')

        self.feature_names = feature_names

        # create a dictionary with first occurrences information of vertices
        self.first_occurrences = {}

    def insert_record(self, vertex_name, vertex_type, time_window, feature_values):
        """
        Inserts a record to the database.
        :param vertex_name: The name of the vertex.
        :param vertex_type: The type of the vertex.
        :param time_window: The time step.
        :param feature_values: The corresponding feature values in a list.
        """
        # if first occurrence, add a new entry to self.first_occurrences
        if (vertex_name, vertex_type) not in self.first_occurrences:
            self.first_occurrences[(vertex_name, vertex_type)] = time_window

        # insert
        self.database = self.database.append(
            pd.DataFrame(
                data=[[vertex_name, vertex_type, time_window] + feature_values],
                columns=['name', 'type', 'time_window'] + self.feature_names), ignore_index=True)

    def insert_records(self, records):
        """
        Inserts a record to the database.
        :param records: DataFrame where each row is a record with meta information about the vertex and its features.
        """
        # for each entry: if first occurrence, add a new entry to self.first_occurrences
        for vertex_name, vertex_type, time_window in zip(records['name'], records['type'], records['time_window']):
            if (vertex_name, vertex_type) not in self.first_occurrences:
                self.first_occurrences[(vertex_name, vertex_type)] = time_window

        # insert the records
        self.database = self.database.append(records, ignore_index=True)

    def select_all(self):
        """
        Selects all rows in the database.
        :return a dataframe with all historic data.
        """
        return self.database

    def select_by_vertex_name(self, vertex_name):
        """
        Selects all rows in the database where name=vertex_name.
        :param vertex_name: The given vertex_name.
        :return a dataframe with all historic data of the given vertex.
        """
        return self.database[self.database['name'] == vertex_name]

    def select_by_vertex_type(self, vertex_type):
        """
        Selects all rows in the database where type=vertex_type.
        :param vertex_type: The given vertex type.
        :return a dataframe with all historic data of vertices, which are of the given type.
        """
        return self.database[self.database['type'] == vertex_type]

    def select_by_time_step(self, time_window):
        """
        Selects all rows in the database where time_window=time_window.
        :param time_window: The given time window.
        :return a dataframe with all historic data of vertices, which have the same time window entry.
        """
        return self.database[self.database['time_window'] == time_window]

    def get_vertices_same_age(self, vertex_name, vertex_type):
        """
        Returns a list with all existing vertices with same age as the given vertex (given vertex not included).
        :param vertex_name: The given vertex_name.
        :param vertex_type: The given vertex type.
        :return a a list with all existing vertices with same age as the given vertex.
        """
        age = self.first_occurrences[(vertex_name, vertex_type)]
        vertices_same_age = []

        # extract all vertices with the same age
        for key, value in self.first_occurrences.items():
            if value == age and key != (vertex_name, vertex_type):
                vertices_same_age.append(key)

        return vertices_same_age
