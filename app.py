from flask import Flask, render_template,request,jsonify
import math
from ml_course import ML_VIDEO_DATA, ML_SIDEBAR_TOPICS
from python_course import PY_VIDEO_DATA,SIDEBAR_TOPICS
app = Flask(__name__)

# machine learning
# Video data that will be passed to the template
@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/python", methods=["GET"])
def python():
    # Get selected topic from URL parameter, default to first topic
    selected_topic = request.args.get('topic', SIDEBAR_TOPICS[0])
    page = request.args.get('page', 1, type=int)
    per_page = 5  # Number of videos per page
    
    # Get videos for the selected topic
    topic_videos = PY_VIDEO_DATA.get(selected_topic, [])
    
    # Calculate pagination for selected topic
    total_videos = len(topic_videos)
    total_pages = math.ceil(total_videos / per_page) if total_videos > 0 else 1
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    
    # Get videos for current page of selected topic
    videos = topic_videos[start_index:end_index]
    
    # Create sidebar topics with status indicators
    sidebar_topics_with_status = []
    for topic in SIDEBAR_TOPICS:
        topic_data = {
            'name': topic,
            'video_count': len(PY_VIDEO_DATA.get(topic, [])),
            'is_active': topic == selected_topic,
            'url_param': topic.replace(' ', '%20')  # URL encode spaces
        }
        sidebar_topics_with_status.append(topic_data)
    
    # Pagination info
    pagination = {
        'current_page': page,
        'total_pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages,
        'prev_page': page - 1 if page > 1 else None,
        'next_page': page + 1 if page < total_pages else None,
        'total_videos': total_videos
    }
    
    return render_template('python.html', 
                           videos=videos, 
                           sidebar_topics=sidebar_topics_with_status,
                           pagination=pagination,
                           selected_topic=selected_topic)

# AJAX route for loading more videos within a topic
@app.route("/load_more_videos", methods=["GET"])
def load_more_videos():
    selected_topic = request.args.get('topic', SIDEBAR_TOPICS[0])
    page = request.args.get('page', 1, type=int)
    per_page = 5
    
    topic_videos = PY_VIDEO_DATA.get(selected_topic, [])
    total_videos = len(topic_videos)
    total_pages = math.ceil(total_videos / per_page) if total_videos > 0 else 1
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    
    videos = topic_videos[start_index:end_index]
    
    pagination = {
        'current_page': page,
        'total_pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages,
        'prev_page': page - 1 if page > 1 else None,
        'next_page': page + 1 if page < total_pages else None,
        'total_videos': total_videos
    }
    
    return jsonify({
        'videos': videos,
        'pagination': pagination
    })


# Updated ML route to handle topic-based filtering
@app.route("/machinlearning", methods=['GET'])
def mlcourse():
    # Get selected topic from query parameter, default to first topic
    selected_topic = request.args.get('topic', ML_SIDEBAR_TOPICS[0])
    page = request.args.get('page', 1, type=int)
    per_page = 5  # Videos per page
    
    # Get videos for the selected topic
    topic_videos = ML_VIDEO_DATA.get(selected_topic, [])
    total_videos = len(topic_videos)
    total_pages = math.ceil(total_videos / per_page) if total_videos > 0 else 1
    
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    videos = topic_videos[start_index:end_index]
    
    # Create sidebar topics with status indicators
    sidebar_topics_with_status = []
    for topic in ML_SIDEBAR_TOPICS:
        topic_data = {
            'name': topic,
            'video_count': len(ML_VIDEO_DATA.get(topic, [])),
            'is_active': topic == selected_topic,
            'url_param': topic.replace(' ', '%20')  # URL encode spaces
        }
        sidebar_topics_with_status.append(topic_data)
    
    pagination = {
        'current_page': page,
        'total_pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages,
        'prev_page': page - 1 if page > 1 else None,
        'next_page': page + 1 if page < total_pages else None,
        'total_videos': total_videos
    }
    
    return render_template('machinlearning.html',
                           videos=videos,
                           sidebar_topics=sidebar_topics_with_status,
                           selected_topic=selected_topic,
                           pagination=pagination)

# Updated AJAX route for topic-based loading
@app.route('/load_more_ml_videos')
def load_more_ml_videos():
    selected_topic = request.args.get('topic', ML_SIDEBAR_TOPICS[0])
    page = request.args.get('page', 1, type=int)
    per_page = 5

    # Get videos for the selected topic
    topic_videos = ML_VIDEO_DATA.get(selected_topic, [])
    total_videos = len(topic_videos)
    total_pages = math.ceil(total_videos / per_page) if total_videos > 0 else 1
    
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    videos = topic_videos[start_index:end_index]

    pagination = {
        'current_page': page,
        'total_pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages,
        'prev_page': page - 1 if page > 1 else None,
        'next_page': page + 1 if page < total_pages else None,
        'total_videos': total_videos
    }

    return jsonify({
        'videos': videos,
        'pagination': pagination
    })

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
            'profileUrl': "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgOaSSjkAwM3adr-2VYhVKuv1sgRJ9Z4T4Ew&s",
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
