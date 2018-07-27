from multiprocessing import Pool, cpu_count
from time import time
import os
import sys
import requests
import sqlite3


def get_data(cedula):
    """We're ready to get our precious data, don't we?
    """
    # Avra kadavra
    db = sqlite3.connect('./datos.db')
    cursor = db.cursor()

    # Get our database ready
    set_db(cursor)

    try:
        # Gimme the shit
        payload = {'cedula': cedula}
        url = 'https://servicios.set.gov.py/eset-publico/ciudadano/recuperar'
        result = requests.get(url, params=payload)
        res_json = result.json()
        existe = 'existente'

        if (res_json['presente']):
            # Holy moly! o.O
            r = res_json['resultado']

            try:
                cursor.execute("""
                    INSERT INTO `datos`
                        (cedula, nombres, apellido_paterno,
                        apellido_materno, nombre_completo)
                    VALUES
                        (:cedula, :nombres, :apellidoPaterno,
                        :apellidoMaterno, :nombreCompleto);""", r)

                # Gotcha!
                db.commit()

                existe = 'nuevo'

            except sqlite3.IntegrityError:
                # Yo buddy, we got you sound and safe! ;)
                # We don't tolerate duplicated data, OK?
                pass

        # Just showing some info
        print('[{}] {} ({})'.format(str(os.getpid()).rjust(5), cedula, existe))

        # Close the curtain
        db.close()

    except requests.exceptions.RequestException as error:
        print(error)


def set_db(cursor):
    """Setting up our database.
    """
    # Pragma settings FTW
    cursor.execute('PRAGMA JOURNAL_MODE=WAL;')
    cursor.execute('PRAGMA SYNCHRONOUS=FULL;')
    cursor.execute('PRAGMA TEMP_STORE=MEMORY;')

    # Database structure (just one table)
    cursor.execute("""CREATE TABLE IF NOT EXISTS `datos` (
        `cedula` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        `nombres` TEXT,
        `apellido_paterno` TEXT,
        `apellido_materno` TEXT,
        `nombre_completo` TEXT);""")


if __name__ == '__main__':
    # From where we begin
    start, stop = 1, 10000000

    if len(sys.argv) > 1 and sys.argv[1]:
        start = int(sys.argv[1])

    if len(sys.argv) > 2 and sys.argv[2]:
        stop = int(sys.argv[2])

    # Put those cores to work, bruh!
    p = Pool(processes=cpu_count())

    # Let the hack begin
    t_start = time()
    r = p.map(get_data, range(start, stop + 1))
    t_total = time() - t_start

    print('\nTotal time: {:.3f} seconds'.format(t_total))
