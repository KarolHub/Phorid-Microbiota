library(Hmsc)
da1 = read.csv(file="data/SPH_Bact_OTU_v6.txt",sep="\t")
da2 = read.csv(file="data/SPH_Bact_ZOTU_v6.txt",sep="\t")
da3 = read.csv(file="data/SPH_Wolb_ZOTU_v6.txt",sep="\t")

all(da1$sample_ID==da2$sample_ID)
all(da1$sample_ID==da3$sample_ID)

colnames(da2)[1:20]
studyDesign = data.frame(insect.individual = as.factor(da2$sample_ID), site = as.factor(da2$site),
                         insect.sp = as.factor(da2$insect_species), 
                         insect.gt = as.factor(da2$insect_genotype))

XData = data.frame(season = as.factor(da2$season), sex = as.factor(da2$sex))

rL.insect.individual = HmscRandomLevel(units = levels(studyDesign$insect.individual))
rL.site = HmscRandomLevel(units = levels(studyDesign$site))
rL.insect.sp = HmscRandomLevel(units = levels(studyDesign$insect.sp))
rL.insect.gt = HmscRandomLevel(units = levels(studyDesign$insect.gt))

Y.BO = as.matrix(da1[,-(1:6)])
Y.BO.pa = 1*(Y.BO>0)
Y.BO.abuc = Y.BO
Y.BO.abuc[Y.BO==0] = NA
Y.BO.abuc = scale(log(Y.BO.abuc))

Y.BZ = as.matrix(da2[,-(1:6)])
Y.BZ.pa = 1*(Y.BZ>0)
Y.BZ.abuc = Y.BZ
Y.BZ.abuc[Y.BZ==0] = NA
Y.BZ.abuc = scale(log(Y.BZ.abuc))

Y.WZ = as.matrix(da3[,-(1:6)])
Y.WZ.pa = 1*(Y.WZ>0)
Y.WZ.abuc = Y.WZ
Y.WZ.abuc[Y.WZ==0] = NA
Y.WZ.abuc = scale(log(Y.WZ.abuc))

m.BO.pa = Hmsc(Y=Y.BO.pa,
               XData = XData, XFormula = ~.,
               studyDesign = studyDesign,
               ranLevels = list(insect.individual = rL.insect.individual, site = rL.site, insect.sp = rL.insect.sp, insect.gt = rL.insect.gt),
               distr = "probit"
)

m.BO.abuc = Hmsc(Y=Y.BO.abuc,
                 XData = XData, XFormula = ~.,
                 studyDesign = studyDesign,
                 ranLevels = list(insect.individual = rL.insect.individual, site = rL.site, insect.sp = rL.insect.sp, insect.gt = rL.insect.gt),
                 distr = "normal"
)

m.BZ.pa = Hmsc(Y=Y.BZ.pa,
               XData = XData, XFormula = ~.,
               studyDesign = studyDesign,
               ranLevels = list(insect.individual = rL.insect.individual, site = rL.site, insect.sp = rL.insect.sp, insect.gt = rL.insect.gt),
               distr = "probit"
)

m.BZ.abuc = Hmsc(Y=Y.BZ.abuc,
                 XData = XData, XFormula = ~.,
                 studyDesign = studyDesign,
                 ranLevels = list(insect.individual = rL.insect.individual, site = rL.site, insect.sp = rL.insect.sp, insect.gt = rL.insect.gt),
                 distr = "normal"
)

m.WZ.pa = Hmsc(Y=Y.WZ.pa,
               XData = XData, XFormula = ~.,
               studyDesign = studyDesign,
               ranLevels = list(insect.individual = rL.insect.individual, site = rL.site, insect.sp = rL.insect.sp, insect.gt = rL.insect.gt),
               distr = "probit"
)

m.WZ.abuc = Hmsc(Y=Y.WZ.abuc,
                 XData = XData, XFormula = ~.,
                 studyDesign = studyDesign,
                 ranLevels = list(insect.individual = rL.insect.individual, site = rL.site, insect.sp = rL.insect.sp, insect.gt = rL.insect.gt),
                 distr = "normal"
)

models = list(m.BO.pa,m.BO.abuc,m.BZ.pa,m.BZ.abuc,m.WZ.pa,m.WZ.abuc)
names(models) = c("m.BO.pa","m.BO.abuc","m.BZ.pa","m.BZ.abuc","m.WZ.pa","m.WZ.abuc")
save(models,file="models/unfitted_models.RData")

