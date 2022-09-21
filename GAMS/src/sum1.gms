SETS
    I /1*3/
    J /1*2/
    K /1*2/
    M /1*2/
    N /1*3/;

PARAMETERS

    X(I) /1 1,2 2,3 3/
    Z(I) /1 2,2 4,3 6/;

TABLE Y(I,J)
      1 2
    1 2 3
    2 4 1
    3 1 4;

TABLE V(I,J)
      1 2
    1 2 3
    2 4 1
    3 1 4;

TABLE P(I, J, K)
      1.1 1.2 2.1 2.2
    1   1   3   5   7
    2   2   4   6   8
    3   1   2   3   4;

TABLE Q(M, N)
      1  2  3
    1 1  5 10
    2 10 5  1;
    
PARAMETER
    SUM1 SUM OF AN ITEM;
    SUM1 = SUM(I, X(I));
    
DISPLAY SUM1;

PARAMETER
    SUM2 MULTIPLE SUMS;
    SUM2 = SUM((I,J), Y(I,J));
    
DISPLAY SUM2;

DISPLAY J;