from src.data_cleaning import (
    load_data,
    clean_data,
    save_cleaned_data
)

from src.visualization import (
    create_visualizations
)

from src.forecasting import (
    run_forecasting
)

from src.performance_evaluation import (
    run_performance_evaluation
)


def main():

    print("=" * 70)
    print("        AGRIBUSINESS DATA ANALYTICS PROJECT")
    print("              WEEKS 1 - 4 WORKFLOW")
    print("=" * 70)

    # =================================================
    # WEEK 1
    # DATA COLLECTION & CLEANING
    # =================================================

    print("\n" + "=" * 70)
    print("WEEK 1 - DATA COLLECTION & CLEANING")
    print("=" * 70)

    df = load_data()

    df = clean_data(df)

    save_cleaned_data(df)

    # =================================================
    # WEEK 2
    # DATA VISUALIZATION
    # =================================================

    print("\n" + "=" * 70)
    print("WEEK 2 - DATA VISUALIZATION")
    print("=" * 70)

    create_visualizations(df)

    # =================================================
    # WEEK 3
    # PREDICTIVE ANALYSIS & FORECASTING
    # =================================================

    print("\n" + "=" * 70)
    print("WEEK 3 - PREDICTIVE ANALYSIS & FORECASTING")
    print("=" * 70)

    run_forecasting(df)


    # =================================================
    # WEEK 4
    # PERFORMANCE EVALUATION
    # =================================================

    print("\n" + "=" * 70)
    print("WEEK 4 - PERFORMANCE EVALUATION")
    print("=" * 70)

    run_performance_evaluation(df)

    # =================================================
    # FINAL PROJECT SUMMARY
    # =================================================

    print("\n" + "=" * 70)
    print("           COMPLETE PROJECT FINISHED")
    print("=" * 70)

    print("\nGenerated Data Files:")
    print("  1. cleaned_agriculture_data.csv")
    print("  2. model_comparison.csv")
    print("  3. future_production_forecast.csv")
    print("  4. agribusiness_kpi_results.csv")
    print("  5. kpi_benchmark_comparison.csv")
    print("  6. strategic_recommendations.csv")

    print("\nGenerated Visualization Files:")
    print("  1. top_10_crops_production.png")
    print("  2. yearly_production_trend.png")
    print("  3. top_states_production.png")
    print("  4. correlation_heatmap.png")
    print("  5. actual_vs_predicted.png")
    print("  6. future_production_forecast.png")
    print("  7. kpi_performance_vs_benchmark.png")

    print("\n" + "=" * 70)
    print("   AGRIBUSINESS ANALYTICS PROJECT COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()