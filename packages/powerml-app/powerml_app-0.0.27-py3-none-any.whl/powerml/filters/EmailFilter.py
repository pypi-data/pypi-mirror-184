from powerml import Filter

class EmailFilter(Filter):
    '''
    This is a class that can be used to filter noise from data for WriteEmail models.
    '''

    def __init__(self):
        super().__init__('text-davinci-002', 'marketing email for the company')