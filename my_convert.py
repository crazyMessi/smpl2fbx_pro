"""
   Copyright (C) 2017 Autodesk, Inc.
   All rights reserved.

   Use of this software is subject to the terms of the Autodesk license agreement
   provided at the time of installation or download, or which otherwise accompanies
   this software in either electronic or hard copy form.
 
"""

from FbxReadWriter import FbxReadWrite
from SmplObject import SmplObjects
import argparse
import tqdm
import sys

def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_pkl_base', type=str, default='cont/gBR_sFM', help='文件夹')
    parser.add_argument('--fbx_name', type=str, default='character_fixed', help='fbx目录')
    args, unknown = parser.parse_known_args()
    return args

if __name__ == "__main__":
    args = getArg()
    input_pkl_base = './Pkls/%s'%args.input_pkl_base
    fbx_source = './FBXs/%s.fbx'%args.fbx_name
    output_dir = './output/%s/%s/'%(args.fbx_name,args.input_pkl_base)

    smplObjects = SmplObjects(input_pkl_base)
    for pkl_name, smpl_params in tqdm.tqdm(smplObjects):
        try:
            fbxReadWrite = FbxReadWrite(fbx_source)
            fbxReadWrite.addAnimation(pkl_name, smpl_params)
        except AttributeError:
            fbxReadWrite.addAnimation(pkl_name, smpl_params)
        except Exception as e:
            fbxReadWrite.destroy()
            print ("- - Distroy")
            raise e
        finally:
            fbxReadWrite.writeFbx(output_dir, pkl_name)
            fbxReadWrite.destroy()

