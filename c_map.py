'''
maps a c library and how components relate to each other
'''

import os

def make_map(pathname,d):
	other_files = []
	for r, di, f in os.walk(pathname):
		for i in f:
			if i.endswith('.c') or i.endswith('.h') or i.endswith('.cpp'):
				rf = open(os.path.join(r,i),'r').readlines()
				for j in rf:
					if '#include' in j:
						if os.path.join(r,i) in d:
							d[os.path.join(r,i)].append(j)
						else:
							d[os.path.join(r,i)] = [j]
			else:
				other_files.append(os.path.join(r,i))
	d['other_files'] = other_files
	return d

if __name__ == "__main__":
	d = make_map('linux',{})
