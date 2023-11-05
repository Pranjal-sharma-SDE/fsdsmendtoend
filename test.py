# import os

# path="notebooks/research.ipynb"

# dir,file=os.path.split(path)

# os.makedirs(dir,exist_ok=True)

# with open(path,"w") as f:
#     pass

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(
    carat=1.34,
    cut="Premium",
    color="G",
    clarity="SI2",
    depth=62.5,
    table=57.0,
    x=7.0,
    y=7.05,
    z=4.38 


)

df=custdataobj.get_data_as_dataframe()
print(df)