from powerml import Filter

class SQLFilter(Filter):
    '''
    This is a class that can be used to filter noise from data for AutocompleteSQL models.
    '''

    def __init__(self):
        super().__init__('text-davinci-002', 'SQL query')