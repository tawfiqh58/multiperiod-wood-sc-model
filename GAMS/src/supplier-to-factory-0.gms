Sets
    a supplier index
    / 1, 2/
;

Parameters
    Ta(a)
    / 1 10, 2 11 /
    
    Hd
    / 10 /
    
    cx(a,v)
    / 1.1 10
      1.2 10
      2.1 10
      2.2 10 /
      
    cxx(m,a)
    / 1.1 2
      1.2 1
      2.1 1
      2.2 3 /
      
    Vol(v)
    /   1    70
        2    80  /
        
    Im(m) 
    /   1    325
        2    300  /
;

Binary variables     
     x(a,v)
;

Free Variable z;
     
Positive Variables
     w(a,v)
     y(a,v,m)
;
     
Equations
     cost
     eqn7(a,v)
     eqn21(a,v)
;

cost..        z  =e= sum(a,sum(v,cx(a,v)*x(a,v)))+sum(a,sum(v,sum(m,cxx(m,a)*y(a,v,m))));
eqn7(a,v).. w(a,v)*Ta(a) =l= Hd*x(a,v);
eqn21(a,v).. sum(m,Im(m)*y(a,v,m)) =l= Vol(v)*w(a,v);

Model supplychainmodel /all/ ;

Solve supplychainmodel using MIP minimizing z ;