from typing import Protocol

from fastapi import APIRouter


class RouterModule(Protocol):
    router: APIRouter
