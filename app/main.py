from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from .dependencies import *
from .utils import utils

app = FastAPI()


@app.post('/files/')
async def upload_file(token: str, file: UploadFile = File(...)):
    is_token = parse_token(token)
    if is_token:
        try:
            contents = await file.read()
        except Exception as e:
            print(e)
            return {"message": "failed to upload file"}
        finally:
            await file.close()

        img = utils.webp_converter(contents)
        return StreamingResponse(img, media_type='image/webp')

    return {"message": "invalid token"}
