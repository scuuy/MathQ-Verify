import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import matplotlib.cm as cm

# --- Global Configuration ---
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# --- Load and Process Data ---
def generate_distribution_heatmap(file_path, save_path):
    """Generate a heatmap showing distribution of math problems by category and difficulty"""
    # Load data
    data = pd.read_json(file_path)
    data['difficulty_rating'] = pd.to_numeric(data['difficulty_rating'], errors='coerce')

    # Define primary categories
    primary_categories = [
        "1. Foundations and Logic",
        "2. Algebra and Number Theory",
        "3. Analysis and Differential Equations",
        "4. Geometry and Topology",
        "5. Probability, Statistics, and Discrete Mathematics",
        "6. Applied and Computational Mathematics",
        "7. Arithmetic"
    ]

    # Icons & Colors
    icons = ['o', 's', '^', 'v', 'D', 'p', 'h']
    cmap = cm.get_cmap('Set1')
    category_colors = [cmap(i/len(primary_categories)) for i in range(len(primary_categories))]

    # Standardize primary_category field
    data['primary_category'] = data['primary_category'].apply(
        lambda x: next((cat for cat in primary_categories if cat.startswith(x.split('.')[0])), x)
    )

    # Bin and pivot - set frequency to 1
    bins = pd.interval_range(0, data['difficulty_rating'].max()+1, freq=1)
    data['difficulty_interval'] = pd.cut(data['difficulty_rating'], bins=bins)
    heatmap_data = (
        data.groupby(['primary_category','difficulty_interval'], observed=False)
            .size()
            .unstack(fill_value=0)
            .reindex(index=primary_categories, fill_value=0)
            .T
    )

    # --- Create Plot ---
    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(
        heatmap_data, annot=True, fmt='g',
        cmap='YlGnBu', linewidths=0.5, ax=ax
    )
    ax.invert_yaxis()

    # Y-axis ticks - set step to 1
    yt = np.arange(0, data['difficulty_rating'].max()+1, 1)
    ax.set_yticks(np.arange(len(yt)))
    ax.set_yticklabels(yt)

    # Hide default X-axis ticks
    ax.set_xlim(0, len(primary_categories))
    ax.set_xticks([])
    ax.tick_params(axis='x', which='both', length=0)

    # Increase bottom margin for labels and icons
    plt.subplots_adjust(bottom=0.28)

    # Draw markers outside axis: move up to -0.03, size to 120
    for i, (icon, color) in enumerate(zip(icons, category_colors)):
        ax.scatter(
            i+0.5,
            -0.03,              # Position at 3% below axis
            marker=icon,
            color=color,
            s=120,              # Size 120
            transform=ax.get_xaxis_transform(),
            clip_on=False,
            zorder=3
        )

    # Manually set xlabel position: below icons
    ax.set_xlabel('Primary Category Labels')
    ax.xaxis.set_label_coords(0.5, -0.12)  # x centered, y at 12% below
    ax.set_ylabel('Difficulty Levels')
    plt.title('Distribution Heatmap of Different Categories and Difficulty Levels')

    # Legend
    handles = [
        Line2D([0],[0], marker=ic, color='w', label=cat,
               markerfacecolor=col, markersize=10)
        for ic,cat,col in zip(icons, primary_categories, category_colors)
    ]
    plt.legend(
        handles=handles,
        loc='upper center',
        bbox_to_anchor=(0.5, -0.18),
        ncol=1, frameon=False
    )

    # Save & Display
    plt.savefig(save_path, bbox_inches='tight')
    print(f'Heatmap saved to {save_path}')
    plt.show()


if __name__ == "__main__":
    # Example usage
    input_file = "data/categorized_questions_with_ratings.json"
    output_file = "results/category_difficulty_heatmap.png"
    generate_distribution_heatmap(input_file, output_file)