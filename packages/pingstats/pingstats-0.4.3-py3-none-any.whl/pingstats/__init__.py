# Written under the MIT license. See LICENSE for more details
# For authors refer to AUTHORS.rst
# PY 2 TO 3 IMPORTS
from __future__ import print_function, with_statement

# STANDARD LIBRARY PACKAGES
from subprocess import Popen
from tempfile import NamedTemporaryFile
from os import system, name
from argparse import ArgumentParser

import time

# NON STANDARD LIBRARY PACKAGES
try:
    from hipsterplot.hipsterplot import plot
except ImportError:
    from .hipsterplot.hipsterplot import plot


# PARSER CONFIG
parser = ArgumentParser()

parser.add_argument('address', help='The address to ping. This could be either '
                    'a web address (i.e, "google.ca") or an IP address.')


def _get_tty_size():
    temp_file = NamedTemporaryFile()

    p = Popen('stty size'.split(), stdout=temp_file)
    p.wait()

    with open(temp_file.name) as f:
        rows, columns = f.read().split()
        rows = int(rows)
        columns = int(columns)

    return rows, columns


def run():
    """ Actually runs the logic. Uses ``subprocess.Popen`` to run system ``ping``
    and plots the results to ``hipsterplot.plot``.

    :address: A system ``ping`` compatible address, either web or IP.  """
    parsed = parser.parse_args()
    y = []

    print('Waiting for first ping...')  # Notify user in case of high ping

    try:
        while 1:
            time_start = time.time()

            temp_file = NamedTemporaryFile()
            process = Popen(['ping', '-c 1', parsed.address], stdout=temp_file)

            process.wait()

            with open(temp_file.name) as tf:

                for line in tf:
                    if len(y) > 20:
                        y.pop(0)

                    if line.lower().count('ttl'):
                        y.append(float(line.split('time=')[1].split(' ')[0]))

                    elif line.lower().count('0 received'):
                        y.append(-10)

            if time.time() - time_start < 0.5:  # Wait for time if no time elapsed
                time.sleep(0.5 - (time.time() - time_start))

            system('clear' if not name == 'nt' else 'cls')
            rows, columns = _get_tty_size()
            plot(y, num_x_chars=columns - 16, num_y_chars=rows - 3)
            if y.count(-10) == 1:
                print('1 packet dropped of %s'.center(columns) % len(y))
            elif y.count(-10) > 1:
                print('%s packets dropped of %s'.center(columns)
                      % (y.count(-10), len(y)))
            else:
                print('Displaying %s total packets from %s'.center(columns)
                      % (len(y), parsed.address))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        pass
