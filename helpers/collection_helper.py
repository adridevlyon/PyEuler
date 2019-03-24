class CollectionHelper:

    def maximum_term_by_term(self, list_1, list_2):
        merged_lists = [0] * max(len(list_1), len(list_2))
        self.__max_by_index(merged_lists, list_1)
        self.__max_by_index(merged_lists, list_2)
        return merged_lists

    def __max_by_index(self, all_elements, elements):
        for ind, val in enumerate(elements):
            all_elements[ind] = max(all_elements[ind], val)
