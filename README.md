<<<<<<< HEAD
---
license: apache-2.0
---
# Love Letter Generation Using GPT-J
The project aims to create an app that allow people to generate love letters using GPT-J, an open-source transformer model. 

## Deployed Application
<a href="https://alihussainia-love-letter-generator-streamlit-app-yvxpjy.streamlit.app/">AI based Love Letter Generator Application</a>

## Tools Used:
- GPT-J, using <a href="https://beta.forefront.ai/solutions">Forefront.ai</a>
- <a href="https://streamlit.io/">Streamlit</a>

## Sample Input 
```text
Thank you for coming into my life and helping me to transform it into its best version.
```
## Directory Structure
```dir
|-- .gitignore 
|-- data_prep_notebook.ipynb 
|-- requirements.txt 
|-- streamlit_app.py 
|-- datasets
    |-- README.md 
    |-- love_letter_dataset.json 
    |-- love_letter_dataset.jsonl
|-- README.md 
```
## DataSet Sources
<a href="https://relishbay.com">https://relishbay.com</a>

<a href="https://happilylover.com">https://happilylover.com</a>

## Principal Author:
- Muhammad Ali
  - <a href="https://www.linkedin.com/in/alihussainia/">Linkedin</a>
  - <a href="https://github.com/alihussainia">Github</a>
  - <a href="https://huggingface.co/alihussainia">Hugging Face</a>
=======
# Love Letter Generator Using HuggingFace

In this project, we are going to use an open-source 6 billion parameters model, GPT-J hosted on HuggingFace. Follow the steps below to setup and utilize the project resources.

### Step No. 1: Download and Save the GPT-J Model

Run the below cell into `ipython` shell. This will download and save the 16fp GPT-J model locally which will help us easily load the model for our API.

```python
from transformers import GPTJForCausalLM
import torch

# download the fp 16 model
model = GPTJForCausalLM.from_pretrained(
    "EleutherAI/gpt-j-6B", revision="float16", torch_dtype=torch.float16, low_cpu_mem_usage=True
)

# save model with torch.save
torch.save(model, "gptj_fp16_model.pt")
```
>>>>>>> bfb3f62e2b11c2d267d26c7e3addf3b85277ea00
