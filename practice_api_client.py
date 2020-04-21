import logging
import os
import requests

from urllib.parse import urlparse, urljoin

log = logging.getLogger(__name__)


class PracticeApiClient(object):
    """Class managing the interaction with the Siyavula Practice service."""

    DEFAULT_TIMEOUT = 30     # In seconds

    def __init__(self, theme='responsive', region='ZA', curriculum='CAPS'):
        """Initialise the Practice API Client."""
        self.api_host = os.environ['practice_api_host']
        self.client_ip = '127.0.0.1'
        self.token = self._get_token(theme, region, curriculum)

    def _get_token(self, theme, region, curriculum):
        """Get a JSON web token to authenticate communication with the practice service."""
        request_url = urljoin(self.api_host, '/api/practice/v1/get-token')
        data = {
            'name': os.environ['api_client_name'],
            'password': os.environ['api_client_password'],
            'client_ip': self.client_ip,
            'theme': theme,
            'region': region,
            'curriculum': curriculum}

        response = requests.post(request_url, json=data, verify=False, timeout=self.DEFAULT_TIMEOUT)

        if response.status_code == 200:
            return response.json()['token']

        raise Exception('PracticeApiClient could not be initialised: {}'.format(response.content))

    def verify_token(self):
        request_url = urljoin(self.api_host, '/api/practice/v1/verify')
        headers = {'JWT': self.token}
        data = {
            'name': os.environ['api_client_name'],
            'password': os.environ['api_client_password'],
            'client_ip': self.client_ip}

        response = requests.get(
            request_url, json=data, headers=headers, verify=False, timeout=self.DEFAULT_TIMEOUT)

        if response.status_code == 200:
            return response.json()['is_token_valid']

        raise Exception('PracticeApiClient token validity could not be established: {}'.format(
            response.content))

    def get_question(self, template_id, random_seed=None):
        """
        Mark a given question and return the question as answered by the given answer.

        Returns the following information:
        - template_id:        The ID of the question [integer]
        - random_seed:        The seed on which the question variability is anchored [integer]
        - theme:              Whether to render the theme suitable for smartphones ('responsive') or
                              feature phones ('basic'), the most obvious difference being that
                              latex equations are rendered as PNG images rather than passed to the
                              client latex rendering libraries ['responsive' or 'basic']
        - region:             The locale in which the question is being rendered, eg. ZA, NG, US.
                              This can impact the way answers are marked and minor differences in
                              wording that may be more suitable for different
                              countries [2-letter string]
        - curriculum:         The curriculum relevant to the viewers of the question, eg. CAPS, NG.
                              This can impact the way answers are marked and minor differences in
                              wording that may be more suitable for different
                              countries ['CAPS', 'NG' or 'INTL']
        - question_html:      The HTML of the question itself
        """
        request_url = urljoin(self.api_host, '/api/practice/v1/get-question')
        headers = {'JWT': self.token}
        data = {'template_id': template_id}

        if random_seed:
            data['random_seed'] = random_seed

        response = requests.post(
            request_url, json=data, headers=headers, verify=False, timeout=self.DEFAULT_TIMEOUT)

        if response.status_code == 200:
            return response.json()

        raise Exception('PracticeApiClient could not get question: {}'.format(response.content))

    def mark_question(self, template_id, random_seed, user_responses):
        """
        Mark a given question and return the question as answered by the given answer.

        Returns the following information:
        - template_id:        The ID of the question [integer]
        - random_seed:        The seed on which the question variability is anchored [integer]
        - theme:              Whether to render the theme suitable for smartphones ('responsive') or
                              feature phones ('basic'), the most obvious difference being that
                              latex equations are rendered as PNG images rather than passed to the
                              client latex rendering libraries ['responsive' or 'basic']
        - region:             The locale in which the question is being rendered, eg. ZA, NG, US.
                              This can impact the way answers are marked and minor differences in
                              wording that may be more suitable for different
                              countries [2-letter string]
        - curriculum:         The curriculum relevant to the viewers of the question, eg. CAPS, NG.
                              This can impact the way answers are marked and minor differences in
                              wording that may be more suitable for different
                              countries ['CAPS', 'NG' or 'INTL']
        - question_html:      The HTML of the question itself
        - response_correct:   A list of lists with the amount of correct answers per section
                              [list of lists of integers]
        - response_marks:     A list of lists with the marks gained from correct answers per section
                              [list of lists of integers]
        """
        request_url = urljoin(self.api_host, '/api/practice/v1/submit-answer')
        headers = {'JWT': self.token}
        data = {
            'template_id': template_id,
            'random_seed': random_seed,
            'user_responses': user_responses}

        response = requests.post(
            request_url, json=data, headers=headers, verify=False, timeout=self.DEFAULT_TIMEOUT)

        if response.status_code == 200:
            return response.json()

        raise Exception('PracticeApiClient could not get question: {}'.format(response.content))
