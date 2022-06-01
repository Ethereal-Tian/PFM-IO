import numpy as np
import scipy.io as sio
import matplotlib.pyplot as matplot
from pfm_io import writePFM
import cv2

if __name__ == '__main__':
 # data = sio.loadmat('../data/horse_disparity_median.mat')
    data = sio.loadmat('../data/horse_disparity_Large.mat')

    polAng = data['polAng'].ravel()

    depthmap = data['depthmap']
    cam1 = data['cam1'][0][0]
    mask1 = cam1['mask']
    specmask = cam1['specmask']

    P1 = cam1['P']
    Iun = cam1['Iun_est']
    rho = cam1['rho_est']
    phi = cam1['phi_est']
    theta_diffuse = cam1['theta_est_diffuse']
    theta_spec = cam1['theta_est_spec']
    N_guide = data['N_guide']

    print("mask1",np.sum(mask1),np.max(mask1),np.min(mask1),mask1.shape,mask1.dtype,type(mask1))
    print("specmask",np.sum(specmask),np.max(specmask),np.min(specmask),specmask.shape,specmask.dtype,type(specmask))

    print("depthmap",np.max(depthmap),np.min(depthmap),specmask.shape,depthmap.dtype,type(depthmap))
    print("Iun",np.max(Iun),np.min(Iun),Iun.shape,Iun.dtype,type(Iun))
    print("rho",np.max(rho),np.min(rho),rho.shape,rho.dtype,type(rho))
    print("phi",np.max(phi),np.min(phi),phi.shape,phi.dtype,type(phi))
    print("theta_diffuse",np.max(theta_diffuse),np.min(theta_diffuse),phi.shape,theta_diffuse.dtype,type(theta_diffuse))
    print("theta_spec",np.max(theta_spec),np.min(theta_spec),theta_spec.shape,theta_spec.dtype,type(theta_spec))
    print("N_guide",np.max(N_guide),np.min(N_guide),N_guide.shape,N_guide.dtype,type(N_guide))

    cv2.imwrite('/home/tcr/pro_toolkit/PFM_IO/data/mask1.png',mask1)
    cv2.imwrite('/home/tcr/pro_toolkit/PFM_IO/data/specmask.png',specmask)
    
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data/depthmap.pfm',depthmap)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data/Iun.pfm',Iun)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data/rho.pfm',rho)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data/phi.pfm',phi)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data/theta_diffuse.pfm',theta_diffuse)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data/theta_spec.pfm',theta_spec)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data/N_guide.pfm',N_guide)

    # ('specmask', 5673, 1, 0, (820, 1268), dtype('uint8'), <type 'numpy.ndarray'>)
    # ('mask1', 201542, 1, 0, (820, 1268), dtype('uint8'), <type 'numpy.ndarray'>)
    # ('depthmap', nan, nan, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('Iun', 1.002173986887761, 0.0, (820, 1268, 3), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('rho', 0.5704795064364461, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('phi', 3.1415642208496695, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('theta_diffuse', 1.5706571270527543, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('theta_spec', 0.6523129681485362, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('N_guide', nan, nan, (820, 1268, 3), dtype('<f8'), <type 'numpy.ndarray'>)

