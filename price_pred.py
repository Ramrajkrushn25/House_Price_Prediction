from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and expected features
model = joblib.load("price_predictor.pkl")

# Define all feature names used during training (manual list based on your message)
expected_features = [
    "LotFrontage", "LotArea", "LotShape", "OverallQual", "OverallCond", "MasVnrArea",
    "BsmtQual", "BsmtExposure", "BsmtFinType1", "BsmtUnfSF", "TotalBsmtSF", "HeatingQC",
    "GrLivArea", "BsmtFullBath", "FullBath", "HalfBath", "BedroomAbvGr", "Fireplaces",
    "GarageFinish", "GarageArea", "WoodDeckSF", "OpenPorchSF", "WhetherRemodelled", "AgeOfProperty",
    
    # One-hot encoded features
    "MSSubClass_30", "MSSubClass_40", "MSSubClass_45", "MSSubClass_50", "MSSubClass_60",
    "MSSubClass_70", "MSSubClass_75", "MSSubClass_80", "MSSubClass_85", "MSSubClass_90",
    "MSSubClass_120", "MSSubClass_160", "MSSubClass_180", "MSSubClass_190",

    "MSZoning_FV", "MSZoning_RH", "MSZoning_RL",

    "Neighborhood_Blueste", "Neighborhood_BrDale", "Neighborhood_BrkSide", "Neighborhood_ClearCr",
    "Neighborhood_CollgCr", "Neighborhood_Crawfor", "Neighborhood_Edwards", "Neighborhood_Gilbert",
    "Neighborhood_IDOTRR", "Neighborhood_MeadowV", "Neighborhood_Mitchel", "Neighborhood_NAmes",
    "Neighborhood_NPkVill", "Neighborhood_NWAmes", "Neighborhood_NoRidge", "Neighborhood_NridgHt",
    "Neighborhood_OldTown", "Neighborhood_SWISU", "Neighborhood_Sawyer", "Neighborhood_SawyerW",
    "Neighborhood_StoneBr", "Neighborhood_Timber", "Neighborhood_Veenker",

    "RoofStyle_Gable", "RoofStyle_Gambrel", "RoofStyle_Mansard", "RoofStyle_Shed",

    "Exterior1st_AsphShn", "Exterior1st_BrkComm", "Exterior1st_BrkFace", "Exterior1st_CBlock",
    "Exterior1st_CemntBd", "Exterior1st_HdBoard", "Exterior1st_ImStucc", "Exterior1st_MetalSd",
    "Exterior1st_Plywood", "Exterior1st_Stone", "Exterior1st_Stucco", "Exterior1st_VinylSd",
    "Exterior1st_Wd Sdng", "Exterior1st_WdShing",

    "Exterior2nd_AsphShn", "Exterior2nd_Brk Cmn", "Exterior2nd_BrkFace", "Exterior2nd_ImStucc",
    "Exterior2nd_Other", "Exterior2nd_Stone", "Exterior2nd_Wd Shng",

    "Foundation_CBlock", "Foundation_Slab", "Foundation_Stone", "Foundation_Wood",

    "GarageType_Attchd", "GarageType_Basment", "GarageType_BuiltIn", "GarageType_CarPort", "GarageType_None",

    "LotConfig_CulDSac", "LotConfig_FR2", "LotConfig_FR3", "LotConfig_Inside",

    "HouseStyle_1Story", "HouseStyle_2.5Fin", "HouseStyle_2.5Unf",

    "MasVnrType_BrkFace", "MasVnrType_Stone"
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Basic numerical input
        data = {
            "LotFrontage": float(request.form["LotFrontage"]),
            "LotArea": float(request.form["LotArea"]),
            "LotShape": int(request.form["LotShape"]),
            "OverallQual": float(request.form["OverallQual"]),
            "OverallCond": float(request.form["OverallCond"]),
            "MasVnrArea": float(request.form["MasVnrArea"]),
            "BsmtQual": int(request.form["BsmtQual"]),
            "BsmtExposure": int(request.form["BsmtExposure"]),
            "BsmtFinType1": int(request.form["BsmtFinType1"]),
            "BsmtUnfSF": float(request.form["BsmtUnfSF"]),
            "TotalBsmtSF": float(request.form["TotalBsmtSF"]),
            "HeatingQC": int(request.form["HeatingQC"]),
            "GrLivArea": float(request.form["GrLivArea"]),
            "BsmtFullBath": float(request.form["BsmtFullBath"]),
            "FullBath": float(request.form["FullBath"]),
            "HalfBath": float(request.form["HalfBath"]),
            "BedroomAbvGr": float(request.form["BedroomAbvGr"]),
            "Fireplaces": float(request.form["Fireplaces"]),
            "GarageFinish": int(request.form["GarageFinish"]),
            "GarageArea": float(request.form["GarageArea"]),
            "WoodDeckSF": float(request.form["WoodDeckSF"]),
            "OpenPorchSF": float(request.form["OpenPorchSF"]),
            "WhetherRemodelled": float(request.form["WhetherRemodelled"]),
            "AgeOfProperty": float(request.form["AgeOfProperty"]),
        }

        # One-hot encoded categories
        categories = ["MSSubClass", "MSZoning", "Neighborhood", "RoofStyle", "Exterior1st",
                      "Exterior2nd", "Foundation", "GarageType", "LotConfig", "HouseStyle", "MasVnrType"]

        for cat in categories:
            value = request.form[cat]
            col_name = f"{cat}_{value}"
            data[col_name] = 1  # This one is active

        # Create full feature vector
        input_df = pd.DataFrame([data])
        input_df = input_df.reindex(columns=expected_features, fill_value=0)

        # Predict
        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
