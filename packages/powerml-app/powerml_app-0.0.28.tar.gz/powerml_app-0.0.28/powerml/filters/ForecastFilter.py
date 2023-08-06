from powerml import Filter

# NOTE: anticipating name change to ForecastSequence
class ForecastFilter(Filter):
    '''
    This is a class that can be used to filter noise from data for PredictSequence models.
    '''

    def __init__(self):
        super().__init__('text-davinci-002', 'daily revenue forecast for the podcast') # TODO: figure out a prompt that works