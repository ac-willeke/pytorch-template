def data_info(X, y):

    print(f"The data X:{X.shape} contains {X.shape[0]} samples and {X.shape[1]} features.")
    print(f"The data has size: {X.shape} = {X.size}")
    print(f"The labels y:{y.shape} contain a label for all {X.shape[0]} samples.") 

    # count number of labels and print labels
    n_classes = y.max() + 1
    print(f'Number of labels: {n_classes}')
    print(f'Class labels: {set(y)}')
    return 