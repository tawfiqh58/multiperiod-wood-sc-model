Sets
    i /a,b,c/
    ;

Free Variable z;

Positive Variable
    R(i)
    C(i);

Equations
    return
    c1
    c2
    c3
    c4
    c5
    c6
    c7
    c8;

return .. z =e= sum(i,R(i));
c1 .. sum(i,C(i)) =e= 100000;
c2 .. R('a')=e=0.05*C('a');
c3 .. R('b')=e=0.1*C('b');
c4 .. R('c')=e=0.12*C('c');
c5 .. C('b')=l= 0.2*100000;
c6 .. C('c')=l= 0.1*100000;
c7 .. 0=l=C('b');
c8 .. 0=l=C('c');

Model transport /all/ ;

Solve transport using lp maximizing z ;