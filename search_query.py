from operator_factory import OperatorFactory


class SearchQuery(object):
    DATA_FILE_PATH = "data_source.txt"
    DATA_FILE_OPERATION = "r"
    OPERATION_TYPES = ["AND", "OR"]

    def __init__(self):
        """
            It reads the data source file.
        """
        with open(self.DATA_FILE_PATH, self.DATA_FILE_OPERATION) as file_obj:
            self.news_list = file_obj.readlines()
            file_obj.close()

    def read_user_query(self):
        """
            It is used for reading the input params
            :return: A list of words which are to be searched in the source data file, and the operation to be performed.
        """
        # Read the space seperated search keywords.
        query_list = input("Enter Search keywords: ").lower().split()

        # Read the search type
        search_options = "Enter Search Type:\n"
        for index, word in enumerate(self.OPERATION_TYPES, start=1):
            search_options += str(index) + ". " + word + "\n"
        try:
            search_type = str(input(search_options).upper())
        except ValueError:
            return "Kindly select search type", None, None

        # Check validation for search type
        try:
            if search_type not in self.OPERATION_TYPES:
                raise Exception("Kindly select correct search type")
        except Exception as e:
            return e.__str__(), None, None

        return query_list, search_type, self.news_list


if __name__ == "__main__":
    search_obj = SearchQuery()
    query_list, type_of_search, data_source = search_obj.read_user_query()

    if query_list and type_of_search and data_source:
        operator_obj = OperatorFactory()
        print(operator_obj.choose_operator(type_of_search, query_list, data_source).operate())
    else:
        print(query_list)
