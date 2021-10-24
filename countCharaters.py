import pprint #importing prety print, as the name goes
message = """Local ICA Date of Issue 04 August 2021 Location Sub Office Dadaab Closing Date 17 August 2021 
Organizational Context (role of the position within the team, describing its leadership role, it’s external
/internal work relationships or contacts, the contextual environment in which it operates, and the scope of 
supervision received, and where applicable, exercise by the incumbent) Since 2013, Vodafone Foundation and UNHCR 
have worked together on the Instant Network Schools (INS) Programme. INS aims to improve access to quality 
education for displaced children in refugee camps, through the use of technology and connectivity, alongside 
teacher training and capacity building support. An MoU has been signed between Vodafone Foundation and UNHCR 
for 2015-16, covering four countries across east Africa: Dadaab and Kakuma camps in Kenya; Nyarugusu camp in 
Tanzania; Ajuon Tok in South Sudan; and Boyabu, Mole, Inke and Goma in DRC. Currently 16 INS centres have been 
established, rising to 35 by the end of 2016. In each operation, the programme aims to establish Instant Network 
Classrooms in formal schools which are already operating in the refugee camps. Schools are selected by UNHCR along 
with the community and implementing partners, and cover primary, secondary, and vocational training. From 2015, 
Community Learning Hubs are also being established to serve the wider community; and in Kenya World Reader Mobile 
is being leveraged to give community access to eBooks on their own phones. Both the Classrooms and the Hubs are 
equipped with internet connectivity, power, and equipment for use by teachers or coaches and students. An Instant 
Classroom Kit, comprising a laptop, projector, speakers, and a local server for teachers to use, alongside tablets 
to encourage student interactivity, has been developed by the Vodafone Foundation and is being deployed. The Hubs 
will use the Kit and will also be given eReaders which can be used by the community as part of a digital library. 
In Dadaab, 13 Instant Network Classrooms were equipped and piloted during 2014. Each location had received tablets, 
a projector, and speakers along with access to a Rachel Pi server which can be used to find on and offline content. 
The Digital Learning program in Dadaab has since expanded to 28 schools (22 Primary and 6 Secondary) through 
education partners led effort with Computer for Schools Kenya(CFSK) Project and donation of 450 Tablets from 
Samsung Electronics. These centres are managed by trained teachers and are located within existing Primary, 
Secondary and vocational centres, covering all three camps in Dadaab refugee complex. During the period 2021-2022, 
the intention in Dadaab is to sustain the centres, continuing to support and train the teachers, expand virtual and
digital learning programs during the period of Covid-19 pandemic and to maximize the use of the technology in 
improving learning outcomes for the children in the camp. Accountability (key results that will be achieved) 
Digital learning activities are guided by global, regional and country priorities and reflect UNHCR's policy on 
age, gender and diversity (AGD) Participation of persons of concern is assured through continuous assessment and 
evaluation using participatory, rights and community based approaches Persons of concern are treated with dignity 
and respect and all protection incidents are immediately identified and addressed. Responsibility (process and 
functions undertaken to achieve results) This position is hired by UNHCR and reports to the Senior Operations 
Coordinator, with support-supervision from UNHCR Innovation’s Learn Lab Manager. The incumbent will be responsible 
for the day-to-day implementation and monitoring of the Digital learning programs in Dadaab. Working closely with 
the school-based ICT Coaches who are hired by implementing partners to run the Digital Learning on a daily basis in 
schools, the Programme Manager is responsible for the effective and efficient management and implementation of all 
activities within the Digital Learning Programme in Dadaab. Support to programme set-up and consolidation: Provide 
programmatic and operational support to the setup and consolidation of the digital learning locations in schools 
and community hubs across Dadaab Camps including regular visits to schools Programme Management: Responsible for 
supporting the implementation of the digital elarning programme in accordance with approved time schedules, budgets 
and both UNHCR and Vodafone Foundation guidelines and procedures. Support UNHCR and VF team with the strategy, 
project planning, and identifying mobile technology based solutions for the specific education needs in the 
location. Monitoring & Evaluation: Support Coaches and partners in monitoring the programme, including support in 
the effective use of online tools for data collection and analysis on digital learning programme usage - Resource 
Planning & Management: Support the work of the Coaches in the schools and ensure effective and optimal deployment 
and use of INS platforms and tools. Training and Support: Provide on-the-job training, and facilitate training by 
others, to Coaches, partners and other stakeholders in using educational technology, ICT maintenance and other 
relevant areas. Train Coaches in use and basic maintenance of the equipment, use of content, integrating technology
 into lesson planning and delivery Authority (decisions made in executing responsibilities and to achieve results) 
 Implement Digital Learning project activities as required Issue documents and reports for clearance by the 
 Education or Protection and/or Senior Protection Officer Provide advice on Digital learning, INS and other 
 Connected education projects implementation Monitoring and Progress Controls (Clear description of measurable 
 outputs, milestones, key performance indicators and/or reporting requirements which will enable performance 
 monitoring) 1.To support management and implementation of the Connected Education program • Overall management of 
 the CE projects- • Manage the INS Network with regular internet maintenance • Identify best Internet technology 
 that need to be implemented and advise • Organize meeting with Coaches, partners, and other stakeholders on 
 inclusion of Technology in Education • Ensure quarterly and annual implementation plans developed, approved, and 
 followed • Ensure educational content selected, rolled out and utilized • Monitor CE and INS projects. • Follow 
 up with Partners implementing the CE Projects • Advocate for use of right digital content in the CE projects • 
 Analyze user data collected • Attend Education meetings 2.To prepare/implement project workplan, reports and other
  records •Prepare/implement monthly, quarterly, and yearly plan • Prepare and submit INS usage reports • Prepare 
  and submit quarterly, mid/end year reports • Create and submit activity budgets for approvals •Support monitoring,
   data collection and research •Write project activity reports/proposals •Contribute to the national/global mid/end
    year reports 3.To manage INS and DL resources • Mapping all DL resources-both hardware and software • Keeping proper 
    and accurate records of equipment • Facilitate the transfer of project equipment to partners • Report on any 
    discrepancies loss or damage of materials/tool/equipment assigned. • Ensure proper utilization of all materials,
     tools, and equipment for learning/teaching. • Carry out repair and maintenance of equipment as applicable • D
     evelop and maintain a database/list of stakeholders and their contact details • Case Studies, interviews, stories collected from the coaches and released/distributed as appropriate 4.To enrich and train the ICT coaches, teachers, and other Partners stakeholders with knowledge of use of technology in education, ICT Maintenance • Provide on-job training for coaches • Reviewing Coach/Teacher on boarding package • Organize relevant capacity building training for coaches • Organize for partners teachers training on integrating ICT in class • Organize for training for students’ leaders • Training Coaches in use and basic maintenance of the equipment, use of content, integrating technology into lesson planning and delivery. • Keep up to date INS/DL staff database and profile. 5.To ensure adequate INS/DL program Coordination, Monitoring and evaluation is provided • Support with partnership management and coordination • School monitoring and support to regular education work • Infographic mapping of all education Facilities with Site team & TCG • Stock-manager and focal point of all ICT materials of all centers/schools; doing regular verification, audits, progress reports and follow up with partners and UNHCR Team. • Contribute to timely Donor and partner reporting of programme issues implementation. • Serves as a liaison between UNHCR and Digital Learning (DL)/Connected Education (CE) Partn"""
count = {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] += 1
pprint.pprint(count)
# test = pprint.pformat(count)
# print("\n\n"+test)