from fastapi import APIRouter

from . import songs
from movie_predict.data_types.router_module import RouterModule

_SUB_ROUTERS: tuple[RouterModule] = (  # type: ignore
    songs,
)


router = APIRouter(
    prefix='/api',
)

for sub_router in _SUB_ROUTERS:
    router.include_router(sub_router.router)


@router.get('/')
def status():
    return {
        'status': 'ok',
    }
