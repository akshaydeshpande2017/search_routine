class ANDOperation(object):
    def __init__(self, query_list, news_list):
        self.query_list = query_list
        self.news_list = news_list

    def operate(self):
        """
            It performs the AND operation of query list to determine the number of occurences in news_list.
            :param query_list: It is a list of words
            :param news_list: It is a list of number of lines inside a file
            :return: It returns an element set.
        """
        final_list = []
        for word in self.query_list:
            word_set = set()
            for line_number, news in enumerate(self.news_list):
                if word in news.lower():
                    word_set.add(line_number)
                    continue
            final_list.append(word_set)

        final_set = final_list[0]
        for value_set_index in range(1, len(final_list)):
            final_set = final_set.intersection(final_list[value_set_index])

        return final_set


class OROperation(object):
    def __init__(self, query_list, news_list):
        self.query_list = query_list
        self.news_list = news_list

    def operate(self):
        """
            It performs the OR operation of query list to determine the number of occurences in news_list.
            :param query_list: It is a list of words.
            :param news_list: It is a list of number of lines inside a file.
            :return: It returns an element set
        """
        element_set = set()
        for word in self.query_list:
            for line_number, news in enumerate(self.news_list):
                if word in news.lower():
                    element_set.add(line_number)
                    continue

        return element_set
