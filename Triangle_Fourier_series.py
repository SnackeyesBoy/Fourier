import numpy as np
import matplotlib.pyplot as plt

N = eval( input( "Please enter number of terms for partial sum: " ) )

t = np.linspace( -1, 1, 1000 )	# 定義時間陣列	

x = np.zeros( 1000 )			# 方波的傅立葉級數
for n in range( 1, N + 1 ):
	x += 8 / np.power( np.pi , 2 ) / np.power( 2*n-1, 2 )  * ( np.power( -1 , n-1 )) * np.sin( (2*n-1) * np.pi * t ) 
	
plt.plot( t, x )								
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )

plt.show( )