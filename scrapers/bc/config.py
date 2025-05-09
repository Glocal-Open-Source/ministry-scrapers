# BC config

# urls for:
# Role
# Attorney General
# Ministers
# Deputy Ministers
# Deputy Attorney Generals

#          fields
#  -----------------------
# | Type              str |
# | Ministry          str |
# | Role              str |
# | Honorable         bool|
# | Name              str |
# | French            bool|
# | Biography         str |
# | Contact URL       str |
# | Contact Phone     str |
# | Office            str |
#  -----------------------
#

minister_urls = {

    "Ministry of Agriculture and Food": [
        "https://news.gov.bc.ca/ministries/agriculture-and-food/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/cabinet/cabinet-ministers/parliamentary-secretary-for-agriculture",
    ],

    "Attorney General": [
        "https://news.gov.bc.ca/ministries/attorney-general/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/cabinet/cabinet-ministers/parliamentary-secretary-for-anti-racism-initiatives"
    ],

    "Children and Family Development": [
        "https://news.gov.bc.ca/ministries/children-and-family-development/biography",
    ],

    "Citizens' Services": [
        "https://news.gov.bc.ca/ministries/citizens-services/biography"
    ],

    "Education and Child Care": [
        "https://news.gov.bc.ca/ministries/education-and-child-care/child-care/biography"
    ],

    "Emergency Management and Climate Readiness": [
        "https://news.gov.bc.ca/ministries/emergency-management-and-climate-readiness/biography",
    ],

    "Energy and Climate Solutions": [
        "https://news.gov.bc.ca/ministries/energy-and-climate-solutions/biography",
    ],

    "Environment and Parks": [
        "https://news.gov.bc.ca/ministries/environment-and-parks/biography",
    ],

    "Finance": [
        "https://news.gov.bc.ca/ministries/finance/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/ministries-organizations/ministries/finance"
    ],

    "Forests": [
        "https://news.gov.bc.ca/ministries/forests/biography",
    ],

    "Health": [
        "https://news.gov.bc.ca/ministries/health/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/ministries-organizations/ministries/health"
    ],

    "Housing and Municipal Affairs": [
        "https://news.gov.bc.ca/ministries/housing-and-municipal-affairs/biography",
    ],

    "Indigenous Relations and Reconciliation": [
        "https://news.gov.bc.ca/ministries/indigenous-relations-and-reconciliation/biography",
    ],

    "Infrastructure": [
        "https://news.gov.bc.ca/ministries/infrastructure/biography",
    ],

    "Jobs, Economic Development and Innovation": [
        "https://news.gov.bc.ca/ministries/jobs-economic-development-and-innovation/biography",
    ],

    "Labour": [
        "https://news.gov.bc.ca/ministries/labour/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/ministries-organizations/ministries/labour"
    ],

    "Mining and Critical Minerals": [
        "https://news.gov.bc.ca/ministries/mining-and-critical-minerals/biography",
    ],

    "Post-Secondary Education and Future Skills": [
        "https://news.gov.bc.ca/ministries/post-secondary-education-and-future-skills/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/cabinet/cabinet-ministers/parliamentary-secretary-for-international-credentials"
    ],

    "Public Safety and Solicitor General": [
        "https://news.gov.bc.ca/ministries/public-safety-and-solicitor-general/biography",
        "https://news.gov.bc.ca/ministries/community-safety-and-integrated-services/biography"
    ],

    "Social Development and Poverty Reduction": [
        "https://news.gov.bc.ca/ministries/social-development-and-poverty-reduction/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/cabinet/cabinet-ministers/parliamentary-secretary-accessibility",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/cabinet/cabinet-ministers/parliamentary-secretary-community-development-non-profits"
    ],

    "Tourism, Arts, Culture and Sport": [
        "https://news.gov.bc.ca/ministries/tourism-arts-culture-and-sport/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/cabinet/cabinet-ministers/parliamentary-secretary-arts-film"
    ],

    "Trade": [
        "https://news.gov.bc.ca/ministries/trade/biography",
    ],

    "Transportation and Transit": [
        "https://news.gov.bc.ca/ministries/transportation-and-transit/biography",
        "https://www2.gov.bc.ca/gov/content/governments/organizational-structure/cabinet/cabinet-ministers/parliamentary-secretary-for-transit"
    ],

    "Water, Land and Resource Stewardship": [
        "https://news.gov.bc.ca/ministries/water-land-and-resource-stewardship/biography",
    ]
}
# maps crown corp contact info to minister in charge of ministry responsible
crown_to_ministry = {
    "BC Assessment": "Finance",
    "BC Council for International Education": "Post-Secondary Education and Future Skills",
    "BC Family Maintenance Agency": "Attorney General",
    "BC Financial Services Authority": "Finance",
    "BC Games Society": "Tourism, Arts, Culture and Sport",
    "BC Housing": "Housing and Municipal Affairs",
    "BC Hydro and Power Authority": "Energy and Climate Solutions",
    "BC Infrastructure Benefits": "Infrastructure",
    "BC Energy Regulator": "Energy and Climate Solutions",
    "BC Pavilion Corporation": "Tourism, Arts, Culture and Sport",
    "BC Transit": "Transportation and Transit",
    "British Columbia Lottery Corporation": "Finance",
    "British Columbia Securities Commission": "Finance",
    "Columbia Basin Trust": "Finance",
    "Columbia Power Corporation": "Finance",
    "Community Living BC": "Social Development and Poverty Reduction",
    "Destination BC": "Tourism, Arts, Culture and Sport",
    "First Peoples' Cultural Council": "Indigenous Relations and Reconciliation",
    "Forest Enhancement Society of BC": "Forests",
    "Forestry Innovation Investment": "Jobs, Economic Development and Innovation",
    "InBC Investment Corp": "Jobs, Economic Development and Innovation",
    "Infrastructure BC": "Infrastructure",
    "Innovate BC": "Jobs, Economic Development and Innovation",
    "Insurance Corporation of British Columbia": "Public Safety and Solicitor General",
    "Knowledge Network": "Tourism, Arts, Culture and Sport",
    "Legal Aid BC": "Attorney General",
    "Royal BC Museum": "Tourism, Arts, Culture and Sport",
    "SkilledTradesBC": "Post-Secondary Education and Future Skills",
    "Transportation Investment Corporation": "Transportation and Transit",
}

crown_to_urls = {
    corp: minister_urls[ministry]
    for corp, ministry in crown_to_ministry.items()
}