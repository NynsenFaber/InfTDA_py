# InfTDA: A Top Down Approach to differentially private hierarchical queries
InfTDA is a simple and efficient algorithm for releasinga dataset under differential privacy with 
hierarchical indexings. It is based on the Top Down approach, developed by the US Census Bureau to release
2020 Census data under differential privacy. InfTDA differs from the aforementioned approach in the optimization
step, where it uses Chebyshev minimization leading to a more simple and efficient algorithm for integer queries, with
theoretical guarantees.

From the paper:
> Boninsegna, Fabrizio, and Francesco Silvestri. "Differential Privacy Releasing of Hierarchical Origin/Destination Data with a TopDown Approach." arXiv preprint arXiv:2412.09256 (2024).
## Installation
To install the package, you can use the following command:
```bash
pip install infTDA
```
The algorithm is implemented for pandas Series with MultiIndex, so the package includes the pandas library as a dependency.

## Usage
It requires a pandas Series with a MultiIndex as input, the privacy parameters epsilon and delta, and the sensitivity of the query. The output is a pandas Series with the same index as the input.
It applies discrete Gaussian mechanism to the input, so it requires that the input contains all the possible tuples in the index. If the input does not contain all the tuples, 
you can use the `reindex` method from pandas to add the missing tuples with value 0.
```python
from infTDA import inf_tda
import pandas as pd

# Define the dataset
index = [("A", "a"), ("A", "b"), ("B", "a"), ("B", "b")]
values = [1, 2, 3, 4]
data = pd.Series(values, index=pd.MultiIndex.from_tuples(index))

# Define the privacy parameters
epsilon = 1.
delta = 1e-6
budget = (epsilon, delta)
# Sensitivity of the query (how many tuples a user can add or remove from the dataset)
sensitivity = 1. 

# Run the algorithm
result: pd.Series = inf_tda(data, budget, sensitivity)
```
The result is a pandas Series with the same index as the input data, but with the values perturbed to ensure differential privacy.

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