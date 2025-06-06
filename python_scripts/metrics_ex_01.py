# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% [markdown]
# # 📝 Exercise M7.02
#
# We presented different classification metrics in the previous notebook.
# However, we did not use it with a cross-validation. This exercise aims at
# practicing and implementing cross-validation.
#
# Here we use the blood transfusion dataset.

# %%
import pandas as pd

blood_transfusion = pd.read_csv("../datasets/blood_transfusion.csv")
data = blood_transfusion.drop(columns="Class")
target = blood_transfusion["Class"]

# %% [markdown]
# ```{note}
# If you want a deeper overview regarding this dataset, you can refer to the
# Appendix - Datasets description section at the end of this MOOC.
# ```

# %% [markdown]
# First, create a decision tree classifier.

# %%
# Write your code here.

# %% [markdown]
# Create a `StratifiedKFold` cross-validation object. Then use it inside the
# `cross_val_score` function to evaluate the decision tree. We first use
# the accuracy as a score function. Explicitly use the `scoring` parameter of
# `cross_val_score` to compute the accuracy (even if this is the default score).
# Check its documentation to learn how to do that.

# %%
# Write your code here.

# %% [markdown]
# Repeat the experiment by computing the `balanced_accuracy`.

# %%
# Write your code here.

# %% [markdown]
# We now add a bit of complexity. We would like to compute the precision of
# our model. However, during the course we saw that we need to mention the
# positive label which in our case we consider to be the class `donated`.
#
# We can show that computing the precision without providing the positive label
# is not supported by scikit-learn because it is indeed ambiguous.

# %%
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier()
try:
    scores = cross_val_score(
        tree, data, target, cv=10, scoring="precision", error_score="raise"
    )
except ValueError as exc:
    print(exc)

# %% [markdown]
# ```{tip}
# We use a `try`/`except` block to catch possible `ValueError`s and print them
# if they occur. By setting `error_score="raise"`, we ensure that the exception
# is raised immediately when an error is encountered. Without this setting, the
# code would show a warning for each cross-validation split before raising the
# exception. You can try using the default `error_score` to better understand
# what this means.
# ```
# We get an exception because the default scorer has its positive label set to
# one (`pos_label=1`), which is not our case (our positive label is "donated").
# In this case, we need to create a scorer using the scoring function and the
# helper function `make_scorer`.
#
# So, import `sklearn.metrics.make_scorer` and
# `sklearn.metrics.precision_score`. Check their documentations for more
# information. Finally, create a scorer by calling `make_scorer` using the score
# function `precision_score` and pass the extra parameter `pos_label="donated"`.

# %%
# Write your code here.

# %% [markdown]
# Now, instead of providing the string `"precision"` to the `scoring` parameter
# in the `cross_val_score` call, pass the scorer that you created above.

# %%
# Write your code here.

# %% [markdown]
# `cross_val_score` can compute one score at a time, as specified by the scoring
# parameter. In contrast, cross_validate can compute multiple scores by passing
# a list of strings or scorers to the scoring parameter
#
# Import `sklearn.model_selection.cross_validate` and compute the accuracy and
# balanced accuracy through cross-validation. Plot the cross-validation score
# for both metrics using a box plot.

# %%
# Write your code here.
