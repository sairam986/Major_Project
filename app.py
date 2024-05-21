from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    skills = request.form['skills']
    experience = int(request.form['experience'])

    # Perform prediction here based on the input
    prediction = predict_job_recommendations_svm(skills, experience)

    if prediction == 1:
        result = "The user is likely to apply for a job."
    else:
        result = "The user is not likely to apply for a job."

    return render_template('index.html', result=result)

def predict_job_recommendations_svm(user_skills, user_experience_years):
    # This function should contain the prediction logic using the trained SVM classifier
    # You can implement the logic here or call the function from your previous code

    # For demonstration purposes, return a dummy prediction
    if 'Python' in user_skills:
        return 1
    else:
        return 0

# Serve favicon.ico file
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)


