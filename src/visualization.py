import os

import matplotlib.pyplot as plt
import seaborn as sns


def create_visualizations(df):
    """
    Create all major agricultural
    data visualizations.
    """

    output_directory = "visualizations"

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    print("\nCreating visualizations...")

    # -------------------------------------------------
    # 1. Top 10 Crops by Production
    # -------------------------------------------------

    crop_production = (
        df.groupby("Crop")["Production"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 7))

    crop_production.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top 10 Crops by Total Production"
    )

    plt.xlabel(
        "Total Production"
    )

    plt.ylabel(
        "Crop"
    )

    plt.xscale("log")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_directory,
            "top_10_crops_production.png"
        ),
        dpi=300
    )

    plt.close()

    print(
        "Created: top_10_crops_production.png"
    )

    # -------------------------------------------------
    # 2. Yearly Production Trend
    # -------------------------------------------------

    yearly_production = (
        df.groupby("Crop_Year")["Production"]
        .sum()
        .sort_index()
    )

    # Remove years with zero production
    yearly_production = yearly_production[
        yearly_production > 0
    ]

    plt.figure(figsize=(12, 7))

    plt.plot(
        yearly_production.index,
        yearly_production.values,
        marker="o"
    )

    plt.title(
        "Yearly Agricultural Production Trend"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "Total Production"
    )

    plt.grid(
        True,
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_directory,
            "yearly_production_trend.png"
        ),
        dpi=300
    )

    plt.close()

    print(
        "Created: yearly_production_trend.png"
    )

    # -------------------------------------------------
    # 3. Top 10 States by Production
    # -------------------------------------------------

    state_production = (
        df.groupby("State_Name")["Production"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 7))

    state_production.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top 10 States by Agricultural Production"
    )

    plt.xlabel(
        "Total Production"
    )

    plt.ylabel(
        "State"
    )

    plt.xscale("log")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_directory,
            "top_states_production.png"
        ),
        dpi=300
    )

    plt.close()

    print(
        "Created: top_states_production.png"
    )

    # -------------------------------------------------
    # 4. Correlation Heatmap
    # -------------------------------------------------

    correlation_data = df[
        [
            "Crop_Year",
            "Area",
            "Production"
        ]
    ].corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation_data,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title(
        "Agricultural Data Correlation Heatmap"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_directory,
            "correlation_heatmap.png"
        ),
        dpi=300
    )

    plt.close()

    print(
        "Created: correlation_heatmap.png"
    )

    print(
        "\nAll visualizations created successfully."
    )