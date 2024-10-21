from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None

    if request.method == 'POST':
        try:
            x = float(request.form.get('x'))
            y = float(request.form.get('y'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = x + y
            elif operation == 'subtract':
                result = x - y
            elif operation == 'multiply':
                result = x * y
            elif operation == 'divide':
                if y == 0:
                    error = "Error! Division by zero."
                else:
                    result = x / y
        except ValueError:
            error = "Invalid input! Please enter numbers."

    return render_template('calculator.html', result=result, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000)
