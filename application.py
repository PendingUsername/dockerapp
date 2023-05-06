from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def calculator():
	if request.method == 'POST':
		num1 = request.form['num1']
		num2 = request.form['num2']
		operation = request.form['operation']

		if operation == 'add':
			result = int(num1) + int(num2)
		elif operation == 'subtract':
			result = int(num1) - int(num2)
		elif operation == 'multiply':
			result = int(num1) * int(num2)
		elif operation == 'divide':
			result = int(num1) / int(num2)

		return render_template('calculator.html', result=result)

	return render_template('calculator.html')

if __name__ == '__main__':
	application.run(debug=True)