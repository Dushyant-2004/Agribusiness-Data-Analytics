import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_kpis(df):
    """
    Calculate key agribusiness performance indicators
    using the available agricultural production data.
    """

    print("\nCalculating agribusiness KPIs...")

    # -------------------------------------------------
    # 1. Production Efficiency
    # -------------------------------------------------
    total_production = df["Production"].sum()
    total_area = df["Area"].sum()

    if total_area > 0:
        production_efficiency = (
            total_production / total_area
        )
    else:
        production_efficiency = 0

    # -------------------------------------------------
    # 2. Yield Performance
    # -------------------------------------------------
    # Yield is calculated as production per unit area.
    yield_per_area = production_efficiency

    # -------------------------------------------------
    # 3. Production Growth
    # -------------------------------------------------
    yearly_production = (
        df.groupby("Crop_Year")["Production"]
        .sum()
        .sort_index()
    )

    valid_years = yearly_production[
        yearly_production > 0
    ]

    if len(valid_years) >= 2:

        first_value = valid_years.iloc[0]
        last_value = valid_years.iloc[-1]

        if first_value > 0:
            production_growth = (
                (last_value - first_value)
                / first_value
            ) * 100
        else:
            production_growth = 0

    else:
        production_growth = 0

    # -------------------------------------------------
    # 4. Crop Diversity
    # -------------------------------------------------
    crop_count = df["Crop"].nunique()

    # -------------------------------------------------
    # 5. State Coverage
    # -------------------------------------------------
    state_count = df["State_Name"].nunique()

    # -------------------------------------------------
    # 6. Production Concentration
    # -------------------------------------------------
    crop_production = (
        df.groupby("Crop")["Production"]
        .sum()
        .sort_values(ascending=False)
    )

    if total_production > 0:

        top_10_production_share = (
            crop_production.head(10).sum()
            / total_production
        ) * 100

    else:
        top_10_production_share = 0

    # -------------------------------------------------
    # Create KPI DataFrame
    # -------------------------------------------------

    kpi_data = {
        "KPI": [
            "Production Efficiency",
            "Yield Performance",
            "Production Growth",
            "Crop Diversity",
            "State Coverage",
            "Top 10 Crop Production Share"
        ],

        "Value": [
            production_efficiency,
            yield_per_area,
            production_growth,
            crop_count,
            state_count,
            top_10_production_share
        ],

        "Unit": [
            "Production / Area",
            "Production / Area",
            "%",
            "Number of Crops",
            "Number of States",
            "%",
        ]
    }

    kpi_df = pd.DataFrame(kpi_data)

    print("\nKPI Results:")
    print(kpi_df.to_string(index=False))

    return kpi_df


def create_benchmark_comparison(kpi_df):
    """
    Compare selected KPI values with illustrative
    benchmark values.

    Benchmark values are analytical reference values
    and are not claimed to represent an official
    industry standard.
    """

    print("\nCreating benchmark comparison...")

    benchmark_values = {
        "Production Efficiency": 4.0,
        "Yield Performance": 4.0,
        "Production Growth": 5.0,
        "Crop Diversity": 20,
        "State Coverage": 25,
        "Top 10 Crop Production Share": 80.0
    }

    comparison = kpi_df.copy()

    comparison["Benchmark"] = (
        comparison["KPI"]
        .map(benchmark_values)
    )

    comparison["Gap"] = (
        comparison["Value"]
        - comparison["Benchmark"]
    )

    comparison["Performance_%"] = np.where(
        comparison["Benchmark"] != 0,
        (
            comparison["Value"]
            /
            comparison["Benchmark"]
        ) * 100,
        np.nan
    )

    # -------------------------------------------------
    # Performance Status
    # -------------------------------------------------

    def determine_status(row):

        performance = row["Performance_%"]

        if pd.isna(performance):
            return "Not Available"

        if performance >= 100:
            return "Meets / Exceeds"

        if performance >= 80:
            return "Moderate Gap"

        return "Needs Improvement"

    comparison["Status"] = comparison.apply(
        determine_status,
        axis=1
    )

    print("\nBenchmark Comparison:")

    print(
        comparison.to_string(
            index=False
        )
    )

    return comparison


def create_strategic_recommendations(
    comparison_df
):
    """
    Generate strategic recommendations based
    on KPI performance.
    """

    print(
        "\nGenerating strategic recommendations..."
    )

    recommendations = []

    for _, row in comparison_df.iterrows():

        kpi = row["KPI"]
        status = row["Status"]
        performance = row["Performance_%"]

        if status == "Needs Improvement":

            if kpi == "Production Efficiency":

                recommendation = (
                    "Improve production efficiency by "
                    "reviewing crop yield, cultivated "
                    "area, input usage, irrigation, "
                    "and regional performance."
                )

            elif kpi == "Yield Performance":

                recommendation = (
                    "Investigate yield gaps using "
                    "weather conditions, crop practices, "
                    "input availability, and regional "
                    "performance."
                )

            elif kpi == "Production Growth":

                recommendation = (
                    "Analyze declining production trends "
                    "and identify opportunities through "
                    "crop planning, resource optimization, "
                    "and improved farming practices."
                )

            elif kpi == "Crop Diversity":

                recommendation = (
                    "Evaluate crop diversification "
                    "opportunities to reduce concentration "
                    "risk and improve resilience."
                )

            elif kpi == "State Coverage":

                recommendation = (
                    "Expand regional analysis gradually "
                    "where reliable agricultural data "
                    "and comparable operating conditions "
                    "are available."
                )

            elif kpi == "Top 10 Crop Production Share":

                recommendation = (
                    "Monitor dependence on major crops "
                    "and evaluate diversification and "
                    "market-risk management strategies."
                )

            else:

                recommendation = (
                    "Investigate the KPI gap and develop "
                    "a targeted improvement plan."
                )

        elif status == "Moderate Gap":

            recommendation = (
                f"Monitor {kpi.lower()} closely and "
                "implement targeted improvement actions "
                "to move performance toward the benchmark."
            )

        else:

            recommendation = (
                f"Maintain current {kpi.lower()} "
                "performance and continue periodic "
                "monitoring."
            )

        recommendations.append({
            "KPI": kpi,
            "Current_Value": row["Value"],
            "Benchmark": row["Benchmark"],
            "Performance_%": performance,
            "Status": status,
            "Strategic_Recommendation":
                recommendation
        })

    recommendations_df = pd.DataFrame(
        recommendations
    )

    return recommendations_df


def create_kpi_visualization(
    comparison_df
):
    """
    Create KPI benchmark comparison chart.
    """

    print(
        "\nCreating KPI performance visualization..."
    )

    os.makedirs(
        "visualizations",
        exist_ok=True
    )

    plot_df = comparison_df.copy()

    plot_df = plot_df[
        plot_df["Performance_%"].notna()
    ]

    plt.figure(
        figsize=(12, 7)
    )

    bars = plt.bar(
        plot_df["KPI"],
        plot_df["Performance_%"]
    )

    plt.axhline(
        y=100,
        linestyle="--",
        linewidth=2,
        label="Benchmark = 100%"
    )

    plt.title(
        "Agribusiness KPI Performance vs Benchmark"
    )

    plt.xlabel(
        "KPI"
    )

    plt.ylabel(
        "Performance (% of Benchmark)"
    )

    plt.xticks(
        rotation=35,
        ha="right"
    )

    plt.legend()

    plt.grid(
        axis="y",
        alpha=0.3
    )

    plt.tight_layout()

    output_path = os.path.join(
        "visualizations",
        "kpi_performance_vs_benchmark.png"
    )

    plt.savefig(
        output_path,
        dpi=300
    )

    plt.close()

    print(
        f"KPI chart saved to: {output_path}"
    )


def run_performance_evaluation(df):
    """
    Run the complete Week 4 performance
    evaluation workflow.
    """

    print("\n" + "=" * 60)
    print(
        "       WEEK 4 PERFORMANCE EVALUATION"
    )
    print("=" * 60)

    # -------------------------------------------------
    # STEP 1: Calculate KPIs
    # -------------------------------------------------

    kpi_df = calculate_kpis(df)

    # -------------------------------------------------
    # STEP 2: Benchmark Comparison
    # -------------------------------------------------

    comparison_df = create_benchmark_comparison(
        kpi_df
    )

    # -------------------------------------------------
    # STEP 3: Strategic Recommendations
    # -------------------------------------------------

    recommendations_df = (
        create_strategic_recommendations(
            comparison_df
        )
    )

    # -------------------------------------------------
    # STEP 4: Save Results
    # -------------------------------------------------

    os.makedirs(
        "data",
        exist_ok=True
    )

    kpi_path = os.path.join(
        "data",
        "agribusiness_kpi_results.csv"
    )

    benchmark_path = os.path.join(
        "data",
        "kpi_benchmark_comparison.csv"
    )

    recommendation_path = os.path.join(
        "data",
        "strategic_recommendations.csv"
    )

    kpi_df.to_csv(
        kpi_path,
        index=False
    )

    comparison_df.to_csv(
        benchmark_path,
        index=False
    )

    recommendations_df.to_csv(
        recommendation_path,
        index=False
    )

    print(
        f"\nKPI results saved to: {kpi_path}"
    )

    print(
        f"Benchmark comparison saved to: "
        f"{benchmark_path}"
    )

    print(
        f"Strategic recommendations saved to: "
        f"{recommendation_path}"
    )

    # -------------------------------------------------
    # STEP 5: Visualization
    # -------------------------------------------------

    create_kpi_visualization(
        comparison_df
    )

    print("\nWeek 4 evaluation completed successfully.")

    return (
        kpi_df,
        comparison_df,
        recommendations_df
    )