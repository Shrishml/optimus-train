from trainer import load_training_dataset, load_tokenizer
print("loading tokenizer")
load_tokenizer()
print("loading training dataset")
load_training_dataset()

import json
gpu = 't4'

# Load JSON data from file
if gpu=='a100':
    with open(r'configs/training_config.json') as json_file:
        data = json.load(json_file)

if gpu=='t4':
    with open(r'configs/training_config_t4.json') as json_file:
        data = json.load(json_file)

# Extract variables from JSON data
num_gpus = data['num_gpus']
input_model = data['input_model']
deepspeed_config = data['deepspeed_config']
epochs = data['epochs']
local_output_dir = data['local_output_dir']
per_device_train_batch_size = data['per_device_train_batch_size']
per_device_eval_batch_size = data['per_device_eval_batch_size']
logging_steps = data['logging_steps']
save_steps = data['save_steps']
save_total_limit = data['save_total_limit']
eval_steps = data['eval_steps']
warmup_steps = data['warmup_steps']
test_size = data['test_size']
lr = data['lr']
bf16 = data['bf16']
fp16 = data['fp16']

# Run deepspeed command with variables
command = f"deepspeed --num_gpus {num_gpus} \
--module trainer \
--input-model \"{input_model}\" \
--deepspeed \"{deepspeed_config}\" \
--epochs {epochs} \
--local-output-dir \"{local_output_dir}\" \
--per-device-train-batch-size {per_device_train_batch_size} \
--per-device-eval-batch-size {per_device_eval_batch_size} \
--logging-steps {logging_steps} \
--save-steps {save_steps} \
--save-total-limit {save_total_limit} \
--eval-steps {eval_steps} \
--warmup-steps {warmup_steps} \
--test-size {test_size} \
--lr {lr} \
--bf16 {bf16} \
--fp16 {fp16}"

import os
os.system('ls')
os.system(command)
# os.system('ls')
# os.system('python3 blob.py')