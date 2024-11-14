import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

def dataframe_to_jpg(df, jpg_path="output.jpg", dpi=150):
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(len(df.columns) * 1.5, len(df) * 0.5))
    ax.axis('tight')
    ax.axis('off')
    
    # Create the table
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    
    # Autofit column widths
    for i, col in enumerate(df.columns):
        max_width = max(len(str(value)) for value in [col] + df[col].astype(str).tolist())
        table.auto_set_column_width([i])
    
    # Render the plot to a temporary PNG and convert it to JPG
    fig.savefig("tempxxxxyyyy121.png", format="png", dpi=dpi, bbox_inches="tight")
    plt.close(fig)  # Close the figure to free memory
    
    # Convert PNG to JPG using Pillow
    with Image.open("tempxxxxyyyy121.png") as img:
        rgb_img = img.convert("RGB")
        rgb_img.save(jpg_path, "JPEG")
    if os.path.exists("tempxxxxyyyy121.png"):
        os.remove("tempxxxxyyyy121.png")
    print(f"JPG saved as {jpg_path}")


