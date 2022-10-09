Sets
       a   supplier
       / supplierA, supplierB /
       b   wholesaler
       / wholesalerA, wholesalerB /
       e   customer
       / retailerA, retailerB /
       f   factory vehicle
       / factoryVehicleA, factoryVehicleB /
       g   wholesaler vehicle
       / wholesalerVehicleA, wholesalerVehicleB /
       i   available vehicles in collection centers that carry wooden waste from [retailer -> collection-center]
       / vehicleA, vehicleB /
       ix   available vehicles in collection centers servicing producer [collection-center -> producer|factory]
       / vehicleC , vehicleD /
       j   collection center
       / collection-centerA, collection-centerB /
       m   raw material
       / raw-materialA, raw-materialB /
       p   product
       / productA, productB /
       t   time period of planning
       / day1, day2 /
       v   vehicle supplier
       / vehicle-supplierA, vehicle-supplierB /;

Parameters
    ct(p) production cost per unit p in the factory
    / productA 80, productB 90 /
    
    cs(b,f) fixd cost of sending vehicle [factory -> wholesaler b]
    / wholesalerA.factoryVehicleA 6
      wholesalerA.factoryVehicleB 7
      wholesalerB.factoryVehicleA 5
      wholesalerB.factoryVehicleB 6 /
    
    cf(b,p) transportation cost per unit p [factory -> wholesaler b]
    / wholesalerA.productA 2
      wholesalerA.productB 1
      wholesalerB.productA 3
      wholesalerB.productB 2 /
        
    ch(m,t) maintainance cost of material m in factory on day t
    / raw-materialA.day1 20
      raw-materialA.day2 22
      raw-materialB.day1 21
      raw-materialB.day2 23 /
      
    cinv cost of environment destruction by cutting tree
    / 100 /
    
    ck(e,p) purchasing cost each product p from retailer e
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
    
    chx(p,t)  maintainance cost unit product p in factory on day t
    /   productA.day1    5
        productA.day2    3
        productB.day1    4
        productB.day2    2 /

    cinvx benifit of environment enhancement for each tree
    / 10 /
    
    c(m,a) cost of purchasing unit wooden raw material m form [supplier a -> factory]
    / raw-materialA.supplierA 15
      raw-materialA.supplierB 16
      raw-materialB.supplierA 16
      raw-materialB.supplierB 17 /

    cx(a,v) fixed cost sending vehicle v form [supplier a -> factory]
    / supplierA.vehicle-supplierA 10
      supplierA.vehicle-supplierB 10
      supplierB.vehicle-supplierA 10
      supplierB.vehicle-supplierB 10 /
    
    cxx(m,a) transportation cost unit wooden raw material m form [supplier a -> factory]
    / raw-materialA.supplierA 2
      raw-materialA.supplierB 1
      raw-materialB.supplierA 1
      raw-materialB.supplierB 3 /
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

table cz(e,j,p) transportation cost of waste m [collection-center j -> factory]
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

Free Variable
     z
;

Positive Variables
     y111(b,e,g,p,t) number of product p transported by vehicle g from wholesaller b to retailer e on day t
     bo(e,p,t)
     u1(m,t)
     u_pt(p,t)
     u11(b,p,t)
     u111(e,p,t)      storage inventory or customer e from product p on day t
     yb(e,i,j,p,t)    amount of p product sent retailer e to collection-center j on day t using vehicle i
     yb1(ix,j,m,t)
     y(a,v,m,t)   m material sent by v vahicle from a supplier to the factory on t day
     y1(p,t)
     y11(b,g,p,t)
;

Binary Variables     
     x(a,v,t)
     x1(b,f,t)
     x11(b,e,g,t)
     xb(e,i,j,t)
     xb1(ix,j,t)
;

Equations
     cost        define objective function
;

cost..        z  =e=  (sum(a,sum(v,sum(m,sum(t,c(m,a)*y(a,v,m,t))))))
 + (sum(a,sum(v,sum(t,cx(a,v)*x(a,v,t))))+sum(a,sum(v,sum(m,sum(t,cxx(m,a)*y(a,v,m,t)))))) +
(sum(p,sum(t,ct(p)*y1(p,t)))) + (sum(b,sum(f,sum(t,cs(b,f)*x1(b,f,t))))+ sum(b,sum(g,sum(p,sum(t,cf(b,p)*y11(b,g,p,t)))))) +
(sum(b,sum(e,sum(g,sum(t,cr(b,e,g)*x11(b,e,g,t)))))+sum(b,sum(e,sum(g,sum(p,sum(t,cd(b,e,p)*y111(b,e,g,p,t))))))) +
(sum(m,sum(t,ch(m,t)*u1(m,t))) + sum(p,sum(t,chx(p,t)*u_pt(p,t))) + sum(b,sum(p,sum(t,chxx(b,p,t)*u11(b,p,t)))) + sum(e,sum(p,sum(t,chxxx(e,p,t)*u111(e,p,t))))) +
sum(e,sum(p,sum(t,Pept(e,p,t)*bo(e,p,t)))) + (cinv*sum(a,sum(v,sum(m,sum(t,y(a,v,m,t)))))) + (sum(e,sum(i,sum(j,sum(p,sum(t,ck(e,p)*yb(e,i,j,p,t))))))) +
(sum(e,sum(j,sum(i,sum(t,feij(e,i,j)*xb(e,i,j,t))))) + sum(e,sum(j,sum(i,sum(p,sum(t,cz(e,j,p)*yb(e,i,j,p,t))))))) +
(sum(j,sum(ix,sum(t,fx(ix,j)*xb1(ix,j,t)))) + sum(j,sum(ix,sum(m,sum(t,czx(j,m)*yb1(ix,j,m,t))))) - (cinvx*sum(j,sum(ix,sum(m,sum(t,yb1(ix,j,m,t)))))));


Model scmodel /all/ ;

Solve scmodel using MIP minimizing z ;
