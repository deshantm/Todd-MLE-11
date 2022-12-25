from fastapi import FastAPI
import transformers
from transformers import pipeline
from pydantic import BaseModel


en_fr_translator = pipeline("translation_en_to_fr", model="t5-small")

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

class TextstoTranslate(BaseModel):
    input_texts: list[str]



app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def translate(text_to_translate: TextToTranslate):
   return {"message": en_fr_translator(text_to_translate.input_text)}

@app.post("/translatebatch")
def translate_batch(texts_to_translate: TextstoTranslate): 
    translations = [] 
    for to_translate in texts_to_translate.input_texts:
        translated_text = en_fr_translator(to_translate)
        translations.append(translated_text)
    return translations

"""def echo(message: str):
    return {"message": message}"""
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)