from .io import opener
from pathlib import Path
import numpy as np
import logging
from datetime import datetime
from io import BytesIO
import xarray
from typing import Dict, List, Tuple, Any
from typing.io import TextIO
#
"""https://github.com/mvglasow/satstat/wiki/NMEA-IDs"""
SBAS = 100  # offset for ID
GLONASS = 37
QZSS = 192
BEIDOU = 0


def rinexobs3(fn: Path,
              use: List[str]=None,
              tlim: Tuple[datetime, datetime]=None,
              useindicators: bool=False,
              meas: List[str]=None,
              verbose: bool=False) -> xarray.Dataset:
    """
    process RINEX 3 OBS data

    use: 'G'  or ['G', 'R'] or similar
    meas:  'L1C'  or  ['L1C', 'C1C'] or similar
    """
    if isinstance(use, str):
        use = [use]

    if isinstance(meas, str):
        meas = [meas]

    if not use or not use[0].strip():
        use = None

    if not meas or not meas[0].strip():
        meas = None
# %% allocate
    # times = obstime3(fn)
    data: xarray.Dataset = None  # data = xarray.Dataset(coords={'time': times, 'sv': None})
    if tlim is not None:
        assert isinstance(tlim[0], datetime), 'time bounds are specified as datetime.datetime'
# %% loop
    with opener(fn) as f:
        hdr = obsheader3(f, use, meas)
# %% process OBS file
        for ln in f:
            if not ln.startswith('>'):  # end of file
                break

            try:
                time = _timeobs(ln, fn)
            except ValueError:  # garbage between header and RINEX data
                logging.error(f'garbage detected in {fn}, trying to parse at next time step')
                continue
# %% get SV indices
            # Number of visible satellites this time %i3  pg. A13
            Nsv = int(ln[33:35])

            sv = []
            raw = ''
            for i, ln in zip(range(Nsv), f):
                sv.append(ln[:3].replace(' ', '0'))
                raw += ln[3:]

            if tlim is not None:
                if time < tlim[0]:
                    continue
                elif time > tlim[1]:
                    break

            if verbose:
                print(time, end="\r")

            data = _epoch(data, raw, hdr, time, sv, useindicators, verbose)

    if data is None:  # all outside time bounds, etc.
        return

    data.attrs['filename'] = fn.name
    data.attrs['version'] = hdr['version']
    data.attrs['position'] = hdr['position']
    data.attrs['rinextype'] = 'obs'
    # data.attrs['toffset'] = toffset

    return data


def _timeobs(ln: str, fn: Path) -> datetime:
    """
    convert time from RINEX 3 OBS text to datetime
    """
    if not ln.startswith('>'):  # pg. A13
        raise ValueError(f'RINEX 3 line beginning > is not present in {fn}')

    return datetime(int(ln[2:6]), int(ln[7:9]), int(ln[10:12]),
                    hour=int(ln[13:15]), minute=int(ln[16:18]),
                    second=int(ln[19:21]),
                    microsecond=int(float(ln[19:29]) % 1 * 1000000))


def obstime3(fn: Path) -> xarray.DataArray:
    """
    return all times in RINEX file
    """
    times = []
    header = obsheader3(fn)

    with opener(fn) as f:
        for ln in f:
            if ln.startswith('>'):
                times.append(_timeobs(ln, fn))

    timedat = xarray.DataArray(times,
                               dims=['time'],
                               attrs={'filename': fn,
                                      'interval': header['interval']})

    return timedat


def _epoch(data: xarray.Dataset, raw: str,
           hdr: Dict[str, Any],
           time: datetime,
           sv: List[str],
           useindicators: bool,
           verbose: bool) -> xarray.Dataset:
    """
    block processing of each epoch (time step)
    """
    darr = np.atleast_2d(np.genfromtxt(BytesIO(raw.encode('ascii')),
                                       delimiter=(14, 1, 1) * hdr['Fmax']))
# %% assign data for each time step
    for sk in hdr['fields']:  # for each satellite system type (G,R,S, etc.)
        # satellite indices "si" to extract from this time's measurements
        si = [i for i, s in enumerate(sv) if s[0] in sk]
        if len(si) == 0:  # no SV of this system "sk" at this time
            continue

        # measurement indices "di" to extract at this time step
        di = hdr['fields_ind'][sk]
        garr = darr[si, :]
        garr = garr[:, di]

        gsv = np.array(sv)[si]

        dsf: Dict[str, tuple] = {}
        for i, k in enumerate(hdr['fields'][sk]):
            dsf[k] = (('time', 'sv'), np.atleast_2d(garr[:, i*3]))

            if useindicators:
                dsf = _indicators(dsf, k, garr[:, i*3+1:i*3+3])

        if verbose:
            print(time, '\r', end='')

        if data is None:
            # , attrs={'toffset':toffset})
            data = xarray.Dataset(dsf, coords={'time': [time], 'sv': gsv})
        else:
            if len(hdr['fields']) == 1:  # one satellite system selected, faster to process
                data = xarray.concat((data,
                                      xarray.Dataset(dsf, coords={'time': [time], 'sv': gsv})),
                                     dim='time')
            else:  # general case, slower for different satellite systems all together
                data = xarray.merge((data,
                                     xarray.Dataset(dsf, coords={'time': [time], 'sv': gsv})))

    return data


def _indicators(d: dict, k: str, arr: np.ndarray) -> Dict[str, tuple]:
    """
    handle LLI (loss of lock) and SSI (signal strength)
    """
    if k.startswith(('L1', 'L2')):
        d[k+'lli'] = (('time', 'sv'), np.atleast_2d(arr[:, 0]))

    d[k+'ssi'] = (('time', 'sv'), np.atleast_2d(arr[:, 1]))

    return d


def obsheader3(f: TextIO,
               use: List[str]=None,
               meas: List[str]=None) -> Dict[str, Any]:
    """
    get RINEX 3 OBS types, for each system type
    optionally, select system type and/or measurement type to greatly
    speed reading and save memory (RAM, disk)
    """
    fields = {}
    Fmax = 0

    if isinstance(f, Path):
        fn = f
        with opener(fn) as f:
            return obsheader3(f)
# %% first line
    ln = f.readline()
    header = {'version': float(ln[:9]),  # yes :9
              'systems': ln[40],
              }
    for ln in f:
        if "END OF HEADER" in ln:
            break

        h = ln[60:80]
        c = ln[:60]
        if 'SYS / # / OBS TYPES' in h:
            k = c[0]
            fields[k] = c[6:60].split()
            N = int(c[3:6])
# %% maximum number of fields in a file, to allow fast Numpy parse.
            Fmax = max(N, Fmax)

            n = N-13
            while n > 0:  # Rinex 3.03, pg. A6, A7
                ln = f.readline()
                assert 'SYS / # / OBS TYPES' in ln[60:]
                fields[k] += ln[6:60].split()
                n -= 13

            assert len(fields[k]) == N

            continue

        if h.strip() not in header:  # Header label
            header[h.strip()] = c  # don't strip for fixed-width parsers
            # string with info
        else:  # concatenate to the existing string
            header[h.strip()] += " " + c
# %% useful values

    # list with x,y,z cartesian
    header['position'] = [float(j) for j in header['APPROX POSITION XYZ'].split()]
# %% time
    t0s = header['TIME OF FIRST OBS']
    # NOTE: must do second=int(float()) due to non-conforming files
    header['t0'] = datetime(year=int(t0s[:6]), month=int(t0s[6:12]), day=int(t0s[12:18]),
                            hour=int(t0s[18:24]), minute=int(t0s[24:30]), second=int(float(t0s[30:36])),
                            microsecond=int(float(t0s[30:43]) % 1 * 1000000))

    try:
        header['interval'] = float(header['INTERVAL'][:10])
    except KeyError:
        header['interval'] = None
# %% select specific satellite systems only (optional)
    if use is not None:
        if not set(fields.keys()).intersection(use):
            raise KeyError(f'system type {use} not found in RINEX file')

        fields = {k: fields[k] for k in use if k in fields}

    # perhaps this could be done more efficiently, but it's probably low impact on overall program.
    # simple set and frozenset operations do NOT preserve order, which would completely mess up reading!
    sysind = {}
    if isinstance(meas, (tuple, list, np.ndarray)):
        for sk in fields:  # iterate over each system
            # ind = np.isin(fields[sk], meas)  # boolean vector
            ind = np.zeros(len(fields[sk]), dtype=bool)
            for m in meas:
                for i, f in enumerate(fields[sk]):
                    if f.startswith(m):
                        ind[i] = True

            fields[sk] = np.array(fields[sk])[ind].tolist()
            sysind[sk] = np.empty(Fmax*3, dtype=bool)  # *3 due to LLI, SSI
            for j, i in enumerate(ind):
                sysind[sk][j*3:j*3+3] = i
    else:
        sysind = {k: slice(None) for k in fields}

    header['fields'] = fields
    header['fields_ind'] = sysind
    header['Fmax'] = Fmax

    return header
