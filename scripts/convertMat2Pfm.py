import numpy as np
import scipy.io as sio
import matplotlib.pyplot as matplot
from pfm_io import writePFM
from pfm_io import readPFM

import cv2

if __name__ == '__main__':
    data = sio.loadmat('/home/tcr/pro_toolkit/PFM_IO/data_io/horse_disparity_median.mat')
   #  data = sio.loadmat('../data_io/horse_disparity_Large.mat')

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

    cv2.imwrite('/home/tcr/pro_toolkit/PFM_IO/data_io/mask1.png',mask1)
    cv2.imwrite('/home/tcr/pro_toolkit/PFM_IO/data_io/specmask.png',specmask)


    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/depthmap.pfm',depthmap)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/Iun.pfm',Iun)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/rho.pfm',rho)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/phi.pfm',phi)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/theta_diffuse.pfm',theta_diffuse)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/theta_spec.pfm',theta_spec)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/N_guide.pfm',N_guide)



    valid_img = np.zeros(mask1.shape, dtype=np.uint8)
    for v in range(mask1.shape[1]):
        for u in range(mask1.shape[0]):
            if mask1[u,v] == 1:
                valid_img[u,v] = 255

    reflect_guess_img = np.zeros(specmask.shape, dtype=np.uint8)
    for v in range(specmask.shape[1]):
        for u in range(specmask.shape[0]):
            if specmask[u,v] == 0:
                reflect_guess_img[u,v] = 255


    left_img = np.zeros(Iun.shape, dtype=np.uint8)
    for v in range(Iun.shape[1]):
        for u in range(Iun.shape[0]):
            for c in range(Iun.shape[2]):
                if Iun[u,v,c] > 1:
                    left_img[u,v,c] = 255
                else:
                    left_img[u,v,c] = round(255 * Iun[u,v,c])

    sgbm_depth_img = depthmap.astype(np.float32)
    sgbm_normal_img = N_guide.astype(np.float32)
    dolp_img = rho.astype(np.float32)
    aolp_img = phi.astype(np.float32)
    diff_zenith = theta_diffuse.astype(np.float32)
    spec_zenith = theta_spec.astype(np.float32)


    cv2.imwrite('/home/tcr/pro_toolkit/PFM_IO/data_io/valid_img.png',valid_img)
    cv2.imwrite('/home/tcr/pro_toolkit/PFM_IO/data_io/reflect_guess_img.png',reflect_guess_img)
    cv2.imwrite('/home/tcr/pro_toolkit/PFM_IO/data_io/left_img.png',left_img)
    
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/sgbm_depth_img.pfm',sgbm_depth_img)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/sgbm_normal_img.pfm',sgbm_normal_img)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/dolp_img.pfm',dolp_img)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/aolp_img.pfm',aolp_img)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/diff_zenith.pfm',diff_zenith)
    writePFM('/home/tcr/pro_toolkit/PFM_IO/data_io/spec_zenith.pfm',spec_zenith)


    # ('specmask', 5673, 1, 0, (820, 1268), dtype('uint8'), <type 'numpy.ndarray'>)
    # ('mask1', 201542, 1, 0, (820, 1268), dtype('uint8'), <type 'numpy.ndarray'>)
    # ('depthmap', nan, nan, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('Iun', 1.002173986887761, 0.0, (820, 1268, 3), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('rho', 0.5704795064364461, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('phi', 3.1415642208496695, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('theta_diffuse', 1.5706571270527543, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('theta_spec', 0.6523129681485362, 0.0, (820, 1268), dtype('<f8'), <type 'numpy.ndarray'>)
    # ('N_guide', nan, nan, (820, 1268, 3), dtype('<f8'), <type 'numpy.ndarray'>)

    test_img = readPFM('/home/tcr/pro_toolkit/PFM_IO/data_io/sgbm_normal_img.pfm').astype(np.float32)
    print(N_guide[100,200,0],N_guide[100,200,0],N_guide[100,200,0])
    print(test_img[100,200,0],test_img[100,200,0],test_img[100,200,0])

    print(N_guide[200,200,0],N_guide[200,200,0],N_guide[200,200,0])
    print(test_img[200,200,0],test_img[200,200,0],test_img[200,200,0])
