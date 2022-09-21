Set t / 1*24 /
i /1*5/
j /1*5/;
Sets
tb(t) base period
tn(t) non-base periods
tt(t) terminal period;

tb(t) = (ord(t) = 1);
tn(t) = (ord(t) > 1);
tt(t) = (ord(t) = card(t));

Variables
level(t), inflow(t), outflow(t), v(t,i);

Equations
balance(t) couple fill levels of reservoir over time
eqn(t,i)
basebalance(t) define fill level for base period;

eqn(t,i).. sum(j,v(t-1,i)*5) =g= v(t,i);
* only for time periods > base period
balance(tn(t)).. level(t) =e= level(t-1) + inflow(t) - outflow(t);
* only for base period
basebalance(tb).. level(tb) =e= 100 + inflow(tb) - outflow(tb);
* lower bound on fill level in terminal period
level.lo(tt) = 100;

*Alternatively (but less readable):
*equation basebalance; basebalance..
*sum(tb, level(tb)) =e= 100 + sum(tb, inflow(tb) - outflow(tb));
