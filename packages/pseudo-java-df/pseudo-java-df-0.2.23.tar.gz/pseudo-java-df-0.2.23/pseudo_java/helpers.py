def w_type(self,s):
		try:
			return(int(s))
		except ValueError:
			try:
				return float(s)
			except ValueError:
				return s.strip('\"')
	
