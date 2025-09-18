from transformers import AutoModel, AutoTokenizer

def load_model(model_name: str, task: str = "text-generation"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return model, tokenizer
