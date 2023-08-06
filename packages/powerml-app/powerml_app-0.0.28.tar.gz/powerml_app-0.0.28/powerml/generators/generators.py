from random import sample
from math import ceil
from powerml.utils.run_ai import run_ai
import time
from datetime import datetime
from nltk.stem import WordNetLemmatizer
from powerml import CreateTopicsModel
import nltk
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

unblocked_human_unprompted_1gram_topics = [
    "SourceMarks",
    "VSCode",
    "Web",
    "Dashboard",
    "Kotlin",
    "Styles",
    "Services",
    "Video",
    "Messages",
    "Threads",
    "Mentions",
    "Git",
    "GitHub",
    "Auth",
    "Hub",
    "Slack",
    "Webhooks",
    "Gradle",
    "Intercom",
    "Adminconsole",
    "Ingestion",
    "Api",
    "Onboarding",
    "Discussions",
    "Insights",
    "Email",
    "Teams",
    "Notifications",
    "Pusher",
    "Logging",
    "Security",
    "Commands",
    "Controllers",
    "Stores",
    "Datastores",
    "Test",
    "Typescript",
    "React",
    "Recommendations",
    "Logs",
    "Compression",
    "Compute",
    "Webpack",
    "Webextension"]

unblocked_human_unprompted_1gram_topics_set = set([lemmatizer.lemmatize(
    topic.lower()) for topic in unblocked_human_unprompted_1gram_topics])

# ideally would like to set this to 20, but would require changes to run_ai
parallel_request_limit = 1
per_minute_request_limit = 20
delay_in_seconds = 60.0 / per_minute_request_limit


def fuzzy_modify(data, model, prompt):  # NOTE: could add reference data for this
    modified_examples = []
    for i in range(0, len(data), parallel_request_limit):
        curr_data = data[i:i+parallel_request_limit]
        prompt_append = f'\n\nModify this example to {prompt}.\n\n\"'
        prompts = [f'\"{datum}\"{prompt_append}' for datum in curr_data]
        generations = run_ai(prompts,
                             stop='\"',
                             api="openai",
                             model=model,
                             max_tokens=256,
                             temperature=0.5,
                             )
        if type(generations) != list:
            generations = [generations]
        modified_examples.extend([generation.strip()
                                 for generation in generations])
        time.sleep(delay_in_seconds)
    return modified_examples


def generate_modified(data, modifier, num_generate):
    print('Start Generating Modified Data:', datetime.now())
    model = 'text-davinci-002'
    generated_data = fuzzy_modify(sample(data, num_generate), model, modifier)
    print('End Generating Modified Data:', datetime.now())
    return generated_data


def coverage_generator(data, gold_labels=unblocked_human_unprompted_1gram_topics_set, coverage_type='topics', return_metrics=True):
    if coverage_type == 'topics':
        model = CreateTopicsModel()
        model.fit(data, 'one-word system components')
        generated_topics = model.predict()
        generated_topics = set([lemmatizer.lemmatize(topic.lower())
                               for topic in generated_topics])
        num_matched_topics = len(gold_labels.intersection(generated_topics))
        num_real_topics = len(unblocked_human_unprompted_1gram_topics_set)
        coverage = num_matched_topics / num_real_topics
        rare_topics = gold_labels.difference(generated_topics)
        generated_data = []
        # generate at least 1 example per rare_topic, proportional to the amount of coverage of the data
        num_generate = max(
            ceil((1 - coverage) * len(data) / len(rare_topics)), 1)
        for topic in rare_topics:
            modifier = f'include the topic \'{topic}\''
            generated_data.extend(generate_modified(
                data, modifier, num_generate))
        metrics = {
            'coverage': coverage,
            'rare_topics': rare_topics,
        }
        if return_metrics:
            return generated_data, metrics
        return generated_data
