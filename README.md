# InfTDA: A Top Down Approach to differentially private hierarchical queries
InfTDA is a simple and efficient algorithm for releasinga dataset under differential privacy with 
hierarchical indexing. It builds upon the Top-Down Algorithm (TDA), originally developed by the US Census Bureau for the 2020 
Census data release under differential privacy. 
The key distinction of InfTDA lies in its optimization step, 
where it employs Chebyshev minimization. 
This approach results in a simpler and more efficient algorithm 
for handling integer queries while providing strong theoretical guarantees.

From the paper:
> Differentially Private Release of Hierarchical Origin/Destination Data with a TopDown Approach
Fabrizio Boninsegna, Francesco Silvestri. Proc. 25th Privacy Enhancing Technologies Symposium (PETS), 2025.



This library is for general application to **pandas Series with MultiIndex**, better described in
> InfTDA: a Simple TopDown Mechanism for Hierarchical Differentially Private Counting Queries
Fabrizio Boninsegna Workshop on Theory and Practice of Differential Privacy (TPDP) 2025.
## Installation
To install the package, you can use the following command:
```bash
pip install inf-tda
```
The algorithm is implemented for pandas Series with MultiIndex, so the package includes the pandas library as a dependency.

## Usage
It requires a pandas Series with a MultiIndex as input, the privacy parameters epsilon and delta, and the sensitivity of the query. The output is a pandas Series with the same index as the input.
It applies discrete Gaussian mechanism to the input, so it requires that the input contains all the possible tuples in the index. If the input does not contain all the tuples, 
you can use the `reindex` method from pandas to add the missing tuples with value 0.
```python
from InfTDA import inf_tda
import pandas as pd

# Define the dataset
index = [("Male", ">= 18"), ("Male", "< 18"), ("Female", ">= 18"), ("Female", "< 18")]
values = [100, 200, 300, 400]
data = pd.Series(values, index=pd.MultiIndex.from_tuples(index))

# Define the privacy parameters
epsilon = 1.
delta = 1e-6
budget = (epsilon, delta)
# Sensitivity of the query (in this case each user contributes to 1 tuple)
contribution = 1  # how many tuples each user contributes to
privacy_type = "bounded"  # or "unbounded"
distinct_tuples = True  # or False if each user can contribute to multiple non-distinct tuples

# Run the algorithm
result: pd.Series = inf_tda(data=data,
                            budget=budget,
                            contribution=contribution,
                            privacy_type=privacy_type,
                            distinct_tuples=distinct_tuples)
```
The result is a pandas Series with the same index as the input data, but with the values perturbed to ensure differential privacy.
```
print("Result on n")
print("True: ", data.sum())
print("DP: ", result.sum())
print("\n Result on first level")
print("True: ", data.groupby(level=0).sum())
print("DP: ", result.groupby(level=0).sum())
print("\n Result on second level")
print("True: ", data.groupby(level=[0, 1]).sum())
print("DP: ", result.groupby(level=[0, 1]).sum())

Result on n
True:  1000
DP:  1000

 Result on first level
True:  Female    700
Male      300
dtype: int64
DP:  Female    700
Male      300
dtype: int64

 Result on second level
True:  Female  < 18     400
        >= 18    300
Male    < 18     200
        >= 18    100
dtype: int64
DP:  Female  < 18     393
        >= 18    307
Male    < 18     198
        >= 18    102
dtype: int64
```

### How to set the sensitivity
The sensitivity is automatically determined based on the parameters `contribution` (which is how many tuples each user contributes to), `privacy_type` (which can be "bounded" or "unbounded",
default is "bounded") and `distinct_tuples` (a boolean parameter, defaulting to True, that specifies whether a user can only contribute to distinct tuples).


The sensitivity is the maximum $\ell_2$ distance for counting queries between neighboring dataset. It is computed
according to the following table:

| Sensitivity             | Bounded Privacy | Unbounded Privacy |
|-------------------------|-----------------|-------------------|
| For $m$ distinct tuples | $\sqrt{2 m}$    | $\sqrt{m}$        |
| For $m$ tuples          | $\sqrt{2} m$    | $m$               |

- **Bounded Privacy**: is considered for neighboring datasets that differ in the substitution of one user. So the total number of user remains constant.
- **Unbounded Privacy**: is considered for neighboring datasets that differ in the addition or removal of one user. So the total number of user can change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation
If you use this code in your research, please cite the following paper:
```
@article{boninsegna2024differential,
  title={Differential Privacy Releasing of Hierarchical Origin/Destination Data with a TopDown Approach},
  author={Boninsegna, Fabrizio and Silvestri, Francesco},
  journal={arXiv preprint arXiv:2412.09256},
  year={2024}
}
```