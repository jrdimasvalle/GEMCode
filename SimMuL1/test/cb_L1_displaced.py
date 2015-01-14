## pick your scenario:
## 1: 2019
## 2: 2019WithGem
## 3: 2023Muon

scenario = 3

## This configuration runs the DIGI+L1Emulator step
import os
import FWCore.ParameterSet.Config as cms

process = cms.Process("MUTRG")

## Standard sequence
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
if scenario is 1 or scenario is 2:
    process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
    process.load('Configuration.Geometry.GeometryExtended2019_cff')
elif scenario is 3:
    process.load('Configuration.Geometry.GeometryExtended2023MuonReco_cff')
    process.load('Configuration.Geometry.GeometryExtended2023Muon_cff')
else:
    print 'Something wrong with geometry'
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("Configuration.StandardSequences.SimL1Emulator_cff")
process.load("Configuration.StandardSequences.L1Extra_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
if scenario is 1 or scenario is 2:
    process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')
elif scenario is 3:
    process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')    

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

## calibration
from CalibMuon.CSCCalibration.CSCIndexer_cfi import CSCIndexerESProducer
process.CSCIndexerESProducer= CSCIndexerESProducer

from CalibMuon.CSCCalibration.CSCChannelMapper_cfi import CSCChannelMapperESProducer
process.CSCChannelMapperESProducer= CSCChannelMapperESProducer

## input
'''
from .SimMuL1.GEMCSCTriggerSamplesLib import eosfiles
from .GEMValidation.InputFileHelpers import useInputDir
dataset = '_Nu_SLHC12_2023Muon_PU140'
dataset = '_Nu_SLHC12_2023Muon_PU140_geonmo'
process = useInputDir(process, eosfiles[dataset], True)
'''

dataset = "_pt2-50"
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
readFiles.extend([
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_10_1_rbL.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_11_1_MwW.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_1_1_fqY.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_12_1_4Qq.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_13_1_hCM.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_14_1_EkT.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_15_1_oej.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_16_1_1sz.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_17_1_w9J.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_18_1_cQh.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_19_1_AcR.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_20_1_R2d.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_21_1_s6M.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_2_1_S7i.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_22_1_Q2I.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_23_1_PMY.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_24_1_EZq.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_25_1_NHW.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_26_1_L31.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_27_1_CLL.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_28_1_CFj.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_29_1_aXR.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_30_1_24V.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_31_1_X31.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_3_1_qo1.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_32_1_DeV.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_33_1_Rr6.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_34_1_UGX.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_35_1_EDZ.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_36_1_4Rk.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_37_1_qFp.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_38_1_kF4.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_39_1_3Gh.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_40_1_UKm.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_41_1_Qg0.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_4_1_qZ6.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_42_1_R4X.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_43_1_i5t.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_44_1_Jvt.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_45_1_pXh.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_46_1_L2U.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_47_1_S5p.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_48_1_noE.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_49_1_Ouh.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_50_1_5QK.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_51_1_oeE.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_5_1_Gul.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_52_1_9je.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_53_1_Bep.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_54_1_tIe.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_55_1_TrP.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_56_1_4wG.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_57_1_w9h.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_58_1_ibk.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_59_1_R2m.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_60_1_8Hc.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_61_1_xO5.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_6_1_L5L.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_62_1_ZHL.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_63_1_JIe.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_64_1_VnZ.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_65_1_zIC.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_66_1_EfA.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_67_1_mKB.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_68_1_U5P.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_69_1_e2O.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_70_1_owA.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_71_1_t0c.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_7_1_FQr.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_72_1_tU9.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_73_1_yEV.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_74_1_jmG.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_75_1_1Il.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_76_1_cDR.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_77_1_uXU.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_78_1_6o2.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_79_1_uZS.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_80_1_Q2E.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_81_1_sUR.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_8_1_a6K.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_82_1_1s3.root',
'file:/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_GEN_SIM/DarkSUSY_mH_125_mGammaD_0400_ctau_5_14TeV_madgraph452_bridge224_LHE_pythia6_DIGI_RECO/90998fdfabd32352e84b8d7ca7f654f1/out_reco_9_1_23z.root'
])
secFiles.extend( [
                ] )


process.source = cms.Source ("PoolSource",
        duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
        fileNames = readFiles, secondaryFileNames = secFiles,
        inputCommands = cms.untracked.vstring('keep  *_*_*_*')
)
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

physics = False
if not physics:
    ## drop all unnecessary collections
    process.source.inputCommands = cms.untracked.vstring(
        'keep  *_*_*_*',
        'drop *_simCscTriggerPrimitiveDigis_*_*',
        'drop *_simDtTriggerPrimitiveDigis_*_*',
        'drop *_simRpcTriggerDigis_*_*',
        'drop *_simCsctfTrackDigis_*_*',
        'drop *_simDttfDigis_*_*',
        'drop *_simCsctfDigis_*_*',
        'drop *_simGmtDigis_*_*',
        'drop *_l1extraParticles_*_*'
        )
    
## output commands 
theOutDir = ''
theFileName = 'out_L1_ctau5_14TeV_'+ dataset + '.root'
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(theOutDir + theFileName),
    outputCommands = cms.untracked.vstring('keep  *_*_*_*')
)

physics = False
if not physics:
    ## drop all unnecessary collections
    process.output.outputCommands = cms.untracked.vstring(
        'keep  *_*_*_*',
        # drop all CF stuff
        'drop *_mix_*_*',
        # drop tracker simhits
        'drop PSimHits_*_Tracker*_*',
        # drop calorimetry stuff
        'drop PCaloHits_*_*_*',
        'drop L1Calo*_*_*_*',
        'drop L1Gct*_*_*_*',
        # drop calorimetry l1extra
        'drop l1extraL1Em*_*_*_*',
        'drop l1extraL1Jet*_*_*_*',
        'drop l1extraL1EtMiss*_*_*_*',
        # clean up simhits from other detectors
        'drop PSimHits_*_Totem*_*',
        'drop PSimHits_*_FP420*_*',
        'drop PSimHits_*_BSC*_*',
        # drop some not useful muon digis and links
        'drop *_*_MuonCSCStripDigi_*',
        'drop *_*_MuonCSCStripDigiSimLinks_*',
        'drop *SimLink*_*_*_*',
        'drop *RandomEngineStates_*_*_*',
        'drop *_randomEngineStateProducer_*_*'
        )

## custom sequences
process.mul1 = cms.Sequence(
  process.SimL1MuTriggerPrimitives *
  process.SimL1MuTrackFinders *
  process.simRpcTriggerDigis *
  process.simGmtDigis *
  process.L1Extra
)

process.muL1Short = cms.Sequence(
  process.simCscTriggerPrimitiveDigis * 
  process.SimL1MuTrackFinders *
  process.simGmtDigis *
  process.L1Extra
)

## define path-steps
shortRun = False
if shortRun:
    process.L1simulation_step = cms.Path(process.muL1Short)
else: 
    process.L1simulation_step = cms.Path(process.mul1)
process.endjob_step = cms.Path(process.endOfProcess)
process.out_step = cms.EndPath(process.output)

## Schedule definition
process.schedule = cms.Schedule(
    process.L1simulation_step,
    process.endjob_step,
    process.out_step
)

## customization
if scenario is 1:
    from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2019
    process = cust_2019(process)
elif scenario is 2:
    from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2019WithGem
    process = cust_2019WithGem(process)
elif scenario is 3:
    from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2023Muon
    process = cust_2023Muon(process)

## some extra L1 customs
process.l1extraParticles.centralBxOnly = cms.bool(True)
process.l1extraParticles.produceMuonParticles = cms.bool(True)
process.l1extraParticles.produceCaloParticles = cms.bool(False)
process.l1extraParticles.ignoreHtMiss = cms.bool(False)

## messages
print
print 'Input files:'
print '----------------------------------------'
print process.source.fileNames
print
print 'Output file:'
print '----------------------------------------'
print process.output.fileName
print 
