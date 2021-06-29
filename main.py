import logging
import time
import os
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi_utils.tasks import repeat_every
from processing.word_processing import get_most_repeated_word, filter_words, filter_words, word_lemmanting, word_tags, stemming_word

logger = logging.getLogger(__name__)
app = FastAPI(title="Natural Language Processing")


@app.get('/most-repeated-word', tags=['Get most repeated word'])
async def get_word(words: str):
    return get_most_repeated_word(words)


@app.post('/remove-stop-words', tags=['remove stop words from string'])
async def get_words(words: str):
    return filter_words(words)


@app.post('/Stemming-words', tags=['Stemming Words'])
async def get_stemmed_words(words: str):
    return stemming_word(words)


@app.post('/lemmanted-words', tags=['Lemmanted Words'])
async def get_lemmanted_words(words: str):
    return word_lemmanting(words)


@app.post('/word-tags', tags=['Word tags (types)'])
async def get_tags_of_words(words: str):
    return word_tags(words)

@app.on_event("startup")
@repeat_every(seconds=86400, logger=logger, wait_first=True)
def periodic():
    pass