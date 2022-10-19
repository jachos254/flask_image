import pyodide
from pyodide.http import pyfetch

def on_click(e):
    left_ul = document.getElementById('left')
    left_ul.innerHTML = 'Hello World'

async def make_request(url, method, headers=None):
    if not headers:
        headers = {
            'X-Requested-Width': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }

    response = await pyfetch(
        url=url,
        method=method,
        headers=headers
    )

    return await response.json()

async def get_number_onclick(e):
    data = await make_request(url='/', method='GET')


def main():
    button = document.getElementById('button')
    button.addEventListener('click', pyodide.ffi.create_proxy(on_click))

main()