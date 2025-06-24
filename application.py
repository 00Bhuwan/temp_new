from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Longitude=float(request.form.get('Longitude')),
            Latitude=float(request.form.get('Latitude')),
            MaxTemp_2m=float(request.form.get('MaxTemp_2m')),
            MinTemp_2m=float(request.form.get('MinTemp_2m')),
            Pressure=float(request.form.get('Pressure')),
            Humidity_2m=float(request.form.get('Humidity_2m')),
            WindSpeed_10m=float(request.form.get('WindSpeed_10m')),
            District=request.form.get('District')
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("before prediction")

        predict_pipeline = PredictPipeline()
        print("mid prediction")
        results = predict_pipeline.predict(pred_df)
        print('after prediction')
        return render_template('home.html', results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
