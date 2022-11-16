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
