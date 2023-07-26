echo 'caching data'
ls
python3 cache_data.py
echo 'starting training'
deepspeed --num_gpus 4 \
  --module trainer \
  --input-model "EleutherAI/pythia-6.9b" \
  --deepspeed "configs/ds_t4_config.json" \
  --epochs 2 \
  --local-output-dir "checkpoints" \
  --per-device-train-batch-size 2 \
  --per-device-eval-batch-size 2 \
  --logging-steps 10 \
  --save-steps 100 \
  --save-total-limit 20 \
  --eval-steps 100 \
  --warmup-steps 20 \
  --test-size 200 \
  --lr 5e-6 \
  --bf16 False \
  --fp16 True
