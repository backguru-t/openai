import json
import sys
import openai
import os
import pandas as pd
from pprint import pprint
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("API_KEY")
print(OPENAI_API_KEY)

openai.api_key = OPENAI_API_KEY

# 파일 경로 지정
dataset_path = "examples/data/cookbook_recipes_nlg_10k.csv"

# 파일이 존재하는지 확인
if os.path.exists(dataset_path):
    print(f"File, '{dataset_path}' exists.")
else:
    print(f"File '{dataset_path}' does not exist.")
    sys.exit("Exiting the program.")

# Getting the Panda's DataFrame
recipe_df = pd.read_csv(dataset_path)
print(recipe_df.head())

training_data = []

system_message = "You are a helpful recipe assistant. You are to extract the generic ingredients from each of the recipes provided."

def create_user_message(row):
    return f"""Title: {row['title']}\n\nIngredients: {row['ingredients']}\n\nGeneric ingredients: """

def prepare_example_conversation(row):
    messages = []
    messages.append({"role": "system", "content": system_message})

    user_message = create_user_message(row)
    messages.append({"role": "user", "content": user_message})

    messages.append({"role": "assistant", "content": row["NER"]})

    return {"messages": messages}

# A sample of dataset generated
# pprint(prepare_example_conversation(recipe_df.iloc[0]))

# generating 50 rows of the dataset for training
training_df = recipe_df.loc[0:50]
training_data = training_df.apply(prepare_example_conversation, axis=1).tolist()

# for example in training_data[:5]:
#     print(example)

# generating additional 50 rows of the dataset for verification
validation_df = recipe_df.loc[51:100]
validation_data = validation_df.apply(prepare_example_conversation, axis=1).tolist()

# We then need to save our data as .jsonl files, with each line being one training example conversation.
def write_jsonl(data_list: list, filename: str) -> None:
    with open(filename, "w") as out:
        for ddict in data_list:
            jout = json.dumps(ddict) + "\n"
            out.write(jout)

training_file_name = "examples/data/tmp_recipe_finetune_training.jsonl"
write_jsonl(training_data, training_file_name)

validation_file_name = "examples/data/tmp_recipe_finetune_validation.jsonl"
write_jsonl(validation_data, validation_file_name)

# upload files
training_file_name = "examples/data/training_data_twolinecode.jsonl"
with open(training_file_name, "rb") as training_fd:
    training_response = openai.files.create(
        file=training_fd, purpose="fine-tune"
    )

training_file_id = training_response.id

# with open(validation_file_name, "rb") as validation_fd:
#     validation_response = openai.files.create(
#         file=validation_fd, purpose="fine-tune"
#     )
# validation_file_id = validation_response.id

print("Training file ID:", training_file_id)
# print("Validation file ID:", validation_file_id)

# Fine tuning
response = openai.fine_tuning.jobs.create(
    training_file=training_file_id,
    # validation_file=validation_file_id,
    model="gpt-3.5-turbo",
    suffix="tlc-ft",
)

job_id = response.id

print("Job ID:", response.id)
print("Status:", response.status)

# Check job status
response = openai.fine_tuning.jobs.retrieve(job_id)

print("Job ID:", response.id)
print("Status:", response.status)
print("Trained Tokens:", response.trained_tokens)

# We can track the progress of the fine-tune with the events endpoint. You can rerun the cell below a few times until the fine-tune is ready.
response = openai.fine_tuning.jobs.list_events(job_id)

events = response.data
events.reverse()

for event in events:
    print(event.message)

# Now that it's done, we can get a fine-tuned model ID from the job:
response = openai.fine_tuning.jobs.retrieve(job_id)
fine_tuned_model_id = response.fine_tuned_model

if fine_tuned_model_id is None: 
    raise RuntimeError("Fine-tuned model ID not found. Your job has likely not been completed yet.")

print("Fine-tuned model ID:", fine_tuned_model_id)