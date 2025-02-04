import os
import openai
import glob
# from utils.formatters import format_json_output
# from utils.image_processor import process_image
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import json
import base64
import pytesseract
from PIL import Image
import requests
from openai import OpenAI
# import test
from pydantic import ValidationError
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import date
import datetime
import json
from datetime import datetime
import streamlit as st


class Cliente(BaseModel):
    nome: str = Field(description="Nome completo del cliente")
    piva: Optional[str] = Field(
        None, description="Partita IVA (se presente)")
    indirizzo: Optional[str] = Field(None, description="Indirizzo completo")
    citta: Optional[str] = Field(None, description="Città")


class Prodotto(BaseModel):
    codice: str = Field(description="Codice prodotto univoco")
    descrizione: str = Field(description="Descrizione completa")
    quantita: float = Field(gt=0, description="Quantità ordinata")
    prezzo_unitario: float = Field(gt=0, description="Prezzo unitario")
    unita_misura: Optional[str] = Field("pz", description="Unità di misura")


class Ordine(BaseModel):
    cliente: Cliente
    data_ordine: date = Field(description="Data ordine in formato YYYY-MM-DD")
    prodotti: List[Prodotto]
    totale_iva: float = Field(0, description="Totale IVA")
    totale_ordine: float = Field(..., gt=0, description="Totale ordine")
    sconto: Optional[float] = Field(0, description="Sconto applicato")
    data_consegna: Optional[date] = Field(
        None, description="Data consegna prevista")
    modalita_consegna: Optional[str] = Field(
        None, description="Modalità di consegna")

    @field_validator("data_ordine", "data_consegna", mode="before")
    def parse_dates(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%d/%m/%Y").date()
        return value

    model_config = {
        "json_schema_extra": {
            "additionalProperties": False  # Blocca campi non definiti
        }
    }


# if __name__ == "__main__":

#     schema_example = Ordine.model_json_schema()

#     print(type(schema_example))

#     json = json.dumps(schema_example)
#     print("\n\n\n")
#     print(json)


def ocr_extract(image_path: str) -> str:
    """Estrai testo con Tesseract OCR ottimizzato"""
    img = Image.open(image_path)
    custom_config = r'--oem 3 --psm 6 -l eng+ita'  # Modalità alta precisione
    return pytesseract.image_to_string(img, config=custom_config)


def get_flattened_schema():
    """Appiattisce lo schema e aggiunge il nome richiesto"""
    schema = Ordine.model_json_schema()
    definitions = schema.pop("$defs", None)

    # Aggiungi il nome dello schema
    schema["name"] = "OrdineSchema"  # <--- Nome richiesto dall'API

    # Sostituisci i $ref
    for prop in schema.get("properties", {}).values():
        if "$ref" in prop:
            ref_key = prop["$ref"].split("/")[-1]
            if definitions and ref_key in definitions:
                prop.update(definitions[ref_key])
                prop.pop("$ref", None)

    return schema


def process_image(api:str, image_path: str, prompt: str, extracted_text: str = None) -> dict:
    """Analisi combinata OCR + GPT-4 Vision"""
    client = OpenAI(api_key=api)
    
    # Codifica immagine
    base64_image = encode_image(image_path)

    # Costruzione messaggio
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "text", "text": f"Testo estratto dall'OCR: {extracted_text}"} if extracted_text else None,
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "high"
                    }
                }
            ]
        }
    ]

    # Chiamata API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[m for m in messages if m is not None],
        max_tokens=2000,
        temperature=0.1,  # Massima precisione
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "OrdineSchema",  # Deve matchare con lo schema
                "schema": get_flattened_schema()  # Schema appiattito
            }
        }
    )

    return response.choices[0].message.content


def encode_image(image_path: str) -> str:
    """Codifica immagine in base64"""
    if image_path.startswith(('http://', 'https://')):
        response = requests.get(image_path)
        return base64.b64encode(response.content).decode('utf-8')
    else:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')


def format_json_output(raw_response: str) -> Ordine:
    """Converti e valida la risposta in JSON"""
    try:
        # Pulizia preliminare
        clean_response = raw_response.strip()
        if '```json' in clean_response:
            clean_response = clean_response.split('```json')[1].split('```')[0]
        # Converti la stringa JSON in un dizionario
        data = json.loads(clean_response)
        # Validazione della struttura
        return Ordine(**data)
    except (json.JSONDecodeError, ValueError, ValidationError) as e:
        print(f"Errore di parsing o validazione: {e}")
        return {"error": str(e), "raw_response": raw_response, "status": "VALIDATION_FAILED"}


# Configurazione
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_and_save(api: str, image_path: str, output_dir: str = "./output", use_ocr: bool = True) -> Ordine:
    """
    Analizza un'immagine e salva il risultato in JSON
    :param image_path: Percorso locale o URL dell'immagine
    :param output_dir: Cartella di destinazione
    :param use_ocr: Combina OCR+Tesseract per precisione
    """
    

    
    # Estrazione Contenuto
    extracted_text = None
    if use_ocr:
        extracted_text = ocr_extract(image_path)

    # Analisi GPT-4 Vision
    gpt_response = process_image(
        api=api,
        image_path=image_path,
        prompt=build_prompt(),
        extracted_text=extracted_text
    )

    print("Risposta grezza dell'AI:\n", gpt_response)  # debug

    print(type(gpt_response))

    # # Formattazione e validazione JSON
    # json_output = format_json_output(gpt_response)

    # # Salvataggio
    # save_json_output(json_output, output_dir)

    # return json_output

    # try:
    #     order_data = format_json_output(gpt_response)
    #     # save_json_output(order_data.model_dump(), output_dir)
    #     save_json_output(order_data, output_dir)
    #     return order_data

    # except ValidationError as e:
    #     print(f"Errore di validazione: {e}")
    #     return {"status": "error", "details": str(e)}

    # Conversione della stringa JSON in dizionario Python
    try:
        data_dict = json.loads(gpt_response)
        print(type(data_dict))
        print(data_dict)
        data = json.dumps(data_dict, ensure_ascii=False, indent=2)
        print(type(data))
        print(data)
        save_json_output(data_dict, output_dir)
        return data
    except json.JSONDecodeError as e:
        print(f"Errore di decodifica JSON: {e}")


def build_prompt() -> str:
    old = """
    Sei un assistente esperto addetto alla ricezione di ordini effettuati da vari clienti diversi, lavori per l'azienda di nome FOX ITALIA/BAR ITALIA.

    Analizza questa immagine e restituisci SOLO un JSON strutturato con:
1. 'type': 'table'|'concept_map'|'diagram'|'text'
2. 'content': Dati strutturati
3. 'confidence': % confidenza analisi
Per tabelle: array di oggetti con header/valori
Per mappe: nodi e relazioni
Per schemi: descrizione gerarchica


Dati importanti:
1. Cliente (nome completo e partita IVA se presente, indirizzo, località)
2. Data ordine (formato ISO 8601)
3. Prodotti (codice, descrizione completa, quantità, prezzo unitario, unità di misura)
4. Totali (IVA, totale ordine, eventuali sconti)
5. Informazioni logistiche (data consegna, modalità di consegna)

questi dati rappresentano un esempio di quello che potrebbe essere scritto nell'immagine.

Istruzioni aggiuntive:
- Converti tutti i numeri in formato float (es. 1.610,20 → 1610.20)
- Se un campo non è presente, usa null
- Non inventare dati mancanti
- Ignora testo non rilevante
- Gestisci valori concatenati (es. "3,300|3,00+" → prezzo_unitario: 3.30)
- Mantieni la struttura JSON anche se alcuni dati sono parziali
- Ricorda che lavori per FOX ITALIA / BAR ITALIA quindi i riferimenti a FOX ITALIA / BAR ITALIA nelle immagini ovviamente non sono dei clienti ma dell'azienda per cui lavori
- Nella foto può capitare che si faccia riferimento a due enti, devi sempre ignorare FOX ITALIA / BAR ITALIA e concentrarti sull altro
- Tu SEI FOX ITALIA / BAR ITALIA
    
    """

    schema = Ordine.model_json_schema()
    print(f"tipo 'schema': {type(schema)}")
    schema_json = json.dumps(schema, indent=2)
    return """
Sei un assistente esperto addetto alla ricezione di ordini effettuati da vari clienti diversi, lavori per l'azienda di nome FOX ITALIA/BAR ITALIA.
Estrai i seguenti dati dall'immagine rispettando STRETTAMENTE questo schema:


Istruzioni aggiuntive:
- Converti tutti i numeri in formato float (es. 1.610,20 → 1610.20)
- Se un campo non è presente, usa null
- Non inventare dati mancanti
- Ignora testo non rilevante
- Gestisci valori concatenati (es. "3,300|3,00+" → prezzo_unitario: 3.30)
- Mantieni la struttura JSON anche se alcuni dati sono parziali
- Ricorda che lavori per FOX ITALIA / BAR ITALIA quindi i riferimenti a FOX ITALIA / BAR ITALIA nelle immagini ovviamente non sono dei clienti ma dell'azienda per cui lavori
- Nella foto può capitare che si faccia riferimento a due enti, devi sempre ignorare FOX ITALIA / BAR ITALIA e concentrarti sull altro
- Tu SEI FOX ITALIA / BAR ITALIA

"""


def save_json_output(data: dict, output_dir: str):
    # Crea cartella se non esiste
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Genera filename univoco
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)

    # Scrittura file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"JSON salvato correttamente in: {filepath}")


if __name__ == "__main__":

    print(f"prompt:\n\n{build_prompt()}\n\n")
    # Configurazione
    load_dotenv()
    # api = os.getenv("TEST_FOX")
    api = st.secrets['TEST_FOX']
    # client = OpenAI(api_key=api)

    # Esempio con salvataggio automatico
    result = analyze_and_save(
        api=api,
        image_path="images/page_0_copy.jpg",
        output_dir="./analisi-results",
        use_ocr=True
    )
    print("Risultato JSON:", result)

    print(type(result))

    st.write(result)
