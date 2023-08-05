# HiQ version 1.1.4
#
# Copyright (c) 2022, Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl/
#
import os.path
import time

import hiq
from hiq import HiQLatency, HiQMemory
from hiq.constants import *
from hiq.hiq_utils import func_args_handler
from hiq.memory import get_memory_mb

from typing import Union, Callable, List
from hiq.hiq_utils import (
    func_args_handler,
    get_tau_id,
)

from contextvars import ContextVar
from typing import *
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Optional
from uuid import UUID, uuid4

from starlette.datastructures import Headers, MutableHeaders

# Middleware
correlation_id: ContextVar[Optional[str]] = ContextVar('correlation_id', default=None)

if TYPE_CHECKING:
    from starlette.types import ASGIApp, Message, Receive, Scope, Send


def is_valid_uuid4(uuid_: str) -> bool:
    """
    Check whether a string is a valid v4 uuid.
    """
    try:
        return bool(UUID(uuid_, version=4))
    except ValueError:
        return False


FAILED_VALIDATION_MESSAGE = 'Generated new request ID (%s), since request header value failed validation'


@dataclass
class CorrelationIdMiddleware:
    app: 'ASGIApp'
    header_name: str = 'X-Request-ID'

    async def __call__(self, scope: 'Scope', receive: 'Receive', send: 'Send') -> None:
        """
        Load request ID from headers if present. Generate one otherwise.
        """
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return

        async def handle_outgoing_request(message: 'Message') -> None:
            if message['type'] == 'http.response.start' and correlation_id.get():
                headers = MutableHeaders(scope=message)
                headers.append(self.header_name, correlation_id.get())
                headers.append('Access-Control-Expose-Headers', self.header_name)

            await send(message)

        await self.app(scope, receive, handle_outgoing_request)

    def __post_init__(self) -> None:
        pass


class FastAPIReqIdGenerator(object):
    def __call__(self):
        return correlation_id.get()


g_cpu_info = None

from uuid import uuid4


def run_fastapi(driver, app, header_name='X-Request-ID', host='0.0.0.0', port=8080, worker=1,
                endpoints={'predict'},
                generator=lambda: uuid4().hex,
                templates_dir="templates",
                custom={"/custom": None}):
    from fastapi import Request
    from fastapi.templating import Jinja2Templates

    try:
        templates = Jinja2Templates(directory=templates_dir)
    except:
        templates = None

    app.add_middleware(CorrelationIdMiddleware, header_name=header_name)

    @app.middleware("http")
    async def add_latency_header(request: Request, call_next):
        if str(request.url).split('/')[-1] in endpoints:
            cid = request.headers.get(header_name) if header_name in request.headers else generator()
            correlation_id.set(cid)
            start_time = time.monotonic()
            response = await call_next(request)
            response.headers["X-latency"] = str(time.monotonic() - start_time)
            return response
        else:
            return await call_next(request)

    def not_implemented_func():
        return "NOT_IMPLEMENTED"

    for k, v in custom:
        app.get(k)(not_implemented_func if v is None else v)

    @app.get("/hiq_enable")
    async def hiq_enable():
        if not driver:
            return ""
        driver.enable_hiq()

        from fastapi.responses import RedirectResponse
        return RedirectResponse(url='/hiq')

    @app.get("/hiq_disable")
    async def hiq_disable():
        if not driver:
            return ""
        driver.disable_hiq()
        from fastapi.responses import RedirectResponse
        return RedirectResponse(url='/hiq')

    @app.get("/data.json")
    async def hiq_data():
        if not driver:
            return "[]"
        if not os.path.exists("data.json"):
            return hiq.mod('fastapi').responses.Response("")
        return hiq.mod('fastapi').responses.FileResponse('data.json')

    @app.get("/hiq.css")
    async def hiq_data():
        if not driver:
            return ""
        if not os.path.exists("hiq.css"):
            return hiq.mod('fastapi').responses.Response("")
        return hiq.mod('fastapi').responses.FileResponse('hiq.css')

    @app.get("/plot")
    async def plot(request: Request) -> dict:
        if not driver or not os.path.exists(templates_dir)or not templates:
            return ""
        return templates.TemplateResponse("index.html", {"request": request})

    @app.get("/hiq")
    async def hiq_report():
        global g_cpu_info
        from fastapi.responses import HTMLResponse
        import cpuinfo

        if not g_cpu_info:
            g_cpu_info = cpuinfo.get_cpu_info()["brand_raw"]
        if not driver:
            return ""
        r = driver.get_k0s_summary()
        tmp = []
        for k, span, start, end in r:
            s = f'<tr><td><a href=latency/{k}>🌲 {k}</a><td align=right>{span}<td align=right>{hiq.ts_to_dt(start)}<td align=right>{hiq.ts_to_dt(end)}'
            tmp.append(s)
        resp = '<table width=100%><tr><td width=50% align=left>Req ID<td align=right>Latency<td align=right>Start<td align=right>End' + '\n'.join(
            tmp) + "</table>"

        html_resp = f"""
                <!DOCTYPE html>
                <html>
                  <head>
                      <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
                      <link rel="stylesheet" href="https://leeoniya.github.io/uPlot/dist/uPlot.min.css">
                      <script src="https://leeoniya.github.io/uPlot/dist/uPlot.iife.min.js"></script>
                  </head>
                  <body class="bg-white">
                    <section style='font-family: monospace, Times, serif;'>
                        <div class="container py-12 mx-auto">
                            <div class="flex flex-col flex-wrap pb-6 mb-2 text-black ">
                                <h1 class="mb-2 text-3xl font-medium text-black">
                                    Request Latency Report
                                </h1>
                                <p class="text-sm">
                                HiQ: {'🟢Enabled' if driver.enabled else '🔴Disabled'},
                                CPU: {g_cpu_info},
                                Load: {os.getloadavg()[0]:.2f},
                                Memory: {hiq.memory.get_memory_gb():.2f}GB </p> </div>
                                <div class="flex flex-wrap 
                                items-end justify-start w-full transition duration-500 ease-in-out transform bg-white 
                                border-2 border-gray-600 rounded-lg hover:border-white "> <div class="w-full"> <div 
                                class="relative flex flex-col h-full p-8 text-sm"> <pre>{resp}</pre>
                                </div>
                            </div>
                        </div>
                    </section>
                  </body>
                </html>
                """
        return HTMLResponse(content=html_resp, status_code=200)

    @app.get("/latency/{req_id}")
    async def latency(req_id: str):
        if not driver:
            return ""
        from fastapi.responses import HTMLResponse

        t = driver.get_metrics_by_k0(req_id if req_id != 'None' else None)
        resp = t.get_graph(FORMAT_DATETIME) if t else f"Error: The reqeust id({req_id}) is invalid!"
        html_resp = f"""
        <!DOCTYPE html>
        <html>
          <head>
              <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
          </head>
          <body class="bg-white">
            <section style='font-family: monospace, Times, serif;'>
                <div class="container py-12 mx-auto">
                    <div class="flex flex-col flex-wrap pb-6 mb-2 text-black ">
                        <h1 class="mb-2 text-3xl font-medium text-black">
                            Request Latency Report
                        </h1>
                        <p class="text-xl leading-relaxed">Request Id: {req_id}</p>
                    </div>
                    <div class="flex flex-wrap 
                        items-end justify-start w-full transition duration-500 ease-in-out transform bg-white 
                        border-2 border-gray-600 rounded-lg hover:border-white "> <div class="w-full"> <div 
                        class="relative flex flex-col h-full p-8 text-sm"> <pre>{resp}</pre> </div> </div> <div 
                        class="w-full xl:w-1/4 md:w-1/4 lg:ml-auto"> <div class="relative flex flex-col h-full p-8"> 
                        <button class="w-full px-4 py-2 mx-auto mt-3"> <a href="../hiq">Back to HiQ Report Home 🏠</a> </button> </div> </div> 
                        </div> </section> </body> </html>"""
        return HTMLResponse(content=html_resp, status_code=200)

    import uvicorn
    uvicorn.run(app, host=host, port=port, workers=worker)


def get_corr_id():
    from asgi_correlation_id.context import correlation_id
    return correlation_id.get()


class HiQFastAPILatencyMixin:
    def __init__(sf,
                 hiq_table_or_path: Union[str, list] = [],
                 metric_funcs: List[Callable] = [time.time],
                 hiq_id_func: Callable = FastAPIReqIdGenerator(),
                 func_args_handler: Callable = func_args_handler,
                 target_path=None,
                 max_hiq_size=30,
                 verbose=False,
                 fast_fail=True,
                 tpl=None,
                 extra_hiq_table=[],
                 attach_timestamp=False,
                 extra_metrics=set(),
                 lmk_path=None,
                 lmk_handler=None,
                 lmk_logger=None,
                 ):
        super().__init__(hiq_id_func=hiq_id_func,
                         hiq_table_or_path=hiq_table_or_path,
                         metric_funcs=metric_funcs,
                         func_args_handler=func_args_handler,
                         target_path=target_path,
                         max_hiq_size=max_hiq_size,
                         verbose=verbose,
                         fast_fail=fast_fail,
                         tpl=tpl,
                         extra_hiq_table=extra_hiq_table,
                         attach_timestamp=attach_timestamp,
                         extra_metrics=extra_metrics,
                         lmk_path=lmk_path,
                         lmk_handler=lmk_handler,
                         lmk_logger=lmk_logger,
                         )


class HiQFastAPILatency(HiQLatency):
    def __init__(
            sf,
            hiq_table_or_path: Union[str, list] = [],
            metric_funcs: List[Callable] = [time.time],
            func_args_handler: Callable = func_args_handler,
            target_path=None,
            max_hiq_size=30,
            verbose=False,
            fast_fail=True,
            tpl=None,
            extra_hiq_table=[],
            attach_timestamp=False,
            extra_metrics=set(),
            lmk_path=None,
            lmk_handler=None,
            lmk_logger=None,
    ):
        HiQLatency.__init__(
            sf,
            hiq_table_or_path=hiq_table_or_path,
            metric_funcs=metric_funcs,
            hiq_id_func=FastAPIReqIdGenerator(),
            func_args_handler=func_args_handler,
            target_path=target_path,
            max_hiq_size=max_hiq_size,
            verbose=verbose,
            fast_fail=fast_fail,
            tpl=tpl,
            extra_hiq_table=extra_hiq_table,
            attach_timestamp=attach_timestamp,
            extra_metrics=extra_metrics,
            lmk_path=lmk_path,
            lmk_handler=lmk_handler,
            lmk_logger=lmk_logger,
        )

    def custom(sf):
        pass

    def custom_disable(sf):
        pass


class HiQFastAPIMemory(HiQMemory):
    def __init__(
            sf,
            hiq_table_or_path: Union[str, list] = [],
            metric_funcs: List[Callable] = [time.time, get_memory_mb],
            func_args_handler: Callable = func_args_handler,
            target_path=None,
            max_hiq_size=30,
            verbose=False,
            fast_fail=True,
            tpl=None,
            extra_hiq_table=[],
            attach_timestamp=False,
            extra_metrics=set(),
            lmk_path=None,
            lmk_handler=None,
            lmk_logger=None,
    ):
        HiQLatency.__init__(
            sf,
            hiq_table_or_path=hiq_table_or_path,
            metric_funcs=metric_funcs,
            hiq_id_func=FastAPIReqIdGenerator(),
            func_args_handler=func_args_handler,
            target_path=target_path,
            max_hiq_size=max_hiq_size,
            verbose=verbose,
            fast_fail=fast_fail,
            tpl=tpl,
            extra_hiq_table=extra_hiq_table,
            attach_timestamp=attach_timestamp,
            extra_metrics=extra_metrics,
            lmk_path=lmk_path,
            lmk_handler=lmk_handler,
            lmk_logger=lmk_logger,
        )

    def custom(sf):
        pass

    def custom_disable(sf):
        pass
