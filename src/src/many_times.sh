source /home/shangbin/miniconda3/bin/activate
conda activate tin
# GPU 10
nohup CUDA_VISIBLE_DEVICES=10 python /home/shangbin/curiosity_math/src/many_times.py > /home/shangbin/curiosity_math/many_times_results/gpu_10.log 2>&1 &

# GPU 11
nohup CUDA_VISIBLE_DEVICES=11 python /home/shangbin/curiosity_math/src/many_times.py > /home/shangbin/curiosity_math/many_times_results/gpu_11.log 2>&1 &

# GPU 12
nohup CUDA_VISIBLE_DEVICES=12 python /home/shangbin/curiosity_math/src/many_times.py > /home/shangbin/curiosity_math/many_times_results/gpu_12.log 2>&1 &

# GPU 13
nohup CUDA_VISIBLE_DEVICES=13 python /home/shangbin/curiosity_math/src/many_times.py > /home/shangbin/curiosity_math/many_times_results/gpu_13.log 2>&1 &

# GPU 14
nohup CUDA_VISIBLE_DEVICES=14 python /home/shangbin/curiosity_math/src/many_times.py > /home/shangbin/curiosity_math/many_times_results/gpu_14.log 2>&1 &