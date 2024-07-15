import numpy as np
import configuration as C
from setframe import Frame as SetFrame

"""
[Energy] = kJ / mol
[M] = g / mol
[F] = kJ /mol / A (A je angstrem)
[a] = A / ps^2
[t] = ps
[v] = A / ps
a = 0.1 * {F}/{m} -> proto se to tam někde dole násobí 0.1
"""

class Calculation:
    # funkce pro výpočet síly
    def __init__(self, particles: list, setframe: SetFrame) -> None:
        super().__init__()
        self.setframe = setframe
        self.particles = particles
        self.timestep = C.timestep
        self.cutoff = C.cutoff
        self.masses = self.setframe.conds.masses
        self.sigmas = self.setframe.conds.sigmas
        self.epsilons = self.setframe.conds.epsilons
        self.integrate()

    def integrate(self):
        self._new_coord()
        self._new_velocity()
    
    def _new_coord(self):
        for particle in self.particles:
            x = particle.xcoord + self.timestep * particle.xvelocity
            y = particle.ycoord + self.timestep * particle.yvelocity

            if x < 0:
                x += C.box_size_x
            elif x > C.box_size_x:
                x -= C.box_size_x

            if y < 0:
                y += C.box_size_y
            elif y > C.box_size_y:
                y -= C.box_size_y

            particle.xcoord = x
            particle.ycoord = y

    def _new_velocity(self):
        for i in range(len(self.particles)):
            particle = self.particles[i]
            #mainEpsilon = particle.epsilon
            #mainSigma = particle.sigma
            forceXi = 0.0
            forceYi = 0.0
            totForceX = 0.0
            totForceY = 0.0
            tot3Potenc = 0.0
            tot4Potenc = 0.0

            for j in range(len(self.particles)):
                if i == j:
                    continue
                sec_part = self.particles[j]
                #secSigma = sec_part.sigma
                #secEpsilon = sec_part.epsilon
                #aSigma = self.sigma_ave(mainSigma, secSigma)
                #aEpsilon = self.epsilon_ave(mainEpsilon, secEpsilon)
                totForceX, totForceY, tot3Potenc = self.force(particle, sec_part)
                forceXi += totForceX
                forceYi += totForceY
                tot4Potenc += tot3Potenc

                # zrychlení to je
                ########################################################################
                #vector_dist = sec_part.coord - particle.coord # vektorová vzdálenost 
                #distance = np.sqrt(vector_dist[0]**2 + vector_dist[1]**2) # číselná vzdálenost
                #force += vector_dist / distance * self.force_LJ(self.epsilon_ave, self.sigma_ave, distance)
                ########################################################################

            mass = self.masses[particle.type]
            ax = forceXi / mass * 0.1
            ay = forceYi / mass * 0.1

            particle.xvelocity += self.timestep * ax
            particle.yvelocity += self.timestep * ay



    def force(self, mainpart, secpart):
        tot_forceX = 0.0
        tot_forceY = 0.0
        #secpart = self.particles
        #for i in range(len(secpart)):

        #sigma, epsilon
        mainEpsilon = self.epsilons[mainpart.type]
        mainSigma = self.sigmas[mainpart.type]
        secSigma = self.sigmas[secpart.type]
        secEpsilon = self.epsilons[secpart.type]
        aSigma = self.sigma_ave(mainSigma, secSigma)
        aEpsilon = self.epsilon_ave(mainEpsilon, secEpsilon)
        

        xmain = mainpart.xcoord
        ymain = mainpart.ycoord
        x0 = secpart.xcoord
        xl = x0 - C.box_size_x
        xp = x0 + C.box_size_x
        y0 = secpart.ycoord
        tot2Potenc = 0.0

        if xmain - xl <= self.cutoff:
            force_X, force_Y, totPotenc = self.y_check(xmain, ymain, xl, y0, aSigma, aEpsilon)
            tot_forceX += force_X
            tot_forceY += force_Y
            tot2Potenc += totPotenc

        if xp - xmain <= self.cutoff:
            force_X, force_Y, totPotenc = self.y_check(xmain, ymain, xp, y0, aSigma, aEpsilon)
            tot_forceX += force_X
            tot_forceY += force_Y
            tot2Potenc += totPotenc

        if np.abs(xmain - x0) <= self.cutoff:
            force_X, force_Y, totPotenc = self.y_check(xmain, ymain, x0, y0, aSigma, aEpsilon)
            tot_forceX += force_X
            tot_forceY += force_Y
            tot2Potenc += totPotenc

        return tot_forceX, tot_forceY, tot2Potenc

    def y_check(self, xmain, ymain, xsec_real, ysec, sigma_ave, epsilon_ave):
        yd = ysec - C.box_size_y
        yu = ysec + C.box_size_y
        forceX = 0.0
        forceY = 0.0
        totPotenc = 0.0

        if ymain - yd <= self.cutoff:
            force_mag, potencial = self.force_LJ(epsilon_ave, sigma_ave, self.distance(xmain, ymain, xsec_real, yd))
            fX, fY = self.force_vec(xmain, ymain, xsec_real, yd, force_mag)
            forceX += fX
            forceY += fY
            totPotenc += potencial

        if yu - ymain <= self.cutoff:
            force_mag, potencial = self.force_LJ(epsilon_ave, sigma_ave, self.distance(xmain, ymain, xsec_real, yu))
            fX, fY = self.force_vec(xmain, ymain, xsec_real, yu, force_mag)
            forceX += fX
            forceY += fY
            totPotenc += potencial

        if np.abs(ymain - ysec) <= self.cutoff:
            force_mag, potencial = self.force_LJ(epsilon_ave, sigma_ave, self.distance(xmain, ymain, xsec_real, ysec))
            fX, fY = self.force_vec(xmain, ymain, xsec_real, ysec, force_mag)
            forceX += fX
            forceY += fY
            totPotenc += potencial
        return forceX, forceY, totPotenc

    def force_vec(self, xmain, ymain, xsec_real, ysec, force_mag):
            dx = xsec_real - xmain
            dy = ysec - ymain
            fX = dx * force_mag / np.sqrt(dx*dx + dy*dy)
            fY = dy * force_mag / np.sqrt(dx*dx + dy*dy)
            return fX, fY

    def distance(self, x1, y1, x2, y2):
        return np.sqrt(np.power(x1 - x2, 2) + np.power(y1 - y2, 2))

    def sigma_ave(self, sigma1, sigma2):
        return ((sigma1 + sigma2) / 2)
    
    def epsilon_ave(self, epsilon1, epsilon2):
        return (np.sqrt(epsilon1*epsilon2))
    
    def force_LJ(self, epsilon, sigma, distance):
        sig_over_r = sigma / distance
        const = -24* epsilon / sigma
        force = const * (2*np.power(sig_over_r, 13) - np.power(sig_over_r, 7))
        ###########################################################################################
        print(force, ' force\n', sigma, ' sigma\n', epsilon, ' epsilon\n', distance, ' distance\n')
        potencial = 4*epsilon*(np.power(sig_over_r, 12) - np.power(sig_over_r, 6))
        return force, potencial