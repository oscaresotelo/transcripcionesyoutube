from huggingface_hub import InferenceClient


headers = {"Authorization": "Bearer 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"} 
prompt = "cuando nacio peron?"
prompt_template=f'''[INST] {prompt} [/INST]
'''

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1", headers)
response = client.text_generation(prompt,
                                  max_new_tokens=600,
                                  do_sample=True,
                                  temperature=0.9,
                                  top_p=0.95,
                                  top_k=40,
                                  repetition_penalty=1.1)

print(f"Model output: ", response)

# import requests

# API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()
    
# output = query({
#     "inputs": "cuando nacio peron ",

# })
# print(output)