from sanic import Blueprint
from sanic.response import text
from sanic.exceptions import NotFound

import patton_server

end_points_home = Blueprint("home")


@end_points_home.route('/', methods=['GET'])
async def hello_world(*args, **kwargs):
    return text(f"""
████████████████████████████████████████████████████████████████████████████████
██ Welcome to patton {patton_server.__version__} █████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████▀,  ▀████████████████████████████████
█████████████████████████████▀▀`    ²"²╕, ``  ▀ ╙███████████████████████████████
██████████████████████████▀          ⁿ▒∩         ▐██████████████████████████████
█████████████████████████                         ██████████████████████████████
████████████████████████▌         ,,▄▄▓▓█████`██████████████████████████████████
█████████████████████████     ,▄▓████████████⌐╟█████▀▀█»="`   ██████████████████
█████████████████████████,,▄▓█████████▀▀▀▀▀▀▀▀▒▄═²"`         ▐██████████████████
████████████████████▀██-«≈≈≈*ⁿ" ````  ,▄▄▄▄▄ææªª≈▀▀#▄       ▄███████████████████
██████████████████,╨       ,▄▄²▀▀`   ▄▀%▄   ⌐   ╓▓▀▀╙▌ , ,▄█████████████████████
█████████████████       ,▄╣█▀▀      `    `▀▀  "▀▀     ▄╟████████████████████████
██████████████████▄,   ╟▄▄   *    ▄   ]█▄       ▐█     █████████████████████████
████████████████████████▄,╚            ▀▀    ,, ╙▀   j▓█████████████████████████
██████████████████████████▀                   ,█     ╓██████████████████████████
███████████████████████████▓▓▀       ╓≈¬    "▀    ╦, ███████████████████████████
████████████████████████████        ] "≈w▄,,,,,▄æ"╓▀▓███████████████████████████
██████████████████████████▀ █▄              #*ⁿ    ▄████████████████████████████
███████████████████████▀    ▓ ▀╦         »     x ,██████████████████████████████
██████████████████▀▀ #       ▌   ▀¥▄       '`^▄▄▓█   ▀▀█████████████████████████
████████████▀▀"    ╓▌        ╫   ▄▓██████▓██████▌▌      ▀▄▀▀▀███████████████████
███████▀▀`          ,▄═▀▀     ▌  ████████████████▌   ,▄²▀        ▀▀█▀  █████████
█████▀            ]▌          └▌ ███████████████▀   ▀ `"``▀▄æ≈w▄, ]▌  ╓█████████
████               ▀▄          ╙▄████▀▀    ▀▀███           █      "▀  ▀█████████
███     ▄H          "▓          ╙▄     L   ▌  á         ╒█   `"^²%¥═    ▐███████
██   j  ▌▌            ▀▄         ╙▄    ▌▀▀ ▌ å           █▄╓,            ███████
█▌    █ █               ▀▄         █   ▌   ╠▀           █               ████████
█▌     ▌╟                 ▀%,       ▀▄    ▄▀          ▄▀█▌ ⁿ═╖▄▄       █▐███████
█▀  ╘  └█▌                   ▀▄      ╙▌ ▄▀        ,▄▀` ╙▌     ╤       ▐█ █▀█████
█    ¥   █                     `▀▄   ,▄▀       ╓#▀       █ ▓▓▀        ██l███████
▌     ▀▄  █                       ▄█▀`     ,A▀`          █  ▌        █ █████████
""")


@end_points_home.exception(NotFound)
async def ignore_404s(request, exception):
    return text("", status=404)


__all__ = ("end_points_home",)
