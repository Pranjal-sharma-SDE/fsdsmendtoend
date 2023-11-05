from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline
from flask import Flask, request,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict',methods=["GET","POST"])
def predict_datapoints():
    if request.method == "GET":
        return render_template('form.html')
    else:
        data = CustomData(
            carat = request.form.get('carat'),
            cut = request.form.get('cut'),
            color = request.form.get('color'),
            clarity = request.form.get('clarity'),
            depth = request.form.get('depth'),
            table = request.form.get('table'),
            x = request.form.get('x'),
            y = request.form.get('y'),
            z = request.form.get('z')
        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        results=round(results[0],2)
        print(results)
        return render_template("result.html",results=results)
        

app.run(debug=True)

# @app.route('/predict',methods=['POST'])
# def predict():
    # data = CustomData(
    #     carat = request.form.get('carat'),
    #     cut = request.form.get('cut'),
    #     color = request.form.get('color'),
    #     clarity = request.form.get('clarity'),
    #     depth = request.form.get('depth'),
    #     table = request.form.get('table'),
    #     x = request.form.get('x'),
    #     y = request.form.get('y'),
    #     z = request.form.get('z')
    # )
    # pred_df = data.get_data_as_dataframe()
    # print(pred_df)
    # predict_pipeline = PredictPipeline()
    # results = predict_pipeline.predict(pred_df)
    # return str(results)

