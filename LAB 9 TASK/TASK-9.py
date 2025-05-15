from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

model.eval()

prompt = "PAkistan is a country in South Asia. It shares borders with India to"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

output = model.generate(
    input_ids,
    max_length=100,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:\n", generated_text)
