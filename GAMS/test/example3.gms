Sets
    i /a,b,c/;

Positive Variable
    C(i);
Binary Variable
    B(i);
Integer Variable
    P(i);
Free Variable z;

Equations
    cost
    c1
    c2
    c3
    c4
    c5
    c6
    c7(i);

cost .. z =e= sum(i,C(i));
c1 .. C('a') =e= 0.1*sqr(P('a'))+0.5*P('a')+B('a')*0.1;
c2 .. C('b') =e= 0.3*P('b')+B('b')*0.5;
c3 .. C('c') =e= 0.01*sqr(P('c'))*P('c');
c4 .. P('a') =l= B('a')*1000000;
c5 .. P('b') =l= B('b')*1000000;
c6 .. sum(i, P(i)) =e= 10000;
c7(i) .. P(i) =g= 0;

Model example3 /all/;
Solve example3 using minlp minimizing z ;