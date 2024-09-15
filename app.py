from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_string = request.form.get('fields')
    fields = [field.strip() for field in input_string.split(',')]
    
    result = []
    for field in fields:
        result.append(f"{field} - $result.{field}$")
    
    formatted_result = "\n".join(result)
    
    return f"<pre>{formatted_result}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
