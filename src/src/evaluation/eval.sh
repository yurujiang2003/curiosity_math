### Tutorial ###
### git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
### cd lm-evaluation-harness
### pip install -e .

### Script ###
OUTPUT_DIR="./evaluation_results"
mkdir -p "$OUTPUT_DIR"

MATH_TASKS=(
    "leaderboard_math_algebra_hard"
    "leaderboard_math_counting_and_prob_hard"
    "leaderboard_math_geometry_hard"
    "leaderboard_math_intermediate_algebra_hard"
    "leaderboard_math_num_theory_hard"
    "leaderboard_math_prealgebra_hard"
    "leaderboard_math_precalculus_hard"
)

for task in "${MATH_TASKS[@]}"
do
    echo "Evaluating task: $task"
    lm_eval --model hf \
        --model_args pretrained=\path\to\your\model,dtype="float" \
        --tasks "$task" \
        --device cuda:0 \
        --batch_size 8 \
        --output_path "${OUTPUT_DIR}/${task}_results.json"
done

### Task List ###
### leaderboard_math_algebra_hard
### leaderboard_math_counting_and_prob_hard
### leaderboard_math_geometry_hard
### leaderboard_math_intermediate_algebra_hard
### leaderboard_math_num_theory_hard
### leaderboard_math_prealgebra_hard
### leaderboard_math_precalculus_hard