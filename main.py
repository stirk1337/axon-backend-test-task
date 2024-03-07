import uvicorn
from fastapi import FastAPI

from src.handlers.batch_handlers import router as batch_router
from src.handlers.product_handlers import router as product_router
from config import settings

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

log_config = uvicorn.config.LOGGING_CONFIG
log_config['formatters']['access']['fmt'] = \
    '%(asctime)s - %(levelname)s - %(message)s'
log_config['formatters']['default']['fmt'] = \
    '%(asctime)s - %(levelname)s - %(message)s'


if __name__ == '__main__':
    uvicorn.run(app, host=settings.app_host, port=settings.app_port, log_config=log_config)
