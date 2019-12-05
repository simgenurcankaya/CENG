def mateval (lst):
	def  kesir(lst):
		
		if type(lst) == list:
			if len(lst) == 2 :
				
				if type(lst[0]) == int and type(lst[1]) == int:
					return True
				else:
					return False
		
			else:
				return False
		else:
			return False

	def matris(lst):
		
		if type(lst) == list:
			if kesir(lst) == False :
				for i in  range (len(lst)):
					if type(lst[i]) != list:

						return False
				return True
			
		else:
			return False
	def sadeles(lst):
		
		#sadece ksirler[x,y]
		if kesir(lst) == True:
			x=lst[0]
			y=lst[1]
			if y==1 :
				return x
			if x%y == 0:
				return x/y
			else:
				lst=[(lst[0]/gcd(x, y)),(lst[1]/gcd(x, y))]	
				
				return	lst

	def gcd(x, y):
		while y != 0:
			(x, y) = (y, x % y)
		return x	

	def toplama(lst):
		
		eleman_sayi = len(lst)
		if eleman_sayi > 1:
			
			for i in range (eleman_sayi):
				
				if type (lst[i]) == list :
					
					if type (lst[i][0]) == str:
						if i == 0:
							
							return toplama([mateval(lst[0])]+lst[1:])
						
						elif i > 0 and i != eleman_sayi:
							return toplama(lst[:i]+[mateval(lst[i])]+lst[i+1:])
						
						elif i > 0 and i == eleman_sayi:
							
							return toplama(lst[:i]+[mateval(lst[i])])
						
						#WHILE lst[i]=mateval(lst[i])
			#####3## hata showwwww
							
					if type (lst[i][0]) == list: #matris toplama #hicbir sikinti yok
						a = lst[0]
						b = lst[1]
						if len(lst) == 1:
							return lst
							
						if len(lst) > 1:
							res = []
							for satir in range(len(a)):
								row = []
								for sutun in range(len(a[0])):
									row.append(toplama([a[satir][sutun],b[satir][sutun]]))	
								res.append(row)
							#return toplama([res]+lst[2:])
						
						if lst[2:] == []:
							return res
						if len(lst[2:]) > 0:
					
							return toplama([res]+lst[2:])

					if kesir(lst[0])== True and kesir(lst[1]) ==True : #kesir	
						a = lst[0]
						b = lst[1]
						res = [0,0]
						res[0]=((a[0]*b[1])+(b[0]*a[1]))
						res[1]=(a[1]*b[1])
						res = sadeles(res)
						return toplama([res]+lst[2:])
				#kesir+int
					if kesir(lst[0]) == True and type(lst[1])== int:
						
						a = lst[0]
						b = lst[1]
						res= [0,0]
						res[0]=(a[0]+(a[1]*b))
						res[1]=(a[1])
						res= sadeles(res)
						return toplama([res]+lst[2:])


				if type(lst[0]) == int and type(lst[1]) == int:  #integer toplama calisiyor
					toplam = lst[0]+lst[1]
					return toplama([toplam]+lst[2:])

				if kesir(lst[0]) == True and kesir(lst[1]) == True : #kesir	
					
					a = lst[0]
					b = lst[1]
					res = [0,0]
					res[0]=((a[0]*b[1])+(b[0]*a[1]))
					res[1]=(a[1]*b[1])
					res = sadeles(res)
					return toplama([res]+lst[2:])
					#int+kesir
				if type(lst[0]) == int and kesir(lst[1]) == True:
					
					a = lst[0]
					b = lst[1]
					res = [0,0]
					res[0]=((a*b[1])+b[0])
					res[1]=(b[1])
					res = sadeles(res)
					return toplama([res]+lst[2:])

		if eleman_sayi == 1 and len(lst) == 1:
			return lst[0]

		elif eleman_sayi == 1:
			return lst

	def cikarma(lst):
		
		x=lst[0]
		y=lst[1]
		
		if type(x) == list and type(x[0]) == str:
			x = mateval(x)
		if type(y) == list and type(y[0]) == str:
			y = mateval(y)
		
		#int-int
		if type(x) == int and type(y) == int:
					return x-y

		elif kesir(x)== True and kesir(y) ==True : #kesir-kesir	
			res = [0,0]
			res[0]=((x[0]*y[1])-(y[0]*x[1]))
			res[1]=(x[1]*y[1])
			res = sadeles(res)
			return res
				#kesir-int
		elif kesir(x) == True and type(y)== int:
			res=[0,0]
			res[0]=(x[0]-(x[1]-y))
			res[1]=(x[1])
			res = sadeles(res)
			return res
		#int-kesir
		elif type(x) == int and kesir(y) ==True:
			res=[0,0]
			res[0]=(x*y[1])-y[0]
			res[1]=y[1]
			res = sadeles(res)
			return res
			#matris-matris
		elif matris(x)== True and matris(y)== True :
			res=[]
			for satir in range(len(x)):
				row =[]
				for sutun in range(len(x[0])):		
					row.append(cikarma([x[satir][sutun],y[satir][sutun]]))
					res.append(row)
				return res	

	def carpma(lst):
		
		eleman_sayi=len(lst)
		if eleman_sayi == 1 and len(lst) == 1:
			return lst[0]

		elif eleman_sayi == 1:
			return lst

		elif (eleman_sayi)>1:
			
			for i in range (eleman_sayi):
				
				if type (lst[i]) == list :
					#icinde islem varsa
					
					if type (lst[i][0]) == str:
						if i == 0:
							
							return carpma([mateval(lst[0])]+lst[1:])
						
						elif i > 0 and i != eleman_sayi:
							return carpma(lst[:i]+[mateval(lst[i])]+lst[i+1:])
						
						elif i > 0 and i == eleman_sayi:
							
							return carpma(lst[:i]+[mateval(lst[i])])


							#kesir*kesir
			if kesir(lst[0]) == True and kesir(lst[1]):
				a = lst[0]
				b = lst[1]						
				res = [0,0]
				res[0]=(a[0]*b[0])
				res[1]=(a[1]*b[1])
				res =sadeles(res)
				return carpma([res]+lst[2:])
					#kesir*sayi
			if kesir(lst[0]) == True and type(lst[1]) == int:
				a = lst[0]
				b = lst[1]
				res = [0,0]
				res[0]=(a[0]*b)
				res[1]=a[1]
				res =sadeles(res)
				return carpma([res]+lst[2:])

			

						#	kesir * matris
			if kesir(lst[0]) == True and matris(lst[1]) == True:
				
				i=lst[0]
				mtrx=lst[1]
			
				carpim = [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
				return carpma([carpim]+lst[2:])
			
			

					#matris*matris	
			if matris(lst[0]) == True and matris(lst[1]) == True:
				A=lst[0]
				B=lst[1]
			
				satir_a = len(A)
				sutun_a = len(A[0])
				satir_b = len(B)
				sutun_b = len(B[0])
						# ici doldurulack matris
				C = [[0 for satir in range(satir_b)] for sutun in range(satir_a)]
				#BU NEEEEEEEEEEEEEEEEEEEEEEEEEEE
				for i in range(satir_a):
					for j in range(sutun_b):
						for k in range(sutun_a):
						
							C[i][j] = toplama([C[i][j],carpma([A[i][k],B[k][j]])])
				
				#return C
				
				if lst[2:] == []:
					return C
				if len(lst[2:][0]) > 0:
					
					return carpma([C,lst[2:][0]])
				
				###########HATALI CARPMAYI SADECE INTEGER YAPIYO VE TOPLAMAYIDA ########

						#matris*sayi
			if matris(lst[0]) == True and type(lst[1])==int:
				mtrx=(lst[0])
				i=lst[1]
							    
				carpim= [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
				return carpma([carpim]+lst[2:])

					#matris*kesir
			if matris(lst[0]) == True and kesir(lst[1]) == True:
				i=lst[1]
				mtrx=lst[0]
				carpim = [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
				return carpma([carpim]+lst[2:])


								#int*int
			if type(lst[0]) == int and type(lst[1]) == int :
				carpim = lst[0]*lst[1] 
						
				return carpma([carpim]+lst[2:])
					#sayi*kesir
			if type(lst[0]) == int and kesir(lst[1]) == True:
						
				a = lst[0]
				b = lst[1]
				res = [0,0]
				res[0]=(a*b[0])
				res[1]=(b[1])
				res =sadeles(res)
						
				return carpma([res]+lst[2:])
				#kesir*sayi
			if kesir(lst[0]) == True and type(lst[1]) == int:
				a = lst[0]
				b = lst[1]
				res = [0,0]
				res[0]=(a[0]*b)
				res[1]=a[1]
				res =sadeles(res)
				return carpma([res]+lst[2:])
				#int*matris
			if type(lst[0]) == int and matris(lst[1]) == True:
				i=lst[0]
				mtrx=lst[1]
				carpim= [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
				return carpma([carpim]+lst[2:])
				
					






		

					#kesir*kesir
		if kesir(lst[0]) == True and kesir(lst[1]):
			a = lst[0]
			b = lst[1]						
			res = [0,0]
			res[0]=(a[0]*b[0])
			res[1]=(a[1]*b[1])
			res =sadeles(res)
			return carpma([res]+lst[2:])
				#kesir*sayi
		if kesir(lst[0]) == True and type(lst[1]) == int:
			a = lst[0]
			b = lst[1]
			res = [0,0]
			res[0]=(a[0]*b)
			res[1]=a[1]
			res =sadeles(res)
			return carpma([res]+lst[2:])

		

					#	kesir * matris
		if kesir(lst[0]) == True and matris(lst[1]) == True:
			
			i=lst[0]
			mtrx=lst[1]
			
			carpim = [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
			return carpma([carpim]+lst[2:])
		
		

				#matris*matris	
		if matris(lst[0]) == True and matris(lst[1]) == True:
			A=lst[0]
			B=lst[1]
			
			satir_a = len(A)
			sutun_a = len(A[0])
			satir_b = len(B)
			sutun_b = len(B[0])
					# ici doldurulack matris
			C = [[0 for satir in range(satir_b)] for sutun in range(satir_a)]
			#BU NEEEEEEEEEEEEEEEEEEEEEEEEEEE
			for i in range(satir_a):
				for j in range(sutun_b):
					for k in range(sutun_a):
						
						C[i][j] = toplama([C[i][j],carpma([A[i][k],B[k][j]])])
			
			#return C
			if lst[2:] == []:
					return C
			if len(lst[2:][0]) > 0:
					
				return carpma([C,lst[2:][0]])
			###########HATALI CARPMAYI SADECE INTEGER YAPIYO VE TOPLAMAYIDA ########

					#matris*sayi
		if matris(lst[0]) == True and type(lst[1])==int:
			mtrx=(lst[0])
			i=lst[1]
						    
			carpim= [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
			return carpma([carpim]+lst[2:])

				#matris*kesir
		if matris(lst[0]) == True and kesir(lst[1]) == True:
			i=lst[1]
			mtrx=lst[0]
			carpim = [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
			return carpma([carpim]+lst[2:])


							#int*int
		if type(lst[0]) == int and type(lst[1]) == int :
			carpim = lst[0]*lst[1] 
					
			return carpma([carpim]+lst[2:])
				#sayi*kesir
		if type(lst[0]) == int and kesir(lst[1]) == True:
					
			a = lst[0]
			b = lst[1]
			res = [0,0]
			res[0]=(a*b[0])
			res[1]=(b[1])
			res =sadeles(res)
					
			return carpma([res]+lst[2:])
			#kesir*sayi
		if kesir(lst[0]) == True and type(lst[1]) == int:
			a = lst[0]
			b = lst[1]
			res = [0,0]
			res[0]=(a[0]*b)
			res[1]=a[1]
			res =sadeles(res)
			return carpma([res]+lst[2:])
			#int*matris
		if type(lst[0]) == int and matris(lst[1]) == True:
			i=lst[0]
			mtrx=lst[1]
			carpim= [[carpma([eleman,i]) for eleman in satir] for satir in mtrx]
			return carpma([carpim]+lst[2:])
			



		
###################################################################
	#mateval fonksiyonu
	for i in range (len(lst)-1):
		if type(lst[0]) == str:
		
			if lst[0] == "+":
				
				return toplama(lst[1:])
			elif lst[0] == "-":
				
				return cikarma(lst[1:])
			elif lst[0] == "*":
			
				return carpma(lst[1:])	

		if type(lst[i]) == list:
			if type(lst[i][0]) == str:
				return mateval(lst[i])				
		return lst
	

	

