from transformers import pipeline
import os

summarizer = pipeline("summarization")

def summarize_text_file(input_file_path, output_file_path):
    with open(input_file_path, "r") as f:
        input_text = f.read()

    summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)

    with open(output_file_path, "w") as f:
        f.write(summary[0]['summary_text'])

    print("Generated Summary:")
    print(summary[0]['summary_text'])


