
from powerml import PowerML
import logging
import re
logger = logging.getLogger(__name__)


class AutocompleteSQL:
    def __init__(self,
                 config={},
                 max_output_tokens=256,
                 ):
        self.model = PowerML(config)
        self.model_name = "hex/sql-autocomplete"
        self.max_output_tokens = max_output_tokens

    def predict(self, prompt):
        output = self.model.predict(
            prompt,
            max_tokens=self.max_output_tokens,
            stop=['\\\\nEND', '\\nEND', '\nEND', ';'],
            temperature=0.7,
            model=self.model_name)
        print(output)
        return self.post_process(output)

    def post_process(self, output):
        # TODO: replace with stop tokens
        results = re.split('\\\\nEND|\\nEND|\nEND|select|;', output)
        return results[0].strip()
