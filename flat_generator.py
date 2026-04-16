def flat_generator(list_of_lists):
    for nested_list in list_of_lists:
        for item in nested_list:
            yield item
