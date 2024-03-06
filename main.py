import uvicorn
from fastapi import FastAPI

from src.handlers.batch_handlers import router as batch_router
from src.handlers.product_handlers import router as product_router

app = FastAPI(title='Axon Backend Task',
              description='API Documentaion',
              version='0.0.1',
              contact={
                  'name': 'Ramil Mavliutov',
                  'url': 'https://t.me/stirk1337',
                  'email': 'stirk-delovoy@mail.ru',
              },
              )


app.include_router(batch_router)
app.include_router(product_router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
