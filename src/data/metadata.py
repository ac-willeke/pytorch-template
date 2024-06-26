def data_info(X, y):
    import logging

    logger = logging.getLogger(__name__)

    logger.info(
        f"The data X:{X.shape} contains {X.shape[0]} samples and {X.shape[1]} features."
    )
    logger.info(f"The data has size: {X.shape} = {X.size}")
    logger.info(f"The labels y:{y.shape} contain a label for all {X.shape[0]} samples.")

    # count number of labels
    n_classes = y.max() + 1
    logger.info(f"Number of labels: {n_classes}")
    logger.info(f"Class labels: {set(y)}")
    return


if __name__ == "__main__":
    # set up logging
    import logging

    import numpy as np

    from src.logger import setup_logging

    setup_logging()
    logger = logging.getLogger(__name__)

    # test data info
    X = np.random.rand(10, 5)
    y = np.random.randint(0, 2, 10)
    data_info(X, y)
