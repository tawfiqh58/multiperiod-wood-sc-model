Sets
       a   supplier
       / supplierA, supplierB /
       b   wholesaler
       / wholesalerA, wholesalerB /
       e   customer
       / retailerA, retailerB /
       eb(e) retailer who takes service from b wholesaler
       / retailerA wholesalerA wholesalerB, retailerB wholesalerB /
       f   factory vehicle
       / factoryVehicleA, factoryVehicleB /
       g   wholesaler vehicle
       / wholesalerVehicleA, wholesalerVehicleB /
       Gb(b) vehicle in wholesaller b
       / wholesalerA vahicleK, wholesalerB vehicleL /
       i   available vehicles in collection centers that carry wooden waste from [retailer -> collection-center]
       / vehicleA, vehicleB /
       ix   available vehicles in collection centers servicing producer [collection-center -> producer|factory]
       / vehicleC , vehicleD /
       ixx   available vehicles in collection centers servicing producer (ixx belongs to ix)??
       / vehicleC, vehicleD /
       j   collection center
       / collection-centerA, collection-centerB /
       ij(i,j)  vehicle in collection center j carry waste from [customer -> collection-center]                     
*      one to many relationship pageno:40 (GAMS-user-guide)
       / (vehicleA,vehicleB).(collection-centerA,collection-centerB) /
       hj(j) retailer who takes service from j collection center
       / collection-centerA retailerA, collection-centerB retailerB /
       m   raw material
       / raw-materialA, raw-materialB /
       p   product
       / productA, productB /
       t   time period of planning
       / day1, day2 /
       v   vehicle supplier
       / vehicle-supplierA, vehicle-supplierB /
       Va(a) vahicle in supplier
*      let: supplierA has vehicleI, supplierB has vehicleJ
       / supplierA vehicleI vehicle2 vehicle3, supplierB vehicleJ /
       Bapm(p,m) p product transform to m materia
       / (productA,productB).(raw-materialA,raw-materialB) /
       ixj(i,j) vehicle in collection center j carry waste from [collection-center -> factory]
       / (vehicleA,vehicleB).(collection-centerA,collection-centerB) / ;

Parameters
    Ta(a) time hour to go-and-come [supplier a -> factory]
    / supplierA 104, supplierB 112 /
    
    Tx(b) time to go-and-come [factory -> wholesaler b]
    / wholesalerA 2358, wholesalerB 3239 /
    
    Txx(b,e) time to go-and-come [holesaler b -> retailer e]
    / wholesalerA.retailerA 326
      wholesalerA.retailerB 27
      wholesalerB.retailerA 54
      wholesalerB.retailerB 56 /
      
    ct(p) production cost per unit p in the factory
    / productA 805, productB 9023 /
    
    cs(b,f) fixd cost of sending vehicle [factory -> wholesaler b]
*   it should be g instead of f
    / wholesalerA.factoryVehicleA 62
      wholesalerA.factoryVehicleB 75
      wholesalerB.factoryVehicleA 5
      wholesalerB.factoryVehicleB 6 /
    
    cf(b,p) transportation cost per unit p [factory -> wholesaler b]
*   it should be g instead of f
    / wholesalerA.productA 223
      wholesalerA.productB 123
      wholesalerB.productA 33
      wholesalerB.productB 42 /
    
    cp  capacity of factory for raw material
    / 350534 /
    
    cpx  capacity of factory for product
    / 250324 /
    
    cpxx(b)  capacity of retailer b
*    maybe it will be e index
    / wholesalerA 25023
      wholesalerB 23235 /
    
    Alpha(m,p) consumption coefficient of material m in product p
    / raw-materialA.productA 21
      raw-materialA.productB 12
      raw-materialB.productA 233
      raw-materialB.productB 232 /
      
    Im(m)  volume of each material m
    /   raw-materialA    325
        raw-materialB    300  /
    
    Ip(p)  volume of each product m
    /   productA    325
        productB    300  /
        
    ch(m,t) maintainance cost of material m in factory on day t
    / raw-materialA.day1 20
      raw-materialA.day2 22
      raw-materialB.day1 21
      raw-materialB.day2 23 /
      
    cinv cost of environment destruction by cutting tree
    / 100 /
    
    Ts(e,j) time to go-and-come [customer e -> collection-center j]
    / retailerA.collection-centerA 3
      retailerA.collection-centerB 2
      retailerB.collection-centerA 2
      retailerB.collection-centerB 3 /
    
    Tsx(j) time to go-and-come [collection-center j -> factory]
    / collection-centerA 7
      collection-centerB 8 /
      
    LargeM large number
    / 10000000 /
    
    BigM very large number
    / 100000000000 /
    
    Hd work hours in day
    / 10 /
    
    ck(e,p) purchasing cost each product p from retailer e
*   it says waste but denotes p
    / retailerA.productA 100
      retailerA.productB 120
      retailerB.productA 110
      retailerB.productB 130 /
    
    fx(ix,j) fixed const sending vehicle ix from [collection-center j -> factory]
    / vehicleC.collection-centerA 30
      vehicleC.collection-centerB 20
      vehicleD.collection-centerA 20
      vehicleD.collection-centerB 30 /
    
    czx(j,m) transportation cost unit of wooden waste m from [collection-center j -> factory]
    / collection-centerA.raw-materialA 7
      collection-centerA.raw-materialB 8
      collection-centerB.raw-materialA 6
      collection-centerB.raw-materialB 7 /
      
    Sp(i)  capacity of vehicle i
    /   vehicleA    80
        vehicleB    90  /
    
    chx(p,t)  maintainance cost unit product p in factory on day t
    /   productA.day1    5
        productA.day2    3
        productB.day1    4
        productB.day2    2 /
    
    Spx(ix)  capacity of vehicle i
*   sir told me that it's not necessary. I can remove this index.
*   so don't use Spx in equations
    /   vehicleC    80
        vehicleD    90  /

    cab(j) storage capacity of collection-center j
    / collection-centerA 120
      collection-centerB 110 /
    
    BRpe(p,e)  volume of each material m
    /   productA.retailerA    325
        productA.retailerB    300
        productB.retailerB    305
        productB.retailerA    275 /

    Cinvx benifit of environment enhancement for each tree
    / 10 /
    
    c(m,a) cost of purchasing unit wooden raw material m form [supplier a -> factory]
    / raw-materialA.supplierA 15
      raw-materialA.supplierB 16
      raw-materialB.supplierA 16
      raw-materialB.supplierB 17 /

    cx(a,v) fixed cost sending vehicle v form [supplier a -> factory]
    / supplierA.vehicle-supplierA 10
      supplierA.vehicle-supplierB 12
      supplierB.vehicle-supplierA 12
      supplierB.vehicle-supplierB 13 /
    
    cxx(m,a) transportation cost unit wooden raw material m form [supplier a -> factory]
    / raw-materialA.supplierA 2
      raw-materialA.supplierB 1
      raw-materialB.supplierA 1
      raw-materialB.supplierB 3 /
    
    Vol(v)  capacity of vehicle v
    /   vehicle-supplierA    70
        vehicle-supplierB    80  /

    Volx(f)  capacity of vehicle f
    /   factoryVehicleA    75
        factoryVehicleB    85  /

    Volxx(g)  capacity of vehicle g
    /   wholesalerVehicleA    40
        wholesalerVehicleB    20  /
;

table cr(b,e,g) fixed cost sending vehicle g from wholesaler b to customer e
                       wholesalerVehicleA   wholesalerVehicleB
wholesalerA.retailerA           20                  18
wholesalerA.retailerB           19                  17
wholesalerB.retailerA           21                  19
wholesalerB.retailerB           20                  18 ;

table cd(b,e,p) transportation cost per unit p from [wholesaler b -> retailer e]
                             productA            productB
wholesalerA.retailerA           20                  18
wholesalerA.retailerB           19                  17
wholesalerB.retailerA           21                  19
wholesalerB.retailerB           20                  18 ;

table dem(e,p,t) demand customer e product p on day t
                            day1                day2
retailerA.productA           20                  18
retailerB.productA           19                  17
retailerA.productB           21                  19
retailerB.productB           20                  18 ;

table Pept(e,p,t) penalty of shortage of product p for retailer e on day t
                            day1                day2
retailerA.productA           5                   8
retailerB.productA           4                   7
retailerA.productB           3                   9
retailerB.productB           6                   8 ;

table feij(e,i,j) fxd transportation cost of vehicle i from [customer e -> collection-center j]
                     collection-centerA    collection-centerB
retailerA.vehicleA           20                    18
retailerA.vehicleB           19                    17
retailerB.vehicleA           21                    19
retailerB.vehicleB           20                    18 ;

table cz(e,j,p) transportation cost of each wooden waste m [collection-center j -> factory]
* it should be waste
                                productA  productB
retailerA.collection-centerA        3         4
retailerA.collection-centerB        2         5
retailerB.collection-centerA        2         6
retailerB.collection-centerB        3         5 ;

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

Positive Variables
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
     u111(e,p,t)      storage inventory or customer e from product p on day t
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

* let
* i" = ix because of sir told me; for regain it back you have to replace all ix -> ixx by following thesis paper eqn
* u' = u_pt because u' has duplicate
* I'p = Ip because ix already defined

cost..        z  =e=  (sum(a,sum(v,sum(m,sum(t,c(m,a)*y(a,v,m,t))))));

eqn1(e,p,t)..  (sum(b,sum(g, y111(b,e,g,p,t))) + u111(e,p,t-1) - u111(e,p,t)) * BRpe(p,e) =e= sum(j,sum(i,yb(e,i,j,p,t))) ;
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
