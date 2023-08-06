import numpy as np
from ..reactions import isotope
from ..misc import pallate,plt


class reaction(object):
	def __init__(self,reaction_name):
		pass
	def reaction_integral(self,E,phi,sig):
		# Trapezoidal Riemann sum
		E,phi,sig = np.array(E),np.array(phi),np.array(sig)
		phisig = phi*sig
		return np.sum(0.5*(E[1:]-E[:-1])*(phisig[:-1]+phisig[1:]))
	def flux_averaged_cross_section(self,E,phi,sig):
		return self.reaction_integral(E,phi,sig)/self.reaction_integral(E,phi,np.ones(len(E)))

class decay_chain(object):
	def __init__(self,parents,dc_threshold=0.0,units='s'):
		self.parents = [isotope(p) if type(p)==str else p for p in ([parents] if type(parents)==str else parents)]
		self.units,self.stems,self.children = units,[[] for p in self.parents],[{} for p in self.parents]
		for n,parent in enumerate(self.parents):
			if not parent.stable:
				par_prods = parent.decay_products(closest_SFY=True)
				self.children[n] = {istp:isotope(istp) for istp in par_prods}
				stems = [[{'ip':parent.name,'dc':0.0,'br':1.0}]+[{'ip':i,'dc':parent.decay_const(units=units),'br':par_prods[i]}] for i in par_prods]
				while len(stems)>0:
					new_stems = []
					for stem in stems:
						if stem[-1]['ip'] not in self.children:
							self.children[n][stem[-1]['ip']] = isotope(stem[-1]['ip'])
						if self.children[n][stem[-1]['ip']].stable:
							self.stems[n].append(stem)
						elif self.children[n][stem[-1]['ip']].decay_const(units=units)<=dc_threshold:
							self.stems[n].append(stem)
						else:
							ch_dp = self.children[n][stem[-1]['ip']].decay_products()
							if not ch_dp:
								self.stems[n].append(stem)
							for istp in ch_dp:
								dx = self.children[n][stem[-1]['ip']].decay_const(units=units)
								new_stems.append(stem+[{'ip':istp,'dc':(dx if dx!=stem[-1]['dc'] else 1.001*dx),'br':ch_dp[istp]}])
					stems = list(new_stems)
			mult = {ip:sum([1.0 for stem in self.stems[n] for s in stem if s['ip']==ip]) for ip in self.children[n]}
			mult[parent.name] = float(len(self.stems[n]))
			self.stems[n] = [decay_stem([s['ip'] for s in stem],np.array([s['dc'] for s in stem[1:]]+[0.0]),np.array([s['br']/mult[s['ip']] for s in stem])) for stem in self.stems[n]]
	def filter_name(self,istp):
		if istp[-1] in '0123456789g':
			return istp
		if istp.endswith('m'):
			return istp+'1'
		return istp+'g'
	def to_list(self,val):
		return [val for i in self.stems] if type(val) in [int,float,np.float64] or val is None else val
	def production_activity(self,istp,t=None,R=1.0):
		istp,R = self.filter_name(istp),self.to_list(R)
		if t is not None:
			return np.sum([stem.production_activity(istp,t,R[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
		return lambda T:np.sum([stem.production_activity(istp,T,R[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
	def decay_activity(self,istp,t=None,A0=1.0):
		istp,A0 = self.filter_name(istp),self.to_list(A0)
		if t is not None:
			return np.sum([stem.decay_activity(istp,t,A0[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
		return lambda T:np.sum([stem.decay_activity(istp,T,A0[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
	def production_population(self,istp,t=None,R=1.0):
		istp,R = self.filter_name(istp),self.to_list(R)
		if t is not None:
			return np.sum([stem.production_population(istp,t,R[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
		return lambda T:np.sum([stem.production_population(istp,T,R[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
	def decay_population(self,istp,t=None,N0=1.0):
		istp,N0 = self.filter_name(istp),self.to_list(N0)
		if t is not None:
			return np.sum([stem.decay_population(istp,t,N0[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
		return lambda T:np.sum([stem.decay_population(istp,T,N0[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
	def decay_emissions(self,istp,t_start=0.0,t_stop=None,A0=1.0,N0=None):
		istp,A0,N0 = self.filter_name(istp),self.to_list(A0),self.to_list(N0)
		if t_stop is not None:
			return np.sum([stem.decay_emissions(istp,t_start,t_stop,A0[n],N0[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
		return lambda T_start,T_stop:np.sum([stem.decay_emissions(istp,T_start,T_stop,A0[n],N0[n]) for n,stems in enumerate(self.stems) for stem in stems if istp in stem.isotopes],axis=0)
	def plot(self,kind,activity_units='Bq',logscale=False,saveas=None,**kwargs):
		clr = pallate()
		f,ax = plt.subplots()
		func = {'production_activity':self.production_activity,'decay_activity':self.decay_activity,'production_population':self.production_population,'decay_population':self.decay_population,'decay_emissions':self.decay_emissions}[kind]
		time = np.array(kwargs['t_stop']) if kind=='decay_emissions' else np.array(kwargs['t'])
		clrs,lss,min_plot = [clr[i] for i in clr],['-','--','-.',':'],(1E-20 if logscale else 0.0)
		all_itps = list(set([p.name for p in self.parents]+[c for children in self.children for c in children if not (children[c].stable and kind.endswith('activity'))]))
		TeX = {itp.name:itp.TeX() for itp in self.parents+[children[c] for children in self.children for c in children]}
		ydat = [func(i,**kwargs) for i in all_itps]
		labels = [i[1] for i in sorted([(max(y),n) for n,y in enumerate(ydat)],key=lambda k:k[0],reverse=True)]
		for m,n in enumerate(labels):
			ax.plot(time[np.where(ydat[n]>=min_plot)],ydat[n][np.where(ydat[n]>=min_plot)],color=clrs[m%len(clrs)],ls=lss[n%4],label=(TeX[all_itps[n]] if n in labels[:12] else None))
		ax.set_xlabel('Time ('+self.units+')')
		ax.set_ylabel('Isotope '+kind.split('_')[1].title()+(' ('+activity_units+')' if kind.endswith('activity') else ''))
		if logscale:
			ax.set_yscale('log')
		f.tight_layout()
		ax.legend(loc=0)
		if saveas is None:
			plt.show()
		else:
			f.savefig(saveas)
			plt.close()


class decay_stem(object):
	def __init__(self,isotopes,decay_consts,branch_ratios):
		self.isotopes,self.decay_consts,self.branch_ratios = isotopes,decay_consts,branch_ratios
		self.lm_threshold = 1E-12
	def filter_name(self,istp):
		if istp[-1] in '0123456789g':
			return istp
		if istp.endswith('m'):
			return istp+'1'
		return istp+'g'
	def production_activity(self,istp,t=None,R=1.0):
		idx = self.isotopes.index(self.filter_name(istp))
		if t is not None:
			return self.decay_consts[idx]*self.production_population(istp,t,R)
		return lambda T:self.decay_consts[idx]*self.production_population(istp,T,R)
	def decay_activity(self,istp,t=None,A0=1.0):
		idx = self.isotopes.index(self.filter_name(istp))
		r = 1.0/self.decay_consts[0] if self.decay_consts[0]>0 else 1.0
		if t is not None:
			return self.decay_consts[idx]*self.decay_population(istp,t,A0*r)
		return lambda T:self.decay_consts[idx]*self.decay_population(istp,T,A0*r)
	def production_population(self,istp,t=None,R=1.0):
		idx = self.isotopes.index(self.filter_name(istp))
		ridx = range(idx+1)
		mult = R*(self.branch_ratios[0] if idx==0 else 1.0)*np.prod((self.branch_ratios[1:idx+1],self.decay_consts[:idx]))
		denom = np.array([l if l>self.lm_threshold else 1.0 for l in self.decay_consts[ridx]])*np.array([np.prod(self.decay_consts[ridx[:j]]-self.decay_consts[j])*np.prod(self.decay_consts[ridx[j+1:]]-self.decay_consts[j]) for j in ridx])
		if t is not None:
			return mult*np.sum([((1.0-np.exp(-self.decay_consts[j]*t)) if self.decay_consts[j]>self.lm_threshold else t)/denom[j] for j in ridx],axis=0)
		return lambda T:mult*np.sum([((1.0-np.exp(-self.decay_consts[j]*T)) if self.decay_consts[j]>self.lm_threshold else T)/denom[j] for j in ridx],axis=0)
	def decay_population(self,istp,t=None,N0=1.0):
		idx = self.isotopes.index(self.filter_name(istp))
		ridx = range(idx+1)
		mult = N0*(self.branch_ratios[0] if idx==0 else 1.0)*np.prod((self.branch_ratios[1:idx+1],self.decay_consts[:idx]))
		denom = np.array([np.prod(self.decay_consts[ridx[:j]]-self.decay_consts[j])*np.prod(self.decay_consts[ridx[j+1:]]-self.decay_consts[j]) for j in ridx])
		if t is not None:
			return mult*np.sum([np.exp(-self.decay_consts[j]*t)/denom[j] for j in ridx],axis=0)
		return lambda T:mult*np.sum([np.exp(-self.decay_consts[j]*T)/denom[j] for j in ridx],axis=0)
	def decay_emissions(self,istp,t_start=0.0,t_stop=None,A0=1.0,N0=None):
		idx = self.isotopes.index(self.filter_name(istp))
		if any(self.decay_consts[:idx+1]<self.lm_threshold):
			if t_stop is not None:
				return 0.0*t_stop
			return lambda T_start,T_stop:0.0*T_stop
		ridx = range(idx+1)
		mult = (A0*self.decay_consts[idx]/self.decay_consts[0] if N0 is None else N0*decay_consts[idx])*np.prod((self.branch_ratios[1:idx+1],self.decay_consts[:idx])) 
		denom = np.array([self.decay_consts[j]*np.prod(self.decay_consts[ridx[:j]]-self.decay_consts[j])*np.prod(self.decay_consts[ridx[j+1:]]-self.decay_consts[j]) for j in ridx])
		if t_stop is not None:
			return mult*np.sum([(np.exp(-self.decay_consts[j]*t_start)-np.exp(-self.decay_consts[j]*t_stop))/denom[j] for j in ridx],axis=0)
		return lambda T_start,T_stop:mult*np.sum([(np.exp(-self.decay_consts[j]*T_start)-np.exp(-self.decay_consts[j]*T_stop))/denom[j] for j in ridx],axis=0)
