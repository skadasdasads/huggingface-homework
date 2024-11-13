from transformers import Columnm Integer, Boolean, Text  
from database import Base 

from transformers import Column Integer, Boolean, Text 

def load_translation(): 
    
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    return model, tokenizer