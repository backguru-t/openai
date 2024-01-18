import json
from collections import defaultdict
import tiktoken
import logging
import sys
import os

# User defined levels
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0
logging.basicConfig(level=logging.DEBUG, \
                    format='[%(asctime)s][%(levelname)s] %(message)s',\
                    datefmt='%Y-%m-%d %H:%M:%S', \
                    stream=sys.stdout)

# new_dir = "twolinecode-finetuning"
# os.chdir(new_dir)

# 현재 작업 디렉토리 출력
logging.debug("current working dir: %s", os.getcwd())

# 파일 경로 지정
dataset_path = "examples/data/toy_chat_fine_tuning.jsonl"

# 파일이 존재하는지 확인
if os.path.exists(dataset_path):
    logging.info("File exists.")
else:
    logging.error(f"File '{dataset_path}' does not exist.")
    sys.exit("Exiting the program.")
    

training_dataset = []
# Traning data loading
with open(dataset_path, "r", encoding="utf-8") as f:
    training_dataset = [json.loads(line) for line in f]

dataset_size = len(training_dataset)
logging.info(f"The dataset includes {dataset_size} training examples in json format")
logging.info("For example see the first message:")
for message in training_dataset[0]["messages"]:
    logging.info(message)

# Dataset format validation
# We can perform a variety of error checks to validate that each conversation 
# in the dataset adheres to the format expected by the fine-tuning API. 
# Errors are categorized based on their nature for easier debugging.

# Data Type Check: Checks whether each entry in the dataset is a dictionary (dict). Error type: data_type.
# Presence of Message List: Checks if a messages list is present in each entry. Error type: missing_messages_list.
# Message Keys Check: Validates that each message in the messages list contains the keys role and content. Error type: message_missing_key.
# Unrecognized Keys in Messages: Logs if a message has keys other than role, content, and name. Error type: message_unrecognized_key.
# Role Validation: Ensures the role is one of "system", "user", or "assistant". Error type: unrecognized_role.
# Content Validation: Verifies that content has textual data and is a string. Error type: missing_content.
# Assistant Message Presence: Checks that each conversation has at least one message from the assistant. Error type: example_missing_assistant_message.

format_errors = defaultdict(int)
role_missing_warns = defaultdict(int)

role_system_missing = 0
role_user_missing = 0

for index, element in enumerate(training_dataset):
    logging.info(f"Index: {index}, Value: {element}")
    
    if not isinstance(element, dict):
        format_errors['data_type_error'] += 1
        continue
    
    # element is dictionay so "messages" key shoud be there.
    messages = element.get("messages", None)
    if not messages:
        format_errors['missing_message_list'] += 1
        continue
    
    # validating message
    for message in messages:
        logging.debug(message)
        # "role" and "content" must exsit.
        if "role" not in message or "content" not in message:
            format_errors["message_missing_key_error"] += 1
        
        # other than "role", "content", "name", "function_call" must not be there.
        if any(k not in ("role", "content", "name", "function_call") for k in message):
            format_errors["message_unrecognized_key_error"] += 1
        
        #  the "role" key must be "system", "user", "assistant", "function", the others
        #  not be permitted.
        if message.get("role", None) not in ("system", "user", "assistant", "function"):
            format_errors["unrecognized_role_error"] += 1
        
        # the content should be str type.
        content = message.get("content", None)
        function_call = message.get("function_call", None)
        if (not content and not function_call) or not isinstance(content, str):
            format_errors["missing_content_error"] += 1
                
    # check that each conversation has at least one message from the assistant.
    if not any(message.get("role", None) == "assistant" for message in messages):
        format_errors["example_missing_assistant_message"] += 1

notice = """Errors are categorized based on their nature for easier debugging.
Data Type Check: Checks whether each entry in the dataset is a dictionary (dict). Error type: data_type.
Presence of Message List: Checks if a messages list is present in each entry. Error type: missing_messages_list.
Message Keys Check: Validates that each message in the messages list contains the keys role and content. Error type: message_missing_key.
Unrecognized Keys in Messages: Logs if a message has keys other than role, content, and name. Error type: message_unrecognized_key.
Role Validation: Ensures the role is one of "system", "user", or "assistant". Error type: unrecognized_role.
Content Validation: Verifies that content has textual data and is a string. Error type: missing_content.
Assistant Message Presence: Checks that each conversation has at least one message from the assistant. Error type: example_missing_assistant_message.
"""
if format_errors:
    logging.error(f"Found errors: {notice}")
    for k, v in format_errors.items():
        logging.error(f"[Errors] {k}: {v}")
else:
    logging.info("No errors found")

for messages in training_dataset:
    messages = messages["messages"]
    if not any(message["role"] == "system" for message in messages):
        role_missing_warns['role_system_missing'] += 1
    if not any(message["role"] == "user" for message in messages):
        role_missing_warns['role_user_missing'] += 1

notice = """Missing system/User messages is critical for defining the assistans's
 behavior and initiating the conversation. So, check the training data again."""
oneline_notice = notice.replace("\n", "")

if role_missing_warns:
    logging.warning(f"Found warnings: {oneline_notice}")
    for k, v in role_missing_warns.items():
        logging.warning(f"[Warnings] {k}: {v}")
else:
    logging.info("No warnings found")
