eqn2(m,j,t).. sum(e,sum(i,sum(p,Alpha(m,p)*yb(e,i,j,p,t)))) =e= sum(ix,yb1(ix,j,m,t));
eqn3(t).. sum(m,Im(m)*u1(m,t)) =l= cp;
eqn4(t).. sum(p,Ip(p)*u_pt(p,t)) =l= cpx;
eqn5(b,t).. sum(p,Ip(p)*u11(b,p,t)) =l=cpxx(b);
eqn6(t,m).. sum(a,sum(v,y(a,v,m,t))) + u1(m,t-1) =e= sum(p,Alpha(m,p)*y1(p,t)) + u1(m,t);
eqn7(a,v,t).. w(a,v,t)*Ta(a) =l= Hd*x(a,v,t);
eqn8(f,t).. sum(b,w1(b,f,t)*Tx(b)) =l= Hd;
eqn9(b,g,t).. sum(e,w11(b,e,g,t)*Txx(b,e)) =l= Hd;
eqn10(b,f,t).. w1(b,f,t) =l= LargeM*x1(b,f,t);
eqn11(b,e,g,t).. w11(b,e,g,t) =l= BigM*x11(b,e,g,t);
eqn12(p,t).. y1(p,t) + u_pt(p,t-1) =e= sum(b,sum(g,y11(b,g,p,t))) + u_pt(p,t);
eqn13(b,p,t).. sum(g,y11(b,g,p,t)) + u11(b,p,t-1) =e= sum(e,sum(g,y111(b,e,g,p,t))) + u11(b,p,t);
eqn14(e,p,t).. sum(b,sum(g,y111(b,e,g,p,t))) + u111(e,p,t-1) + bo(e,p,t) =e= dem(e,p,t) + u111(e,p,t);
eqn15(e,i,j,t).. sum(p,Ip(p)*yb(e,i,j,p,t)) =l= Sp(i)*wb(e,i,j,t);
eqn16(ix,j,t).. sum(m,Im(m)*yb1(ix,j,m,t)) =l= Spx(ix)*wb1(ix,j,t);
eqn17(i,j,t).. sum(e,wb(e,i,j,t)*Ts(e,j)) =l= Hd;
eqn18(ix,j,t).. wb1(ix,j,t)*Tsx(j) =l= Hd*xb1(ix,j,t);
eqn19(j,i,e,t).. wb(e,i,j,t) =l= LargeM*xb(e,i,j,t);
eqn20(t,m).. sum(a,sum(v,y(a,v,m,t))) + sum(j,sum(ix,yb1(ix,j,m,t))) + u1(m,t-1) =e= sum(p,Alpha(m,p)*y1(p,t)) + u1(m,t);
eqn21(a,v,t).. sum(m,Im(m)*y(a,v,m,t)) =l= Vol(v)*w(a,v,t);
eqn22(b,f,g,t).. sum(p,Ip(p)*y11(b,g,p,t)) =l= volx(f)*w1(b,f,t);
eqn23(b,e,g,t).. sum(p,Ip(p)*y111(b,e,g,p,t)) =l= volxx(g)*w11(b,e,g,t);


eqn2(m,j,t)
     eqn3(t)
     eqn4(t)
     eqn5(b,t)
     eqn6(t,m)
*    eqn7 v belongs to Va
     eqn7(a,v,t)
     eqn8(f,t)
*    eqn9 g belongs to Gb
     eqn9(b,g,t)
     eqn10(b,f,t)
*    eqn11 e belongs to Eb, g belongs to Gb
     eqn11(b,e,g,t)
     eqn12(p,t)
     eqn13(b,p,t)
     eqn14(e,p,t)
*    eqn15 i belongs to i'j
     eqn15(e,i,j,t)
*    eqn16 i" belongs to i'j
     eqn16(ix,j,t)
*    eqn17 i belongs to i'j
     eqn17(i,j,t)
*    eqn18 i" belongs to i'j
     eqn18(ix,j,t)
*    eqn19 i belongs to i'j, e belongs to hj
     eqn19(j,i,e,t)
     eqn20(t,m)
*    eqn21 v belongs to Va
     eqn21(a,v,t)
*    eqn22 g belongs to Ga
     eqn22(b,f,g,t)
*    eqn23 e belongs to eb, g belongs to Ga
     eqn23(b,e,g,t)