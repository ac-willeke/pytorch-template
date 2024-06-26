from matplotlib import pyplot as plt


def scatter_plot(X, y, title, n_clusters):
    """Scatter plot that can plot up to 5 clusters"""

    colors = ["red", "blue", "green", "purple", "orange"]  # Add more colors if needed
    markers = ["o", "x", "s", "^", "v"]  # Add more markers if needed

    for i in range(n_clusters):
        plt.scatter(
            X[y == i, 0],
            X[y == i, 1],
            color=colors[i],
            marker=markers[i],
            label=f"class {i}",
        )

    plt.title(title)
    plt.xlabel("feature 1")
    plt.ylabel("feature 2")
    plt.legend(loc="upper left")
    plt.show()


def scatter_plot_3d(X, y, title, n_clusters):
    """3D scatter plot that can plot up to 5 clusters"""
    import matplotlib.pyplot as plt

    colors = ["red", "blue", "green", "purple", "orange"]  # Add more colors if needed
    markers = ["o", "x", "s", "^", "v"]  # Add more markers if needed

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111, projection="3d")

    for i in range(n_clusters):
        ax.scatter(
            X[y == i, 0],
            X[y == i, 1],
            X[y == i, 2],
            color=colors[i],
            marker=markers[i],
            label=f"class {i}",
        )

    ax.set_title(title)
    ax.set_xlabel("feature 1: Spatial")
    ax.set_ylabel("feature 2: Channels")
    ax.set_zlabel("feature 3: Time")
    ax.legend(loc="upper left")

    plt.show()
