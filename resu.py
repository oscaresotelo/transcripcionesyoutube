import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

def format_prompt(message, history):
    prompt = "<s>"
    for user_prompt, bot_response in history:
        prompt += f"[INST] {user_prompt} [/INST]"
        prompt += f" {bot_response}</s> "
    prompt += f"[INST] {message} [/INST]"
    return prompt

def generate(
    prompt, history, system_prompt, temperature=0.9, max_new_tokens=256, top_p=0.95, repetition_penalty=1.0,
):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(f"{system_prompt}, {prompt}", history)
    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text
        yield output
    return output

def main():
    system_prompt = st.text_input("System Prompt", "")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.9, step=0.05, format="%f")
    max_new_tokens = st.slider("Max new tokens", 0, 1048, 256, step=64)
    top_p = st.slider("Top-p (nucleus sampling)", 0.0, 1.0, 0.90, step=0.05, format="%f")
    repetition_penalty = st.slider("Repetition penalty", 1.0, 2.0, 1.2, step=0.05, format="%f")

    history = []
    if st.button("Generate"):
        output = list(generate(
            "", history, system_prompt, temperature, max_new_tokens, top_p, repetition_penalty
        ))
        st.write(output[-1])

if __name__ == "__main__":
    main()
