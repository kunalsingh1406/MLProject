from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from source.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## route for a home page
@app.route('/', methods=['GET','POST'])
def  predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        gender = request.form.get('gender')
        race_ethnicity = request.form.get('race_ethnicity')
        parental_level_of_education = request.form.get('parental_level_of_education')
        lunch = request.form.get('lunch')
        test_preparation_course = request.form.get('test_preparation_course')
        reading_score = request.form.get('reading_score')
        writing_score = request.form.get('writing_score')

        # Validate required fields
        missing_fields = []
        for field, value in [
            ("gender", gender),
            ("race_ethnicity", race_ethnicity),
            ("parental_level_of_education", parental_level_of_education),
            ("lunch", lunch),
            ("test_preparation_course", test_preparation_course),
            ("reading_score", reading_score),
            ("writing_score", writing_score)
        ]:
            if value is None or value == "":
                missing_fields.append(field)

        if missing_fields:
            return render_template('home.html', error=f"Missing fields: {', '.join(missing_fields)}")

        # Convert scores to float
        try:
            reading_score = float(reading_score)
            writing_score = float(writing_score)
        except ValueError:
            return render_template('home.html', error="Scores must be numbers.")

        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")






        
