# :boom: holy-SET-scraper :boom:

Versión recargada basada en el original de [SET-scraper](https://github.com/Karlheinzniebuhr/SET-scraper) hecho por [Karl](https://github.com/Karlheinzniebuhr).

La única dependencia es `requests` para realizar las peticiones HTTP. Esta 
versión tiene dos agregados:

1. Las peticiones se realizan en paralelo utilizando la cantidad total de cores 
de tu CPU.
2. El almacenamiento se realiza en SQLite3, dado que trabajamos con peticiones 
en paralelo.

Hecho con fines educativos... y porque somos curiosos. :smiling_imp:

## Instalación

```shell
$ git clone https://github.com/aquiandres/holy-set-scraper
$ cd holy-set-scraper
$ pip install -r requirements.txt
$ python holyscrap.py
```


## Utilización

`holyscrap.py` acepta dos parámetros en la linea de comandos de forma opcional:

```shell
$ python holyscrap.py [start, [stop]]
```

Por defecto `start` es 1 y `stop` es 10000000. Especial si querés hacer trabajar  el script usando [Celery](http://www.celeryproject.org/), [RQ](http://python-rq.org/) o [alguna otra librería](https://www.fullstackpython.com/task-queues.html) para procesamiento de tareas. En algún momento puede que te ocurra que la conexión HTTP se cierre, como me pasó a mí, entonces podés continuar fácilmente desde el último número de cédula almacenado.

Como no se almacena exactamente la última cédula solicitada, vas a tener que comenzar desde la última cédula existente que fue solicitada e insertada en la base de datos. Pero como sos capo, eso no es problema para vos ;)

**Happy scraping!** :neckbeard:

## Licencia

**The Unlicense**

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
