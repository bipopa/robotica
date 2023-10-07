import numpy as np
def orientacion(Tdes,l0,l1,l2,l3):
    pmx= Tdes[0,3]-l3*Tdes[0,2]
    pmy= Tdes[1,3]-l3*Tdes[1,2]
    pmz= Tdes[2,3]-l3*Tdes[2,2]
    
    q1=np.arctan2(pmy,pmx)
    if q1<0:
        q1+=np.pi
    R=np.sqrt(pmx**2+pmy**2+(pmz-l0)**2)
    r=np.sqrt(pmx**2+pmy**2)

    cq3 = (R**2-l1**2-l2**2)/(2*l1*l2)
    q3 = np.arctan2(np.sqrt(1-cq3**2),cq3)
    q2 = np.pi/2+np.arctan2(-pmz+l0,r)-np.arctan2(l2*np.sin(q3),l1+l2*np.cos(q3))
    # Resultado

    ROT03=[[-np.cos(q1)*np.cos(q2 + q3), np.sin(q1), -np.sin(q2 + q3)*np.cos(q1)], 
[-np.sin(q1)*np.cos(q2 + q3), -np.cos(q1), -np.sin(q1)*np.sin(q2 + q3)], 
[-np.sin(q2 + q3), 0, np.cos(q2 + q3)]] 
    
    ROT06=Tdes[0:3,0:3]

    ROT36=np.transpose(ROT03) .dot(ROT06)
    nx= ROT36[0,0]
    ox= ROT36[0,1]
    ax= ROT36[0,2]
    ny= ROT36[1,0]
    oy= ROT36[1,1]
    ay= ROT36[1,2]
    nz= ROT36[2,0]
    oz= ROT36[2,1]
    az= ROT36[2,2]
    q4=np.arctan2(ay,ax)
    q5=np.arctan2(ay/np.sin(q4),az)
    q6=np.arctan2(oz,-nz)
    print (nx,ny,nz)

    q = np.array([q1, q2, q3, q4, q5, q6]).T
    return (nx,ox,ny,oy,nz,oz)
