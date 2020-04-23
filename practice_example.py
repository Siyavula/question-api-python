from practice_api_client import PracticeApiClient

template_id = 2122
random_seed = 256951
right_answer = [["30", "13"]]
wrong_answer = [["40", "13"]]


def example_blank_render(practice_api_client, template_id, random_seed):
    question_content = practice_api_client.get_question(template_id, random_seed=random_seed)
    html = render_question_responsive(question_content['question_html'])

    with open('example_blank_render.html', 'w') as example_file:
        example_file.write(html)


def example_right_answer(practice_api_client, template_id, random_seed, right_answer):
    right_data = {
        'question1a': right_answer[0][0],
        'question1b': right_answer[0][1]
    }
    question_content = practice_api_client.mark_question(template_id, random_seed, right_data)
    html = render_question_responsive(question_content['question_html'])

    with open('example_right_answer.html', 'w') as example_file:
        example_file.write(html)


def example_wrong_answer(practice_api_client, template_id, random_seed, wrong_answer):
    wrong_data = {
        'question1a': wrong_answer[0][0],
        'question1b': wrong_answer[0][1]
    }
    question_content = practice_api_client.mark_question(template_id, random_seed, wrong_data)
    html = render_question_responsive(question_content['question_html'])

    with open('example_wrong_answer.html', 'w') as example_file:
        example_file.write(html)


def example_blank_answer(practice_api_client, template_id, random_seed):
    blank_data = {
        'question1a': '',
        'question1b': ''
    }
    question_content = practice_api_client.mark_question(template_id, random_seed, blank_data)
    html = render_question_responsive(question_content['question_html'])

    with open('example_blank_answer.html', 'w') as example_file:
        example_file.write(html)


def example_blank_render_basic(template_id, random_seed):
    practice_api_client = PracticeApiClient(theme='basic')
    question_content = practice_api_client.get_question(template_id, random_seed=random_seed)
    html = render_question_basic(question_content['question_html'])
    with open('example_blank_render_basic.html', 'w') as example_file:
        example_file.write(html)


def render_question_responsive(question_html):
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Practice Example</title>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>
            <link rel="stylesheet" href="https://www.siyavula.com/static/themes/emas/practice-api/practice-api.min.css"/>
        </head>
        <body>
            <main class="sv-region-main emas sv">
                <div id="monassis" class="monassis monassis--practice monassis--practice-api">
                    <div class="question-wrapper">
                    <div class="question-content">{question_html}</div>
                    </div>
                </div>
            </main>
        </body>
        <script src="https://www.siyavula.com/static/themes/emas/node_modules/mathjax/MathJax.js?config=TeX-MML-AM_HTMLorMML-full"></script>
        <script src="https://www.siyavula.com/static/themes/emas/practice-api/practice-api.min.js"></script>
    </html>""".format(question_html=question_html)


def render_question_basic(question_html):
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Practice API</title>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>

        <link rel="stylesheet" href="https://www.siyavula.com/static/themes/mobile/practice-api/practice-api.min.css"/>
      </head>
      <body class="za-mobile mobile sv">
        <div id="margins">
          <div id="content">
            <div id="monassis" class="monassis monassis--practice monassis--maths monassis--practice-api">
              <div class="question-wrapper">
                <div class="question-content">
                  {question_html}
                </div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </html>""".format(question_html=question_html)


practice_api_client = PracticeApiClient()
practice_api_client.verify_token()
example_blank_render(practice_api_client, template_id, random_seed)
example_right_answer(practice_api_client, template_id, random_seed, right_answer)
example_wrong_answer(practice_api_client, template_id, random_seed, wrong_answer)
example_blank_answer(practice_api_client, template_id, random_seed)
example_blank_render_basic(template_id, random_seed)
