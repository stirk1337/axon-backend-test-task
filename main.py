import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title='Axon Backend Task',
              description='API Documentaion',
              version='0.0.1',
              contact={
                  'name': 'Ramil Mavliutov',
                  'url': 'https://t.me/stirk1337',
                  'email': 'stirk-delovoy@mail.ru',
              },
              )

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


log_config = uvicorn.config.LOGGING_CONFIG
log_config['formatters']['access']['fmt'] = \
    '%(asctime)s - %(levelname)s - %(message)s'
log_config['formatters']['default']['fmt'] = \
    '%(asctime)s - %(levelname)s - %(message)s'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000,
                log_config=log_config, root_path='/api/v1/')
