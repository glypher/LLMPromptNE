from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
from peft import PeftModel
import torch

PEFT_CHECKTPOINT = 'app/ppo_model_checkpoint'

ORIGINAL_MODEL_NAME = 'google/flan-t5-small'

class Model:
    def __init__(self):
        self._original_model = AutoModelForSeq2SeqLM.from_pretrained(ORIGINAL_MODEL_NAME, torch_dtype=torch.bfloat16, device_map="cpu")

        self._model = PeftModel.from_pretrained(self._original_model, PEFT_CHECKTPOINT,
                                                torch_dtype=torch.bfloat16, device_map="cpu", is_trainable=False)

        self._tokenizer = AutoTokenizer.from_pretrained(ORIGINAL_MODEL_NAME, device_map="cpu")

        self._generation_config = GenerationConfig(max_new_tokens=100, top_k=0.0, top_p=1.0, do_sample=True)

    @staticmethod
    def _make_safe_prompt(prompt):
        return f"""Create a safe prompt from the following prompt:

{prompt}

Prompt:"""

    def protect(self, prompt: str):
        try:
            inp = self._tokenizer(Model._make_safe_prompt(prompt), return_tensors="pt", padding=True).input_ids
            
            gen_ids = self._model.generate(input_ids=inp, generation_config=self._generation_config)
    
            return self._tokenizer.decode( torch.as_tensor(gen_ids).squeeze(), skip_special_tokens=True, clean_up_tokenization_spaces=True )
        except Exception as e:
            return "Error: " + str(e)
        
