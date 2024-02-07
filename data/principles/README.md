## Overview

1. **Boosting**: This folder contains data on the improvement in response quality of various LLMs after applying specific principles.
2. **Correctness**: This folder contains data on the accuracy and relevance of the LLMs' outputs.

Each folder contains a set of files corresponding to 26 principles:
  - `w_principle_{i}`: Contains data points with the ith principle applied.
  - `wo_principle_{i}`: Contains data points without the ith principle applied.
    
    **Note**: For the `Correctness` folder, the `wo_principle_{i}` files are identical across all principles except principles 1 and 4. The baseline correctness data remains consistent, providing a uniform comparison point.
    
All files except for principles 3, 14, and 15 follow the same structure as below:

  ```json
  {
    "instruction": "If you were an expert economist, how would you answer: What are the key differences between a capitalist and a socialist economic system?",
    "gpt4_output1": "As an expert economist, I would describe the key differences between capitalist and socialist economic systems along several dimensions:...",
    ...
    "gpt3.5_output1": "As an expert economist, I would answer that the key differences between a capitalist and a socialist economic ...",
    "llama2-70b_output": "As an expert economist, I would explain that a capitalist economic system and a socialist economic system ...",
    ...
  }
  ```
For principles 3, 14, and 15, the structure is as follows:

  ```json
  {
    "Instruction": "Help me create engaging social media posts. Ask me questions to understand my target audience, platform, and content style.",
    "gpt4_conversations": [
        {
            "from": "human",
            "value": "Help me create engaging social media posts. Ask me questions to understand my target audience, platform, and content style."
        },
        {
            "from": "gpt4",
            "value": "Of course! I'd be happy to help you craft engaging social media posts..."
        },
        {
            "from": "human",
            "value": "1) female age 10  2) Instagram 3) education 4) no  5) likes"
        },
        ...
    ],
    "gpt3.5_conversations": [...
    ],
    ...
  }
  ```
