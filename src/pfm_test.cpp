/*
 *     PFM_IO
 *
 *     Authors:  Antoine TOISOUL LE CANN
 *
 *     Copyright © 2016 Antoine TOISOUL LE CANN
 *              All rights reserved
 *
 *
 * PFM_IO is free software: you can redistribute it and/or modify
 *
 * it under the terms of the GNU Lesser General Public License as published by
 *
 * the Free Software Foundation, either version 3 of the License, or
 *
 * (at your option) any later version.
 *
 * PFM_IO is distributed in the hope that it will be useful,
 *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 *
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * \file main.cpp
 * \brief Example of how to read and save PFM files.
 * \author Antoine Toisoul Le Cann
 * \date September, 1st, 2016
 *
 * Example of how to read and save PFM files.
 */

#include <iostream>
#include <string>

#include "PFMReadWrite.h"

cv::Point3d pixel2pt(cv::Vec3f pixel){
    return cv::Point3d(pixel[0],pixel[1],pixel[2]);
}

int main(){
  cv::Mat read_depth_img = loadPFM(std::string("/home/tcr/pro_toolkit/PFM_IO/data_io/sgbm_depth_img.pfm"));
  cv::Mat read_normal_img = loadPFM(std::string("/home/tcr/pro_toolkit/PFM_IO/data_io/sgbm_normal_img.pfm"));

  std::cout<<"read_depth_img.cols "<<read_depth_img.cols<<std::endl;
  std::cout<<"read_normal_img.rows "<<read_normal_img.rows<<std::endl;

  std::cout<<read_depth_img.at<float>(200,200)<<std::endl;
  std::cout<<read_depth_img.at<float>(100,200)<<std::endl;
  std::cout<<read_depth_img.at<float>(200,100)<<std::endl;

  std::cout<<pixel2pt(read_normal_img.at<cv::Vec3f>(200,200))<<std::endl;

  return 0;
}