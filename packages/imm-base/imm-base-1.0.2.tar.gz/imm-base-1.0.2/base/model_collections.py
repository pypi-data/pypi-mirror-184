from pathlib import Path
from config import BASEDIR,DATADIR


title = ["Command", "Arguments", "Options", "Remark"]

make = [
    "make",
    "model, excel_name",
    "",
    "Make excel based on the model and this excel name, with or without '.xlsx'",
]
check = [
    "check",
    "model, excel_name",
    "",
    "Check this excel data based on the model, with or without '.xlsx'",
]
run = [
    "run",
    "model, excel_name",
    "",
    "run a model for calculaton or something else with result return",
]


def word(options, remark):
    return [
        "word",
        "model, excel_name,[word_name],[doctype]",
        options,
        remark,
    ]


def webform(options):
    return [
        "webform",
        "model, excel_name, [outputjson]",
        options,
        "Make json file for filling web form",
    ]


def pdfform(options, remark):
    return [
        "pdfform",
        "model, excel_name, [outputjson]",
        options,
        remark,
    ]


helps = {
    "5593": [
        title,
        make,
        check,
        webform("--rcic,--uploaddir"),
        word(
            "",
            "Make word for rs:Recruitment Summary, et:Employer Training, sl: Submission Letter",
        ),
    ],
    "5626": [
        title,
        make,
        check,
        webform("--rcic,--uploaddir"),
        word(
            "",
            "Make word for rs:Recruitment Summary, et:Employer Training, sl: Submission Letter",
        ),
    ],
    "5627": [
        title,
        make,
        check,
        webform("--rcic,--uploaddir"),
        word(
            "",
            "Make word for rs:Recruitment Summary, et:Employer Training, sl: Submission Letter",
        ),
    ],
    "lmia-cap": [title, make, check, run],
    "exp-rs": [
        title,
        make,
        check,
        word("--tempnum", "Make resume word"),
    ],
    "recruit-ja": [
        title,
        make,
        check,
        word("--rciccompany, --tempnum", "Make resume word"),
    ],
    "recruit-jo": [title, make, check, word("--tempnum", "Make resume word")],
    "recruit-rs": [title, make, check, word("", "Make recruitment summary doc")],
    "bcpnp-ci": [title, make, check, word("", "Make company brief word")],
    "bcpnp-ert": [title, make, check, word("", "Make Employer Training doc")],
    "bcpnp-eet": [title, make, check, word("", "Make Employee Training doc")],
    "bcpnp-jd": [title, make, check, word("", "Make Job Description doc")],
    "bcpnp-rl": [
        title,
        make,
        check,
        word("", "Make Employer Recommendation Letter doc"),
    ],
    "bcpnp-edf": [
        title,
        make,
        check,
        pdfform("", "Make Employer Declaration Form json"),
    ],
    "bcpnp-rpf": [
        title,
        make,
        check,
        pdfform("--rcic", "Make Employer Declaration Form json"),
    ],
    "5476": [
        title,
        make,
        check,
        pdfform("--rcic", "Make 5476 Form json"),
    ],
    "assess": [
        title,
        make,
        check,
    ],
}


def get_models(
    rcic_company_id_name: str = "noah",
    temp_num: int = 1
):
    models = {
        "exp-rs": {
            "path": "base.models.experience.resume",
            "class_list": ["ResumeModel", "ResumeModelE"],
            "remark": "Experience module for Resume model",
            "docx_template": {
                "rs":  f"word/resume-regular{temp_num}.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate resume and employment certificate docx ",
                "helps": helps["exp-rs"],
            },
        },
        # Recruitment
        "recruit-ja": {
            "path": "base.models.recruit.jobad",
            "class_list": ["JobadModel", "JobadModelE"],
            "remark": "Recruit module for Job Advertisement model",
            "docx_template": {
                "ja":  "word/jobad.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate job advertisement docx ",
                "helps": helps["recruit-ja"],
            },
        },
        "recruit-jo": {
            "path": "base.models.recruit.joboffer",
            "class_list": ["JobofferModel", "JobofferModelE"],
            "remark": "Recruitment module for Job Offer model",
            "docx_template": {
                "jo":  f"word/joboffer{temp_num}.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate job offer docx ",
                "helps": helps["recruit-jo"],
            },
        },
        "recruit-rs": {
            "path": "base.models.recruit.recruitmentsummary",
            "class_list": ["RecruitmnetSummaryModel", "RecruitmnetSummaryModelE"],
            "remark": "Recruitment module for Recruitment Summary model",
            "docx_template": {
                "ja":  "word/lmia-rs.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate LMIA recruitment summary docx ",
                "helps": helps["recruit-rs"],
            },
        },
        # LMIA
        "lmia-st1": {
            "path": "lmia.model.stage1",
            "class_list": ["LmiaAssess", "LmiaAssessE"],
            "remark": "LMIA module for stage 1 model (assessment)",
        },
        "lmia-st2": {
            "path": "lmia.model.stage2",
            "class_list": ["LmiaRecruitment", "LmiaRecruitmentE"],
            "remark": "LMIA module for stage 2 model (recruitment)",
        },
        "lmia-st3": {
            "path": "lmia.model.stage3",
            "class_list": ["LmiaApplication", "LmiaApplicationE"],
            "remark": "LMIA module for for stage 3 model (application)",
        },
        "lmia-rcic": {
            "path": "lmia.model.rcic",
            "class_list": ["LmiaRcic", "LmiaRcicE"],
            "remark": "LMIA module for RCIC model (Plannning)",
        },
        "lmia-5593": {
            "path": "lmia.model.m5593",
            "class_list": ["M5593Model", "M5593ModelE"],
            "docx_template": {
                "rs":  "word/lmia-rs.docx",
                "et":  "word/5593-et.docx",
                "sl":  f"word/5593-sl-{rcic_company_id_name}.docx",
            },
            "remark": "LMIA module for EE doc generation application",
            "web_function": "Yes ",
            "help": {
                "description": "This model can automatically make docx, and make json file for filling web form ",
                "helps": helps["5593"],
            },
        },
        "lmia-5626": {
            "path": "lmia.model.m5626",
            "class_list": ["M5626Model", "M5626ModelE"],
            "docx_template": {
                "rs":  "word/lmia-rs.docx",
                "et":  "word/5626-et.docx",
                "sl":  f"word/5626-sl-{rcic_company_id_name}.docx",
            },
            "web_function": "Yes ",
            "remark": "LMIA module for HWS application",
            "help": {
                "description": "This model can automatically make docx, and make json file for filling web form ",
                "helps": helps["5626"],
            },
        },
        "lmia-5627": {
            "path": "lmia.model.m5627",
            "class_list": ["M5627Model", "M5627ModelE"],
            "docx_template": {
                "rs":  "word/lmia-rs.docx",
                "et":  "word/5627-et.docx",
                "sl":  f"word/5627-sl-{rcic_company_id_name}.docx",
            },
            "web_function": "Yes ",
            "remark": "LMIA module for LWS application",
            "help": {
                "description": "This model can automatically make docx, and make json file for filling web form ",
                "helps": helps["5627"],
            },
        },
        "lmia-cap": {
            "path": "lmia.model.cap",
            "class_list": ["CapModel", "CapModelE"],
            "remark": "LMIA CAP module for LWS application",
            "help": {
                "description": "This model makes and checks excel, and calculate CAP ",
                "helps": helps["lmia-cap"],
            },
        },
        # BCPNP
        "bcpnp-ci": {
            "path": "bcpnp.model.companyinfo",
            "class_list": ["CompanyInfoModel", "CompanyInfoModel_E"],
            "remark": "BCPNP module for Company Info model",
            "docx_template": {
                "bcpnp-ci":  "word/bcpnp_company_information.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate BCPNP company brief docx ",
                "helps": helps["bcpnp-ci"],
            },
        },
        "bcpnp-ert": {
            "path": "bcpnp.model.employertraining",
            "class_list": ["EmployerTrainingModel", "EmployerTrainingModelE"],
            "remark": "BCPNP module for Employer Training model",
            "docx_template": {
                "bcpnp-ert":  "word/bcpnp-ert.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate BCPNP employer training docx ",
                "helps": helps["bcpnp-ert"],
            },
        },
        "bcpnp-eet": {
            "path": "bcpnp.model.employeetraining",
            "class_list": ["EmployeeTrainingModel", "EmployeeTrainingModelE"],
            "remark": "BCPNP module for Employee Training model",
            "docx_template": {
                "bcpnp-eet":  "word/bcpnp-eet.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate BCPNP employee training docx ",
                "helps": helps["bcpnp-eet"],
            },
        },
        "bcpnp-jd": {
            "path": "bcpnp.model.jobdescription",
            "class_list": ["JobDescriptionModel", "JobDescriptionModelE"],
            "remark": "BCPNP module for Job Description model",
            "docx_template": {
                "bcpnp-jd":  "word/bcpnp-jd.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate BCPNP Job Description docx ",
                "helps": helps["bcpnp-jd"],
            },
        },
        "bcpnp-edf": {
            "path": "bcpnp.model.employerdeclaraton",
            "class_list": [
                "EmployerDeclaratonFormModel",
                "EmployerDeclaratonFormModelE",
            ],
            "remark": "BCPNP module for Employer Declaraton Form Model Form model",
            "pdf_function": "Yes",
            "help": {
                "description": "This model can make and check excel model, and generate BCPNP Employer Declaration Form data(Job Offer Form) ",
                "helps": helps["bcpnp-edf"],
            },
        },
        "bcpnp-rl": {
            "path": "bcpnp.model.recommendationletter",
            "class_list": ["RecommendationLetterModel", "RecommendationLetterModelE"],
            "remark": "BCPNP module for Recommendation Letter model",
            "docx_template": {
                "bcpnp-rl":  "word/bcpnp-rl.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate BCPNP Employer Recommendation Letter docx ",
                "helps": helps["bcpnp-rl"],
            },
        },
        "bcpnp-rpf": {
            "path": "bcpnp.model.mrep",
            "class_list": ["MRepModel", "MRepModelE"],
            "remark": "BCPNP module for Representative Form model",
            "pdf_function": "Yes",
            "help": {
                "description": "This model can make and check excel model, and generate BCPNP Rep form ",
                "helps": helps["bcpnp-rpf"],
            },
        },
        "bcpnp-pro": {
            "path": "bcpnp.webform.bcpnpmodel_pro",
            "class_list": ["BcpnpModelPro", "BcpnpModelProE"],
            "remark": "BCPNP module for BCPNP Profile model",
            "web_function": "Yes",
        },
        "bcpnp-reg": {
            "path": "bcpnp.webform.bcpnpmodel_reg",
            "class_list": ["BcpnpModelReg", "BcpnpModelRegE"],
            "remark": "BCPNP module for BCPNP Registration model",
            "web_function": "Yes",
        },
        "bcpnp-reg-ee": {
            "path": "bcpnp.webform.bcpnpmodel_reg",
            "class_list": ["BcpnpEEModelReg", "BcpnpEEModelRegE"],
            "remark": "BCPNP module for BCPNP Registration model(EE)",
            "web_function": "Yes",
        },
        "bcpnp-app": {
            "path": "bcpnp.webform.bcpnpmodel_app",
            "class_list": ["BcpnpModelApp", "BcpnpModelAppE"],
            "remark": "BCPNP module for BCPNP Application model",
            "web_function": "Yes ",
        },
        "bcpnp-app-ee": {
            "path": "bcpnp.webform.bcpnpmodel_app",
            "class_list": ["BcpnpEEModelApp", "BcpnpEEModelAppE"],
            "remark": "BCPNP module for BCPNP application (EE) model",
            "web_function": "Yes ",
        },
        # PR
        "0008": {
            "path": "pr.model.m0008",
            "class_list": ["M0008Model", "M0008ModelE"],
            "remark": "PR module for form 0008 model",
        },
        "0008dp": {
            "path": "pr.model.m0008",
            "class_list": ["M0008DPModel", "M0008DPModelE"],
            "remark": "PR module for form 0008 dependant model",
        },
        "5406": {
            "path": "pr.model.m5406",
            "class_list": ["M5406Model", "M5406ModelE"],
            "remark": "PR module for form 5406 model",
        },
        "5562": {
            "path": "pr.model.m5562",
            "class_list": ["M5562Model", "M5562ModelE"],
            "remark": "PR module for form 5562 model",
        },
        "5669": {
            "path": "pr.model.m5669",
            "class_list": ["M5669Model", "M5669ModelE"],
            "remark": "PR module for form 5669 model",
        },
        # TR
        "1294": {
            "path": "tr.model.m1294",
            "class_list": ["M1294Model", "M1294ModelE"],
            "pdf_function": "Yes",
            "docx_template": {
                "sl":  f"word/1294-sl-{rcic_company_id_name}.docx"
            },
            "remark": "TR module for form 1294 model",
        },
        "1295": {
            "path": "tr.model.m1295",
            "class_list": ["M1295Model", "M1295ModelE"],
            "pdf_function": "Yes",
            "docx_template": {
                "sl":  f"word/1295-sl-{rcic_company_id_name}.docx"
            },
            "remark": "TR module for form 1295 model",
        },
        "5257": {
            "path": "tr.model.m5257",
            "class_list": ["M5257Model", "M5257ModelE"],
            "pdf_function": "Yes",
            "remark": "TR module for form 5257 model",
        },
        "5708": {
            "path": "tr.model.m5708",
            "class_list": ["M5708Model", "M5708ModelE"],
            "pdf_function": "Yes",
            "docx_template": {
                "sl":  f"word/5708-sl-{rcic_company_id_name}.docx"
            },
            "remark": "TR module for form 5708 model",
        },
        "5709": {
            "path": "tr.model.m5709",
            "class_list": ["M5709Model", "M5709ModelE"],
            "pdf_function": "Yes",
            "remark": "TR module for form 5709 model",
        },
        "5710": {
            "path": "tr.model.m5710",
            "class_list": ["M5710Model", "M5710ModelE"],
            "pdf_function": "Yes",
            "remark": "TR module for form 5710 model",
        },
        "5476": {
            "path": "base.models.m5476",
            "class_list": ["M5476Model", "M5476ModelE"],
            "pdf_function": "Yes ",
            "remark": "Rep form",
            "help": {
                "description": "This model can automatically make json file for filling pdf form ",
                "helps": helps["5476"],
            },
        },
        "assess": {
            "path": "assess.model",
            "class_list": ["AssessModel", "AssessModelE"],
            "remark": "Assess form",
            "help": {
                "description": "This model can generate and check assess excel form ",
                "helps": helps["assess"],
            },
        },
    }

    return models
