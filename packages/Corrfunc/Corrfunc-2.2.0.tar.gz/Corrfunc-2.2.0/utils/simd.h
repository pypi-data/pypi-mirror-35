

/* For setting up the array that contains the number bits set in a mask */
// Can be used to generate up to 16 bit lookup tables
#   define B2(n)  n,      n+1,      n+1,      n+2
#   define B4(n)  B2(n),  B2(n+1),  B2(n+1),  B2(n+2)
#   define B6(n)  B4(n),  B4(n+1),  B4(n+1),  B4(n+2)
#   define B8(n)  B6(n),  B6(n+1),  B6(n+1),  B6(n+2)
#   define B10(n) B8(n),  B8(n+1),  B8(n+1),  B8(n+2)
#   define B12(n) B10(n), B10(n+1), B10(n+1), B10(n+2)
#   define B14(n) B12(n), B12(n+1), B12(n+1), B12(n+2)
#   define B16(n) B14(0),B14(1), B14(1),   B14(2)
