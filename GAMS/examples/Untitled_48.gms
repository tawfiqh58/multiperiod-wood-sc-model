$ title networkDEA facility model
sets
i "retailers locations" /i1*i18/
w "warehouses locations"/w1*w8/
j "plant locations"/j1*j8/
l "commodities"/l1*l8/
p "plant candidate"/p1*p4/
e "warehouse candidate"/e1*e4/
t "inputs of plant"/t1*t1/
f "inputs of warehouses"/f1*f2/
;
table De(l,i)
          i1        i2        i3        i4        i5        i6        i7        i8        i9        i10       i11       i12       i13       i14       i15       i16       i17       i18
 l1       37        61        96        45        43        45        43        55        65        34        54        33        54        23        44        65        66        76
 l2       64        53        54        78        29        27        35        52        27        44        28        31        59        60        67        30        60        76
 l3       24        73        21        33        26        27        53        59        47        68        55        43        61        49        22        72        21        68
 l4       26        65        40        26        56        79        71        79        74        37        68        50        26        68        38        45        74        56
 l5       69        26        68        60        68        41        20        66        48        63        66        61        66        21        56        42        37        44
 l6       52        33        76        77        68        76        74        66        72        39        63        24        51        35        55        29        72        50
 l7       53        36        54        41        62        68        23        33        47        50        52        27        33        53        37        56        51        75
 l8       46        45        53        38        66        22        55        59        56        58        27        44        52        71        76        63        57        59
;

table f1(p,j)
           j1        j2         j3         j4         j5         j6         j7         J8
p1        350        630        240        420        380        430        450        530
p2        520        420        360        450        430        510        740        510
P3        420        520        280        670        360        310        640        340
P4        360        480        650        720        780        680        630        520
;
table f2(e,w)
          w1         w2         w3         w4          w5        w6         w7          w8
e1        472        267        312        433        405        493        385        289
e2        400        440        284        413        343        351        392        304
e3        442        392        471        440        359        383        363        391
e4        485        377        498        348        345        380        334        373
;
table C1(j,w)
          w1           w2          w3          w4          w5          w6          w7          w8
j1        2025        5250        5060        2450        3265        2453        4150        3260
j2        2016        3734        3683        2827        3241        4782        2276        3305
j3        4345        3405        3522        4443        4522        2238        2397        4158
j4        3980        3365        3298        4220        4836        3961        3067        2790
J5        3560        2873        3596        4257        4586        3903        2608        4428
J6        4364        3886        2276        2213        2145        4471        4596        3680
J7        3772        4005        4145        4559        3954        3950        2155        3704
J8        2817        3903        4424        3328        2779        4014        4893        4088
;
table C2(w,i)
          i1         i2         i3         i4         i5         i6         i7         i8         i9         i10        i11        i12        i13        i14        i15        i16        i17        i18
W1        805        850        598        850        990        931        869        528        823        962        500        564        697        761        681        969        874        900
W2        792        924        612        623        958        986        554        595        549        861        539        927        662        936        802        934        955        896
W3        966        898        960        614        676        924        963        677        778        673        899        639        548        636        588        699        922        975
W4        765        709        793        694        795        570        611        506        558        869        923        714        500        745        655        959        717        814
W5        829        972        881        721        846        676        518        752        585        761        957        833        508        986        940        633        709        548
W6        850        896        809        605        833        654        519        834        769        632        867        565        763        782        728        628        512        565
W7        942        550        958        804        610        818        834        819        546        858        817        812        771        768        994        988        939        659
W8        734        746        611        615        604        971        910        526        535        575        575        554        628        696        932        937        881        1000
;
table I1(p,j,t)
          t1
p1.j1     2000
p1.j2     2100
p1.j3     1200
p1.j4     4500
p1.j5     2000
p1.j6     2100
p1.j7     1200
p1.j8     4500
p2.j1     2500
p2.j2     3600
p2.j3     2500
p2.j4     3000
p2.j5     2500
p2.j6     3600
p2.j7     2500
p2.j8     3000
p3.j1     2500
p3.j2     3600
p3.j3     2500
p3.j4     3000
p3.j5     2500
p3.j6     3600
p3.j7     2500
p3.j8     3000
p4.j1     2500
p4.j2     3600
p4.j3     2500
p4.j4     3000
p4.j5     2500
p4.j6     3600
p4.j7     2500
p4.j8     3000
;

table I3(e,w,f)
          f1          f2
e1.w1     2600        2100
e1.w2     2000        2200
e1.w3     3500        4500
e1.w4     6000        6500
e1.w5     6000        6500
e1.w6     6000        6500
e1.w7     6000        6500
e1.w8     6000        6500
e2.w1     3600        2000
e2.w2     2100        4500
e2.w3     3200        2500
e2.w4     2300        2600
e2.w5     3200        2500
e2.w6     2300        2600
e2.w7     3200        2500
e2.w8     2300        2600
e3.w1     3600        2000
e3.w2     2100        4500
e3.w3     3200        2500
e3.w4     2300        2600
e3.w5     3200        2500
e3.w6     2300        2600
e3.w7     3200        2500
e3.w8     2300        2600
e4.w1     3600        2000
e4.w2     2100        4500
e4.w3     3200        2500
e4.w4     2300        2600
e4.w5     3200        2500
e4.w6     2300        2600
e4.w7     3200        2500
e4.w8     2300        2600
;

table O1(p,j)
          j1            j2           j3           j4         j5            j6          j7            j8
p1        4000         2400         4230          6100       6400         6362         4150          6362
p2        3200         4100         2362          5320       2360         3335         5320          6230
p3        2100         4250         4250          6150       4241         6225         4110          6365
p4        2300         4130         6120          2330       2336         2230         3362          6125
;

table O2(e,w)
          w1            w2             w3         w4       w5       w6      w7       w8
e1        2500          3400           4400       3500     5400     1500    1400     1500
e2        3500          2300           5500       2400     3300     1400    1300     1400
e3        3500          3400           3400       3500     1400     1500    1400     1500
e4        4500          2300           4500       6400     1300     1400    1300     1400

;
scalars
wt1 /0.5/
wt2/0.5/
f11/2547/
f22/63.92318619/
;
positive variables
b
v
u
d
;

* V.V.I
binary variables
x(p,j)
s(e,w)
y(e,i)
;

scalar M/1000000000000000/;
free variables
z "cost efficiency"
z1 "cost"
z2 "efficiency"
;
Alias(w,ww);
Alias(j,jj);
scalar k/0.0000000000002/;
Scalar Epsilon /0.0001/;
Equations
objective1
objective2
costefficiency
const10000,const11000,const12000,const13000,const14000,const15000,const16000,const17000,const18000,const19000
const20000,const21000,const22000,const23000,const24000,const25000,const26000,const27000,const28000,const29000,const30000
const31000,const32000,const33000,const34000,const35000,const36000,const37000,const38000,const39000,const40000,const41000,const42000
equation1,equation2,equation3,equation4
;




objective1..z1=e=sum(p,sum(j,f1(p,j)*x(p,j)))+sum(e,sum(w,f2(e,w)*s(e,w)))+sum(j,sum(w,sum(l,c1(j,w)*b(j,w,l))))+sum(w,sum(i,sum(l,c2(w,i)*b(w,i,l))));
objective2..z2=e=sum(p,sum(j,1-d(p,j)))+sum(e,sum(w,1-d(e,w)));
costefficiency..z=e=wt1*(sum(p,sum(j,f1(p,j)*x(p,j)))+sum(e,sum(w,f2(e,w)*s(e,w)))+sum(j,sum(w,sum(l,c1(j,w)*b(j,w,l))))+sum(w,sum(i,sum(l,c2(w,i)*b(w,i,l)))))/f11-wt2*(sum(p,sum(j,1-d(p,j)))+sum(e,sum(w,1-d(e,w))))/f22;

const10000(i)..sum(e,y(e,i))=g=1;
const16000(j)..sum(p,x(p,j))=l=1;
const17000(p)..sum(j,x(p,j))=e=1;
const18000(e)..sum(w,s(e,w))=e=1;
const19000(w)..sum(e,s(e,w))=l=1;
const20000(e,i)..y(e,i)=l=sum(w,s(e,w));
const32000(e,w)..u(e,w)*o2(e,w)+d(e,w)=e=s(e,w);
const41000(p,j)..u(p,j)*o1(p,j)+d(p,j)=e=x(p,j);
const24000(p,j)..u(p,j)*o1(p,j)=l=x(p,j);
const25000(e,w)..u(e,w)*o2(e,w)=l=s(e,w);
const13000(j)..sum(w,sum(l,b(j,w,l)))=l=sum(p,x(p,j))*M;
const26000(p,j)..sum(t,v(p,j,t)*I1(p,j,t))=e=x(p,j);
const27000(e,w)..sum(f,v(e,w,f)*I3(e,w,f))=e=s(e,w);
const34000(p,j,jj) $(not(sameas (j,jj)))..u(p,j)*o1(p,jj)-sum(t,v(p,j,t)*I1(p,jj,t))=l=0;
const35000(e,w,ww) $(not(sameas (w,ww)))..u(e,w)*o2(e,ww)-sum(f,v(e,w,f)*I3(e,ww,f))=l=0;
*const42000(p,j,e,w,t)..u(p,j)=e=k*v(e,w,t);
const11000(i,l)..sum(w,b(w,i,l))=e=De(l,i);
const12000(w,i,l)..b(w,i,l)=l=De(l,i)*(sum(e,s(e,w)));
const15000(w,l)..sum(i,b(w,i,l))=e=sum(j,b(j,w,l));
equation1(p,j)..u(p,j)=g=epsilon*x(p,j);
equation2(e,w)..u(e,w)=g=epsilon*s(e,w);
equation3(p,j,t)..v(p,j,t)=g=epsilon*x(p,j);
equation4(e,w,f)..v(e,w,f)=g=epsilon*s(e,w);
models networkDEA  /const10000,const11000,const12000,const13000,const15000,const16000,const17000,const18000,const19000,costefficiency,objective1,objective2,
const34000,const35000,const41000
const24000,const25000,const26000,const27000,const32000,const20000
equation1,equation2,equation3,equation4 /;
networkDEA.Optfile=1;
option decimals=8;
Solve networkDEA using MINLP minimizing z;
display z.l,z.m;
display z1.l,z1.m;
display z2.l,z2.m;
display x.l,x.m;
display s.l,s.m;
display y.l,y.m;
display u.l,v.l;
display d.l;
display b.l,b.m;




