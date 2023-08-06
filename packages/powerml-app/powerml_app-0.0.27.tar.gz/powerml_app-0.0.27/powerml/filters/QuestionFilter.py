from powerml import Filter

# NOTE: anticipating name to be QuestionAnswer
class QuestionFilter(Filter):
    '''
    This is a class that can be used to filter noise from data for QuestionAnswer models.
    '''

    def __init__(self):
        super().__init__('text-davinci-002', 'question for students of the lesson')