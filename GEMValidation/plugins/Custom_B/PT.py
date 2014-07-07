import ROOT

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()


tree = "GEMCSCAnalyzer/trk_eff_ME11"
den = "pt>2"
num = "pt>2 && has_lct>0"

f2 = ROOT.TFile("hp_CMSSW14_usingL1SLHC7_PU140_TMB_Baseline_2_eff.root")
t2 = f2.Get("GEMCSCAnalyzer/trk_eff_ME11")
e2 = ROOT.TH1F("e2","e2",40,0,55)
t2.Draw("pt >> e2",num)
eb = ROOT.TH1F("eb","eb",40,0,55)
t2.Draw("pt >> eb",den)
#e2.Divide(eb)

e2.SetLineColor(ROOT.kRed)
e2.SetLineWidth(2)
e2.SetLineStyle(1)

b1 = ROOT.TH1F("b1","b1",40,0,55)
b1.GetYaxis().SetRangeUser(0,5000)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
#b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle("Pt of 1.5 < |#eta| < 2.5" )
b1.SetStats(0)
b1.Draw()


e2.SetLineWidth(3)
eb.SetLineWidth(3)

#eb.Draw("same")
e2.Draw("same")


legend = ROOT.TLegend(0.25,0.13,0.72,0.42)
legend.SetFillColor(ROOT.kWhite)
#legend.SetBorderSize(0)
#legend.SetFillStyle(0)
legend.SetHeader("PU140 and 2<Pt<50")
legend.AddEntry(e2,"TMB Baseline 2: has_lct>0","l")
#legend.AddEntry(eb,"TMB Baseline 2: ","l")
legend.Draw("same")

c1.SaveAs("2LCT_reco_eff_PU140.pdf")
c1.SaveAs("2LCT_reco_eff_PU140.png")

