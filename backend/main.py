from fastapi import FastAPI
from pytube import YouTube
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search/{item_id}")
async def search_item(item_id: str, q = None):
    if q:
        return Search(item_id, q)
    else:
        return Search(item_id)

@app.get("/download/{item_id}")
async def download_item(item_id: str, id: str | None = None):
    return Download(item_id, id)

def Search(link, filters=None):
    link = "https://www.youtube.com/watch?v=" + link
    url = YouTube(str(link))
    if filters:
        filters += ", adaptive=True"
        filters = dict(e.split('=') for e in filters.split(', '))
        return url.streams.filter(**filters).first()
    return url.streams.first()
    
def Download(link, id):
    link = "https://www.youtube.com/watch?v=" + link
    url = YouTube(str(link))
    stream = url.streams.get_by_itag(id)
    return stream.download(output_path="./downloads")