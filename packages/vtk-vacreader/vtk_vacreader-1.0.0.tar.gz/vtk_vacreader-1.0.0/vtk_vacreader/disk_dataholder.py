from pathlib import Path

class DiskDataHolder(VacDataSorter):
    '''Add derived fields to dataholder base class.'''

    def __init__(self, conf=None, *args):
        super().__init__(*args)
        if isinstance(conf, f90nml.Namelist):
            self.conf = conf
        elif isinstance(conf, (str, Path)):
            self.conf = f90nml.read(conf)
        else:
            raise TypeError("<conf> should be of type str, pathlib.Path or f90nml.Namelist")
        self._add_derived_fields()

    def _add_derived_fields(self):
        gamma = self.conf['hd_list']['hd_gamma']
        mstar = self.conf['disk_list']['central_mass']
        _, rgrid = self.get_meshgrid()
    
        S = self.conf['usr_list']['aspect_ratio']**2 * mstar*self.conf['usr_list']['rhozero']**(1-gamma)/gamma
        p = S * self['rho']**gamma
        cs = np.sqrt(gamma * p/self['rho'])
        OmegaK = np.sqrt(mstar/rgrid**3)
        H = cs / OmegaK

        A_vac = 16/9 * np.sqrt(gamma/3) #in AMRVAC
        A_epstein = np.sqrt(np.pi/8) #classic epstein

        ts0 = sp*rhop / (self['rho']*cs)
        ts_vac = A_vac * ts0
        t_epstein = A_epstein*ts0 * (np.sqrt(2*np.pi) * H)

        self.fields.update({
            'p': p,
            'cs': cs,
            'H': H,
            'ts_vac': ts_vac,
            'ts_epstein': ts_epstein,
            'St': ts * OmegaK,
        })
