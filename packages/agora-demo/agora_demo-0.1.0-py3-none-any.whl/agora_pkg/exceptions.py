class DatasetNotFoundError(FileNotFoundError):
    def __init__(self, dataset):
        return FileNotFoundError.__init__(self, "Dataset {} not found. Please check the list of datasets to make sure it exists.".format(dataset))

class DatasetExistsError(FileExistsError):
    def __init__(self, dataset):
        return FileExistsError.__init__(self, "Dataset {} already exists".format(dataset))

class CategoryNotFound(Exception):
    def __init__(self, category):
        return Exception.__init__(self, "Category {} not found. Please check the list of categories to make sure it exists".format(category))