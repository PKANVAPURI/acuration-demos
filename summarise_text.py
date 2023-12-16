import os
from transformers import BartForConditionalGeneration, BartTokenizer

def summarize_text(input_text):
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def summarize_text_files(input_folder):
    # Create a new output folder for summaries
    output_folder = os.path.join(input_folder, "summaries")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each text file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_summary.txt")

            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                input_text = input_file.read()

            summary = summarize_text(input_text)

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(summary)

            print(f"Summary saved successfully: {output_file_path}")


input_folder = r"C:\Users\pkanv\OneDrive\Desktop\omg\output_text"  
summarize_text_files(input_folder)
