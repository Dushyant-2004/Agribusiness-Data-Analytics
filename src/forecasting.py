import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from statsmodels.tsa.arima.model import ARIMA


def calculate_metrics(actual, predicted):
    """
    Calculate model evaluation metrics.
    """

    actual = np.array(actual)
    predicted = np.array(predicted)

    mae = np.mean(
        np.abs(actual - predicted)
    )

    mse = np.mean(
        (actual - predicted) ** 2
    )

    rmse = np.sqrt(mse)

    non_zero_actual = actual != 0

    if np.any(non_zero_actual):
        mape = np.mean(
            np.abs(
                (
                    actual[non_zero_actual]
                    - predicted[non_zero_actual]
                )
                /
                actual[non_zero_actual]
            )
        ) * 100
    else:
        mape = np.nan

    ss_total = np.sum(
        (actual - np.mean(actual)) ** 2
    )

    ss_residual = np.sum(
        (actual - predicted) ** 2
    )

    if ss_total != 0:
        r2 = 1 - (
            ss_residual / ss_total
        )
    else:
        r2 = np.nan

    bias = np.mean(
        predicted - actual
    )

    return {
        "MAE": mae,
        "RMSE": rmse,
        "MAPE": mape,
        "R2": r2,
        "Bias": bias
    }


def prepare_forecasting_data(
    df,
    selected_crop="Rice"
):
    """
    Prepare yearly crop production data
    for forecasting.
    """

    available_crops = df["Crop"].unique()

    if selected_crop not in available_crops:

        selected_crop = (
            df.groupby("Crop")["Production"]
            .sum()
            .sort_values(
                ascending=False
            )
            .index[0]
        )

    print(
        f"\nSelected crop for forecasting: "
        f"{selected_crop}"
    )

    crop_data = df[
        df["Crop"] == selected_crop
    ].copy()

    yearly_data = (
        crop_data
        .groupby("Crop_Year")["Production"]
        .sum()
        .reset_index()
        .sort_values("Crop_Year")
    )

    yearly_data = yearly_data[
        yearly_data["Production"] > 0
    ]

    yearly_data["lag_1"] = (
        yearly_data["Production"]
        .shift(1)
    )

    yearly_data["lag_2"] = (
        yearly_data["Production"]
        .shift(2)
    )

    yearly_data["rolling_mean_3"] = (
        yearly_data["Production"]
        .rolling(3)
        .mean()
    )

    yearly_data = yearly_data.dropna()

    return yearly_data, selected_crop


def run_forecasting(df):
    """
    Train Linear Regression, Random Forest
    and ARIMA models and generate forecasts.
    """

    print("\nStarting forecasting analysis...")

    yearly_data, selected_crop = (
        prepare_forecasting_data(
            df,
            selected_crop="Rice"
        )
    )

    print(
        f"Forecasting records: "
        f"{len(yearly_data)}"
    )

    if len(yearly_data) < 8:

        print(
            "Not enough historical records "
            "for reliable forecasting."
        )

        return

    # -------------------------------------------------
    # Time-based train/test split
    # -------------------------------------------------

    split_index = int(
        len(yearly_data) * 0.8
    )

    train_data = yearly_data.iloc[
        :split_index
    ]

    test_data = yearly_data.iloc[
        split_index:
    ]

    features = [
        "lag_1",
        "lag_2",
        "rolling_mean_3"
    ]

    X_train = train_data[features]
    X_test = test_data[features]

    y_train = train_data["Production"]
    y_test = test_data["Production"]

    results = []

    # -------------------------------------------------
    # Linear Regression
    # -------------------------------------------------

    linear_model = LinearRegression()

    linear_model.fit(
        X_train,
        y_train
    )

    linear_predictions = (
        linear_model.predict(X_test)
    )

    linear_metrics = calculate_metrics(
        y_test,
        linear_predictions
    )

    results.append({
        "Model": "Linear Regression",
        **linear_metrics
    })

    # -------------------------------------------------
    # Random Forest
    # -------------------------------------------------

    random_forest = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    random_forest.fit(
        X_train,
        y_train
    )

    rf_predictions = (
        random_forest.predict(X_test)
    )

    rf_metrics = calculate_metrics(
        y_test,
        rf_predictions
    )

    results.append({
        "Model": "Random Forest",
        **rf_metrics
    })

    # -------------------------------------------------
    # ARIMA
    # -------------------------------------------------

    try:

        arima_model = ARIMA(
            train_data["Production"],
            order=(1, 1, 1)
        )

        arima_fit = arima_model.fit()

        arima_predictions = (
            arima_fit.forecast(
                steps=len(test_data)
            )
        )

        arima_metrics = calculate_metrics(
            y_test,
            arima_predictions
        )

        results.append({
            "Model": "ARIMA",
            **arima_metrics
        })

    except Exception as error:

        print(
            f"ARIMA model error: {error}"
        )

        arima_predictions = np.zeros(
            len(test_data)
        )

    # -------------------------------------------------
    # Save model comparison
    # -------------------------------------------------

    results_df = pd.DataFrame(results)

    os.makedirs(
        "data",
        exist_ok=True
    )

    results_path = os.path.join(
        "data",
        "model_comparison.csv"
    )

    results_df.to_csv(
        results_path,
        index=False
    )

    print(
        f"\nModel comparison saved to: "
        f"{results_path}"
    )

    print("\nModel Performance:")

    print(
        results_df.to_string(
            index=False
        )
    )

    # -------------------------------------------------
    # Actual vs Predicted Chart
    # -------------------------------------------------

    plt.figure(figsize=(12, 7))

    plt.plot(
        test_data["Crop_Year"],
        y_test,
        marker="o",
        label="Actual"
    )

    plt.plot(
        test_data["Crop_Year"],
        linear_predictions,
        marker="o",
        label="Linear Regression"
    )

    plt.plot(
        test_data["Crop_Year"],
        rf_predictions,
        marker="o",
        label="Random Forest"
    )

    if len(arima_predictions) > 0:

        plt.plot(
            test_data["Crop_Year"],
            arima_predictions,
            marker="o",
            label="ARIMA"
        )

    plt.title(
        f"Actual vs Predicted Production - "
        f"{selected_crop}"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "Production"
    )

    plt.legend()

    plt.grid(
        True,
        alpha=0.3
    )

    plt.tight_layout()

    os.makedirs(
        "visualizations",
        exist_ok=True
    )

    plt.savefig(
        os.path.join(
            "visualizations",
            "actual_vs_predicted.png"
        ),
        dpi=300
    )

    plt.close()

    # -------------------------------------------------
    # Future ARIMA Forecast
    # -------------------------------------------------

    try:

        full_arima = ARIMA(
            yearly_data["Production"],
            order=(1, 1, 1)
        )

        full_arima_fit = (
            full_arima.fit()
        )

        future_steps = 5

        future_forecast = (
            full_arima_fit.forecast(
                steps=future_steps
            )
        )

        last_year = int(
            yearly_data["Crop_Year"].iloc[-1]
        )

        future_years = [
            last_year + i
            for i in range(
                1,
                future_steps + 1
            )
        ]

        forecast_df = pd.DataFrame({
            "Year": future_years,
            "Forecasted_Production":
                future_forecast.values
        })

        forecast_path = os.path.join(
            "data",
            "future_production_forecast.csv"
        )

        forecast_df.to_csv(
            forecast_path,
            index=False
        )

        print(
            f"\nFuture forecast saved to: "
            f"{forecast_path}"
        )

        # -------------------------------------------------
        # Future Forecast Chart
        # -------------------------------------------------

        plt.figure(figsize=(12, 7))

        plt.plot(
            yearly_data["Crop_Year"],
            yearly_data["Production"],
            marker="o",
            label="Historical Production"
        )

        plt.plot(
            future_years,
            future_forecast,
            marker="o",
            linestyle="--",
            label="Future Forecast"
        )

        plt.title(
            f"Future Production Forecast - "
            f"{selected_crop}"
        )

        plt.xlabel(
            "Year"
        )

        plt.ylabel(
            "Production"
        )

        plt.legend()

        plt.grid(
            True,
            alpha=0.3
        )

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                "visualizations",
                "future_production_forecast.png"
            ),
            dpi=300
        )

        plt.close()

        print(
            "Created: future_production_forecast.png"
        )

    except Exception as error:

        print(
            f"Future forecast error: {error}"
        )

    print(
        "\nForecasting analysis completed."
    )