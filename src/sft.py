from dataclasses import dataclass
from typing import List, Optional
from transformers import AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig
from datasets import load_dataset

#### accept config from yaml: 
#### accelerate launch --config_file=/path/to/config.yaml --num_processes 4 /path/to/sft.py

@dataclass
class TrainingConfig:
    """Configuration for training"""
    per_device_train_batch_size: int = 4
    gradient_accumulation_steps: int = 4
    num_train_epochs: int = 3
    learning_rate: float = 2e-4
    fp16: bool = True
    logging_steps: int = 10
    max_seq_length: int = 512
    optim: str = "paged_adamw_32bit"
    save_strategy: str = "steps"
    save_steps: int = 100
    logging_dir: str = "./logs"

@dataclass
class LoRAConfig:
    """Config for LoRA"""
    r: int = 64
    lora_alpha: int = 16
    target_modules: List[str] = None
    lora_dropout: float = 0.1
    bias: str = "none"
    task_type: str = "CAUSAL_LM"

    def __post_init__(self):
        if self.target_modules is None:
            self.target_modules = [
                "q_proj", "k_proj", "v_proj", "o_proj",
                "gate_proj", "up_proj", "down_proj"
            ]

@dataclass
class QuantizationConfig:
    """Config for quantization"""
    load_in_4bit: bool = True
    bnb_4bit_quant_type: str = "nf4"
    bnb_4bit_compute_dtype: str = "float16"
    bnb_4bit_use_double_quant: bool = True

class QwenTrainer:
    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-0.5B",
        output_dir: str = "Qwen/Qwen2.5-0.5B-qlora",
        dataset_name: str = "trl-lib/Capybara",
        training_config: Optional[TrainingConfig] = None,
        lora_config: Optional[LoRAConfig] = None,
        quant_config: Optional[QuantizationConfig] = None,
    ):
        self.model_name = model_name
        self.output_dir = output_dir
        self.dataset_name = dataset_name

        self.training_config = training_config or TrainingConfig()
        self.lora_config = lora_config or LoRAConfig()
        self.quant_config = quant_config or QuantizationConfig()

        self._init_configs()
        
    def _init_configs(self):
        """Initialize all configurations"""
        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=self.quant_config.load_in_4bit,
            bnb_4bit_quant_type=self.quant_config.bnb_4bit_quant_type,
            bnb_4bit_compute_dtype=self.quant_config.bnb_4bit_compute_dtype,
            bnb_4bit_use_double_quant=self.quant_config.bnb_4bit_use_double_quant,
        )

        self.lora_config = LoraConfig(
            r=self.lora_config.r,
            lora_alpha=self.lora_config.lora_alpha,
            target_modules=self.lora_config.target_modules,
            lora_dropout=self.lora_config.lora_dropout,
            bias=self.lora_config.bias,
            task_type=self.lora_config.task_type
        )

        self.training_args = SFTConfig(
            output_dir=self.output_dir,
            per_device_train_batch_size=self.training_config.per_device_train_batch_size,
            gradient_accumulation_steps=self.training_config.gradient_accumulation_steps,
            num_train_epochs=self.training_config.num_train_epochs,
            learning_rate=self.training_config.learning_rate,
            fp16=self.training_config.fp16,
            logging_steps=self.training_config.logging_steps,
            max_seq_length=self.training_config.max_seq_length,
            optim=self.training_config.optim,
            save_strategy=self.training_config.save_strategy,
            save_steps=self.training_config.save_steps,
            logging_dir=self.training_config.logging_dir,
        )

    def load_dataset(self, split: str = "train"):
        """Load dataset"""
        self.dataset = load_dataset(self.dataset_name, split=split)
        return self.dataset

    def setup_trainer(self):
        """Setup trainer"""
        self.trainer = SFTTrainer(
            model=self.model_name,
            train_dataset=self.dataset,
            peft_config=self.lora_config,
            model_init_kwargs={"quantization_config": self.bnb_config},
            args=self.training_args,
        )
        return self.trainer

    def train(self):
        """Start training"""
        self.trainer.train()
        
    def save_model(self):
        """Save model"""
        self.trainer.save_model(self.training_args.output_dir)

    def run_training(self):
        """Run full training process"""
        self.load_dataset()
        self.setup_trainer()
        self.train()
        self.save_model()

if __name__ == "__main__":
    
    training_config = TrainingConfig(
        per_device_train_batch_size=8,
        num_train_epochs=5,
        learning_rate=1e-4
    )
    
    lora_config = LoRAConfig(
        r=32,
        lora_alpha=8,
        target_modules=["q_proj", "v_proj"]
    )
    
    quant_config = QuantizationConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4"
    )
    
    trainer = QwenTrainer(
        model_name="Qwen/Qwen2.5-0.5B",
        output_dir="Qwen/Qwen2.5-0.5B-qlora",
        dataset_name="trl-lib/Capybara",
        training_config=training_config,
        lora_config=lora_config,
        quant_config=quant_config
    )
    
    trainer.run_training()