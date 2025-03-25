# plotting_module.py
import matplotlib.pyplot as plt

def plot_variations(gray_frame, blurred_images, gaussian_kernel_sizes,
                    clahe_clip2, clahe_clip4, clahe_clip8,
                    morph_images, morph_kernel_sizes):

    # Set up a grid: 3 rows each with 4 columns (original + 3 variants)
    ncols = 4
    fig, axs = plt.subplots(3, ncols, figsize=(20, 15))


    # Row 1: Gaussian Blur Variations
    axs[0, 0].imshow(gray_frame, cmap='gray')
    axs[0, 0].set_title("Original Grayscale")
    axs[0, 0].axis('off')
    for i, (img, k) in enumerate(zip(blurred_images, gaussian_kernel_sizes), start=1):
        axs[0, i].imshow(img, cmap='gray')
        axs[0, i].set_title(f"Gaussian Blur {k}")
        axs[0, i].axis('off')

    # Row 2: CLAHE Variants (no histogram equalization)
    titles_row2 = ["Original Grayscale", "CLAHE clip=2.0", "CLAHE clip=4.0", "CLAHE clip=8.0"]
    images_row2 = [gray_frame, clahe_clip2, clahe_clip4, clahe_clip8]
    for j, (img, title) in enumerate(zip(images_row2, titles_row2)):
        axs[1, j].imshow(img, cmap='gray')
        axs[1, j].set_title(title)
        axs[1, j].axis('off')


    # Row 3: Morphological Opening Variations
    axs[2, 0].imshow(gray_frame, cmap='gray')
    axs[2, 0].set_title("Original Grayscale")
    axs[2, 0].axis('off')

    for i, (img, k) in enumerate(zip(morph_images, morph_kernel_sizes), start=1):
        axs[2, i].imshow(img, cmap='gray')
        axs[2, i].set_title(f"Morph Open {k}x{k}")
        axs[2, i].axis('off')

    # Add group titles for each row.
    fig.text(0.5, 0.92, "Gaussian Blur Variations", ha="center", fontsize=16, fontweight='bold')
    fig.text(0.5, 0.63, "CLAHE Variants", ha="center", fontsize=16, fontweight='bold')
    fig.text(0.5, 0.33, "Morphological Opening Variations", ha="center", fontsize=16, fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Compute positions for horizontal separators.
    pos_row1 = axs[0, 0].get_position()
    pos_row2 = axs[1, 0].get_position()
    pos_row3 = axs[2, 0].get_position()

    line1_y = (pos_row1.y0 + pos_row2.y1) / 2 - 0.005
    line2_y = (pos_row2.y0 + pos_row3.y1) / 2 - 0.005

    fig.add_artist(plt.Line2D([0.05, 0.95], [line1_y, line1_y],
                                transform=fig.transFigure, color='black', linewidth=4))
    fig.add_artist(plt.Line2D([0.05, 0.95], [line2_y, line2_y],
                                transform=fig.transFigure, color='black', linewidth=4))

    plt.show()
