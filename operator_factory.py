import operations


class OperatorFactory(object):
    """
    Factory method to select the type of Operation to be performed on user search query.
    """
    @staticmethod
    def choose_operator(search_type, query_list, data_source):
        targetclass = search_type + "Operation"
        return getattr(operations, targetclass)(query_list, data_source)
