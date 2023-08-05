import numpy as np


def my_normal(x, mu, cov_det, cov_inv):
    """
    Calculate the PDF probability of a multivariate normal distribution
    Covariance matrix must be positive definite, s.t. cov_det cannot be negative!
    :param x: data point
    :param mu: mean of cluster
    :param cov_det: pre-calculated determinant of covariance of cluster (for speed reasons during traversal)
    :param cov_inv: pre-calculated inverse of covariance of cluster (for speed reasons during traversal)
    """
    a = np.sqrt((2 * np.pi) ** x.shape[-1] * cov_det)
    b = -1 / 2 * np.dot(np.dot((x - mu), cov_inv), (x - mu).T)
    return 1 / a * np.exp(b)


def entropy(labels):
    """
    Calculate the Shannon entropy for a set of labels.
    :param labels: an array of labels
    :return: entropy
    """
    value, counts = np.unique(labels, return_counts=True)
    norm_counts = counts / counts.sum()
    return -(norm_counts * np.log(norm_counts) / np.log(np.e)).sum()


def entropy_gaussian(dataset):
    """
    Differential entropy of a d-variate Gaussian density
    :param dataset: dataset in R^(N*D)
    :return: entropy
    """
    # check if there are more dimensions
    if dataset.shape[-1] > dataset.shape[0]:
        raise ValueError('More dimensions than data points, shape dataset:' + str(dataset.shape))

    k = np.linalg.det(np.cov(dataset.T))
    d = dataset.shape[-1]
    ent = np.multiply(np.power((2 * np.pi * np.e), d), k)
    if ent <= 0:
        return 0
    ent = np.log(ent) / 2
    if np.isnan(ent):
        ent = np.infty
    return ent


def print_rule(node):
    """
    Helper function to print the split decision of a given node
    """
    rule_string = str(node.split_dimension) + "$<$" + str(np.round(node.split_value, 1))
    return rule_string


def print_density_tree_latex(node, tree_string):
    """print decision tree in a LaTeX syntax for visualizing the decision tree
    To be called as:
    tree_string = ""
    tree_string = printstuff(root,tree_string)
    """
    tree_string += "["

    tree_string += print_rule(node)
    print_rule(node)

    # check if node is leaf node
    if node.left is None:
        tree_string += "[ent:%.2f]" % node.left_entropy
    # check if node is leaf node
    if node.right is None:
        tree_string += "[ent:%.2f]" % node.right_entropy

    # iterate over node's children
    if node.left is not None:
        tree_string = print_density_tree_latex(node.left, tree_string)

    if node.right is not None:
        tree_string = print_density_tree_latex(node.right, tree_string)
    tree_string += "]"

    return tree_string


def print_decision_tree_latex(node, tree_string):
    """print decision tree in a LaTeX syntax for visualizing the decision tree
    To be called as:
    tree_string = print_decision_tree_latex(root, "")
    """
    tree_string += "["

    # check if node is split node
    if len(node.labels) > 1:
        tree_string += print_rule(node)
        print_rule(node)
    # check if node is leaf node
    if len(node.left_labels) == 1:
        tree_string += "[" + str(int(node.left_labels)) + "]"
    # checkif node is leaf node
    if len(node.right_labels) == 1:
        tree_string += "[" + str(int(node.right_labels)) + "]"

    # iterate over node's children
    if len(node.left_labels) > 1:
        tree_string = print_decision_tree_latex(node.left, tree_string)

    if len(node.right_labels) > 1:
        tree_string = print_decision_tree_latex(node.right, tree_string)
    tree_string += "]"

    return tree_string


def get_best_split(dataset, labelled=False, n_max_dim=0, n_grid=50, min_n_pts=2):
    """
    for a given dimension, get best split based on information gain for labelled and unlabelled data.
    :param dataset: dataset for which to find the best split
    :param labelled: indicator whether dataset contains labels or not
    :param n_max_dim: maximum number of dimensions within which to search for best split
    :param n_grid: grid resolution for parameter search in each dimension
    :param min_n_pts: minimum number of points at either side of split
    :return dim_max: best split dimension
    :return val_dim_max: value at best split dimensions
    :return ig_dims: information gains for all split values in all possible split dimensions
    :return split_dims: split values corresponding to ig_dims

    """
    # get information gains on dimensions
    ig_dims, split_dims = [], []
    ig_dims_len = []

    if labelled:
        entropy_f = entropy
        dimensions = np.arange(dataset.shape[-1] - 1)

    else:
        entropy_f = entropy_gaussian
        dimensions = np.arange(dataset.shape[-1])

    # subsample dimensions
    if n_max_dim > 0:
        dimensions = np.random.choice(dimensions, n_max_dim, replace=False)

    for dim in dimensions:  # loop all dimensions
        ig_dim, split_vals = get_ig_dim(dataset, dim, entropy_f=entropy_f, n_grid=n_grid, min_n_pts=min_n_pts)
        ig_dims_len = np.append(ig_dims_len, len(ig_dim))
        ig_dims = np.append(ig_dims, ig_dim)
        split_dims = np.append(split_dims, split_vals)

    # get all maximum ig indexes and take a random one if there are several
    max_ind = np.where(ig_dims == np.max(ig_dims))[0]
    max_ind = [max_ind] if not len(np.shape(max_ind)) else max_ind  # numpy compatibility
    max_ind = max_ind[0]  # take first value, lowest dimension

    # split dimension of maximum gain
    idx_dim_max = np.sum((max_ind >= np.cumsum(ig_dims_len)) * 1)

    return dimensions[idx_dim_max], split_dims[max_ind], np.max(ig_dims)


def get_ig_dim(dataset, dim_cut, entropy_f=entropy_gaussian, n_grid=50, min_n_pts=2):
    """
    Get information gain for one dimension, works for labelled and unlabelled data (according to entropy function)
    :param dataset: dataset without labels (X)
    :param dim_cut: dimension for which all cut values are to be calculated
    :param entropy_f: entropy function to be used (unlabelled: entropy_gaussian, unlabelled: other)
    :param n_grid: resolution at which to search for optimal split value
    :param min_n_pts: minimum number of points at either side of split
    :return ig_dim, split_vals
    """
    ig_dim, split_vals = [], []

    # min split has to > dim-smallest element of array (to have at least dims points to either side) at minimum.
    # if min_subset is defined, split has to have at least min_subset points on either side
    if entropy_f == entropy_gaussian:  # labelled case
        dataset_dim_min = np.partition(dataset[:, dim_cut], min_n_pts)[min_n_pts]
        dataset_dim_max = np.partition(dataset[:, dim_cut], -min_n_pts)[-min_n_pts]

    else:
        dataset_dim_min = np.min(dataset[:, dim_cut])
        dataset_dim_max = np.max(dataset[:, dim_cut])

        # ensure that at least for one split value, we have n_points >= n_dims on both sides
    iter_set = np.random.uniform(dataset_dim_min, dataset_dim_max, n_grid)

    for split_val in iter_set:
        # split values
        left = dataset[dataset[:, dim_cut] < split_val]
        right = dataset[dataset[:, dim_cut] >= split_val]

        # check that there are more values on each side than dimensions in the dataset
        if (len(left) >= min_n_pts) and (len(right) >= min_n_pts) or (
                (entropy_f != entropy_gaussian) and len(right) and len(left)):
            # entropy
            entropy_l = entropy_f(left)
            entropy_r = entropy_f(right)
            entropy_tot = entropy_f(dataset)

            # information gain
            ig = entropy_tot - (entropy_l * len(left) / len(dataset) + entropy_r * len(right) / len(dataset))

            # append split value and information gain
            ig_dim = np.append(ig_dim, ig)
            split_vals = np.append(split_vals, split_val)

    return ig_dim, split_vals


def get_balanced_subset_indices(gt, classes, pts_per_class=100):
    """
    Get indices of balanced subset of data where every class has pts_per_class points
    helper function of t-SNE plot in density_forest/plots.py
    :param gt: ground truth corresponding to dataset to be indexed
    :param classes: array of possible classes in gt.
    :param pts_per_class: points per class
    :return: dataset_subset_indices
    """
    dataset_subset_indices = []

    for class_label in classes:
        ds_subset_ind = np.where(gt[gt < np.infty] == class_label)[0]
        dataset_subset_indices.append(np.random.choice(ds_subset_ind, size=pts_per_class, replace=False))

    return np.asarray(dataset_subset_indices)


def get_values_preorder(node, split_dims, split_vals):
    """
    Get cut values and dimensions of a density tree by preorder traversal
    :param node: root node
    :param split_vals: array of split values, call with []
    :param split_dims: array of split dimensions, call with []
    :return: split_vals, split_dims
    """
    split_dims.append(node.split_dimension)
    split_vals.append(node.split_value)
    if node.left is not None:
        get_values_preorder(node.left, split_dims, split_vals)
    if node.right is not None:
        get_values_preorder(node.right, split_dims, split_vals)
    return split_vals, split_dims


def draw_subsamples(dataset, subsample_pct=.8, replace=False, return_indices=False):
    """draw random subsamples with or without replacement from a dataset
    :param dataset: the dataset from which to chose subsamples from
    :param subsample_pct: the size of the subsample dataset to create in percentage of the original dataset
    :param replace: subsampling with or without replacement
    :param return_indices: optional parameter to return also indices of subset
    :return dataset or dataset, indices if return_indices is True
    """
    subsample_size = int(np.round(len(dataset) * subsample_pct))  # subsample size
    dataset_indices = np.arange(len(dataset))

    #  draw random samples with replacement
    dataset_subset_indices = np.random.choice(dataset_indices, size=subsample_size, replace=replace)
    dataset_subset = dataset[dataset_subset_indices, :]
    if return_indices:
        return dataset_subset, dataset_subset_indices
    return dataset_subset
