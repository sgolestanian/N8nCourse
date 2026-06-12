import gradio as gr
from openai import OpenAI


def summarize(text, api_key):
    if not text.strip():
        return "Please enter some text to summarize."
    if not api_key.strip():
        return "Please enter your API key."

    try:
        client = OpenAI(base_url="https://api.gapgpt.app/v1", api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes text concisely.",
                },
                {
                    "role": "user",
                    "content": f"Please summarize the following text:\n\n{text}",
                },
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


with gr.Blocks(title="Text Summarizer") as demo:
    gr.Markdown("# Text Summarizer")

    text_input = gr.Textbox(
        label="Text to Summarize",
        placeholder="Paste the text you want to summarize here...",
        lines=10,
    )
    api_key_input = gr.Textbox(
        label="API Key",
        placeholder="Enter your OpenAI API key...",
        type="password",
    )
    summarize_btn = gr.Button("Summarize", variant="primary")
    output = gr.Textbox(label="Summary", lines=6)

    summarize_btn.click(
        fn=summarize,
        inputs=[text_input, api_key_input],
        outputs=output,
    )


if __name__ == "__main__":
    demo.launch()
