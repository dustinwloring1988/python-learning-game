# Python Learning Game

This is a Flask-based web application designed to help users practice and improve their Python programming skills. The application presents users with various coding challenges of different difficulty levels and allows them to write and run their code directly in the browser.

## Features

- **Difficulty Levels**: Challenges are categorized into `easy`, `medium`, and `hard` levels.
- **Code Editor**: Integrated code editor using CodeMirror.
- **Instant Feedback**: Users can run their code and see how many tests they passed.
- **Solutions**: View solutions for completed challenges.

## Folder Structure

```
flask_training/
├── app.py
└── challenges/
    ├── easy.yaml
    ├── medium.yaml
    └── hard.yaml
└── templates/
    ├── index.html
    └── challenge.html
```

## How to Run

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/flask_training.git
    cd flask_training
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```sh
    python app.py
    ```

4. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

## Adding New Challenges

To add new challenges, follow these steps:

1. **Open the Appropriate YAML File**:
    Challenges are stored in YAML files within the `challenges` folder (`easy.yaml`, `medium.yaml`, `hard.yaml`).

2. **Add a New Challenge**:
    Use the following structure to add a new challenge:

    ```yaml
    - title: Challenge Title
      difficulty: easy|medium|hard
      description: "Write a function called 'function_name' that does something."
      example: "Example: function_name(input) should return output."
      template: |
        def function_name(params):
            # Write your code here
            pass
      solution: |
        def function_name(params):
            # Correct solution code
            return result
      tests:
        - input: 'function_name(test_input)'
          expected: expected_output
        - input: 'function_name(another_test_input)'
          expected: another_expected_output
    ```

3. **Save and Test**:
    After adding the new challenge, save the YAML file and restart the application to load the new challenges.

## Example Challenge

Here is an example of an easy challenge:

```yaml
- title: Reverse String
  difficulty: easy
  description: "Write a function called 'reverse_string' that returns the reverse of a given string `s`."
  example: "Example: reverse_string('hello') should return 'olleh'."
  template: |
    def reverse_string(s):
        # Write your code here
        pass
  solution: |
    def reverse_string(s):
        return s[::-1]
  tests:
    - input: 'reverse_string("hello")'
      expected: 'olleh'
    - input: 'reverse_string("world")'
      expected: 'dlrow'
    - input: 'reverse_string("Python")'
      expected: 'nohtyP'
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
