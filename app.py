from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_string = request.form.get('fields')
    fields = [field.strip() for field in input_string.split(',') if field.strip()]

    short_result = []
    full_result_lines = []
    for field in fields:
        label = field.split('.')[-1]  # Используем последнее имя как читаемое имя
        short_result.append(f"{label} - $result.{field}$")
        full_result_lines.append(f"{field} - $result.{field}$\\n")

    short_output = "\n".join(short_result)
    full_output_string = "".join(full_result_lines)  # Строка с символами \n как текст

    return f"<pre>{short_output}\n\n---\n\n{full_output_string}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
