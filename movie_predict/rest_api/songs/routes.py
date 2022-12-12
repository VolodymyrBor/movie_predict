from fastapi import APIRouter, Depends

from sqlmodel import select

from .models import Song, SongCreate
from movie_predict.db import get_session, AsyncSession

router = APIRouter(
    prefix='/song',
)


@router.post('/')
async def create_song(
    song_create: SongCreate,
    session: AsyncSession = Depends(get_session),
) -> Song:
    song = Song.from_orm(song_create)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song


@router.get('/', response_model=list[Song])
async def get_many(
    session: AsyncSession = Depends(get_session),
) -> list[Song]:
    result = await session.execute(select(Song))
    return result.scalars().all()
