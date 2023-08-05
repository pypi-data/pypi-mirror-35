from .io import opener
from pathlib import Path
import numpy as np
import logging
from math import ceil
from datetime import datetime
from io import BytesIO
import xarray
from typing import Union, List, Any, Dict, Tuple
from typing.io import TextIO


def rinexobs2(fn: Path,
              use: List[str]=None,
              tlim: Tuple[datetime, datetime]=None,
              useindicators: bool=False,
              meas: List[str]=None,
              verbose: bool=False) -> xarray.Dataset:
    """
     procss RINEX OBS data
    use: 'G'  or ['G', 'R'] or similar
    meas:  'L1C'  or  ['L1C', 'C1C'] or similar
    """
    Lf = 14
# %% selection
    if isinstance(use, str):
        use = [use]

    if isinstance(meas, str):
        meas = [meas]

    if not use or not use[0].strip():
        use = None

    if not meas or not meas[0].strip():
        meas = None

# %% start reading
    with opener(fn) as f:
        # Capture header info
        hdr = obsheader2(f, useindicators, meas)
# %% process data
        data: xarray.Dataset = None

        for ln in f:
            # %% time
            try:
                time = _timeobs(ln)
            except ValueError:  # garbage between header and RINEX data
                logging.error(f'garbage detected in {fn}, trying to parse at next time step')
                continue

            if tlim is not None:
                assert isinstance(tlim[0], datetime), 'time bounds are specified as datetime.datetime'
                if time < tlim[0]:
                    _skip(f, ln, hdr['Nobs'])
                    continue
                elif time > tlim[1]:
                    break
# %%
            eflag = int(ln[28])
            if eflag not in (0, 1, 5, 6):  # EPOCH FLAG
                logging.info(f'{time}: epoch flag {eflag}')
                continue

            if verbose:
                print(time, end="\r")

            try:
                toffset = ln[68:80]
            except ValueError:
                toffset = None
# %% get SV indices
            sv = _getsvind(f, ln)
# %% select one, a few, or all satellites
            iuse: Union[List[int], slice]
            if use is not None:
                iuse = [i for i, s in enumerate(sv) if s[0] in use]
            else:
                iuse = slice(None)

            gsv = np.array(sv)[iuse]
# %% assign data for each time step
            Nl_sv = ceil(hdr['Nobs']/5)

            darr = np.empty((len(sv), hdr['Nobsused']))

            for i, s in enumerate(sv):
                raw = ''
                for _ in range(Nl_sv):
                    raw += f.readline()[:80]

                # save a lot of time by not processing discarded satellites
                if use is not None and not s[0] in use:
                    continue

                # some files truncate and put \n in data space.
                raw = raw.replace('\n', ' ')

                # can't use "usecols" with "delimiter"
                darr[i, :] = np.genfromtxt(BytesIO(raw.encode('ascii')), delimiter=[Lf, 1, 1]*hdr['Nobs'])[hdr['fields_ind']]
# % select only "used" satellites
            garr = darr[iuse, :]

            dsf: Dict[str, tuple] = {}
            for i, k in enumerate(hdr['fields']):
                if useindicators:
                    dsf[k] = (('time', 'sv'), np.atleast_2d(garr[:, i*3]))
                    dsf = _indicators(dsf, k, garr[:, i*3+1:i*3+3])
                else:
                    dsf[k] = (('time', 'sv'), np.atleast_2d(garr[:, i]))

            if data is None:
                data = xarray.Dataset(dsf, coords={'time': [time], 'sv': gsv}, attrs={'toffset': toffset})
            else:
                data = xarray.concat((data,
                                      xarray.Dataset(dsf, coords={'time': [time], 'sv': gsv}, attrs={'toffset': toffset})),
                                     dim='time')

        data.attrs['filename'] = fn.name
        data.attrs['version'] = hdr['version']
        data.attrs['position'] = hdr['position']
        data.attrs['rinextype'] = 'obs'

        return data


def _indicators(d: dict, k: str, arr: np.ndarray) -> Dict[str, tuple]:
    if k not in ('S1', 'S2'):  # FIXME which other should be excluded?
        if k in ('L1', 'L2'):
            d[k+'lli'] = (('time', 'sv'), np.atleast_2d(arr[:, 0]))

        d[k+'ssi'] = (('time', 'sv'), np.atleast_2d(arr[:, 1]))

    return d


def obsheader2(f: TextIO,
               useindicators: bool=False,
               meas: List[str]=None) -> Dict[str, Any]:

    if isinstance(f, Path):
        fn = f
        with opener(fn) as f:
            return obsheader2(f)

    header: Dict[str, Any] = {}
    Nobs = 0

    for l in f:
        if "END OF HEADER" in l:
            break

        h = l[60:80].strip()
        c = l[:60]
        if '# / TYPES OF OBSERV' in h:
            if Nobs == 0:
                Nobs = int(c[:6])
                c = c[6:].split()

        if h not in header:  # Header label
            header[h] = c  # string with info
        else:  # concatenate
            if isinstance(header[h], str):
                header[h] += " " + c
            elif isinstance(header[h], list):
                header[h] += c
            else:
                raise ValueError(f'not sure what {c} is')
# %% useful values
    header['version'] = float(header['RINEX VERSION / TYPE'][:9])  # %9.2f
    header['systems'] = header['RINEX VERSION / TYPE'][40]
    header['Nobs'] = Nobs
    # list with x,y,z cartesian
    header['position'] = [float(j) for j in header['APPROX POSITION XYZ'].split()]
# %% observation types
    header['fields'] = header['# / TYPES OF OBSERV']
    if Nobs != len(header['fields']):
        raise ValueError(f'{f.name} header read incorrectly')

    if isinstance(meas, (tuple, list, np.ndarray)):
        ind = np.zeros(len(header['fields']), dtype=bool)
        for m in meas:
            for i, f in enumerate(header['fields']):
                if f.startswith(m):
                    ind[i] = True

        # zeros, NOT empty!
        sysind = np.zeros(Nobs*3, dtype=bool)  # *3 due to LLI, SSI
        if useindicators:
            for j, i in enumerate(ind):
                sysind[j*3:j*3+3] = i
        else:
            sysind[::3] = ind

        header['fields_ind'] = sysind
    else:
        ind = slice(None)
        header['fields_ind'] = ind if useindicators else np.arange(0, Nobs*3, 3)

    header['fields'] = np.array(header['fields'])[ind].tolist()

    if isinstance(header['fields_ind'], slice):
        Nobsused = header['Nobs']*3
    elif header['fields_ind'].dtype == bool:
        Nobsused = np.count_nonzero(header['fields_ind'])
    else:
        Nobsused = header['fields_ind'].size
    header['Nobsused'] = Nobsused
# %%
    if '# OF SATELLITES' in header:
        header['# OF SATELLITES'] = int(header['# OF SATELLITES'][:6])
# %% time
    t0s = header['TIME OF FIRST OBS']
    # NOTE: must do second=int(float()) due to non-conforming files
    header['t0'] = datetime(year=int(t0s[:6]), month=int(t0s[6:12]), day=int(t0s[12:18]),
                            hour=int(t0s[18:24]), minute=int(t0s[24:30]), second=int(float(t0s[30:36])),
                            microsecond=int(float(t0s[30:43]) % 1 * 1000000))

    try:
        t0s = header['TIME OF LAST OBS']
        # NOTE: must do second=int(float()) due to non-conforming files
        header['t1'] = datetime(year=int(t0s[:6]), month=int(t0s[6:12]), day=int(t0s[12:18]),
                                hour=int(t0s[18:24]), minute=int(t0s[24:30]), second=int(float(t0s[30:36])),
                                microsecond=int(float(t0s[30:43]) % 1 * 1000000))
    except KeyError:
        pass

    try:  # This key is OPTIONAL
        header['interval'] = float(header['INTERVAL'][:10])
    except KeyError:
        header['interval'] = None

    return header


def _getsvind(f: TextIO, ln: str) -> List[str]:
    Nsv = int(ln[29:32])  # Number of visible satellites this time %i3
    # get first 12 SV ID's
    sv = _getSVlist(ln, min(12, Nsv), [])

    # any more SVs?
    n = Nsv-12
    while n > 0:
        sv = _getSVlist(f.readline(), min(12, n), sv)
        n -= 12
    assert Nsv == len(sv), 'satellite list read incorrectly'

    return sv


def _getSVlist(ln: str, N: int, sv: List[str]) -> List[str]:
    """ parse a line of text from RINEX2 SV list"""
    for i in range(N):
        s = ln[32+i*3:35+i*3].strip()
        if not s.strip():
            raise ValueError(f'did not get satellite names from {ln}')
# %% reformat to assure 0
        sv.append(s.replace(' ', '0'))  # 5x faster than f-string

    return sv


def obstime2(fn: Path) -> xarray.DataArray:
    """
    read all times in RINEX2 OBS file
    """
    times = []
    with opener(fn) as f:
        # Capture header info
        header = obsheader2(f)
        Nobs = header['Nobs']

        while True:
            ln = f.readline()
            if not ln:
                break

            times.append(_timeobs(ln))

            _skip(f, ln, Nobs)

    timedat = xarray.DataArray(times,
                               dims=['time'],
                               attrs={'filename': fn,
                                      'interval': header['interval']})

    return timedat


def _skip(f: TextIO, ln: str, Nobs: int):
    """
    skip ahead to next time step
    """
    sv = _getsvind(f, ln)
    Nl_sv = ceil(Nobs/5)

    # f.seek(len(sv)*Nl_sv*80, 1)  # not for io.TextIOWrapper ?
    for _ in range(len(sv)*Nl_sv):
        f.readline()


def _timeobs(ln: str) -> datetime:
    """
    Python >= 3.7 supports nanoseconds.  https://www.python.org/dev/peps/pep-0564/
    Python < 3.7 supports microseconds.
    """

    year = int(ln[1:3])
    if 80 <= year <= 99:
        year += 1900
    elif year < 80:  # because we might pass in four-digit year
        year += 2000
    else:
        raise ValueError(f'unknown year format {year}')

    return datetime(year=year,
                    month=int(ln[4:6]),
                    day=int(ln[7:9]),
                    hour=int(ln[10:12]),
                    minute=int(ln[13:15]),
                    second=int(ln[16:18]),
                    microsecond=int(float(ln[16:26]) % 1 * 1000000)
                    )
