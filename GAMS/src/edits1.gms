Sets
       a supplier
       / supplierA, supplierB /
       b wholesaler
       / wholesalerA, wholesalerB /
       e retailer
       / retailerA, retailerB /
       eb(b) retailer who takes service from b wholesaler
       / wholesalerA retailerA retailerB, wholesalerB retailerA /
       f factory vehicle
       / factoryVehicleA, factoryVehicleB /
       g wholesaler vehicle
       / wholesalerVehicleA, wholesalerVehicleB /
       i available vehicles in collection centers that carry wooden waste from [retailer -> collection-center]
       / collection-centerAVehicle1, collection-centerAVehicle2, collection-centerBVehicle1, collection-centerBVehicle2 /
       ix 🎲available vehicles in collection centers servicing producer [collection-center -> producer|factory]
       / collection-centerAVehicle3,collection-centerAVehicle4,collection-centerBVehicle3,collection-centerBVehicle4 /
       ixx index of available vehicles in collection centers servicing producer (ixx belongs to ix)??
       / collection-centerAVehicle3,collection-centerAVehicle4,collection-centerBVehicle3,collection-centerBVehicle4 /
       j collection center
       / collection-centerA, collection-centerB /
       ij(i,j) 🎲vehicle i in collection center j carry waste from [retailer -> collection-center]                     
       / (collection-centerAVehicle1, collection-centerAVehicle2, collection-centerBVehicle1, collection-centerBVehicle2).(collection-centerA,collection-centerB) /
       hj(j) retailer who takes service from j collection center
       / collection-centerA retailerA, collection-centerB retailerB /
       m   raw material
       / raw-materialA, raw-materialB /
       p   product
       / productA, productB /
       t   time period of planning
       / day1, day2 /
       v   vehicle of supplier
       / vehicle1-supplierA,vehicle2-supplierA, vehicle1-supplierB,vehicle2-supplierB /
       Va(a) 🎲vahicle in supplier
       / supplierA, supplierB /
       ixj(i,j) 🎲vehicle i in collection center j carry waste from [collection-center -> factory]
       / (collection-centerAVehicle1, collection-centerAVehicle2, collection-centerBVehicle1, collection-centerBVehicle2).(collection-centerA, collection-centerB) /
       Gb(b) 🎲vehicle in wholesaller b
       / wholesalerA, wholesalerB /
       Bapm(p,m) 🎲p product transform to m
       / (productA, productB).(raw-materialA, raw-materialB) /;

Parameters
    Ta(a) time hour to go-and-come [supplier a -> factory]
    / supplierA 1, supplierB 2 /
    
    Tx(b) time to go-and-come [factory -> wholesaler b]
    / wholesalerA 3, wholesalerB 4 /
    
    Txx(b,e) time to go-and-come [wholesaler b -> retailer e]
    / wholesalerA.retailerA 6
      wholesalerA.retailerB 7
      wholesalerB.retailerA 5
      wholesalerB.retailerB 6 /
      
    ct(p) production cost per unit p in the factory
    / productA 5, productB 10 /
    
    cs(b,f) fixd cost of sending vehicle [factory -> wholesaler b]
*   it should be g instead of f
    / (wholesalerA,wholesalerB).(factoryVehicleA,factoryVehicleB) 100 /
    
    cf(b,p) transportation cost per unit p [factory -> wholesaler b]
*   it should be g instead of f
    / wholesalerA.productA 2
      wholesalerA.productB 1
      wholesalerB.productA 3
      wholesalerB.productB 2 /
    
    cp capacity of factory for raw material
    / 8000 /
    
    cpx capacity of factory for product
    / 14000 /
    
    cpxx(b)  capacity of wholesaler b
*    maybe it will be e index
    / wholesalerA 5000
      wholesalerB 6000 /
    
    Alpha(m,p) consumption coefficient of material m in product p
    / raw-materialA.productA 2
      raw-materialA.productB 1
      raw-materialB.productA 3
      raw-materialB.productB 2 /
      
    Im(m) volume of each material m
    /   raw-materialA    5
        raw-materialB    3  /
    
    Ip(p) volume of each product m
    /   productA    6
        productB    5  /
        
    ch(m,t) maintainance cost of material m in factory on day t
    / raw-materialA.day1 20
      raw-materialA.day2 22
      raw-materialB.day1 21
      raw-materialB.day2 23 /
      
    cinv cost of environment destruction by cutting tree
    / 100 /
    
    Ts(e,j) time to go-and-come [retailer e -> collection-center j]
    / retailerA.collection-centerA 3
      retailerA.collection-centerB 2
      retailerB.collection-centerA 2
      retailerB.collection-centerB 3 /
    
    Tsx(j) time to go-and-come [collection-center j -> factory]
    / collection-centerA 3
      collection-centerB 4 /
      
    LargeM large number
    / 10000000 /
    
    BigM very large number
    / 100000000000 /
    
    Hd work hours in day
    / 12 /
    
    ck(e,p) purchasing cost each product p from retailer e
*   it says waste but denotes p
    / retailerA.productA 10
      retailerA.productB 20
      retailerB.productA 11
      retailerB.productB 22 /
    
    fx(ix,j) fixed const sending vehicle ix from [collection-center j -> factory]
    / (collection-centerAVehicle3,collection-centerAVehicle4,collection-centerBVehicle3,collection-centerBVehicle4).(collection-centerA, collection-centerB) 60 /
    
    czx(j,m) transportation cost unit of wooden waste m from [collection-center j -> factory]
    / collection-centerA.raw-materialA 7
      collection-centerA.raw-materialB 8
      collection-centerB.raw-materialA 6
      collection-centerB.raw-materialB 7 /
      
    Sp(i)  capacity of vehicle i
    /   collection-centerAVehicle1      100
        collection-centerAVehicle2       90  
        collection-centerBVehicle1      120  
        collection-centerBVehicle2      100  /
    
    chx(p,t)  maintainance cost unit product p in factory on day t
    /   productA.day1    5
        productA.day2    3
        productB.day1    4
        productB.day2    2 /
    
   Spx(ix)  capacity of vehicle ix
*   sir told me that it's not necessary. I can remove this index.
*   so don't use Spx in equations
    /   collection-centerAVehicle3     80
        collection-centerAVehicle4     90  
        collection-centerBVehicle3     80  
        collection-centerBVehicle4    100  /

    cab(j) storage capacity of collection-center j
    / collection-centerA 120
      collection-centerB 110 /
    
    BR(p,e) The percentage of product p that returns from retailer e
    /   productA.retailerA    3
        productA.retailerB    3
        productB.retailerA    2
        productB.retailerB    2 /

    Cinvx benifit of environment enhancement for each tree
    / 100 /
    
    c(m,a) cost of purchasing unit wooden raw material m form [supplier a -> factory]
    / raw-materialA.supplierA 15
      raw-materialA.supplierB 16
      raw-materialB.supplierA 16
      raw-materialB.supplierB 17 /

    cx(a,v) fixed cost sending vehicle v form [supplier a -> factory]
    / (supplierA,supplierB).(vehicle1-supplierA,vehicle2-supplierA,vehicle1-supplierB,vehicle2-supplierB) 10 /
    
    cxx(m,a) transportation cost unit wooden raw material m form [supplier a -> factory]
    / raw-materialA.supplierA 2
      raw-materialA.supplierB 1
      raw-materialB.supplierA 1
      raw-materialB.supplierB 3 /
    
    Vol(v)  capacity of vehicle v
    /   vehicle1-supplierA    170
        vehicle2-supplierA    180  
        vehicle1-supplierB    160  
        vehicle2-supplierB    170  /

    Volx(f)  capacity of vehicle f
    /   factoryVehicleA    75
        factoryVehicleB    85  /

    Volxx(g)  capacity of vehicle g
    /   wholesalerVehicleA    40
        wholesalerVehicleB    20  /;

table cr(b,e,g) fixed cost sending vehicle g from wholesaler b to retailer e
                                                    wholesalerVehicleA   wholesalerVehicleB
(wholesalerA,wholesalerB).(retailerA,retailerB)             50                  50;


table cd(b,e,p) transportation cost per unit p from [wholesaler b -> retailer e]
                             productA            productB
wholesalerA.retailerA           1                  2
wholesalerA.retailerB           3                  4
wholesalerB.retailerA           2                  3
wholesalerB.retailerB           4                  5 ;

table dem(e,p,t) demand retailer e product p on day t
                            day1                 day2
retailerA.productA          400                  400
retailerB.productA          450                  450
retailerA.productB          500                  500
retailerB.productB          550                  550 ;

table Pept(e,p,t) penalty of shortage of product p for retailer e on day t
                            day1                day2
retailerA.productA           5                   8
retailerB.productA           4                   7
retailerA.productB           3                   9
retailerB.productB           6                   8 ;

table feij(e,i,j) fxd transportation cost of vehicle i from [retailer e -> collection-center j]
                                                                                                                                            collection-centerA    collection-centerB
(retailerA,retailerB).(collection-centerAVehicle1,collection-centerAVehicle2,collection-centerBVehicle1,collection-centerBVehicle2)              50                    50;

table cz(e,j,p) transportation cost of each wooden waste m [collection-center j -> factory]
* it should be waste
                                productA  productB
retailerA.collection-centerA        2         1
retailerA.collection-centerB        2         1
retailerB.collection-centerA        2         1
retailerB.collection-centerB        2         1 ;

table chxx(b,p,t) maintainance cost of each product p for wholesaler b on day t
                              day1                day2
wholesalerA.productA           5                   8
wholesalerB.productA           4                   7
wholesalerA.productB           3                   9
wholesalerB.productB           6                   8 ;

table chxxx(e,p,t) maintainance cost of each product p for retailer e on day t
                            day1               day2
retailerA.productA           2                  4
retailerB.productA           3                  3
retailerA.productB           1                  4
retailerB.productB           3                  2 ;

free variables
     z
;

Variables
     w(a,v,t)
     w1(b,f,t)
     w11(b,e,g,t)
     y111(b,e,g,p,t) number of product p transported by vehicle g from wholesaller b to retailer e on day t
*    bo(k,p,t) k not init     
     bo(e,p,t)
*    ux(m,(t-1)) not working
     u1(m,t)
     u_pt(p,t)
     u11(b,p,t)
*    uxxx(e,p,(t-1)) not working
     u111(e,p,t)      storage inventory or retailer e from product p on day t
     wb(e,i,j,t)
     wb1(ix,j,t)
     yb(e,i,j,p,t)    amount of p product sent retailer e to collection-center j on day t using vehicle i
     yb1(ix,j,m,t)
     y(a,v,m,t)   m material sent by v vahicle from a supplier to the factory on t day
     y1(p,t)
     y11(b,g,p,t)
;

binary variables     
     x(a,v,t)
     x1(b,f,t)
     x11(b,e,g,t)
     xb(e,i,j,t)
     xb1(ix,j,t)
;

Equations
     cost        define objective function
     eqn1(e,p,t) product supply equation 
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
;


cost..        z  =e=  (sum(a,sum(v,sum(m,sum(t,c(m,a)*y(a,v,m,t)))))) + (sum(a,sum(v,sum(t,cx(a,v)*x(a,v,t))))+sum(a,sum(v,sum(m,sum(t,cxx(m,a)*y(a,v,m,t)))))) +
(sum(p,sum(t,ct(p)*y1(p,t)))) + (sum(b,sum(f,sum(t,cs(b,f)*x1(b,f,t))))+ sum(b,sum(g,sum(p,sum(t,cf(b,p)*y11(b,g,p,t)))))) +
(sum(b,sum(e,sum(g,sum(t,cr(b,e,g)*x11(b,e,g,t)))))+sum(b,sum(e,sum(g,sum(p,sum(t,cd(b,e,p)*y111(b,e,g,p,t))))))) +
(sum(m,sum(t,ch(m,t)*u1(m,t))) + sum(p,sum(t,chx(p,t)*u_pt(p,t))) + sum(b,sum(p,sum(t,chxx(b,p,t)*u11(b,p,t)))) + sum(e,sum(p,sum(t,chxxx(e,p,t)*u111(e,p,t))))) +
sum(e,sum(p,sum(t,Pept(e,p,t)*bo(e,p,t)))) + (Cinv*sum(a,sum(v,sum(m,sum(t,y(a,v,m,t)))))) + (sum(e,sum(i,sum(j,sum(p,sum(t,ck(e,p)*yb(e,i,j,p,t))))))) +
(sum(e,sum(j,sum(i,sum(t,feij(e,i,j)*xb(e,i,j,t))))) + sum(e,sum(j,sum(i,sum(p,sum(t,cz(e,j,p)*yb(e,i,j,p,t))))))) +
(sum(j,sum(ix,sum(t,fx(ix,j)*xb1(ix,j,t)))) + sum(j,sum(ix,sum(m,sum(t,czx(j,m)*yb1(ix,j,m,t))))) - (Cinvx*sum(j,sum(ix,sum(m,sum(t,yb1(ix,j,m,t)))))));

eqn1(e,p,t)..  (sum(b,sum(g, y111(b,e,g,p,t))) + u111(e,p,t-1) - u111(e,p,t)) * BR(p,e) =e= sum(j,sum(i,yb(e,i,j,p,t))) ;
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


Model supplychainmodel /all/ ;

Solve supplychainmodel using MIP minimizing z ;