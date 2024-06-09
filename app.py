from flask import Flask, render_template, request
import time
import yaml
import os

app = Flask(__name__)

# Load challenges from YAML files
def load_challenges(difficulty):
    with open(f'challenges/{difficulty}.yaml') as f:
        return yaml.safe_load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/challenge', methods=['GET', 'POST'])
def challenge():
    difficulty = request.args.get('difficulty', 'easy')
    challenges = load_challenges(difficulty)
    challenge = challenges[0]

    if request.method == 'POST':
        code = request.form['code']
        start_time = time.time()
        passed_tests = 0
        error_message = None

        try:
            # Execute the user's code
            exec_globals = {}
            exec(code, exec_globals)

            # Run tests
            for test in challenge['tests']:
                try:
                    result = eval(test['input'], exec_globals)
                    if result == test['expected']:
                        passed_tests += 1
                except Exception as e:
                    error_message = str(e)
                    break

            total_tests = len(challenge['tests'])
            duration = time.time() - start_time
            result = f'{passed_tests}/{total_tests} tests passed in {duration:.2f} seconds.'

        except Exception as e:
            error_message = str(e)
            result = 'Error in your code.'

        return render_template('challenge.html', challenge=challenge, code=code, result=result, error_message=error_message, all_passed=(passed_tests == total_tests))

    return render_template('challenge.html', challenge=challenge, code=challenge['template'], result='', error_message='', all_passed=False)

if __name__ == '__main__':
    app.run(debug=True)
