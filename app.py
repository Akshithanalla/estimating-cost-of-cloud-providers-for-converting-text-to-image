# app.py
from flask import Flask, render_template, request
from cost import calculate_total_cost_scenario1, calculate_total_cost_scenario2
usd_to_inr=75
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_cost', methods=['POST'])
def calculate_cost():
    text_prompt = request.form['text_prompt']
    image_width = float(request.form['image_width'])
    image_height = float(request.form['image_height'])
    image_format = request.form['image_format']

    # Calculate costs using the provided input
    scenario1_cost = calculate_total_cost_scenario1(text_prompt, image_width, image_height, image_format)
    scenario2_cost_usd = calculate_total_cost_scenario2(text_prompt, image_width, image_height, image_format)
    scenario2_cost=scenario2_cost_usd*usd_to_inr
    return render_template('index.html', scenario1_cost=scenario1_cost, scenario2_cost=scenario2_cost)

if __name__ == '__main__':
    app.run(debug=True)
