# P7_LeRoy_Adrien
Project 7

Brute Force:
The bruteforce.py file shows unoptimized brute force code. It test all combinations (20 elements) and determine the best one for the best return over two years for a maximum spend of $ 500.

Best solution :
Total cost of actions : 500 $;
Two years return : 73.24 $;
List of actions taken: 
('name of the action', price, return in %, return in $)
('action-7', 22, 7, 1.54), ('action-8', 26, 11, 2.86), ('action-9', 48, 13, 6.24), ('action-10', 34, 27, 9.18), ('action-11', 42, 17, 7.14), ('action-12', 110, 9, 9.9), ('action-13', 38, 23, 8.74), ('action-14', 14, 1, 0.14), ('action-15', 18, 3, 0.54), ('action-18', 10, 14, 1.4), ('action-19', 24, 21, 5.04), ('action-20', 114, 18, 20.52).

Program executed in :  0.843238 Seconds

Optimized Dynamic:
The optimized_dynamic.py file shows a dynamic optimized code. It determine the best return over two years for a maximum spend of $ 500. It use the same 20 elements list than the brute force code.

Best solution :  
Total return : 99.08 $; 
Total cost of actions : 498 $;
List of actions taken : 
('name of the action', price, return in %, return in $)
('action-20', 114, 18, 20.52), ('action-19', 24, 21, 5.04), ('action-18', 10, 14, 1.4), ('action-13', 38, 23, 8.74), ('action-11', 42, 17, 7.14), ('action-10', 34, 27, 9.18), ('action-8', 26, 11, 2.86), ('action-6', 80, 25, 20.0), ('action-5', 60, 17, 10.2), ('action-4', 70, 20, 14.0).

Program executed in :  0.004809000000000001 Seconds


Optimized Greedy:
The optimized_greedy.py file shows a greedy optimized code. It determine the best return over two years for a maximum spend of $ 500. It use the same 20 elements list than the brute force code.

Best solution :  
Total return : 83.28 $; 
Total cost of actions: 500 $;
List of actions taken : 
('name of the action', price, return in $)
('action-1', 20, 1.0), ('action-2', 30, 3.0), ('action-3', 50, 7.5), ('action-4', 70, 14.0), ('action-5', 60, 10.2), ('action-6', 80, 20.0), ('action-7', 22, 1.54), ('action-8', 26, 2.86), ('action-9', 48, 6.24), ('action-10', 34, 9.18), ('action-11', 42, 7.14), ('action-14', 14, 0.14), ('action-17', 4, 0.48).

Program executed in :  0.00012699999999999864 Seconds


Optimized Dynamique:
The optimized_dynamic_csv.py file shows an dynamic optimized code. It read a file (~1000 elements) with actions information and determine the best combinations for the best return over two years for a maximum spend of $ 500.

Best solution for dataset 1:  
Total return : 198.54 $; 
Total cost of actions : 499.95 $;
List of actions taken : 
('name of the action', price in cents, return in %, return in $)
('Share-KMTG', 2321, 39.97, 9.28), ('Share-GHIZ', 2800, 39.89, 11.17), ('Share-NHWA', 2918, 39.77, 11.6), ('Share-UEZB', 2487, 39.43, 9.81), ('Share-LPDM', 3935, 39.73, 15.63), ('Share-MTLR', 1648, 39.97, 6.59), ('Share-USSR', 2562, 39.56, 10.14), ('Share-GTQK', 1540, 39.95, 6.15), ('Share-FKJW', 2108, 39.78, 8.39), ('Share-MLGM', 1, 18.86, 0.0), ('Share-QLMK', 1738, 39.49, 6.86), ('Share-WPLI', 3464, 39.91, 13.82), ('Share-LGWG', 3141, 39.5, 12.41), ('Share-ZSDE', 1511, 39.88, 6.03), ('Share-SKKC', 2487, 39.49, 9.82), ('Share-QQTU', 3319, 39.6, 13.14), ('Share-GIAJ', 1075, 39.9, 4.29), ('Share-XJMO', 939, 39.98, 3.75), ('Share-LRBZ', 3290, 39.95, 13.14), ('Share-KZBL', 2899, 39.14, 11.35), ('Share-EMOV', 889, 39.52, 3.51), ('Share-IFCP', 2923, 39.88, 11.66).

Program executed in :  12.805854 Seconds

Best solution for dataset 2:  
Total return : 197.95 $; 
Total cost of the actions : 499.9 $;
List of actions taken : 
('name of the action', price in cents, return in %, return in $)
('Share-ECAQ', 3166, 39.49, 12.5), ('Share-IXCI', 2632, 39.4, 10.37), ('Share-FWBE', 1830, 39.82, 7.29), ('Share-ZOFA', 2532, 39.78, 10.07), ('Share-PLLK', 1994, 39.91, 7.96), ('Share-LXZU', 424, 39.54, 1.68), ('Share-YFVZ', 2255, 39.1, 8.82), ('Share-ANFX', 3854, 39.72, 15.31), ('Share-PATS', 2770, 39.97, 11.07), ('Share-SCWM', 642, 38.1, 2.45), ('Share-NDKR', 3306, 39.91, 13.19), ('Share-ALIY', 2908, 39.93, 11.61), ('Share-JWGF', 4869, 39.93, 19.44), ('Share-JGTW', 3529, 39.43, 13.91), ('Share-FAPS', 3257, 39.54, 12.88), ('Share-VCAX', 2742, 38.99, 10.69), ('Share-LFXB', 1483, 39.79, 5.9), ('Share-DWSK', 2949, 39.35, 11.6), ('Share-XQII', 1342, 39.51, 5.3), ('Share-ROOM', 1506, 39.23, 5.91).

Program executed in :  7.143435 Seconds


Optimized Greedy:
The optimized_greedy_csv.py file shows an optimized greedy code. It read a file (~1000 elements) with actions information and determine the best combinations for the best return over two years for a maximum spend of $ 500.

Best solution for dataset 1:  
Total return : 101.86 $; 
Total cost of actions : 499.97 $;
List of actions taken : 
('name of the action', price, return in $)
('Share-DUPH', 10.01, 1.23), ('Share-GTAN', 26.04, 9.91), ('Share-USUF', 9.25, 2.56), ('Share-CFOZ', 10.64, 4.07), ('Share-QLRX', 15.72, 4.32), ('Share-HKFP', 23.97, 4.71), ('Share-PPPH', 24.06, 9.19), ('Share-HLJY', 26.98, 1.49), ('Share-CTCR', 16.6, 2.06), ('Share-LMJG', 16.54, 4.93), ('Share-IGUH', 19.13, 2.74), ('Share-VIRY', 31.94, 0.59), ('Share-PYDS', 34.9, 10.71), ('Share-SOOE', 23.09, 8.78), ('Share-NOIQ', 24.08, 8.86), ('Share-QUXB', 36.97, 13.34), ('Share-SJNY', 24.61, 4.29), ('Share-CQYF', 26.26, 0.17), ('Share-XJSP', 42.08, 1.28), ('Share-YNWM', 9.94, 2.81), ('Share-KTGN', 6.41, 1.63), ('Share-BVMS', 27.84, 1.26), ('Share-DAPD', 8.47, 0.56), ('Share-VLWV', 3.7, 0.14), ('Share-HITN', 0.67, 0.22), ('Share-DBUJ', 0.07, 0.01).

Program executed in :  0.002964999999999999 Seconds

Best solution for dataset 2:  
Total return : 86.52 $; 
Total cost of the actions : 499.5 $;
List of actions taken : 
('name of the action', price, return in $)
('Share-MOEX', 40.6, 6.78), ('Share-GBGY', 27.08, 9.23), ('Share-FJTI', 33.5, 6.97), ('Share-LGDP', 15.26, 0.52), ('Share-GEBJ', 5.87, 2.23), ('Share-GGNT', 33.39, 2.63), ('Share-TNOV', 34.54, 7.71), ('Share-CKCJ', 25.49, 2.64), ('Share-FUDY', 7.03, 1.4), ('Share-UZLL', 16.66, 3.23), ('Share-EMFC', 32.38, 9.86), ('Share-IZKC', 40.45, 0.32), ('Share-PWAT', 24.36, 2.35), ('Share-NWWZ', 45.76, 2.18), ('Share-AJGB', 28.6, 10.42), ('Share-SAPZ', 22.52, 2.69), ('Share-MNSA', 44.49, 10.13), ('Share-QBGQ', 19.63, 5.01), ('Share-DYVD', 0.28, 0.03), ('Share-DSOO', 1.49, 0.18), ('Share-LKSD', 0.12, 0.01).

Program executed in :  0.0023339999999999993 Seconds