# importing app to route different web directories
from app import app
from .models import Projects, Feedback, MiniApps
from flask import request

# if url = localhost:5000/ call this function and return this
@app.route('/')
def index():
    return "Home page"

@app.route('/add-project', methods=["GET"])
def addProject():
    
    title = "Pokemon Battle X"
    display_picture_url = "https://i.imgur.com/JVZi5Nr.png"
    title_img_url = "https://i.imgur.com/60THHlZ.png"
    description = "This App allows users to catch up to 5 pokemon and battle them against other users"
    text1 = "I was tasked with creating this App during my Coding Bootcamp. I used Flask for the Backend, HTML and Jinja for the Frontend and PostgreSQL to organize the databases. User authentication, api calls, conditional rendering on a webpage, database structuring and lots of backend processing are some of the major things I learned and practiced while doing this project."
    text2 = "This App allows users to search for pokemon using the pokedex functionality which also displays the pokemon stats. Users can catch and release pokemon (up to 5 can be caught), look over their pokemon on the 'My Team' page and find other users to battle. These battles update your win stats"
    more_imgs_urls = "https://i.imgur.com/x58F4yh.png*https://i.imgur.com/H1w3kaT.png*https://i.imgur.com/8pUi2Ue.png*https://i.imgur.com/cGX5imp.png*https://i.imgur.com/Qf3kZoO.png*https://i.imgur.com/KtqKI1z.png"
    technologies = "HTML, CSS, Python, Jinja, Flask, PostgreSQL"
    github_link = "https://github.com/davidekunno93/Flask_pokedex.git"
    website_link = "Coming soon..."

    project = Projects(title, display_picture_url, title_img_url, description, text1, text2, more_imgs_urls, technologies, github_link, website_link)

    # project.save_to_db()
    # print("project added")

    return "All done Master Wayne"


@app.route('/add-mini-app', methods=["GET"])
def addMiniApp():
    
    title = "TimeZone App"
    display_picture_url = "https://i.imgur.com/zHV6kqG.png"
    title_img_url = "https://i.imgur.com/iojAoTJ.png"
    description = "Use this app to search the time of any city in the world!"
    text = "I made this App to practice skills I had already learned like user authentication and API calls. My biggest goal was to make the app responsive and have a short turn around time for creating the app from start to finish. The objective was to make myself more efficient and keep myself sharp. Flask was used for the Backend, React was used for the Frontend."
    more_imgs_urls = "https://i.imgur.com/8kqEhsV.png*https://i.imgur.com/GrssIMh.png*https://i.imgur.com/OheG8AI.png*https://i.imgur.com/dl9Wtg0.png*https://i.imgur.com/di3FXvN.png*https://i.imgur.com/YAm2ivH.png"
    technologies = "HTML, CSS, Python, React JS, Flask, PostgreSQL"
    github_link = "https://github.com/davidekunno93/Timezone_App_Frontend.git"
    website_link = "Coming soon..."

    mini_app = MiniApps(title, display_picture_url, title_img_url, description, text, more_imgs_urls, technologies, github_link, website_link)

    # mini_app.save_to_db()
    # print("mini-app added")

    return "Coast is clear"

@app.route('/update-more-imgs', methods=["GET"])
def update_more_img_urls():

    project = Projects.query.filter_by(title="Pokemon Battle X").first()
    print(project)
    # project.update_more_imgs("https://i.imgur.com/x58F4yh.png*https://i.imgur.com/H1w3kaT.png*https://i.imgur.com/8pUi2Ue.png*https://i.imgur.com/cGX5imp.png*https://i.imgur.com/Qf3kZoO.png*https://i.imgur.com/KtqKI1z.png")

    # print("images updated")
    return "Complete Sir"

@app.route('/submit-feedback', methods=["POST"])
def submit_feedback():

    data = request.get_json()
    print(data)

    suggestion = data["suggestion"]
    extra_feedback = data["extraFeedback"]

    feedback = Feedback(suggestion, extra_feedback)
    feedback.save_to_db()
    print("feedback saved")

    return {
        "data" : "submission received"
    }