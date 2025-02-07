import hindilang

if __name__ == "_main_":
    code = r'''
        // Arithmetic test code:
        // Declaration and assignment use "ank" (or a type keyword) and printing is done by "chhapna".

        ank a = 10;
        ank b = 5;
        ank c = a + b;
        chhapna(c);    // Expected output: 15

        ank d = c - b;
        chhapna(d);    // Expected output: 10

        ank e = d * b;
        chhapna(e);    // Expected output: 50

        ank f = e / b;
        chhapna(f);    // Expected output: 10   (integer division)

        ank g = e % b;
        chhapna(g);    // Expected output: 0
    '''
    
    hindilang.run_code(code)