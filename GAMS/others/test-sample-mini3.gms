Sets
       n plant i
       / NAmerica, SAmerica, Europe /
       m market j
       / NAmerica, SAmerica, Europe /
       
;

Parameter
       Dj(m) demand from market j
       / NAmerica 12, SAmerica 8, Europe 14 /
       Ki(n) capacity of plant i
       / NAmerica 10, SAmerica 10, Europe 13 /
       fi(n) fixed cost of plant i
       / NAmerica 6000, SAmerica 4500, Europe 4500 /
;


table cij(n,m) wholesaler vehicle
                    NAmerica   SAmerica   Europe
        NAmerica       81         92       101
        SAmerica      117         77       108
        Europe        102        105        95
;


free variables
     z;

Variables
     
     xij(n,m);

binary variables     
     yi(n);

Equations
     cost
     eqn1(m)
     eqn2(n)
     eqn3(n,m);


cost..    z  =e= sum(n,fi(n)*yi(n)) + sum(n,sum(m,cij(n,m)*xij(n,m)));
eqn1(m).. sum(n,xij(n,m)) =e= Dj(m);
eqn2(n).. sum(m,xij(n,m)) =l= Ki(n)*yi(n);
eqn3(n,m).. xij(n,m) =g= 0;


Model supplychainmodel /all/ ;

Solve supplychainmodel using MIP minimizing z ;