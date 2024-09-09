from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Получаем строку с полями из формы
    input_string = request.form.get('fields')
    
    # Разделяем строку по запятым и убираем лишние пробелы
    fields = [field.strip() for field in input_string.split(',')]
    
    # Формируем шаблон с подстановкой переменных
    result = []
    for field in fields:
        # Для каждого поля добавляем строку с форматированием
        result.append(f"{field} - $result.{field}$")
    
    # Объединяем строки в результат, разделяя их переносами строки
    formatted_result = "\n".join(result)
    
    return f"<pre>{formatted_result}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
