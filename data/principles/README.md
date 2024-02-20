## Overview

1. **Boosting**: This folder contains data on the improvement in response quality of various LLMs after applying specific principles.
2. **Correctness**: This folder contains data on the accuracy and relevance of the LLMs' outputs.

Each folder contains a set of files corresponding to 26 principles:
  - `w_principle_{i}`: Contains data points with the ith principle applied.
  - `wo_principle_{i}`: Contains data points without the ith principle applied.
    
    **Note**: For the `Correctness` folder, the `wo_principle_{i}` files are identical across all principles except principles 1 and 4. The baseline correctness data remains consistent, providing a uniform comparison point.
    
All files follow the structure as follows:

  ```json
  {
    "id": "identity_0",
    "model": "gpt4",
    "conversations": [
      {
        "from": "human",
        "value": "Explain the process of photosynthesis."
      },
      {
        "from": "gpt",
        "value": "Photosynthesis is a biochemical process..."
      }
    ]
  },
  ```
