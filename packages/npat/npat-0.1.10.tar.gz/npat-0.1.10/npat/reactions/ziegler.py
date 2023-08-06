import os,sqlite3,numpy as np
from scipy.interpolate import interp1d
from npat.misc.plotter import plotter,plt
from npat.misc.dbmgr import get_ziegler_cursor
from npat.reactions.isotope import isotope
# _db_connection = sqlite3.connect('/'.join(os.path.realpath(__file__).split('/')[:-2])+'/data/atomic_data/ziegler.db')
# _db = _db_connection.cursor()


class ziegler(object):
	def __init__(self,stack=[],beam_istp='1H'):
		### stack is list of dicts, which must have 'compound', 'sample' and either 'ad' (mg/cm^2) or both 'density' (g/cm^3) and 'thickness' (mm)
		# self.db_connection = _db_connection
		self.db = get_ziegler_cursor()
		self.beam_istp = isotope(beam_istp)
		self.Z_beam,self.amu_beam = self.beam_istp.Z,self.beam_istp.amu
		self.protons = {int(i[0]):map(float,i[1:]) for i in self.db.execute('SELECT * FROM protons')}
		self.helium = {int(i[0]):map(float,i[1:]) for i in self.db.execute('SELECT * FROM helium')}
		self.ionization = {int(i[0]):map(float,i[1:]) for i in self.db.execute('SELECT * FROM ionization')}
		self.weights = {int(i[0]):[float(i[1]),float(i[2])] for i in self.db.execute('SELECT * FROM weights')}
		self.compounds = {str(i[0]):[[int(h.split(':')[0]),float(h.split(':')[1])] for h in i[2].split(',')] for i in self.db.execute('SELECT * FROM compounds')}
		self.compounds = {cm:[[i[0],i[1]/sum([m[1] for m in self.compounds[cm]])] for i in self.compounds[cm]] for cm in self.compounds}
		self.densities = {str(i[0]):float(i[1]) for i in self.db.execute('SELECT * FROM compounds')}
		self.stack = stack
		for s in self.stack:
			if 'ad' not in s:
				if 'density' in s:
					s['ad'] = 100.0*s['density']*s['thickness']
				elif s['compound'] in self.densities:
					s['ad'],s['density'] = 100.0*self.densities[s['compound']]*s['thickness'],self.densities[s['compound']]
			if 'density' not in s:
				s['density'] = self.densities[s['compound']]
				if 'thickness' not in s and 'ad' in s:
					s['thickness'] = s['ad']/(100.0*s['density'])
			if s['compound'] in self.compounds:
				if 'sample' not in s:
					s['sample'] = s['compound']
				#units: atoms/barn
				s['nd'] = s['density']*(0.1*s['thickness'])*6.022E-1/np.average([self.weights[z[0]][0] for z in self.compounds[s['compound']]],weights=[z[1] for z in self.compounds[s['compound']]])
		self.stack_solution = {}
		self.pallate = plotter().pallate()
	def add_compounds(self,densities=[],compounds=[]):
		if type(compounds)==dict:
			compounds = [compounds]
		if type(densities)==dict:
			densities = [densities]
		for cm in compounds:
			if cm not in self.compounds:
				self.db.execute('INSERT INTO compounds VALUES(?,?,?)',(cm,densities[cm],','.join([':'.join(map(str,c)) for c in compounds[cm]])))
				self.compounds[cm] = compounds[cm]
				self.densities[cm] = densities[cm]
		self.db_connection.commit()
	def get_S(self,E,z2,M2=None):
		# energy E in MeV , stopping power in MeV/(mg/cm2)
		E = np.array(E)
		M2 = M2 if M2 is not None else self.weights[z2][0]
		if self.Z_beam==1:
			return (0.6022140857/M2)*(self.get_S_nucl(E,self.Z_beam,self.amu_beam,z2,self.weights[z2][0])+self.get_S_p(E,z2,self.amu_beam))
		elif self.Z_beam==2:
			return (0.6022140857/M2)*(self.get_S_nucl(E,self.Z_beam,self.amu_beam,z2,self.weights[z2][0])+self.get_S_He(E,z2,self.amu_beam))
		return (0.6022140857/M2)*(self.get_S_nucl(E,self.Z_beam,self.amu_beam,z2,self.weights[z2][0])+self.get_S_elec(E,z2,self.amu_beam,self.Z_beam))
	def get_S_nucl(self,E,z1,m1,z2,m2):
		RM = (m1+m2)*np.sqrt((z1**(2/3.0)+z2**(2/3.0)))
		ER = 32.53*m2*1E3*E/(z1*z2*RM)
		return (0.5*np.log(1.0+ER)/(ER+0.10718+ER**0.37544))*8.462*z1*z2*m1/RM
	def get_S_p(self,E,z2,M1=1.00727647):
		S = np.zeros(len(E))
		E = 1E3*E/M1
		A = self.protons[z2]
		beta_sq = np.where(E>=1E3,1.0-1.0/(1.0+E/931478.0)**2,0.9)
		B0 = np.where(E>=1E3,np.log(A[6]*beta_sq/(1.0-beta_sq))-beta_sq,0.0)
		Y = np.log(E[(1E3<=E)&(E<=5E4)])
		B0[np.nonzero(np.where((1E3<=E)&(E<=5E4),B0,0))] -= A[7]+A[8]*Y+A[9]*Y**2+A[10]*Y**3+A[11]*Y**4
		S[E>=1E3] = (A[5]/beta_sq[E>=1E3])*B0[E>=1E3]
		S_low = A[1]*E[(10<=E)&(E<1E3)]**0.45
		S_high = (A[2]/E[(10<=E)&(E<1E3)])*np.log(1.0+(A[3]/E[(10<=E)&(E<1E3)])+A[4]*E[(10<=E)&(E<1E3)])
		S[(10<=E)&(E<1E3)] = S_low*S_high/(S_low+S_high)
		S[(0<E)&(E<10)] = A[0]*E[(0<E)&(E<10)]**0.5
		return S
	def get_S_He(self,E,z2,M1=4.003):
		S = np.zeros(len(E))
		E = E*4.0015/M1
		E = np.where(E>=0.001,E,0.001)
		A = self.helium[z2]
		S_low = A[0]*(1E3*E[E<=10])**A[1]
		S_high = (A[2]/E[E<=10])*np.log(1.0+(A[3]/E[E<=10])+A[4]*E[E<=10])
		S[E<=10] = S_low*S_high/(S_low+S_high)
		Y = np.log(1.0/E[E>10])
		S[E>10] = np.exp(A[5]+A[6]*Y+A[7]*Y**2+A[8]*Y**3)
		return S
	def get_S_elec(self,E,z2,M1,z1):
		S = np.zeros(len(E))
		E_keV = 1E3*E
		S[E_keV/M1<1000] = self.get_eff_Z_ratio(E_keV[E_keV/M1<1000],z1,M1)**2*self.get_S_p(E[E_keV/M1<1000],z2,M1)
		Y = E_keV[E_keV/M1>=1000]/M1
		beta_sq = 1.0-1.0/(1.0+Y/931478.0)**2
		FX = np.log(2E6*0.511003*beta_sq/(1.0-beta_sq))-beta_sq
		ZHY = 1.0-np.exp(-0.2*np.sqrt(Y)-0.0012*Y-0.00001443*Y**2)
		Z1EFF = self.get_eff_Z_ratio(E_keV[E_keV/M1>=1000],z1,M1)*ZHY
		S[E_keV/M1>=1000] = 4E-1*np.pi*(1.9732857/137.03604)**2*Z1EFF**2*z2*(FX-np.log(self.ionization[z2][0]))/(0.511003*beta_sq)
		return S
	def get_eff_Z_ratio(self,E_keV,z1,M1):
		if z1==1:
			return np.ones(len(E))
		elif z1==2:
			Y = np.log(E_keV/M1)
			return z1*(1.0-np.exp(-0.7446-0.1429*Y-0.01562*Y**2+0.00267*Y**3-0.000001325*Y**8))
		elif z1==3:
			Y = E_keV/M1
			return z1*(1.0-np.exp(-0.7138-0.002797*Y-0.000001348*Y**2))
		BB = -0.886*np.sqrt(0.04*E_keV/M1)/z1**(2/3.0)
		return z1*(1.0-np.exp(BB-0.0378*np.sin(0.5*np.pi*BB))*(1.034-0.1777*np.exp(-0.08114*z1)))
	def get_dEdx(self,E,cm,M2=None):
		# E in MeV
		return sum([wt[1]*self.get_S(E,wt[0],M2) for wt in self.compounds[cm]])
	def solve_dE_stack(self,E0,dp=1.0):
		E,E0 = [],np.array(E0)
		for st in self.stack:
			Ein = E0
			M2 = M2 if 'M2' in st else None
			S1 = self.get_dEdx(E0,st['compound'],M2)
			E1 = E0 - dp*st['ad']*S1
			E1 = np.where(E1>0,E1,0.0)
			E0 = E0 - 0.5*dp*st['ad']*(S1+self.get_dEdx(E1,st['compound'],M2))
			E0 = np.where(E0>0,E0,0.0)
			E.append(0.5*(E0+Ein))
		return [np.where(e>=0,e,0.0) for e in E]
	def solve_dEdx_AZMC(self,E0=33.0,dE0=0.3,N=1000,dp=1.0):
		ss = 'E0'+str(E0)+'dE0'+str(dE0)+'N'+str(int(N))+'dp'+str(dp)
		if ss in self.stack_solution:
			return self.stack_solution[ss]
		samples = [s['sample'] for s in self.stack]
		energies = np.array(self.solve_dE_stack(np.random.normal(loc=E0,scale=dE0,size=int(N)),dp=dp))
		histos = [np.histogram(E,bins='auto') for E in energies]
		self.stack_solution[ss] = [{'sample':samples[n],'energy':0.5*(hist[1][1:]+hist[1][:-1]),'flux':hist[0],'edges':hist[1]} for n,hist in enumerate(histos)]
		return self.stack_solution[ss]
	def filter_stack_solution(self,samples,E0=33.0,dE0=0.3,N=1000,dp=1.0):
		return [s for s in self.solve_dEdx_AZMC(E0,dE0,N,dp) if s['sample'] in samples]
	def filter_stack(self,samples):
		if type(samples)==str:
			samples = [samples]
		return [s for s in self.stack if s['sample'] in samples]
	def reaction_integral(self,E,phi,sig):
		# Trapezoidal Riemann sum
		E,phi,sig = np.array(E),np.array(phi),np.array(sig)
		phisig = phi*sig
		return np.sum(0.5*(E[1:]-E[:-1])*(phisig[:-1]+phisig[1:]))
	def flux_interpolation(self,sample,E0=33.0,dE0=0.3,N=1000,dp=1.0):
		s = self.filter_stack_solution([sample],E0,dE0,N,dp)[0]
		return interp1d(s['energy'],s['flux'],bounds_error=False,fill_value=0.0)
	def plot_stopping_power_Z(self,Z):
		f,ax = plt.subplots()
		E_range = 10**(np.arange(-2,4,0.01))
		ax.plot(E_range,zg.get_S(E_range,Z),lw=2.0,color='#2c3e50',label='dE/dx(Z='+str(Z)+')')
		ax.set_yscale('log')
		ax.set_xscale('log')
		ax.set_ylabel(r'Stopping Power [MeV/(mg/cm$^2$)]')
		ax.set_xlabel('Energy [MeV]')
		ax.legend(loc=0)
		f.tight_layout()
		plt.show()
	def plot_flux(self,samples,E0=33.0,dE0=0.3,N=1000,dp=1.0,saveas=None):
		f,ax = plt.subplots()
		for sm in self.filter_stack_solution(samples,E0,dE0,N,dp):
			edges,flux = sm['edges'],sm['flux']
			ax.plot(np.array([edges[:-1],edges[1:]]).T.flatten(),np.array([flux,flux]).T.flatten(),label=sm['sample'])
		ax.set_yscale('log')
		ax.set_xlabel('Energy (MeV)',fontsize=18)
		ax.set_ylabel('Flux (a.u.)',fontsize=18)
		ax.legend(loc=0)
		f.tight_layout()
		if saveas is None:
			plt.show()
		else:
			f.savefig(saveas)
			plt.close()

if __name__=="__main__":
	zg = ziegler(stack=[{'compound':'Ni','thickness':0.025},{'compound':'Ti','thickness':0.025},{'compound':'U','thickness':1.0}],beam_istp='2H')
	# zg.plot_stopping_power_Z(28)
	# print zg.solve_dEdx_AZMC(N=1E5)
	zg.plot_flux(['U','Ni','Ti'],E0=12.0)
