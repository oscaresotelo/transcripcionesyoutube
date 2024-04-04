from huggingface_hub import InferenceClient

# endpoint_url = "https://your-endpoint-url-here"

prompt = "texto de ejemplo"
prompt_template=f'''[INST] {prompt} [/INST]
'''

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")
response = client.text_generation(prompt,
                                  max_new_tokens=600,
                                  do_sample=True,
                                  temperature=0.7,
                                  top_p=0.95,
                                  top_k=40,
                                  repetition_penalty=1.1)

print(f"Model output: ", response)