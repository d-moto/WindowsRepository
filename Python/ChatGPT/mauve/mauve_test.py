from examples import load_gpt2_dataset
import mauve
import matplotlib.pyplot as plt

import torch

# Require import mauve
p_text = load_gpt2_dataset('data/amazon.valid.jsonl', num_examples=1)  # human
q_text = load_gpt2_dataset('data/amazon-xl-1542M.valid.jsonl', num_examples=1)  # machine

# call mauve.compute_mauve using raw text on GPU 0; each generation is truncated to 256 tokens
# out = mauve.compute_mauve(p_text=p_text, q_text=q_text, device_id=0, max_text_length=256, verbose=True)
# print(out.mauve)  # prints 0.9917

# Make sure matplotlib is installed in your environment
# Require import matplotlib.pyplot as plt
# plt.plot(out.divergence_curve[:, 1], out.divergence_curve[:, 0])
# plt.show(block=False)


def testfunc():
    """
    Parses arguments passed to this tool.

    Args: None

    Returns:
        argparse.Namespace: argument store
    """
    return None


print("")
print(p_text)
print("")
print(q_text)
print("")
print(len(p_text))
print("")
print(len(q_text))
print("")
print(type(p_text))
print("")
print(type(q_text))
print("")
help(testfunc)

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name())
print(torch.cuda.get_device_capability())
