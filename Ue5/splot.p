unset logscale x
splot 'C:\Users\Köcki\Desktop\samelcountainer\uni\experimente\git\Ue5\Spektraltest_c.txt' using 1:2:3
pause -1
splot 'C:\Users\Köcki\Desktop\samelcountainer\uni\experimente\git\Ue5\Spektraltest_Randu.txt' using 1:2:3
pause -1
set logscale x 10
plot 'C:\Users\Köcki\Desktop\samelcountainer\uni\experimente\git\Ue5\f_integral.txt' with linespoints
pause -1
unset logscale x
plot 'C:\Users\Köcki\Desktop\samelcountainer\uni\experimente\git\Ue5\vol_integral.txt' with linespoints