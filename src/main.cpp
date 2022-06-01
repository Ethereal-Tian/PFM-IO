/*
 *     PFM_ReadWrite
 *
 *     Authors:  Antoine TOISOUL LE CANN
 *
 *     Copyright © 2016 Antoine TOISOUL LE CANN
 *              All rights reserved
 *
 *
 * PFM_ReadWrite is free software: you can redistribute it and/or modify
 *
 * it under the terms of the GNU Lesser General Public License as published by
 *
 * the Free Software Foundation, either version 3 of the License, or
 *
 * (at your option) any later version.
 *
 * PFM_ReadWrite is distributed in the hope that it will be useful,
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

int main(){
  cv::Mat f1_img = cv::Mat::zeros(2,3,CV_32FC1);
  for(int u = 0;u < f1_img.cols;u++){
      for(int v = 0;v < f1_img.rows;v++){
          f1_img.at<float>(v,u) = 1.2 * v + 10.0  * u; 
      }
  }
  
  cv::Mat f3_img = cv::Mat::zeros(2,3,CV_32FC3);
  for(int u = 0;u < f1_img.cols;u++){
      for(int v = 0;v < f1_img.rows;v++){
          for(int c = 0; c < 3;c++){
              f3_img.at<cv::Vec3f>(v,u)[c] = 1.2 * v + 10.0  * u + 100.0 * c; 
          }
      }
  }

  savePFM(f1_img, "/home/tcr/pro_toolkit/PFM_ReadWrite/data/f1.pfm");
  savePFM(f3_img, "/home/tcr/pro_toolkit/PFM_ReadWrite/data/f3.pfm");


  cv::Mat f1_img2 = loadPFM(std::string("/home/tcr/pro_toolkit/PFM_ReadWrite/data/f1.pfm"));
  cv::Mat f3_img2 = loadPFM(std::string("/home/tcr/pro_toolkit/PFM_ReadWrite/data/f3.pfm"));

  std::cout<<"f1_img2.cols "<<f1_img2.cols<<std::endl;
  std::cout<<"f1_img2.rows "<<f1_img2.rows<<std::endl;
  for(int u = 0;u < f1_img.cols;u++){
    for(int v = 0;v < f1_img.rows;v++){
      std::cout<<cv::Point2d(u,v)<<f1_img.at<float>(v,u)<<" "<<f1_img2.at<float>(v,u)<<std::endl;
    }
  }
  
  std::cout<<"f3_img2.cols "<<f3_img2.cols<<std::endl;
  std::cout<<"f3_img2.rows "<<f3_img2.rows<<std::endl;
  for(int u = 0;u < f3_img.cols;u++){
    for(int v = 0;v < f3_img.rows;v++){
      cv::Point3d pt1(f3_img.at<cv::Vec3f>(v,u)[0],f3_img.at<cv::Vec3f>(v,u)[1],f3_img.at<cv::Vec3f>(v,u)[2]);
      cv::Point3d pt2(f3_img2.at<cv::Vec3f>(v,u)[0],f3_img2.at<cv::Vec3f>(v,u)[1],f3_img2.at<cv::Vec3f>(v,u)[2]);
      std::cout<<cv::Point2d(u,v)<<pt1<<pt2<<std::endl;
    }
  }

  return 0;
}