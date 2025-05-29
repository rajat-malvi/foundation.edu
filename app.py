from flask import Flask, render_template,request

app = Flask(__name__)

# machine learning
# Video data that will be passed to the template
@app.route("/", methods=['GET'])  # Add @ before route
def home():
    return render_template("home.html")

@app.route("/python",methods=["GET"])
def python():
    return render_template("python.html")

@app.route("/machinlearning",methods = ['GET'])
def mlcourse():
    videos = [
        {
            "id": 1,
            "title": "Introduction to Machine Learning",
            "status": "Complete",
            "youtubeLink": "https://youtube.com/watch?v=abc123",
            "reference": "Stanford CS229 Course Materials",
            "code": "https://github.com/example/machine-learning-intro",
            "dataset": "https://kaggle.com/datasets/ml-intro",
            "imageUrl": "https://readdy.ai/api/search-image?query=modern%20machine%20learning%20concept%20visualization%20with%20neural%20networks%20and%20data%20patterns%2C%20clean%20minimalist%20design%20with%20blue%20gradient%20background%2C%20professional%20educational%20thumbnail&width=640&height=360&seq=1&orientation=landscape"
        },
        {
            "id": 2,
            "title": "Deep Learning Fundamentals",
            "status": "In Progress",
            "youtubeLink": "https://youtube.com/watch?v=def456",
            "reference": "Deep Learning Book by Ian Goodfellow",
            "code": "https://github.com/example/deep-learning-basics",
            "dataset": "https://kaggle.com/datasets/deep-learning",
            "imageUrl": "https://readdy.ai/api/search-image?query=deep%20learning%20neural%20network%20visualization%20with%20abstract%20digital%20connections%20and%20nodes%2C%20professional%20educational%20content%20with%20dark%20blue%20gradient%20background%2C%20high%20quality%20thumbnail&width=640&height=360&seq=2&orientation=landscape"
        },
        {
            "id": 3,
            "title": "Natural Language Processing",
            "status": "Complete",
            "youtubeLink": "https://youtube.com/watch?v=ghi789",
            "reference": "NLP Course by Jurafsky & Manning",
            "code": "https://github.com/example/nlp-examples",
            "dataset": "https://kaggle.com/datasets/nlp-corpus",
            "imageUrl": "https://readdy.ai/api/search-image?query=natural%20language%20processing%20concept%20with%20text%20analysis%20visualization%2C%20word%20embeddings%20and%20language%20models%20represented%20with%20clean%20modern%20design%2C%20educational%20thumbnail%20with%20blue%20background&width=640&height=360&seq=3&orientation=landscape"
        },
        {
            "id": 4,
            "title": "Computer Vision Techniques",
            "status": "In Progress",
            "youtubeLink": "https://youtube.com/watch?v=jkl012",
            "reference": "Computer Vision: Algorithms and Applications",
            "code": "https://github.com/example/computer-vision",
            "dataset": "https://kaggle.com/datasets/vision-dataset",
            "imageUrl": "https://readdy.ai/api/search-image?query=computer%20vision%20technology%20concept%20with%20image%20recognition%20and%20object%20detection%20visualization%2C%20professional%20educational%20content%20with%20clean%20modern%20design%20and%20gradient%20background&width=640&height=360&seq=4&orientation=landscape"
        },
        {
            "id": 5,
            "title": "Reinforcement Learning",
            "status": "Complete",
            "youtubeLink": "https://youtube.com/watch?v=mno345",
            "reference": "Reinforcement Learning: An Introduction by Sutton & Barto",
            "code": "https://github.com/example/reinforcement-learning",
            "dataset": "https://kaggle.com/datasets/rl-environments",
            "imageUrl": "https://readdy.ai/api/search-image?query=reinforcement%20learning%20concept%20with%20agent%20environment%20interaction%20visualization%2C%20game%20theory%20and%20decision%20making%20representation%20with%20professional%20educational%20style%20and%20clean%20background&width=640&height=360&seq=5&orientation=landscape"
        },
        {
            "id": 6,
            "title": "Data Visualization Techniques",
            "status": "In Progress",
            "youtubeLink": "https://youtube.com/watch?v=pqr678",
            "reference": "The Visual Display of Quantitative Information",
            "code": "https://github.com/example/data-viz",
            "dataset": "https://kaggle.com/datasets/visualization-examples",
            "imageUrl": "https://readdy.ai/api/search-image?query=data%20visualization%20techniques%20with%20colorful%20charts%2C%20graphs%20and%20infographics%2C%20modern%20clean%20design%20showing%20information%20display%20methods%2C%20educational%20content%20with%20professional%20look&width=640&height=360&seq=6&orientation=landscape"
        },
        {
            "id": 7,
            "title": "Time Series Analysis",
            "status": "Complete",
            "youtubeLink": "https://youtube.com/watch?v=stu901",
            "reference": "Time Series Analysis by Box & Jenkins",
            "code": "https://github.com/example/time-series",
            "dataset": "https://kaggle.com/datasets/time-series-data",
            "imageUrl": "https://readdy.ai/api/search-image?query=time%20series%20analysis%20visualization%20with%20trend%20lines%20and%20forecasting%20graphs%2C%20stock%20market%20or%20weather%20data%20representation%2C%20professional%20educational%20content%20with%20clean%20modern%20design&width=640&height=360&seq=7&orientation=landscape"
        },
        {
            "id": 8,
            "title": "Generative Adversarial Networks",
            "status": "In Progress",
            "youtubeLink": "https://youtube.com/watch?v=vwx234",
            "reference": "GAN Papers by Ian Goodfellow",
            "code": "https://github.com/example/gan-examples",
            "dataset": "https://kaggle.com/datasets/gan-training",
            "imageUrl": "https://readdy.ai/api/search-image?query=generative%20adversarial%20networks%20concept%20visualization%20showing%20generator%20and%20discriminator%20architecture%2C%20AI%20art%20creation%20process%2C%20professional%20educational%20thumbnail%20with%20modern%20design&width=640&height=360&seq=8&orientation=landscape"
        }
    ]
    return render_template('machinlearning.html', videos=videos)


@app.route("/team",methods=['GET'])
def team():
    # Team members data
    team_members = [
        {
            'id': 1,
            'name': "Dr. Kushal Shah",
            'role': "Co-Founder & CEO",
            'bio': "Kushal is a multidisciplinary technologist driving UTMT’s digital direction. With a background spanning education, data science, and design, he creates tools that translate complexity into clarity, aiming to bridge the digital divide through empathy-driven innovation.",
            'linkedIn': "https://www.linkedin.com/in/kushal-shah-95b9a3b/",
            'profileUrl': "https://media.licdn.com/dms/image/v2/D5603AQHEAjO_OXfFnQ/profile-displayphoto-shrink_200_200/B56ZUAPyC5GsAg-/0/1739465894170?e=1753920000&v=beta&t=8WKyGBWkzNvwDBf3UEgBrxS0-DmfzV6j7-GbsyIxGwk",
            'gender': 'male'
        },
        {
            'id': 2,
            'name': "Preeti Shukla",
            'role': "Faculty, Language and Communication",
            'bio': "Preeti brings a rich background in language education. At UTMT, she plays a crucial role in nurturing learners’ expression and clarity. With experience in curriculum design, she empowers students to connect ideas meaningfully.",
            'linkedIn': "#",
            'profileUrl': "https://media.licdn.com/dms/image/v2/D5603AQGllhXy7UstVg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1724394687669?e=1753920000&v=beta&t=e0K9dPmkDWVj6lp0AyyEE0jkTFPxf38C-PKtEG9QZT0",
            'gender': 'female'
        },
        {
            'id': 3,
            'name': "Prof. Kalpesh Kapoor",
            'role': "Visiting Faculty (IISER Pune & IIT Guwahati)",
            'bio': "Specializing in advanced mathematical modeling and data science, Prof. Kapoor enriches our curriculum with insights into modern data analysis techniques from his roles at IISER Pune and IIT Guwahati.",
            'linkedIn': "#",
            'profileUrl': "https://media.licdn.com/dms/image/v2/D5603AQF66XeRUMNuaA/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1687761984098?e=1753920000&v=beta&t=GSd3O6rbXE71nttOox8eY0UToB5opaLPuwGSsnufTVc",
            'gender': 'male'
        },
        {
            'id': 4,
            'name': "Dr. Anish Roychowdhury",
            'role': "Associate Director of Data Science, Plaksha University",
            'bio': "Dr. Anish is a seasoned Data Science professional with 20+ years in industry and academia. He excels in leading digital transformations and has deep expertise in Machine Learning, Deep Learning, and Generative AI, dedicated to advancing Data Science education.",
            'linkedIn': "#",
            'profileUrl': "https://media.licdn.com/dms/image/v2/D5603AQEr1RmREBUOkQ/profile-displayphoto-shrink_200_200/B56ZPtU50PH0AY-/0/1734853501970?e=1753920000&v=beta&t=vRyh1zQlDZs3IHC_F-XXnKtwBowky9-KXgBlaWu_KyY",
            'gender': 'male'
        },
        {
            'id': 5,
            'name': "Dr. S. Balaji",
            'role': "Professor, Mechanical Engineering, IIT Madras",
            'bio': "Dr. Balaji brings extensive expertise in Mechanical Engineering from IIT Madras. His research and teaching focus on [mention key area if known, e.g., thermodynamics, fluid mechanics, or manufacturing processes], contributing valuable insights to our programs.",
            'linkedIn': "#",
            'profileUrl': "https://mech.iitm.ac.in/images/inner-facs/sbalaji.png",
            'gender': 'male'
        },
        {
            'id': 6,
            'name': "Nagapranay Tumuluri",
            'role': "Data Science & ML Professional / Mentor",
            'bio': "Nagapranay is a skilled professional with a strong background in [mention key skills from LinkedIn, e.g., data analysis, machine learning applications]. He contributes to UTMT by [mention role, e.g., mentoring students, developing course content, or leading projects].",
            'linkedIn': "#",
            'profileUrl': "https://media.licdn.com/dms/image/v2/D4E03AQHqEenwEEHe9g/profile-displayphoto-shrink_200_200/B4EZRM8UIqHsAc-/0/1736457667535?e=1753920000&v=beta&t=guuX4nBF_hpbGt-aNkyYTx_FPUOVEHmaO3NbCyA03IU",
            'gender': 'male'
        },
        {
            'id': 7,
            'name': "Vibhanshu G",
            'role': "Founder, TakeOff Talent | AI & Data Science Lead | Mentor",
            'bio': "Vibhanshu is a Data Science and AI leader with 9+ years of experience, specializing in building impactful AI products and talent solutions. As Founder of TakeOff Talent, he helps companies hire top tech talent swiftly and mentors professionals in their data science careers.",
            'linkedIn': "#",
            'profileUrl': "https://media.licdn.com/dms/image/v2/D5635AQFpTTpI3LXWYA/profile-framedphoto-shrink_200_200/B56ZcSJheNHoAc-/0/1748356176032?e=1749150000&v=beta&t=FSoTEnoZMawYO7dQ3QFDyT8Av2EmP0RYTtgaqi4xaKY",
            'gender': 'male'
        },
        {
            'id': 8,
            'name': "Arvind Sivdas",
            'role': "Tech & Product Leader | Advisor",
            'bio': "Arvind is an experienced leader in technology and product development, known for [mention 1-2 key strengths e.g., scaling tech platforms, driving product innovation]. He supports UTMT by [mention role, e.g., advising on tech strategy, mentoring product teams, or contributing to platform development].",
            'linkedIn': "#",
            'profileUrl': "https://media.licdn.com/dms/image/v2/C5603AQG6n5kBNsU8UQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1652428583707?e=1753920000&v=beta&t=871WtyHWiE2s1upjDZgjLzO661mLK0nom_8mE2oAnaQ",
            'gender': 'male'
        }
    ]
    
    # Support pillars data
    support_pillars = [
        {
            'id': 1,
            'title': "Teaching Assistance",
            'icon': "chalkboard-teacher",
            'description': "Dedicated mentors providing personalized guidance and support throughout your learning journey."
        },
        {
            'id': 2,
            'title': "Technical Support",
            'icon': "laptop-code",
            'description': "24/7 technical assistance to ensure uninterrupted access to our digital learning resources."
        },
        {
            'id': 3,
            'title': "Student Services",
            'icon': "users",
            'description': "Comprehensive support for all student needs, from enrollment to certification and placement."
        },
        {
            'id': 4,
            'title': "Curriculum Development",
            'icon': "book",
            'description': "Continuously updated course materials aligned with industry requirements and educational standards."
        }
    ]
    
    return render_template('team.html', 
                         team_members=team_members, 
                         support_pillars=support_pillars)

if __name__ == "__main__":
    app.run(port=3000,debug=True)
