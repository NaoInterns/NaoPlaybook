import os
import pathlib
import requests
from flask import Flask, redirect, abort, session, request, render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests



app = Flask("Google Login App")
app.secret_key = "naomedical.com"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


GOOGLE_CLIENT_ID = "417518146130-pcqqgr68m67u75nt69vo1s3lf4us36f8.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")


flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://35.245.67.155.nip.io/callback"
    )


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) #auth required
        else: 
            return function()
    wrapper.__name__ = function.__name__
    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"]= state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/playbook")




@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    return render_template('welcome2.html')


@app.route("/playbook")
def Playbook():
    return render_template('playbook.html')

#START OF "ALL ABOUT NAO MEDICAL"
@app.route("/promise.html")
def promise():
    return render_template('promise.html')


@app.route("/missionVisionValues.html")
def mVV():
    return render_template('missionVisionValues.html')


@app.route("/storyAndFounders.html")
def sAF():
    return render_template('storyAndFounders.html')

################END OF "ALL ABOUT NAO MEDICAL"#################



#################START OF "STAFF RESOURCES"#####################





@app.route("/companyPersonel.html")
def company():
    return render_template('companyPersonel.html')


@app.route("/orgChart.html")
def orgChart():
    return render_template('orgChart.html')

@app.route("/ourServices.html")
def ourServices():
    return render_template('ourServices.html')

@app.route("/jobRoles.html")
def jobRoles():
    return render_template('jobRoles.html')

@app.route("/hiringProcess.html")
def hiringProcess():
    return render_template('hiringProcess.html')

@app.route("/employeeReferral.html")
def employeeReferral():
    return render_template('employeeReferral.html')

@app.route("/professionalGrowth.html")
def professionalGrowth():
    return render_template('professionalGrowth.html')

@app.route("/employeeInitiatives.html")
def employeeInitiatives():
    return render_template('employeeInitiatives.html')

@app.route("/events.html")
def events():
    return render_template('events.html')

@app.route("/internships.html")
def internships():
    return render_template('internships.html')

@app.route("/engineeringInternships.html")
def engInternships():
    return render_template('engineeringInternships.html')

###########################Start of OFFICE ADMIN#####################
@app.route("/officeAdmin.html")
@login_is_required
def officeAdmin():
    return render_template('officeAdmin.html')


@app.route("/dailyTasks.html")
@login_is_required
def dailyTasks():
    return render_template('dailyTasks.html')

@app.route("/patientForms.html")
@login_is_required
def patientForms():
    return render_template('patientForms.html')

#START OF PATIENT INFO
@app.route("/labPricelists.html")
@login_is_required
def labPrice():
    return render_template('labPricelists.html')

@app.route("/immigration.html")
@login_is_required
def immigration():
    return render_template('immigration.html')


@app.route("/vaccineInfo.html")
@login_is_required
def vaccInfo():
    return render_template('vaccineInfo.html')


@app.route("/suboxoneInfo.html")
@login_is_required
def subInfo():
    return render_template('suboxoneInfo.html')


@app.route("/workersComp.html")
@login_is_required
def workersComp():
    return render_template('workersComp.html')



@app.route("/noFault.html")
@login_is_required
def noFault():
    return render_template('noFault.html')


@app.route("/urineDrugTesting.html")
@login_is_required
def urineTesting():
    return render_template('urineDrugTesting.html')



@app.route("/ppdTesting.html")
@login_is_required
def ppd():
    return render_template('ppdTesting.html')



@app.route("/hippa.html")
@login_is_required
def hippa():
    return render_template('hippa.html')



@app.route("/cdl.html")
@login_is_required
def cdl():
    return render_template('cdl.html')


@app.route("/patientInfo.html")
@login_is_required
def patientInfo():
    return render_template('patientInfo.html')



##################END OF PATIENT Info######################



@app.route("/customerServiceScripts.html")
@login_is_required
def customerServiceScripts():
    return render_template('customerServiceScripts.html')


@app.route("/stationaryTemplates.html")
@login_is_required
def stationaryTemplates():
    return render_template('stationaryTemplates.html')


@app.route("/locationDirectory.html")
@login_is_required
def locationDirectory():
    return render_template('locationDirectory.html')


@app.route("/personnelDirectory.html")
@login_is_required
def personnelDirectory():
    return render_template('personnelDirectory.html')


@app.route("/locationExternalContacts.html")
@login_is_required
def locationExternalContacts():
    return render_template('locationExternalContacts.html')


@app.route("/insuranceExternalContacts.html")
@login_is_required
def insuranceExternalContacts():
    return render_template('insuranceExternalContacts.html')


@app.route("/localHospitals.html")
@login_is_required
def localHospitals():
    return render_template('localHospitals.html')



@app.route("/acceptedProviders.html")
@login_is_required
def acceptedProviders():
    return render_template('acceptedProviders.html')


@app.route("/inventory.html")
@login_is_required
def inventory():
    return render_template('inventory.html')



@app.route("/repairs.html")
@login_is_required
def repairs():
    return render_template('repairs.html')


#START OF FRONT DESK MANUAL
@app.route("/frontDeskManual.html")
@login_is_required
def frontDeskManual():
    return render_template('frontDeskManual.html')

@app.route("/fdm4.html")
@login_is_required
def fdm4():
    return render_template('fdm4.html')

@app.route("/fdm5.html")
@login_is_required
def fdm5():
    return render_template('fdm5.html')


@app.route("/fdm6.html")
@login_is_required
def fdm6():
    return render_template('fdm6.html')


@app.route("/fdm2.html")
@login_is_required
def fdm2():
    return render_template('fdm2.html')


@app.route("/fdm3.html")
@login_is_required
def fdm3():
    return render_template('fdm3.html')



@app.route("/fdm7.html")
@login_is_required
def fdm7():
    return render_template('fdm7.html')


@app.route("/fdm8.html")
@login_is_required
def fdm8():
    return render_template('fdm8.html')



@app.route("/fdm1.html")
@login_is_required
def fdm1():
    return render_template('fdm1.html')



@app.route("/fdm9.html")
@login_is_required
def fdm9():
    return render_template('fdm9.html')



@app.route("/fdm10.html")
@login_is_required
def fdm10():
    return render_template('fdm10.html')
#END OF FRONT DESK MANUAL


@app.route("/support.html")
@login_is_required
def support():
    return render_template('support.html')


##################END OF "STAFF RESOURCES"###################


###################START OF DEPARTMENTAL RESOURCES###########


@app.route("/departmentalResource.html")
@login_is_required
def dR():
    return render_template('departmentalResource.html')

@app.route("/resourceAfterCare.html")
@login_is_required
def rAC():
    return render_template('resourceAfterCare.html')

@app.route("/resourceBusinessDev.html")
@login_is_required
def rBD():
    return render_template('resourceBusinessDev.html')

@app.route("/resourceCallCenterAgent.html")
@login_is_required
def rCCA():
    return render_template('resourceCallCenterAgent.html')

@app.route("/resourceFinance.html")
@login_is_required
def rF():
    return render_template('resourceFinance.html')

@app.route("/resourceHR.html")
@login_is_required
def rHR():
    return render_template('resourceHR.html')


@app.route("/resourceMarketing.html")
@login_is_required
def rM():
    return render_template('resourceMarketing.html')


@app.route("/resourceMedAssist.html")
@login_is_required
def rMA():
    return render_template('resourceMedAssist.html')


@app.route("/resourceoccupMed.html")
@login_is_required
def rOM():
    return render_template('resourceoccupMed.html')


@app.route("/resourcePatientRelation.html")
@login_is_required
def rPR():
    return render_template('resourcePatientRelation.html')


@app.route("/resourcePCA.html")
@login_is_required
def rPCA():
    return render_template('resourcePCA.html')


@app.route("/resourcePhysician.html")
@login_is_required
def rP():
    return render_template('resourcePhysician.html')

@app.route("/resourceScribe.html")
@login_is_required
def rS():
    return render_template('resourceScribe.html')


@app.route("/resourceSiteMngr.html")
@login_is_required
def rSM():
    return render_template('resourceSiteMngr.html')


@app.route("/resourceTechEngr.html")
@login_is_required
def rTE():
    return render_template('resourceTechEngr.html')


@app.route("/resourceTelemed.html")
@login_is_required
def rT():
    return render_template('resourceTelemed.html')

#############END OF DEPARTMENTAL RESOURCES#############


###############START OF "COMMUNICATIONS"###############

@app.route("/commPlaybook.html")
@login_is_required
def commPlay():
    return render_template('commPlaybook.html')


@app.route("/msgPillars.html")
@login_is_required
def msgPillars():
    return render_template('msgPillars.html')


@app.route("/toneVoicePersonality.html")
@login_is_required
def toneVP():
    return render_template('toneVoicePersonality.html')


@app.route("/style.html")
@login_is_required
def style():
    return render_template('style.html')



@app.route("/gramPunc.html")
@login_is_required
def gramPunc():
    return render_template('gramPunc.html')


@app.route("/vocab.html")
@login_is_required
def vocab():
    return render_template('vocab.html')


@app.route("/writeNao.html")
@login_is_required
def writeN():
    return render_template('writeNao.html')



@app.route("/writePeople.html")
@login_is_required
def writeP():
    return render_template('writePeople.html')


@app.route("/writeSocialMedia.html")
@login_is_required
def writeSM():
    return render_template('writeSocialMedia.html')



@app.route("/writeNews.html")
@login_is_required
def writeNews():
    return render_template('writeNews.html')



@app.route("/writeBlog.html")
@login_is_required
def writeBlog():
    return render_template('writeBlog.html')



@app.route("/diversityAndInclusion.html")
@login_is_required
def div_Inc():
    return render_template('diversityAndInclusion.html')


@app.route("/accessibility.html")
@login_is_required
def accessibility():
    return render_template('accessibility.html')


@app.route("/brandGuide.html")
def brandGuide():
    return render_template('brandGuide.html')


##################END OF "COMMUNICATIONS"####################


###################START OF DESIGN & PRODUCT#################
@app.route("/designPlaybook.html")
@login_is_required
def designPlay():
    return render_template('designPlaybook.html')

@app.route("/prodDevPlaybook.html")
@login_is_required
def prodDevPlay():
    return render_template('prodDevPlaybook.html')
####################START OF PROD. DEV. PLAYBOOK##############
@app.route("/productDevelopmentFramework.html")
@login_is_required
def prodDevFrame():
    return render_template('productDevelopmentFramework.html')

@app.route("/helpfulResource.html")
@login_is_required
def helpResource():
    return render_template('helpfulResource.html')

@app.route("/productLifeCycle.html")
@login_is_required
def prodLifeCycle():
    return render_template('productLifeCycle.html')

###########3START OF PROD. LIFE CYCLE#####################
@app.route("/defineTerms.html")
@login_is_required
def defTerms():
    return render_template('defineTerms.html')

@app.route("/breakEpic.html")
@login_is_required
def breakEpic():
    return render_template('breakEpic.html')

@app.route("/featureSpec.html")
@login_is_required
def featureSpec():
    return render_template('featureSpec.html')



@app.route("/designDefineTerms.html")
@login_is_required
def desDefTerms():
    return render_template('designDefineTerms.html')


@app.route("/featLOFI.html")
@login_is_required
def featLOFI():
    return render_template('featLOFI.html')


@app.route("/reviewMeetings.html")
@login_is_required
def reviewMeetings():
    return render_template('reviewMeetings.html')


@app.route("/lofiToHIFI.html")
@login_is_required
def lofitoHIFI():
    return render_template('lofiToHifi.html')



@app.route("/contentWriting.html")
@login_is_required
def contentWrite():
    return render_template('contentWriting.html')


@app.route("/finalReview.html")
@login_is_required
def finalReview():
    return render_template('finalReview.html')


@app.route("/defineTermsAndTools.html")
@login_is_required
def defTermsAndTools():
    return render_template('defineTermsandTools.html')

@app.route("/refactorMaintainCode.html")
@login_is_required
def refactorMaintainCode():
    return render_template('refactorMaintainCOde.html')

@app.route("/understandFeature.html")
@login_is_required
def understandFeature():
    return render_template('understandFeature.html')

@app.route("/developmentProcess.html")
@login_is_required
def developmentProcess():
    return render_template('developmentProcess.html')


@app.route("/finishingChecklist.html")
@login_is_required
def finishingChecklist():
    return render_template('finishingChecklist.html')

#############END OF PROD. LIFE CYCLE#########################
#############END OF PROD. DEV. PLAYBOOK######################




@app.route("/siteTransformPlaybook.html")
@login_is_required
def siteTransformPlay():
    return render_template('siteTransformPlaybook.html')

@app.route("/step1Prep.html")
@login_is_required
def step1():
    return render_template('step1Prep.html')

@app.route("/step2Sign.html")
@login_is_required
def step2():
    return render_template('step2Sign.html')
#END OF DEISGN & PRODUCT

###############START OF PATIENT CARE##########################

@app.route("/manifesto.html")
def manifesto():
    return render_template('manifesto.html')

@app.route("/patientRelations.html")
@login_is_required
def patientRelations():
    return render_template('patientRelations.html')





@app.route("/patientJourney.html")
@login_is_required
def patientJourney():
    return render_template('patientJourney.html')

@app.route("/patientTreatment.html")
@login_is_required
def patientTreatment():
    return render_template('patientTreatment.html')


@app.route("/patientConcerns.html")
@login_is_required
def patientConcerns():
    return render_template('patientConcerns.html')



@app.route("/patientQuestions.html")
@login_is_required
def patientQuestions():
    return render_template('patientQuestions.html')




@app.route("/patientFeedback.html")
@login_is_required
def patientFeedback():
    return render_template('patientFeedback.html')



@app.route("/reception.html")
@login_is_required
def reception():
    return render_template('reception.html')



@app.route("/examRoom.html")
@login_is_required
def examRoom():
    return render_template('examRoom.html')


@app.route("/afterPatientCare.html")
@login_is_required
def afterPatientCare():
    return render_template('afterPatientCare.html')


###############END OF PATIENT CARE###########################



################START OF HUMAN RESOURCES######################
@app.route("/hrPolicies.html")
@login_is_required
def hrPolicies():
    return render_template('hrPolicies.html')



@app.route("/benefits.html")
@login_is_required
def benefits():
    return render_template('benefits.html')

################START OF HUMAN RESOURCES POLICIES###############
@app.route("/naoEmploymentEssentials.html")
@login_is_required
def essentials():
    return render_template('naoEmploymentEssentials.html')


@app.route("/atWill.html")
@login_is_required
def atWill():
    return render_template('atWill.html')



@app.route("/professionalConduct.html")
@login_is_required
def professionalConduct():
    return render_template('professionalConduct.html')




@app.route("/workSchedule.html")
@login_is_required
def workSchedule():
    return render_template('workSchedule.html')




@app.route("/antiHarassment.html")
@login_is_required
def antiHarassment():
    return render_template('antiHarassment.html')





@app.route("/growthPerformance.html")
@login_is_required
def growthPerformnce():
    return render_template('growthPerformance.html')



@app.route("/healthSafety.html")
@login_is_required
def healthSafety():
    return render_template('healthSafety.html')



@app.route("/timeOff.html")
@login_is_required
def timeOff():
    return render_template('timeOff.html')



@app.route("/compensation.html")
@login_is_required
def compenstion():
    return render_template('compensation.html')




@app.route("/trainingTravel.html")
@login_is_required
def trainingTravel():
    return render_template('trainingTravel.html')




@app.route("/electronicCommunications.html")
@login_is_required
def electronicCommunications():
    return render_template('electronicCommunications.html')



@app.route("/cooperationInvestigations.html")
@login_is_required
def cooperationInvestigations():
    return render_template('cooperationInvestigations.html')




@app.route("/patientPracticeConfidentiality.html")
@login_is_required
def patientPracticeConfidentiality():
    return render_template('patientPracticeConfidentiality.html')



@app.route("/externalVisitors.html")
@login_is_required
def externalVisitors():
    return render_template('externalVisitors.html')


@app.route("/solicitation.html")
@login_is_required
def solicitation():
    return render_template('solicitation.html')


@app.route("/dating.html")
@login_is_required
def dating():
    return render_template('dating.html')


@app.route("/outsideEmployment.html")
@login_is_required
def outsideEmployment():
    return render_template('outsideEmployment.html')


@app.route("/seperationFromEmployment.html")
@login_is_required
def seperationFromEmployment():
    return render_template('seperationFromEmployment.html')

@app.route("/employeeConcern.html")
@login_is_required
def employeeConcern():
    return render_template('employeeConcern.html')

@app.route("/employeeConcernForm.html")
@login_is_required
def employeeConcernForm():
    return render_template('employeeConcernForm.html')


#################END OF HUMAN RESOURCES POLICIES##################

#################END OF HUMAN RESOURCES###########################




#################START OF MARKETING###############################
@app.route("/marketingPlaybook.html")
@login_is_required
def marketingPlaybook():
    return render_template('marketingPlaybook.html')


@app.route("/websitePlaybook.html")
@login_is_required
def websitePlaybook():
    return render_template('websitePlaybook.html')

@app.route("/signages.html")
@login_is_required
def signages():
    return render_template('signages.html')


@app.route("/advertisingOOH.html")
@login_is_required
def advertisingOOH():
    return render_template('advertisingOOH.html')



@app.route("/contentMarketing.html")
@login_is_required
def contentMarketing():
    return render_template('contentMarketing.html')



@app.route("/socialMedia.html")
@login_is_required
def socialMedia():
    return render_template('socialMedia.html')



@app.route("/digitalMarketing.html")
@login_is_required
def digitalMarketing():
    return render_template('digitalMarketing.html')




@app.route("/patientCollaterals.html")
@login_is_required
def patientCollaterals():
    return render_template('patientCollaterals.html')



@app.route("/designRequestProcess.html")
@login_is_required
def designReqProcess():
    return render_template('designRequestProcess.html')


@app.route("/legalRequirements.html")
@login_is_required
def legalRequirements():
    return render_template('legalRequirements.html')


@app.route("/wayfinding.html")
@login_is_required
def wayfinding():
    return render_template('wayfinding.html')


@app.route("/fascia.html")
@login_is_required
def fascia():
    return render_template('fascia.html')


@app.route("/interiorSignage.html")
@login_is_required
def interiorSignage():
    return render_template('interiorSignage.html')



@app.route("/untitled.html")
@login_is_required
def untitled():
    return render_template('untitled.html')


@app.route("/blogArticles.html")
@login_is_required
def blogArticles():
    return render_template('blogArticles.html')


@app.route("/collateralLegal.html")
@login_is_required
def collateralLegal():
    return render_template('collateralLegal.html')


@app.route("/collateralAdmin.html")
@login_is_required
def collateralAdmin():
    return render_template('collateralAdmin.html')


@app.route("/collateralDigital.html")
@login_is_required
def collateralDigital():
    return render_template('collateralDigital.html')

@app.route("/collateralPrint.html")
@login_is_required
def collateralPrint():
    return render_template('collateralPrint.html')







#################END OF MARKETING#############################



if __name__ == "__main__":
    app.run(debug=True)