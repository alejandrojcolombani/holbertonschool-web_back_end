#!/usr/bin/env python3
def index_page(page: int, page_size : int) -> tuple:
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
