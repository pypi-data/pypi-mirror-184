from typing import Iterable

from fastapi import Request
from dependency_injector.wiring import inject
from starlette.datastructures import URL

from velait.velait_fastapi.api.pagination import Page, PageInfo


def get_next_page(url: URL, current_page: int, last_page: int):
    if current_page == last_page:
        return None

    return str(url.include_query_params(page=current_page + 1))


def get_prev_page(url: URL, current_page: int):
    if current_page == 0:
        url.remove_query_params('page')
        return str(url)

    return str(url.include_query_params(page=current_page - 1))


@inject
def paginate(
    request: Request,
    page_size: int,
    items: Iterable,
    total_count: int,
) -> Page:
    last_page = total_count // page_size

    return Page(
        results=items,
        pagination=PageInfo(
            total_records=total_count,
            total_pages=last_page,
            first=str(request.url.remove_query_params('page')),
            last=str(request.url.include_query_params(page=last_page)),
            next=get_next_page(
                request.url,
                last_page=last_page,
                current_page=request.path_params.get('page', 0)
            ),
            previous=get_prev_page(request.url, current_page=request.path_params.get('page', 0)),
        ),
    )


def get_page_limits(page: int, page_size: int):
    offset = page * page_size
    return offset, offset + page_size
