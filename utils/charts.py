import matplotlib.pyplot as plt


def plot_moisture(logs):
    if not logs:
        print("No data available to plot.")
        return

    # Extract all moisture values efficiently
    moisture_values = [log.soil.moisture for log in logs]

    # Initialize the figure for better sizing
    plt.figure(figsize=(10, 5))

    # Plot with markers ('o') to ensure every data point is visible
    plt.plot(moisture_values, marker='o', linestyle='-', color='tab:blue', label='Soil Moisture')

    # Formatting
    plt.title("Soil Moisture Trend Over Time", fontsize=14)
    plt.xlabel("Days", fontsize=12)
    plt.ylabel("Moisture Level (%)", fontsize=12)

    # Add a grid for easier reading of data points
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # Adjust layout to prevent clipping
    plt.tight_layout()
    plt.show()
