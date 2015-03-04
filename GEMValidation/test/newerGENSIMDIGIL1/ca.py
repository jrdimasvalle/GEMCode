import FWCore.ParameterSet.Config as cms

process = cms.Process("GEMCSCANA")

## Standard sequence
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2023Muon_cff')
process.load('Configuration.Geometry.GeometryExtended2023MuonReco_cff')
###process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
###process.load('Configuration.Geometry.GeometryExtended2019_cff')

process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

## TrackingComponentsRecord required for matchers
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')

#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:out_L1.root')
#)

process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100)

## input
from GEMCode.SimMuL1.GEMCSCTriggerSamplesLib import *
from GEMCode.GEMValidation.InputFileHelpers import *



maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 

readFiles.extend([
       'file:/eos/uscms/store/user/jdimasva/January_2014/Non_Displaced_L1/out_L1_pt2-50.root'
])
secFiles.extend( [
               ] )

SameWheelOnly = True

if SameWheelOnly:
    whab = "SameWheel"
else:
    whab = "All_Wheel"
    
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

events=-1
process.maxEvents = cms.untracked.PSet(
     input = cms.untracked.int32(events)
)
outputFileName = 'DT_nonDsplaced_modified.root'

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(outputFileName)
)

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

##Change to handle old partition geometry for SLHC7 and arround

###from Geometry.GEMGeometry.gemGeometryCustoms import custom_GE11_6partitions_v1
###process = custom_GE11_6partitions_v1(process)

## global tag for upgrade studies
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')
##process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')
# the analyzer configuration
def enum(*sequential, **named):
  enums = dict(zip(sequential, range(len(sequential))), **named)
  return type('Enum', (), enums)
Stations = enum('ALL','ME11','ME1a','ME1b','ME12','ME13','ME21','ME22','ME31','ME32','ME41','ME42')

StationsDT=enum('ALL', 'MB01', 'MB11', 'MB21', 'MB02', 'MB12', 'MB22', 'MB03', 'MB13', 'MB23', 'MB04', 'MB14', 'MB24', 'MB11n', 'MB21n', 'MB12n', 'MB22n', 'MB13n', 'MB23n', 'MB14n', 'MB24n')


from GEMCode.GEMValidation.simTrackMatching_cfi import SimTrackMatching
process.GEMCSCAnalyzer = cms.EDAnalyzer("GEMCSCAnalyzer",
    verbose = cms.untracked.int32(0),
    stationsToUse = cms.vint32(Stations.ME11,Stations.ME1a,Stations.ME1b,
                               Stations.ME21,Stations.ME31,Stations.ME41),
    DTSTationsToUSE = cms.vint32(StationsDT.ALL,StationsDT.MB01, StationsDT.MB11,StationsDT.MB21,StationsDT.MB02,StationsDT.MB12,StationsDT.MB22,StationsDT.MB03,StationsDT.MB13,StationsDT.MB23,StationsDT.MB04,StationsDT.MB14,StationsDT.MB24,StationsDT.MB11n, StationsDT.MB21n, StationsDT.MB12n, StationsDT.MB22n, StationsDT.MB13n, StationsDT.MB23n, StationsDT.MB14n, StationsDT.MB24n),
    simTrackMatching = SimTrackMatching
)



matching = process.GEMCSCAnalyzer.simTrackMatching
matching.simTrack.minPt = 2.0
matching.gemRecHit.input = ""
"""
matching.cscTfTrack.input = ""
matching.tfCand.input = ""
matching.gmtCand.input = ""
matching.l1Extra.input = ""
"""
doGem = False
if doGem:
  matching.cscSimHit.minNHitsChamber = 3
  matching.cscStripDigi.minNHitsChamber = 3
  matching.cscWireDigi.minNHitsChamber = 3
  matching.cscCLCT.minNHitsChamber = 3
  matching.cscALCT.minNHitsChamber = 3
  matching.cscLCT.minNHitsChamber = 3
  matching.cscLCT.matchAlctGem = True
  matching.cscMPLCT.minNHitsChamber = 3


if SameWheelOnly:
    process.GEMCSCAnalyzer.simTrackMatching.dtSimHit.sameWheelOnly = cms.bool(True);
else:
    process.GEMCSCAnalyzer.simTrackMatching.dtSimHit.sameWheelOnly = cms.bool(False);

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True), SkipEvent = cms.untracked.vstring("CSCTriggerNumbering::InvalidInput")
)

process.p = cms.Path(process.GEMCSCAnalyzer)
mat = process.GEMCSCAnalyzer.simTrackMatching
mat.simTrack.minEta = cms.double(-2.5)
mat.simTrack.maxEta = cms.double(2.5)
mat.me0Segment.run = cms.bool(False)
mat.me0Muon.run = cms.bool(False)
mat.me0SimHit.run = cms.bool(False)
mat.me0SimHit.simMuOnly = cms.bool(False)
mat.me0RecHit.run = cms.bool(False)


## messages
print
print 'Input files:'
print '----------------------------------------'
print process.source.fileNames
print
print 'Output file:'
print '----------------------------------------'
print process.TFileService.fileName
print
