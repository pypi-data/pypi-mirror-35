"""
Vector calculus module
----------------------


"""
from __future__ import division, print_function
from sympy import simplify, Matrix, S, diff, symbols, zeros

x, y, z = symbols("x y z")


def scale_coeff(r_vec, coords):
    """
    Compyte scale coefficients for the vector
    tranform given by r_vec.
    
    Parameters
    -------
    r_vec : Matrix (3, 1)
        Transform vector (x, y, z) as a function of coordinates
        u1, u2, u3.
    coords : Tupl (3)
        Coordinates for the new reference system.
        
    Returns
    -------
    h_vec : Tuple (3)
        Scale coefficients.
    """
    if type(r_vec) == list:
        r_vec = Matrix(r_vec)
    u1, u2, u3 = coords
    h1 = simplify((r_vec.diff(u1)).norm())
    h2 = simplify((r_vec.diff(u2)).norm())
    h3 = simplify((r_vec.diff(u3)).norm())
    return h1, h2, h3

#%% Vector analysis
def levi_civita(i, j, k):
    """Levi-Civita symbol"""
    return (i - j)*(j - k)*(k - i)/S(2)


def dual_tensor(vec):
    r"""Compute the dual tensor for an axial vector

    In index notation, the dual is defined by
    
    .. math::
        
        C_{ij} = \epsilon_{ijk} C_k

    where :math:`\epsilon_{ijk}` is the Levi-Civita symbol.
        
    
    Parameters
    ----------
    vec : SymPy expression
        Axial vector.
    
    Returns
    -------
    dual: Matrix (3, 3)
    Second order matrix that is dual of vec.

    References
    ----------

    .. [ARFKEN] George Arfken, Hans J. Weber and Frank Harris.
        Mathematical methods for physicists, Elsevier, 2013.

    """
    dual = zeros(3, 3)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                dual[i,j] = dual[i, j] + levi_civita(i, j, k) * vec[k]       
    return dual


def dual_vector(tensor):
    r"""Compute the dual (axial) vector for an anti-symmetric tensor

    In index notation, the dual is defined by
    
    .. math::
        
        C_{i} = \frac{1}{2}\epsilon_{ijk} C_{jk}

    where :math:`\epsilon_{ijk}` is the Levi-Civita symbol.

    References
    ----------

    .. [ARFKEN] George Arfken, Hans J. Weber and Frank Harris.
        Mathematical methods for physicists, Elsevier, 2013.

    """
    if not tensor.is_anti_symmetric():
        raise TypeError("The tensor should be antisymmetric")
    else:
        dual = Matrix([0, 0, 0])
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    dual[i] = dual[i] + levi_civita(i, j, k) * tensor[j, k]
        return dual/S(2)


#%% Differential operators
def grad(u, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Compute the gradient of a scalara function phi.

    Parameters
    ----------
    u : SymPy expression
        Scalar function to compute the gradient from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional
        parameters, and it takes a cartesian (x, y, z), as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.
        
    Returns
    -------
    gradient: Matrix (3, 1)
        Column vector with the components of the gradient.
    """
    return Matrix(3, 1, lambda i, j: u.diff(coords[i])/h_vec[j])


def grad_vec(A, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Gradient of a vector function A.
    
    Parameters
    ----------
    A : Matrix (3, 1), list
        Vector function to compute the gradient from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional parameter
        it takes (x, y, z) as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.
        
    Returns
    -------
    gradient: Matrix (3, 3)
        Matrix with the components of the gradient. The position (i, j) has
        as components diff(A[i], coords[j].
    """ 
    return Matrix(3, 3, lambda i, j: (S(1)/h_vec[j])*A[i].diff(coords[j]))


def sym_grad(A, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Symmetric part of the gradient of a vector function A.
    
    Parameters
    ----------
    A : Matrix (3, 1), list
        Vector function to compute the gradient from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional parameter
        it takes (x, y, z) as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.
        
    Returns
    -------
    sym_grad: Matrix (3, 3)
        Matrix with the components of the symmetric part of the gradient.
        The position (i, j) has as components diff(A[i], coords[j].
    """ 
    G = grad_vec(A, coords=(x, y, z), h_vec=(1, 1, 1))
    return S(1)/2*(G + G.T)


def antisym_grad(A, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Antisymmetric part of the gradient of a vector function A.
    
    Parameters
    ----------
    A : Matrix (3, 1), list
        Vector function to compute the gradient from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional parameter
        it takes (x, y, z) as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.
        
    Returns
    -------
    antisym_grad: Matrix (3, 3)
        Matrix with the components of the antisymmetric part of the gradient.
        The position (i, j) has as components diff(A[i], coords[j].
    """ 
    G = grad_vec(A, coords=(x, y, z), h_vec=(1, 1, 1))
    return S(1)/2*(G - G.T)


def div(A, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Divergence of the vector function A.
    
    Parameters
    ----------
    A : Matrix, list
        Scalar function to compute the divergence from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional parameter
        it takes (x, y, z) as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.
        
    Returns
    -------
    divergence: SymPy expression
        Divergence of A.
    """  
    h = h_vec[0]*h_vec[1]*h_vec[2]
    aux = simplify((S(1)/h)*sum(diff(A[k]*h/h_vec[k], coords[k])
                                for k in range(3)))
    return aux 


def curl(A, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Curl of a function vector A.
    
    Parameters
    ----------
    A : Matrix, List
        Vector function to compute the curl from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional parameter
        it takes (x, y, z) as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.

    Returns
    -------
    curl : Matrix (3, 1)
        Column vector with the curl of A.
    """  
    perm = lambda i, j, k: (i - j)*(j - k)*(k - i)/S(2)
    h = h_vec[0]*h_vec[1]*h_vec[2]
    aux = [(S(1)/h)*sum(perm(i, j, k)*h_vec[i]*diff(A[k]*h_vec[k], coords[j])
           for j in range(3) for k in range(3))
           for i in range(3)]
    return Matrix(aux)  


def lap(u, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Laplacian of the scalar function phi.
    
    Parameters
    ----------
    u : SymPy expression
        Scalar function to compute the gradient from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional
        parameters, and it takes a cartesian (x, y, z), as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.
        
    Returns
    -------
    laplacian: Sympy expression
        Laplacian of phi.
    """
    h = S(h_vec[0]*h_vec[1]*h_vec[2])
    return sum([1/h*diff(h/h_vec[k]**2*u.diff(coords[k]), coords[k])
                for k in range(3)])


def lap_vec(A, coords=(x, y, z), h_vec=(1, 1, 1)):
    """
    Laplacian of a vector function A.
    
    Parameters
    ----------
    A : Matrix, List
        Vector function to compute the curl from.
    coords : Tuple (3), optional
        Coordinates for the new reference system. This is an optional parameter
        it takes (x, y, z) as default.
    h_vec : Tuple (3), optional
        Scale coefficients for the new coordinate system. It takes
        (1, 1, 1), as default.
        
    Returns
    -------
    laplacian : Matrix (3, 1)
        Column vector with the components of the Laplacian.
    """  
    return grad(div(A, coords=coords, h_vec=h_vec), coords=coords, h_vec=h_vec) -\
           curl(curl(A, coords=coords, h_vec=h_vec), coords=coords, h_vec=h_vec)
       


if __name__ == "__main__":
    import doctest
    doctest.testmod()