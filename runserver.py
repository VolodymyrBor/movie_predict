import uvicorn

from configs import CONFIG
from movie_predict.app import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app='runserver:app',
        host=CONFIG.HOST,
        port=CONFIG.PORT,
        reload=CONFIG.RELOAD,
    )
