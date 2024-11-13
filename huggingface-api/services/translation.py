from transformers import MBartForConditionalGenration, MBart50Tokenizer 


model = MBartForConditionalGeneration.from_pretranined("facebook/mbart-large-50-many-to-many-mmt")

tokenizer = MBart50Tokenzier.from_pretrained("facebook/mbart-large-50-many-to-many-mmt") 


tokenizer.src_lang = "ko_KR" 


def perform_translation(text : str, lang : str) -> str: 



    encoded_ko = tokenizer(text : str, lang : str) -> str: 

    encoded_ko = tokenizer(text, return_tensors="pt")

    generated)tokens = model.generate(
        **encoded_ko, 
        forced_bos_token_id=tokenizer.lang_Code_to_id[lang] 

    )

translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

return translated_text[0]
