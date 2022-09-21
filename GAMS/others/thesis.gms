Sets
       a   supplier
       / supplierA, supplierB /
       b   wholesaler
       / wholesalerA, wholesalerB /
       e   customer
       / retailerA, retailerB /
       eb(e) retailer who takes service from b wholesaler
       / retailerA, retailerB /
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
*      one to many relationship page: 40 GAMS-user-guide
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

* display ixj; shows "YES" value for each combination in a table
* that's mean if you don't give value to this denotation it will be "YES"
* display i; result: vahicleA,    vehicleB
* WHY i shows string and ixj show VALUE
* ANS: combinatin is just denotation but what is the value, each index has values

* display Va; result: supplierA,    supplierB
* display Va(supplierA); ERROR: we can't access this way

Parameters
    Ta(a) time hour to go-and-come [supplier a -> factory]
    / supplierA 10, supplierB 11 /
    
    Tx(b) time to go-and-come [factory -> holesaler b]
    / wholesalerA 8, wholesalerB 9 /
    
    Txx(b,e) time to go-and-come [holesaler b -> retailer e]
    / wholesalerA.retailerA 6
      wholesalerA.retailerB 7
      wholesalerB.retailerA 5
      wholesalerB.retailerB 6 /
      
    ct(p) production cost per unit p in the factory
    / productA 80, productB 90 /
    
    cs(b,f) fixd cost of sending vehicle [factory -> wholesaler b]
*   it should be g instead of f
    / wholesalerA.factoryVehicleA 6
      wholesalerA.factoryVehicleB 7
      wholesalerB.factoryVehicleA 5
      wholesalerB.factoryVehicleB 6 /
    
    cf(b,p) transportation cost per unit p [factory -> wholesaler b]
*   it should be g instead of f
    / wholesalerA.productA 2
      wholesalerA.productB 1
      wholesalerB.productA 3
      wholesalerB.productB 2 /
    
    cp  capacity of factory for raw material
    / 350 /
    
    cpx  capacity of factory for product
    / 250 /
    
    cpxx(b)  capacity of retailer b
*    maybe it will be e index
    / wholesalerA 250
      wholesalerB 235 /
    
    Alpha(m,p) consumption coefficient of material m in product p
    / raw-materialA.productA 2
      raw-materialA.productB 1
      raw-materialB.productA 3
      raw-materialB.productB 2 /
      
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
    
    Spx(ixx)  capacity of vehicle i
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
    
    cma(m,a) cost of purchasing unit wooden raw material m form [supplier a -> factory]
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

Variables
     w(a,v,t)
     wx(b,f,t)
     wxx(b,e,g,t)
     yxxx(b,e,g,p,t) number of product p transported by vehicle g from wholesaller b to retailer e on day t
*    bo(k,p,t) k not init     
     bo(e,p,t)
*    ux(m,(t-1)) not working
     ux(m,t)
     u_pt(p,t)
     uxx(b,p,t)
*    uxxx(e,p,(t-1)) not working
     uxxx(e,p,t)      storage inventory or customer e from product p on day t
     wb(e,i,j,t)
     wbx(ix,j,t)
     yb(e,i,j,p,t)    amount of p product sent retailer e to collection-center j on day t using vehicle i
     ybx(ix,j,m,t)
     yavmt(a,v,m,t)   m material sent by v vahicle from a supplier to the factory on t day
     yx(p,t)
     yxx(b,g,p,t)
;

binary variables     
     xavt(a,v,t)
     xx(b,f,t)
     xxx(b,e,g,t)
     xb(e,i,j,t)
     xbx(ix,j,t)
;

Positive variables x ;

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
*    eqn15 i belongs to ixj
     eqn15(i,j,t)
*    eqn16 ixx belongs to ixj
     eqn16(ix,j,t)
*    eqn17 i belongs to ixj
     eqn17(i,j,t)
*    eqn18 ixx belongs to ixj
     eqn18(ix,j,t)
*    eqn19 i belongs to ixj, e belongs to hj
     eqn19(j,i,e,t)
     eqn20(t,m)
*    eqn21 v belongs to Va
     eqn21(a,v,t)
*    eqn22 g belongs to Ga
     eqn22(b,f,g,t)
*    eqn23 e belongs to eb, g belongs to Ga
     eqn23(b,e,g,t)
;

* c = cma
* y = yavmt
* x = xavt
* i" = ix because of sir told me
* u' = u_pt
* I'p = Ip
cost..        z  =e=  (sum(a,sum(v,sum(m,sum(t,cma(m,a)*yavmt(a,v,m,t)))))) + (sum(a,sum(v,sum(t,cx(a,v)*xavt(a,v,t))))+sum(a,sum(v,sum(m,sum(t,cxx(m,a)*yavmt(a,v,m,t)))))) +
(sum(p,sum(t,ct(p)*yx(p,t)))) + (sum(b,sum(f,sum(t,cs(b,f)*xx(b,f,t))))+ sum(b,sum(g,sum(p,sum(t,cf(b,p)*yxx(b,g,p,t)))))) +
(sum(b,sum(e,sum(g,sum(t,cr(b,e,g)*xxx(b,e,g,t)))))+sum(b,sum(e,sum(g,sum(p,sum(t,cd(b,e,p)*yxxx(b,e,g,p,t))))))) +
(sum(m,sum(t,ch(m,t)*ux(m,t))) + sum(p,sum(t,chx(p,t)*u_pt(p,t))) + sum(b,sum(p,sum(t,chxx(b,p,t)*uxx(b,p,t)))) + sum(e,sum(p,sum(t,chxxx(e,p,t)*uxxx(e,p,t))))) +
sum(e,sum(p,sum(t,Pept(e,p,t)*bo(e,p,t)))) + (Cinv*sum(a,sum(v,sum(m,sum(t,yavmt(a,v,m,t)))))) + (sum(e,sum(i,sum(j,sum(p,sum(t,ck(e,p)*yb(e,i,j,p,t))))))) +
(sum(e,sum(j,sum(i,sum(t,feij(e,i,j)*xb(e,i,j,t))))) + sum(e,sum(j,sum(i,sum(p,sum(t,cz(e,j,p)*yb(e,i,j,p,t))))))) +
(sum(j,sum(ix,sum(t,fx(ix,j)*xbx(ix,j,t)))) + sum(j,sum(ix,sum(m,sum(t,czx(j,m)*ybx(ix,j,m,t))))) - (Cinvx*sum(j,sum(ix,sum(m,sum(t,ybx(ix,j,m,t)))))));
* eqn1(e,p,t)..  (sum(b,sum(g, xxxxy(b,e,g,p,t))) + xxxu(e,p,(t-1)) - xxxu(e,p,t)) * BRpe(p,e) =e= sum(j,sum(i,yb(e,i,j,p,t))) ;
* eqn1(e,p,t)..  (sum(b,sum(g, xxxxy(b,e,g,p,t))) + xxxu(e,p,"(t-1)") - xxxu(e,p,t)) * BRpe(p,e) =e= sum(j,sum(i,yb(e,i,j,p,t))) ;
* (t-1) not working
* how to write (t-1)
eqn1(e,p,t)..  (sum(b,sum(g, yxxx(b,e,g,p,t))) + uxxx(e,p,t) - uxxx(e,p,t)) * BRpe(p,e) =e= sum(j,sum(i,yb(e,i,j,p,t))) ;

* sum upper limit do not matches as I simply decleared in the above eqn1
* sum(i tolongs to ixj, _)
* sum(g tolongs to Gb, _)
* TODO: ADD more Constraints..

eqn2(m,j,t).. sum(e,sum(i,sum(p,Alpha(m,p)*yb(e,i,j,p,t)))) =e= sum(ix,ybx(ix,j,m,t));
eqn3(t).. sum(m,Im(m)*ux(m,t)) =l= cp;
eqn4(t).. sum(p,Ip(p)*u_pt(p,t)) =l= cpx;
eqn5(b,t).. sum(p,Ip(p)*uxx(b,p,t)) =l=cpxx(b);
eqn6(t,m).. sum(a,sum(v,yavmt(a,v,m,t))) + ux(m,t) =e= sum(p,Alpha(m,p)*yx(p,t)) + ux(m,t);
eqn7(a,v,t).. w(a,v,t)*Ta(a) =l= Hd*xavt(a,v,t);
eqn8(f,t).. sum(b,wx(b,f,t))*Tx(b) =l= Hd;
eqn9(b,g,t).. sum(e,wxx(b,e,g,t))*Txx(b,e) =l= Hd;
eqn10(b,f,t).. wx(b,f,t) =l= LargeM*xx(b,f,t);
eqn11(b,e,g,t).. wxx(b,e,g,t) =l= BigM*xxx(b,e,g,t);
eqn12(p,t).. yx(p,t) + u_pt(p,t) =e= sum(b,sum(g,yxx(b,g,p,t))) + u_pt(p,t);
eqn13(b,p,t).. sum(g,yxx(b,g,p,t)) + uxx(b,p,t) =e= sum(e,sum(g,yxxx(b,e,g,p,t))) + uxx(b,p,t);
eqn14(e,p,t).. sum(b,sum(g,yxxx(b,e,g,p,t))) + uxxx(e,p,t) + bo(e,p,t) =e= dem(e,p,t) + uxxx(e,p,t);
eqn15(e,i,j,t).. sum(p,Ip(p)*yb(e,i,j,p,t)) =l= Sp(i)*wb(e,i,j,t);
eqn16(ix,j,t).. sum(m,Im(m)*ybx(ix,j,m,t)) =l= Spx(ix)*wbx(ix,j,t);
eqn17(i,j,t).. sum(e,wb(e,i,j,t))*Ts(e,j) =l= Hd;
eqn18(ix,j,t).. wbx(ix,j,t)*Tsx(j) =l= Hd*xbx(ix,j,t);
eqn19(j,i,e,t).. wb(e,i,j,t) =l= LargeM*xb(e,i,j,t);
eqn20(t,m).. sum(a,sum(v,yavmt(a,v,m,t))) + sum(j,sum(ix,ybx(ix,j,m,t))) + ux(m,t) = sum(p,Alpha(m,p)*yx(p,t)) + ux(m,t);
eqn21(a,v,t).. sum(m,Im(m)*yavmt(a,v,m,t)) =l= Vol(v)*w(a,v,t);
eqn22(b,f,g,t).. sum(p,Ip(p)*yxx(b,g,p,t)) =l= volx(f)*wx(b,f,t);
eqn23(b,e,g,t).. sum(p,Ip(p)*yxxx(b,e,g,p,t) =l= volxx(g)*wxx(b,e,g,t);


Model thesisSolve /all/ ;

Solve thesisSolve using LP minimizing z ;
