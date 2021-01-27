class Particle(object):
    def __init__(self, name = '', position = (0.0, 0.0, 0.0), \
                 velocity = (0.0, 0.0, 0.0) , spin = 0.0):
        self.position = position
        self.velocity = velocity
        self.name = name
        self.spin = spin

    def __str__(self):
        print('in particle str')
        pos_str = '({}:{}:{})'.format(self.position[0],self.position[1],self.position[2])
        vel_str = '({}:{}:{})'.format(self.velocity[0],self.velocity[1],self.velocity[2])
        result_str = "{} at {} with velocity {} and spin {}".format(self.name, pos_str, vel_str, self.spin)
        return result_str

class MassParticle(Particle):
    def __init__(self, name = '', position = (0.0, 0.0, 0.0), \
             velocity = (0.0, 0.0, 0.0) , spin = 0.0, mass = 0.0):
        Particle.__init__(self, name, position, velocity, spin)
        self.mass = mass

    def __str__(self):
        print('in mass str')
        result_str = Particle.__str__(self)
        result_str = result_str + ' and mass {}'.format(self.mass)
        return result_str
