import ROOT
from triggerPlotHelpers import *

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()

f1 = "hp_dimu_CMSSW_6_2_0_SLHC14_upgrade2019_w3PU140_TMB_Baseline_1_eff.root"
f2 = "hp_dimu_CMSSW_6_2_0_SLHC14_upgrade2019_w3PU140_useDeadTimeZoning_eff.root"
f3 = "hp_dimu_CMSSW_6_2_0_SLHC14_upgrade2019_w3PU140_useDynamicStateMachineZone_eff.root"
f4 = "hp_dimu_CMSSW_6_2_0_SLHC14_upgrade2019_w3PU140_clctPidThreshPretrig_eff.root"
f5 = "hp_dimu_CMSSW_6_2_0_SLHC14_upgrade2019_w3PU140_clctMinSeparation_eff.root"
f6 = "hp_dimu_CMSSW_6_2_0_SLHC14_upgrade2019_w3PU140_TMB_Baseline_2_eff.root"

t1 = "TMB Baseline 1"
t2 = "useDeadTimeZoning: False to True"
t3 = "useDynamicStateMachineZone: False to True"
t4 = "clctPidThreshPretrig: 2 to 4"
t5 = "clctMinSeparation: 10 to 5"
t6 = "TMB Baseline 2"
def setEffHisto2(num_name, den_name, dir, nrebin, lcolor, lstyle, lwidth, mcolor, mstyle,
                htitle, xtitle, ytitle, x_range, y_range):
    hd = getH(dir, den_name)
    hn = getH(dir, num_name)
    hd.Sumw2()
    hn.Sumw2()
    myRebin(hd, nrebin)
    myRebin(hn, nrebin)
    heff = hn.Clone(num_name+"_eff")
    hd.Sumw2()
    heff.Sumw2()
    heff.Divide(heff,hd)
    heff.SetLineColor(lcolor)
    heff.SetLineStyle(lstyle)
    heff.SetMarkerColor(mcolor)
    heff.SetMarkerStyle(mstyle)
    heff.SetLineWidth(lwidth)
    heff.SetTitle(htitle)
    heff.GetXaxis().SetTitle(xtitle)
    heff.GetYaxis().SetTitle(ytitle)
    heff.GetXaxis().SetRangeUser(x_range[0],x_range[1])
    heff.GetYaxis().SetRangeUser(y_range[0],y_range[1])
    heff.GetXaxis().SetTitleSize(0.05)
    heff.GetXaxis().SetTitleOffset(1.)
    heff.GetYaxis().SetTitleSize(0.05)
    heff.GetYaxis().SetTitleOffset(1.)
    heff.GetXaxis().SetLabelOffset(0.015)
    heff.GetYaxis().SetLabelOffset(0.015)
    heff.GetXaxis().SetLabelSize(0.05)
    heff.GetYaxis().SetLabelSize(0.05)
    return heff
def getEff(file,dir,den,num):
    f = ROOT.TFile(file)
    t = f.Get(dir)
    h1 = ROOT.TH1F("h1","h1",40,1.5,2.5)
    t.Draw("eta >> h1",den)
    h2 = ROOT.TH1F("h2","h2",40,1.5,2.5)
    t.Draw("eta >> h2",num)
    e = ROOT.TEfficiency(h2,h1)
    return e

input_dir=""
d1 = getRootDirectory(input_dir, f1) 
d2 = getRootDirectory(input_dir, f2) 
d3 = getRootDirectory(input_dir, f3) 
d4 = getRootDirectory(input_dir, f4) 
d5 = getRootDirectory(input_dir, f5) 
d6 = getRootDirectory(input_dir, f6)
yrange = [0.5,1.02]
xrange = [1.5,2.5]    
xTitle = "Sim track #eta"
yTitle = "Efficiency"
topTitle = ""
etareb=1
h1 = setEffHisto2("h_eta_me1_after_clct_okClct","h_eta_me1_initial",d1, etareb, ROOT.kRed+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)
h2 = setEffHisto2("h_eta_me1_after_clct_okClct","h_eta_me1_initial",d2, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 4, topTitle,xTitle,yTitle,xrange,yrange)
h3 = setEffHisto2("h_eta_me1_after_clct_okClct","h_eta_me1_initial",d3, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 20, topTitle,xTitle,yTitle,xrange,yrange)
h4 = setEffHisto2("h_eta_me1_after_clct_okClct","h_eta_me1_initial",d4, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 21, topTitle,xTitle,yTitle,xrange,yrange)
h5 = setEffHisto2("h_eta_me1_after_clct_okClct","h_eta_me1_initial",d5, etareb, ROOT.kGreen+2, 1, 2, ROOT.kGreen+2, 22, topTitle,xTitle,yTitle,xrange,yrange)
h6 = setEffHisto2("h_eta_me1_after_clct_okClct","h_eta_me1_initial",d6, etareb, ROOT.kBlue+1, 1, 2, ROOT.kRed, 4, topTitle,xTitle,yTitle,xrange,yrange)

b1 = ROOT.TH1F("b1","b1",40,1.4,2.5)
b1.GetYaxis().SetRangeUser(0.5,1.01)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("CLCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle("PU140" + " "*22 + "Comparison between Analyzers on SLHC14")
b1.SetStats(0)

treename = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>2"
num = "has_csc_sh>0 && has_clct>0 && pt>2"

e1 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_1_eff.root",treename,den,num)
e2 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_useDeadTimeZoning_eff.root",treename,den,num)
e3 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_useDynamicStateMachineZone_eff.root",treename,den,num)
e4 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_clctPidThreshPretrig_eff.root",treename,den,num)
e5 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_clctMinSeparation_eff.root",treename,den,num)
e6 = getEff("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root",treename,den,num)
#e7 = getEff("Note_Upgrade_PU140_TMB8_eff.root",treename,den,num)
#e8 = getEff("Note_Upgrade_PU140_SLHC_eff.root",treename,den,num)

#Change the number for different legend/histograms
opq=t6
m=e6
n=h6


m.SetLineColor(ROOT.kOrange)
m.SetFillColor(ROOT.kOrange)
m.SetLineWidth(2)



b1.Draw()
m.Draw("same e3")
if (n==h1 or n==h6):
    oo="l"
    n.Draw("same hist")
else:
   oo="p"
   n.Draw("same hist P")

legend = ROOT.TLegend(0.23,0.16,0.82,0.38)
legend.SetFillColor(ROOT.kWhite)
legend.SetHeader(opq)
legend.AddEntry(m,"Tree Based Analyzer","l")
legend.AddEntry(n,"Histogram Based Analyzer",oo)

legend.Draw("same")

c1.SaveAs("CLCT_reco_eff_PU140.png")
