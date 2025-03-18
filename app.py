from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form.get('name')
    phone = request.form.get('phone')
    product = request.form.get('product')
    return f'Спасибо, {name}! Ваш заказ ({product}) принят. Мы свяжемся с вами по номеру {phone}.'

if __name__ == '__main__':
    app.run(debug=True)
 
