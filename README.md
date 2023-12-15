# Atlas: A LLM Inquiry Principle Benchmark

This repository contains resources and research on formulating effective queries and prompts for large language models (LLMs). The primary contribution is the introduction of 26 guiding principles aimed at optimizing interactions with LLMs of various scales, such as LLaMA-1/2, GPT-3.5, and GPT-4.

## Overview

Our work aims to simplify the underlying concepts of formulating questions for different scales of large language models. By examining their abilities and enhancing user comprehension, we focus on optimizing the design of instructions and prompts. Extensive experiments conducted on models like LLaMA-1/2 and GPT-3.5/4 have verified the effectiveness of the proposed principles. 

## Data Release

Our dataset, comprising 0.5k data points, supports the study of LLM prompting principles. The data is curated to facilitate understanding and application of the 26 principles. 
Our project includes two types of datasets, catering to different needs and research focuses:

1. **General Dataset (`general_dataset.json`)**: This comprehensive dataset combines all the examples from each of the 26 principles into a single file, offering a holistic view of our research and its diverse applications.

   - File: [`general_dataset.json`](./general_dataset.json)
   - Structure:
     - Each entry contains an `instruction` field describing the task.
     - The `output` field provides the model-generated response to the instruction.

   Example:
   ```json
   {
       "instruction": "Provide an instruction example",
       "output": "Model-generated response corresponding to the instruction"
   }
2. **Individual Principle Datasets (`Principle#.json`)**: We offer separate datasets for each of the 26 principles for a more focused study. These files allow researchers to explore and analyze data of specific principles in isolation.

- Files: `Principle1.json`, `Principle2.json`, ..., `Principle26.json`
Each file follows the same structure as the general dataset but contains examples only related to the respective principle.
Example in Principle1.json:


