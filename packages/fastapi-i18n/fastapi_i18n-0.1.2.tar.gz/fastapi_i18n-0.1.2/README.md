# README

## 1. Quick start

Install the package:

```shell
pip install fastapi-i18n
```

Usage in your project:

```python
import i18n
from fastapi import FastAPI, Depends

app = FastAPI()


@app.on_event("startup")
async def startup():
    await i18n.init()

@app.get('/')
async def root(translator: i18n.Translator = Depends(i18n.Translator)):
    return {"message": translator.t('hello.world')}
```
