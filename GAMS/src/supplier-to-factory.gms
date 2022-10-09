Sets
    a supplier index
    / 1, 2/
;

Parameters
    Ta(a)
    / 1 2, 2 1 /
    
    Hd
    / 10 /
    
    cxx(a)
    / 1 2
      2 1
      /
      
    Vol
    / 70 /
        
    Im
    / 2 /
;

Free Variable z;
     
Positive Variables
     w(a)
     y(a)
;
     
Equations
     cost
     eqn7(a)
     eqn21(a)
;

cost..        z  =e= sum(a,cxx(a)*y(a));
eqn7(a).. w(a)*Ta(a) =l= Hd;
eqn21(a).. Im*y(a) =l= Vol*w(a);

Model supplychainmodel /all/ ;

Solve supplychainmodel using LP minimizing z ;