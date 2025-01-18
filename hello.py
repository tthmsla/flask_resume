from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# Create Index Page
@app.route('/')
def index():
	first_name = "Timm"
	favorite_pizza = ["Pepperoni", "Sausage", "Hawaiian"]
	return render_template('index.html', 
		f_name = first_name,
		favorite_pizza = favorite_pizza)

# Create About Page
@app.route('/about')
def about():
	return render_template('about.html')

