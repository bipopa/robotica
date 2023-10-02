import numpy as np

def cinematica_inversa_centauri(Tdes,l0,l1,l2,l3):
    pmx= Tdes[0,3]-l3*Tdes[0,2]
    pmy= Tdes[1,3]-l3*Tdes[1,2]
    pmz= Tdes[2,3]-l3*Tdes[2,2]
    print("pmx=",pmx, "pmy=", pmy, "pmz=", pmz)
    q1=np.arctan2(pmy,pmx)
    if q1<0:
        q1+=np.pi
    R=np.sqrt(pmx**2+pmy**2+(pmz-l0)**2)
    r=np.sqrt(pmx**2+pmy**2)
    #print("R=",R, "r=", r)
    # Valores articulares calculados
    #calpha=(R)/(2*l1)
    
    #alpha= np.arctan2(np.sqrt(1-calpha**2),calpha)
    #print("alpha",np.degrees(aalpha))
    #beta= -np.arctan2(pmz-l0,r)
    #print("beta",np.degrees(beta))
    #q2=0*np.pi/2-beta-alpha
    cq3 = (R**2-l1**2-l2**2)/(2*l1*l2)
    q3 = np.arctan2(np.sqrt(1-cq3**2),cq3)
    q2 = np.pi/2+np.arctan2(-pmz+l0,r)-np.arctan2(l2*np.sin(q3),l1+l2*np.cos(q3))
    # Resultado
    #print(np.degrees(q1))
    ROT03=[[-np.cos(q1)*np.cos(q2 + q3), np.sin(q1), -np.sin(q2 + q3)*np.cos(q1)], 
[-np.sin(q1)*np.cos(q2 + q3), -np.cos(q1), -np.sin(q1)*np.sin(q2 + q3)], 
[-np.sin(q2 + q3), 0, np.cos(q2 + q3)]] 
    #print(np.round(ROT03,4))
    
    ROT06=Tdes[0:3,0:3]
    #print(np.round(ROT06,4))
    ROT36=np.transpose(ROT03) .dot(ROT06)
    #print(np.round(ROT36,4))
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
    

    return (np.degrees(q1), np.degrees(q2), np.degrees(q3), np.degrees(q4), np.degrees(q5), np.degrees(q6))
