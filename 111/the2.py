from math import *

def physics(a):
	a1=radians(float(a[0]))
	a2=radians(float(a[1]))
	a3=radians(float(180-a[0]-a[1]))	
	d=float(a[2])
	stat=float(a[3])
	kin=float(a[4])
	s=float(a[5])
	m1=float(a[6])
	m2=float(a[7])
	t1=float(a[8])
	t2=float(a[9])
	g=9.8
	
	f1=m1*sin(a1)*g
	f2=m2*sin(a2)*g
	s1=stat*m1*cos(a1)*g
	s2=stat*m2*cos(a2)*g
	k1=kin*m1*cos(a1)*g
	k2=kin*m2*cos(a2)*g
	h1=(d*sin(a2))/sin(a3)
	h2=(d*sin(a1))/sin(a3)
	
	#ip kesilince
	ivmeu1=(f1+k1)/m1
	ivmeu2=(f2+k2)/m2
	ivmed1=(f1-k1)/m1
	ivmed2=(f2-k2)/m2
	
	x1 = 0
	x2 = 0

#t1 sifirsa
	if t1==0 :
		x_1=h1-0.1-(s/2.0)
		x_2=h2-0.1-(s/2.0)

		if f1>s1:
			x1=x_1-(ivmed1*t2**2)/2.0
			if x1<0:
				x1=0

		else:
			x1=x_1
		
		if f2>s2: 
			x2=x_2-(ivmed2*t2**2)/2.0
			if x2<0:
				x2=0
		else:
			x2=x_2

		#print [x1,x2]
			#"trorltorotrotorotrotorlololol


#ip kesilmeden once hareket varsa
	if t1>0	:

		#f1>f2
		if f1>f2+s1+s2:
			ivme=(f1-f2-k1-k2)/(m1+m2)
			t3=(ivme*t1)/ivmeu2
			yol=(ivme*(t1**2))/2
			#ip yoldan uzunsa  ip kesilene kadar carpmiyor
			if (s/2)> yol :
				x_1=h1-0.1-s/2-yol
				x_2=h2-0.1-s/2+yol
				x1=x_1-(ivmed1*(t2**2))/2

				if x1<0:
					x1=0
				#else:
					#x1=x_1-(ivmed1*t2**2+2*ivme*t1*t2)/2
				#t2 yukari cikamadan bitebilir
				if t3<t2: # 
					if h2-x_2-0.1>(ivmeu2*(t3**2))/2: #cikarken makaraya carpmazsa
						x2=x_2+(ivmeu2*(t3**2))/2-(ivmed2*(t2-t3)**2)/2
						if x2<0:
							x2=0
					else:
						vs=(2*ivmeu2*(h2-x_2-0.1)+(ivme*t1)**2)**(1/2)
						t4=(ivme*t1-vs)/ivmeu2			
						x2=h2-0.1-(ivmed2*((t2-t4)**2))/2
						if x2<0:
							x2=0
				else:#hatali ekleme yap carpmak
					if h2-x_2-0.1> ((2*ivme*t1-ivmeu2*t2)*t2)/2:
						x2=x_2+((2*ivme*t1-ivmeu2*t2)*t2)/2
						if x2<0:
							x2=0
					else:
						vs=(2*ivmeu2*(h2-x_2-0.1)+(ivme*t1-ivmeu2*t2)**2)**(1/2)			
						t4=(ivme*t1-vs)/ivmeu2
						x2=h2-0.1-(ivmed2*((t2-t4)**2))/2
						if x2<0:
							x2=0
						
			#ip yola esitse
			elif (s/2)==yol:
				x_1=h1-0.1-s
				x_2=h2-0.1
				x1=x_1-((2*ivme*t1+ivmed1*t2)*t2)/2
				if x1<0:
					x1=0
				x2=x_2-(ivmed2*(t2**2))/2
				if x2<0:
					x2=0
			#ip kesilmeden once makaraya carptiysa
			else:#hatali surtunme
				if f1>s1:				
					x_1=h1-0.1-s
					x1=x_1-(ivmed1*(t2**2))/2
					if x1<0:
						x1=0
				else:
					x1=x_1
				if f2>s2:
					x_2=h2-0.1
					x2=x_2-(ivmed2*(t2**2))/2
					if x2<0:
						x2=0
				else:
					x2=h2-0.1
	#f2>f1
		elif f2>f1+s1+s2:
			ivme=(f2-f1-k1-k2)/(m1+m2)
			t3=(ivme*t1)/ivmeu2
			yol=(ivme*(t1**2))/2
			#ip yoldan uzunsa 
			if (s/2)> yol :
				x_1=h1-0.1-s/2+yol
				x_2=h2-0.1-s/2-yol
				x2=x_2-(ivmed2*(t2**2)+2*ivme*t1*t2)/2

				if x2<0:
					x2=0
				#else:
					#x1=x_1-(ivmed1*t2**2+2*ivme*t1*t2)/2
				#t2 yukari cikamadan bitebilir
				if t3<t2:
					if h1-x_1-0.1>(ivmeu1*(t3**2))/2: #cikarken makaraya carpmazsa
						x1=x_1+(ivmeu1*(t3**2))/2-(ivmed1*(t2-t3)**2)/2
						if x1<0:
							x1=0
					else:
						vs=(2*ivmeu1*(h1-x_1-0.1)+(ivme*t1)**2)**(1/2)
						t4=(ivme*t1-vs)/ivmeu1			
						x1=h1-0.1-(ivmed1*(t4**2))/2
						if x1<0:
							x1=0
				else:
					if h1-x_1-0.1> ((2*ivme*t1-ivmeu1*t2)*t2)/2:
						x1=x_1+((2*ivme*t1-ivmeu1*t2)*t2)/2
						if x1<0:
							x1=0
					else:
						vs=(2*ivmeu1*(h1-x_1-0.1)+(ivme*t1-ivmeu1*t2)**2)**(1/2)			
						t4=(ivme*t1-vs)/ivmeu1
						x2=h2-0.1-(ivmed1*((t2-t4)**2))/2
						if x1<0:
							x1=0

			#ip yola esitse
			elif (s/2)==yol:
				x_2=h2-0.1-s
				x_1=h1-0.1
				x2=x_2-((2*ivme*t1+ivmed2*t2)*t2)/2
				if x2<0:
					x2=0
				x1=x_1-(ivmed1*(t2**2))/2
				if x1<0:
					x1=0
			#ip kesilmeden once makaraya carptiysa
			else:
				if f1>s1:				
					x_1=h1-0.1
					x1=x_1-(ivmed1*(t2**2))/2
					if x1<0:
						x1=0
				else:
					x1=h1-0.1
				if f2>s2:
					x_2=h2-0.1-s
					x2=x_2-(ivmed2*(t2**2))/2
					if x2<0:
						x2=0
				else:
					x2=h2-0.1-s
		#f1=f2
		else: # f1-s1==f2-s2:
			x_1=h1-0.1-s/2
			x_2=h2-0.1-s/2
			if f1>s1:
				x1=x_1-(ivmed1*t2**2)/2.0
				if x1<0:
					x1=0
			else:
				x1=x_1
			if f2>s2:
				x2=x_2-(ivmed2*t2**2)/2.0
				if x2<0:
					x2=0
			else:
				x2=x_2		
						
	return [x1,x2]
	
	#print physics( input() )

