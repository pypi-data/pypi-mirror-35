'''A bunch of analytical 1D disk models.

Provide a base class Disk with broad definitions of usual functions of
radial positions. A derived model TransitionDisk is also included and
shows how simple it to add on top of existing code.
'''

import sympy as sp

class Disk:
    '''A simple steady-state, 1D radial disk model.
    
    Assumptions
    -----------

    - density is a powerlaw
    - azimuthal velocity is set so that pressure gradient, 
      gravity from central star, and centrifugal forces balance out
    - radial velocity is assumed to be zero
    - pressure is given by equation of state with 'energy = .false.' 
      case from AMRVAC
    - aspect ratio is supposed to be uniform (hence linear scale height)

    Any one of these assumptions can be dropped by subclassing this
    class and rewriting the corresponding classmethod(s).
    '''

    r,rho0,slope = sp.symbols('r rho0 s')
    star_mass = sp.symbols('Ms')
    S_adiab, gamma = sp.symbols('S_ad gamma')
    eta = sp.symbols('eta') # dynamical molecular viscosity
    G = sp.symbols('G') #gravitational constant

    def __init__(self, values:dict):
        '''Instanciation can be used to store a set of parameters.

        Physical functions can then be evaluated directly via the
        instance's attributes rather than from the class methods.
        '''
        self.values = values

    @classmethod
    def _surface_density(scls, r):
        class SurfaceDensity(sp.Function):
            @classmethod
            def eval(cls, R):
                return scls.rho0 * R**scls.slope
        return SurfaceDensity(r)

    @classmethod
    def _midplane_volumic_density(cls, r):
        '''Assumes a gaussian vertical distribution.'''
        return cls._surface_density(r) / (sp.sqrt(2*sp.pi) * cls._scale_height(r))

    @classmethod
    def _angular_velocity(cls, r):
        return sp.sqrt(r*cls._pressure(r).diff(r)/cls._surface_density(r) + cls.G*cls.star_mass/r) / r

    @classmethod
    def _azimuthal_velocity(cls, r):
        return cls._angular_velocity(r) * r

    @classmethod
    def _radial_velocity(cls, r):
        class RadialVelocity(sp.Function):
            @classmethod
            def eval(cls, R):
                return 0
        return RadialVelocity(r)

    @classmethod
    def _velocity(cls, r):
        return sp.sqrt(cls._azimuthal_velocity(r)**2 + cls._radial_velocity(r)**2)

    @classmethod
    def _pressure(cls, r):
        return cls.S_adiab * cls._surface_density(r)**cls.gamma

    @classmethod
    def _entropy(cls, r):
        return cls._pressure(r) / (cls._surface_density(r)**cls.gamma)

    @classmethod
    def _sound_speed(cls, r):
        return sp.sqrt(cls.gamma * cls.S_adiab * cls._surface_density(r)**(cls.gamma-1))

    @classmethod
    def _reynolds(cls, r):
        return cls._midplane_volumic_density(r) * r * cls._velocity(r) / cls.eta

    #some additional, non-primitive functions are provided for convinience
    #---------------------------------------------------------------------
    @classmethod
    def _keplerian_angular_velocity(scls, r):
        class OmegaK(sp.Function):
            @classmethod
            def eval(cls, R):
                return sp.sqrt(scls.G * scls.star_mass / R**3)
        return OmegaK(r)

    @classmethod
    def _keplerian_azimuthal_velocity(cls, r):
        return r*cls._keplerian_angular_velocity(r)

    @classmethod
    def _scale_height(cls, r):
        '''An effective scale height inherited from the locally-isothermal model.

        It is only meant for comparison with other models, and is not
        used anywhere in AMRVAC.
        '''
        return cls._sound_speed(r) / cls._keplerian_angular_velocity(r)

    @classmethod
    def _aspect_ratio(scls, r):
        'General case: radius-dependent aspect ratio, with an underlying effective flaring.'
        return cls._scale_height(r) / r

    @classmethod
    def _vorticity(cls, r):
        return 1/r * (r * cls._azimuthal_velocity(r)).diff(r)

    @classmethod
    def _vortensity(cls, r):
        return cls._vorticity(r) / cls._surface_density(r)

    @classmethod
    def _rayleigh_function(cls, r):
        '''Rayleigh instability is characterized by negative
        values of this function.
        '''
        return (cls._angular_velocity(r)*r**2).diff(r)

    @classmethod
    def _lovelace_function(cls, r):
        '''The L(r) function as defined by (Lovelace et al 1999) & (Li et al 2000).

        Rossby Wave Instability (RWI) is characterized by the presence
        of a local extremum in this function.
        '''
        return cls._entropy(r)**(2/cls.gamma) / (2*cls._vortensity(r))

    @classmethod
    def _epicyclic_frequency(cls, r):
        return sp.sqrt((r**4 * cls._angular_velocity(r)**2).diff(r) / r**3)

    @classmethod
    def _toomre_number(cls, r):
        '''See (Toomre 1964)

        Toomre's criterion for gravitational stability is Q>1
        '''
        return cls._sound_speed(r) * cls._epicyclic_frequency(r) / (sp.pi * cls._surface_density(r) * cls.G)

    # --- magic ---
    def __getattr__(self, attr):
        '''Turn classmethods into fake instance attributes.

        This allows simple syntax :
            my_disk = Disk(subs)
            my_disk.density(10)

        AttributeError is raised if 'attr' does not match an existing classmethod.
        '''
        r = self.__class__.r
        return getattr(self.__class__, f'_{attr}')(r).subs(self.values)

    def get_value(self, attr, converter=float):
        '''Get the numerical value, if defined.'''
        return eval(f'''converter(self.__class__.{attr}.subs(self.values))''')

class TransitionDisk(Disk):
    '''A simple model of a transition disk.

    An hyperbolic tangent is used to model the cavity.
    This model is called HSJ (Homentropic Step Jump) in (Li et al 2000).
    '''

    #some specific parameters need to be defined
    r0,sig = sp.symbols('r0 sigma')

    #we redefine the density function. All other functions depending
    #on this one are written in a fashion that allows propagation of
    #the modification.
    @classmethod
    def _surface_density(scls, r):
        class Density(sp.Function):
            @classmethod
            def eval(cls, R):
                return Disk._surface_density(R) * 1/2 *(1+sp.tanh((R-scls.r0)/scls.sig))
        return Density(r)


class DustyDisk(Disk):
    '''Add basic dust-related analytical functions.'''

    #devnote : currently only admits one dust size
    #this will probably be generalized later.

    sp, rhop = sp.symbols('s_p rho_p') # particle size, particle intrisec density

    @classmethod
    def _dust_stopping_time(cls, r):
        #from Méheut et al 2012, Epstein regime
        return sp.sqrt(sp.pi/8) * cls.rhop * cls.sp / (cls._sound_speed(r)*cls._midplane_volumic_density(r))

    @classmethod
    def _delta_velocity(cls, r):
        'Get difference in azimuthal velocities between dust and gas'
        return cls._keplerian_azimuthal_velocity(r) - cls._azimuthal_velocity(r)

    @classmethod
    def _dust_reynolds(cls, r):
        return cls.sp * cls._delta_velocity(r) * cls._midplane_volumic_density(r) / cls.eta

    @classmethod
    def _stokes_number(cls, r):
        return cls._dust_stopping_time(r) * cls._keplerian_angular_velocity(r)
