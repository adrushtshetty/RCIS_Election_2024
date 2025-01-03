from flask import Flask, request, jsonify, render_template, url_for, redirect
import webbrowser
import os
from csv import writer
from werkzeug.utils import secure_filename

import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = '_internal/static/img/team'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/thank')
def thank():
    return render_template("thankyouPage.html")

@app.route('/candidates')
def candidates():
    df = pd.read_csv(r'_internal/static/res.csv')
    no_of_votes=len(list(df['Name']))

    return render_template("candidates.html", no_vot='{}'.format(no_of_votes))

@app.route('/documentation_index')
def documentation_index():
    return render_template("dashboard.html")


@app.route('/documentation')
def documentation():
    return render_template("docs-page.html")


@app.route('/clearCandidates')
def clearCand_UI():
    return render_template("clearCand.html")


@app.route('/clearCandidates', methods=["POST"])
def clearCand():
    filename = '_internal/templates/candidates.html'
    start_keyword = '<!--            SchoolCaptain-->'
    end_keyword = '<!--EndOfSchoolCaptain            -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--Ballot            -->'
    end_keyword = '<!--EndOfBallot          -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--DeputyHeadBoy-->'
    end_keyword = '<!--EndOfDeputyHeadBoy-->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--BallotDHB-->'
    end_keyword = '<!--EndOfBallotDHB          -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--            Vice Captain-->'
    end_keyword = '<!--EndOfViceCaptin            -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--          ballot2-->'
    end_keyword = '<!--EndOfBallot2          -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--DeputyHeadGirl-->'
    end_keyword = '<!--EndOfDeputyHeadGirl-->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--BallotDeputyHeadGirl-->'
    end_keyword = '<!--EndBallotDeputyHeadGirl-->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--            SportCaptain-->'
    end_keyword = '<!--EndOfSportsCaptin            -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--          BALLOT3-->'
    end_keyword = '<!--EndOfBallot3          -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = '_internal/templates/admin.html'
    start_keyword = '<!--SchoolCaptain          -->'
    end_keyword = '<!--EndOfSchoolCaptain          -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--DeputyHeadBoyAdmin-->'
    end_keyword = '<!--EndOfDeputyHeadBoyAdmin-->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--          ViceCaptain-->'
    end_keyword = '<!--EndOfViceCAPTIN          -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--DeputyHeadGirlAdmin-->'
    end_keyword = '<!--EndOfDeputyHeadGirlAdmin-->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    start_keyword = '<!--          sportcaptain-->'
    end_keyword = '<!--EndOfBallot3          -->'
    with open(filename, 'r') as file:
        lines = file.readlines()
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_keyword in line:
            start_index = i
        if end_keyword in line:
            end_index = i
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    folder_path = '_internal/static/img/team'
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Error: {e}')

    folder_path = '_internal/static/img/team'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, 'savedir.txt')
    with open(file_path, 'w') as f:
        f.write('This is an text file created so that the directory is present in github.')
    stat = 1

    return render_template("clearCand.html", sata_chk='{}'.format(stat))


@app.route('/HTML_Editor')
def HTML_Editor_UI():
    return render_template("forms-elements.html")

@app.route('/HTML_Editor_DHB')
def HTML_Editor_DHB_UI():
    return render_template("deputyHeadBoy.html")

@app.route('/HTML_Editor_DHG')
def HTML_Editor_DHG_UI():
    return render_template("deputyHeadGirl.html")

@app.route('/HTML_Editor_DHG', methods=["POST"])
def HTML_Editor_DHG():
    name = request.form['CandName']
    dimension = request.form['DIMimg']
    # imgName = request.form['CandIMG']
    achv = request.form['CanAchv']
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path = str('_internal/static/img/team/' + (f.filename))
    strApp = '<div class ="col-lg-3 col-md-6 d-flex align-items-stretch " data-aos="fade-up" data-aos-delay="100"><div class ="member"><div class ="member-img" ><img src = "' + path[9:] + '" class ="img-fluid" alt="" width="' + dimension + '" height="' + dimension + '" ></div><div class ="member-info"><h4>' + name + '</h4 ><span align = "left"> <font size = "3.5%"> Achievements: </font> <p>' + achv + '</p> </span></div></div></div>'
    keyword, new_content = "<!--DeputyHeadGirl-->", strApp
    filename = "_internal/templates/candidates.html"
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/candidates.html"
    rpl_str = '<tr><td><img src = "' + path[9:] + '" class ="img-fluid" alt=""  width="' + dimension + '" height="' + dimension + '"> </td><td style = "font-size: 30px;">' + name + '</td><td><label class ="rad-label"><input type = "radio" class ="rad-input" name="deputyHG" value="' + name + '" required > <div class ="rad-design"> </div><div class ="rad-text"> Select </div></label></td></tr>'
    keyword, new_content = "<!--BallotDeputyHeadGirl-->", rpl_str
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/admin.html"
    keyword, new_content = "<!--DeputyHeadGirlAdmin-->", strApp
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)
    stat = 1
    return render_template("deputyHeadGirl.html", sata_chk='{}'.format(stat))


@app.route('/HTML_Editor_DHB', methods=["POST"])
def HTML_Editor_DHB():
    name = request.form['CandName']
    dimension = request.form['DIMimg']
    # imgName = request.form['CandIMG']
    achv = request.form['CanAchv']
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path = str('_internal/static/img/team/' + (f.filename))
    strApp = '<div class ="col-lg-3 col-md-6 d-flex align-items-stretch " data-aos="fade-up" data-aos-delay="100"><div class ="member"><div class ="member-img" ><img src = "' + path[9:] + '" class ="img-fluid" alt="" width="' + dimension + '" height="' + dimension + '" ></div><div class ="member-info"><h4>' + name + '</h4 ><span align = "left"> <font size = "3.5%"> Achievements: </font> <p>' + achv + '</p> </span></div></div></div>'
    keyword, new_content = "<!--DeputyHeadBoy-->", strApp
    filename = "_internal/templates/candidates.html"
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/candidates.html"
    rpl_str = '<tr><td><img src = "' + path[9:] + '" class ="img-fluid" alt=""  width="' + dimension + '" height="' + dimension + '"> </td><td style = "font-size: 30px;">' + name + '</td><td><label class ="rad-label"><input type = "radio" class ="rad-input" name="deputyHB" value="' + name + '" required > <div class ="rad-design"> </div><div class ="rad-text"> Select </div></label></td></tr>'
    keyword, new_content = "<!--BallotDHB-->", rpl_str
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/admin.html"
    keyword, new_content = "<!--DeputyHeadBoyAdmin-->", strApp
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)
    stat = 1
    return render_template("deputyHeadBoy.html", sata_chk='{}'.format(stat))


@app.route('/HTML_Editor', methods=["POST"])
def HTML_Editor():
    name = request.form['CandName']
    dimension = request.form['DIMimg']
    # imgName = request.form['CandIMG']
    achv = request.form['CanAchv']
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path = str('_internal/static/img/team/' + (f.filename))
    strApp = '<div class ="col-lg-3 col-md-6 d-flex align-items-stretch " data-aos="fade-up" data-aos-delay="100"><div class ="member"><div class ="member-img" ><img src = "' + path[9:] + '" class ="img-fluid" alt="" width="' + dimension + '" height="' + dimension + '" ></div><div class ="member-info"><h4>' + name + '</h4 ><span align = "left"> <font size = "3.5%"> Achievements: </font> <p>' + achv + '</p> </span></div></div></div>'
    keyword, new_content = "<!--            SchoolCaptain-->", strApp
    filename = "_internal/templates/candidates.html"
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/candidates.html"
    rpl_str = '<tr><td><img src = "' + path[9:] + '" class ="img-fluid" alt=""  width="' + dimension + '" height="' + dimension + '"> </td><td style = "font-size: 30px;">' + name + '</td><td><label class ="rad-label"><input type = "radio" class ="rad-input" name="candidate" value="' + name + '" required > <div class ="rad-design"> </div><div class ="rad-text"> Select </div></label></td></tr>'
    keyword, new_content = "<!--Ballot            -->", rpl_str
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/admin.html"
    keyword, new_content = "<!--SchoolCaptain          -->", strApp
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)
    stat = 1
    return render_template("forms-elements.html", sata_chk='{}'.format(stat))


@app.route('/HTML_Editor2')
def HTML_Editor2_UI():
    return render_template("Vice_Captain.html")


@app.route('/HTML_Editor2', methods=["POST"])
def HTML_Editor2():
    name = request.form['CandName']
    dimension = request.form['DIMimg']
    # imgName = request.form['CandIMG']
    achv = request.form['CanAchv']
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path = str('_internal/static/img/team/' + (f.filename))
    strApp = '<div class ="col-lg-3 col-md-6 d-flex align-items-stretch " data-aos="fade-up" data-aos-delay="100"><div class ="member"><div class ="member-img" ><img src = "' + path[9:] + '" class ="img-fluid" alt="" width="' + dimension + '" height="' + dimension + '" ></div><div class ="member-info"><h4>' + name + '</h4 ><span align = "left"> <font size = "3.5%"> Achievements: </font> <p>' + achv + '</p> </span></div></div></div>'
    filename = "_internal/templates/candidates.html"
    keyword, new_content = "<!--            Vice Captain-->", strApp
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/candidates.html"
    rpl_str = '<tr><td><img src = "' + path[9:] + '" class ="img-fluid" alt=""  width="' + dimension + '" height="' + dimension + '"> </td><td style = "font-size: 30px;">' + name + '</td><td><label class ="rad-label"><input type = "radio" class ="rad-input" name="vice_captain" value="' + name + '" required > <div class ="rad-design"> </div><div class ="rad-text"> Select </div></label></td></tr>'
    keyword, new_content = "<!--          ballot2-->", rpl_str
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/admin.html"
    keyword, new_content = "<!--          ViceCaptain-->", strApp
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    stat = 1
    return render_template("Vice_Captain.html", sata_chk='{}'.format(stat))


@app.route('/HTML_Editor3')
def HTML_Editor3_UI():
    return render_template("sportsCaptain.html")


@app.route('/HTML_Editor3', methods=["POST"])
def HTML_Editor3():
    name = request.form['CandName']
    dimension = request.form['DIMimg']
    # imgName = request.form['CandIMG']
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path = str('_internal/static/img/team/' + (f.filename))
    achv = request.form['CanAchv']
    strApp = '<div class ="col-lg-3 col-md-6 d-flex align-items-stretch " data-aos="fade-up" data-aos-delay="100"><div class ="member"><div class ="member-img" ><img src = "' + path[9:] + '" class ="img-fluid" alt="" width="' + dimension + '" height="' + dimension + '" ></div><div class ="member-info"><h4>' + name + '</h4 ><span align = "left"> <font size = "3.5%"> Achievements: </font> <p>' + achv + '</p> </span></div></div></div>'
    filename = "_internal/templates/candidates.html"
    keyword, new_content = "<!--            SportCaptain-->", strApp
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/candidates.html"
    rpl_str = '<tr><td><img src = "' + path[9:] + '" class ="img-fluid" alt=""  width="' + dimension + '" height="' + dimension + '"> </td><td style = "font-size: 30px;">' + name + '</td><td><label class ="rad-label"><input type = "radio" class ="rad-input" name="sports_captain" value="' + name + '" required > <div class ="rad-design"> </div><div class ="rad-text"> Select </div></label></td></tr>'
    keyword, new_content = "<!--          BALLOT3-->", rpl_str
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)

    filename = "_internal/templates/admin.html"
    keyword, new_content = "<!--          sportcaptain-->", strApp
    with open(filename, 'r') as file:
        lines = file.readlines()
    found = True
    for i, line in enumerate(lines):
        if keyword in line:
            found = True
            break
    if found:
        lines.insert(i + 1, '\n' + new_content + '\n' + '\n')
    with open(filename, 'w', newline='\r\n') as file:
        file.writelines(lines)
    stat = 1
    return render_template("sportsCaptain.html", sata_chk='{}'.format(stat))


@app.route('/adminF')
def forgot_cred():
    from email.message import EmailMessage
    import ssl
    import smtplib
    res = []
    df = pd.read_csv(r'_internal/static/mail_list.csv')
    for x in (df.values):
        for y in x:
            res.append(y)
    unique_list = []
    for x in res:
        if x not in unique_list:
            unique_list.append(x)

    file = open("_internal/static/psw.txt", "r")
    content = file.read()
    file.close()
    psw = str(content)
    file = open("_internal/static/usnm.txt", "r")
    content = file.read()
    file.close()
    usnm = str(content)

    email_sender = "electionpeak@gmail.com"
    email_password = "gvsztdjgenggeiur"
    email_receiver = unique_list
    subject = " Login Credentials for Your Account on Election Peak"
    body = """
                   Dear Admin,

                    We hope this message finds you well. We are reaching out to provide you with the login credentials for your account on our platform.

                    Please use the following details to access your account:

                    Username: {usnm_}
                    Password: {psw_}

                    We kindly advise you to keep your login credentials safe and confidential to ensure the security of your account.

                    If you have any questions or concerns, please do not hesitate to contact our dev at adrushtshetty@gmail.com for assistance.

                    Thank you for using our platform, and we look forward to serving you in the future.

                    Best regards,
                    Election Peak Team

                    """.format(usnm_=usnm, psw_=psw)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return render_template("newloginF.html")


@app.route('/adminF', methods=['GET', 'POST'])
def login1():
    error = None
    file = open("_internal/static/psw.txt", "r")
    content = file.read()
    file.close()
    psw = str(content)
    file = open("_internal/static/usnm.txt", "r")
    content = file.read()
    file.close()
    usnm = str(content)
    if request.method == 'POST':
        if request.form['username'] != usnm or request.form['password'] != psw:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('documentation_index'))
    return render_template('newlogin.html', error=error)


@app.route('/admin', methods=['GET', 'POST'])
def login():
    error = None
    file = open("_internal/static/psw.txt", "r")
    content = file.read()
    file.close()
    psw = str(content)
    file = open("_internal/static/usnm.txt", "r")
    content = file.read()
    file.close()
    usnm = str(content)
    if request.method == 'POST':
        if request.form['username'] != usnm or request.form['password'] != psw:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('documentation_index'))
    return render_template('newlogin.html', error=error)

def sortD(student_votes):
    sortedD = dict(sorted(student_votes.items(), key=lambda item: item[1], reverse=True))
    return sortedD

@app.route('/admin_result')
def admin():
    df = pd.read_csv(r'_internal/static/res.csv')
    unq = list(df['Name'].unique())
    dict1 = {}
    for x in unq:
        cnt = 0
        for rows, sr in df.iterrows():
            if sr[0] == x:
                cnt += 1
            dict1[x] = cnt

    dict1 = sortD(dict1)
    dict_HB=dict1.copy()

    resn = []
    resv = []
    for k, v in dict1.items():
        resn.append(k)
        resv.append(v)
    # m = max(resv)
    # cnt = 0
    # newD = {}
    # inds = []
    # for i in resv:
    #     if i == m:
    #         cnt += 1
    #         inds.append(i)
    # #print(inds, cnt)
    #
    # if cnt > 1:
    #     for i in inds:
    #         newD[resn[i]] = m
    # else:
    #     newD[resn[resv.index(inds[0])]] = m
    #print(newD)
    inds = []
    for i in range(0, len(resv)):
        if resv[i] == max(resv):
            inds.append(i)
    dictWHB = {}
    for i in inds:
        dictWHB[resn[i]] = resv[i]
    # print(dictW)
    # print(len(dictW))

    df = pd.read_csv(r'_internal/static/trial.csv')
    unq = list(df['Name'].unique())
    dict1 = {}
    for x in unq:
        cnt = 0
        for rows, sr in df.iterrows():
            if sr[0] == x:
                cnt += 1
            dict1[x] = cnt

    dict1 = sortD(dict1)
    dict_DHB = dict1.copy()

    resn = []
    resv = []
    for k, v in dict1.items():
        resn.append(k)
        resv.append(v)
    inds = []
    for i in range(0, len(resv)):
        if resv[i] == max(resv):
            inds.append(i)
    dictWDHB = {}
    for i in inds:
        dictWDHB[resn[i]] = resv[i]
    # flag = 0
    # flag = len(set(resv)) == len(resv)
    # if (flag):
    #     n = 1
    #     s = ""
    #     msg = str((resn[resv.index(max(resv))], "with total votes of ", max(resv)))
    # else:
    #     var = resv
    #     unique_entries = set(var)
    #     indices = {value: [i for i, v in enumerate(var) if v == value] for value in unique_entries}
    #     indices
    #     indk = []
    #     indv = []
    #     fv = []
    #     for k, v in indices.items():
    #         indk.append(k)
    #         indv.append(v)
    #     for x in indices[(max(indk))]:
    #         fv.append("Name: " + str(resn[x]) + " with a total votes of: " + str(resv[x]) + " |")
    #     n = (len(fv))
    #     s = "s"
    #     msg = ""
    #     for x in fv:
    #         msg += x
    # rab = ""
    # for k, v in dict1.items():
    #     rab += str((k + " with total votes of:", v, "|||"))

    df1 = pd.read_csv(r'_internal/static/resViceCaptain.csv')
    unq = list(df1['Name'].unique())
    dict1 = {}
    for x in unq:
        cnt = 0
        for rows, sr in df1.iterrows():
            if sr[0] == x:
                cnt += 1
        dict1[x] = cnt

    dict1 = sortD(dict1)
    dict_HG=dict1.copy()
    resn = []
    resv = []
    for k, v in dict1.items():
        resn.append(k)
        resv.append(v)
    inds = []
    for i in range(0, len(resv)):
        if resv[i] == max(resv):
            inds.append(i)
    dictWHG = {}
    for i in inds:
        dictWHG[resn[i]] = resv[i]




    df = pd.read_csv(r'_internal/static/DeputyHeadGirl.csv')
    unq = list(df['Name'].unique())
    dict1 = {}
    for x in unq:
        cnt = 0
        for rows, sr in df.iterrows():
            if sr[0] == x:
                cnt += 1
        dict1[x] = cnt

    dict1 = sortD(dict1)
    dict_DHG = dict1.copy()
    resn = []
    resv = []
    for k, v in dict1.items():
        resn.append(k)
        resv.append(v)
    inds = []
    for i in range(0, len(resv)):
        if resv[i] == max(resv):
            inds.append(i)
    dictWDHG = {}
    for i in inds:
        dictWDHG[resn[i]] = resv[i]

    df2 = pd.read_csv(r'_internal/static/resSportsCaptain.csv')
    unq = list(df2['Name'].unique())
    dict1 = {}
    for x in unq:
        cnt = 0
        for rows, sr in df2.iterrows():
            if sr[0] == x:
                cnt += 1
        dict1[x] = cnt

    dict1 = sortD(dict1)
    dict_SPC = dict1.copy()
    resn = []
    resv = []
    for k, v in dict1.items():
        resn.append(k)
        resv.append(v)
    inds = []
    for i in range(0, len(resv)):
        if resv[i] == max(resv):
            inds.append(i)
    dictWSPC = {}
    for i in inds:
        dictWSPC[resn[i]] = resv[i]



    return render_template("admin.html", dict_HBS=dict_HB,newDS=dictWHB,HBWS=len(dictWHB),newDHBS=dictWDHB,DHBWS=len(dictWDHB),dict_DHBS=dict_DHB,dict_HGS=dict_HG,newHGS=dictWHG,HGWS=len(dictWHG),

                           dict_DHGS=dict_DHG,newDHGS=dictWDHG,DHGWS=len(dictWDHG),dict_SPCS=dict_SPC,newSPCS=dictWSPC,SPCWS=len(dictWSPC))


@app.route('/candidates', methods=['POST'])
def add():
    vote_sc = str(request.form['deputyHG'])
    r = [vote_sc]
    with open("_internal/static/DeputyHeadGirl.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(r)
        f_object.close()
    vote_sc = str(request.form['deputyHB'])
    r = [vote_sc]
    with open("_internal/static/trial.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(r)
        f_object.close()
    vote_sc = str(request.form['candidate'])
    r = [vote_sc]
    with open("_internal/static/res.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(r)
        f_object.close()
    vote_vc = str(request.form['vice_captain'])
    r = [vote_vc]
    with open("_internal/static/resViceCaptain.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(r)
        f_object.close()
    vote_spc = str(request.form['sports_captain'])
    r = [vote_spc]
    with open("_internal/static/resSportsCaptain.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(r)
        f_object.close()
    return redirect(url_for('thank'))


@app.route('/admin_result', methods=['POST'])
def clear():
    val = str(request.form['clear'])
    if val == "1":
        r = ['Name']
        with open("_internal/static/res.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()
        with open("_internal/static/resViceCaptain.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()
        with open("_internal/static/resSportsCaptain.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()
    return render_template("index.html")


@app.route('/utils')
def utils_UI():
    return render_template("utils.html")


@app.route('/utils2')
def utils2_UI():
    return render_template("utils2.html")


@app.route('/mailID')
def mail_UI():
    res = []
    df = pd.read_csv(r'_internal/static/mail_list.csv')
    for x in (df.values):
        for y in x:
            res.append(y)
    unique_list = []
    for x in res:
        if x not in unique_list:
            unique_list.append(x)
    return render_template("mailID.html", resource='{}'.format(unique_list))


@app.route('/mailID', methods=['POST'])
def mail_add():
    var = request.form['delete']
    if var == "1":
        with open("_internal/static/mail_list.csv", 'w') as f_object:
            r = ["MAIL_ID's"]
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()

    mailID = request.form['mailADD']
    with open("_internal/static/mail_list.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([mailID])
        f_object.close()
    stat1 = 1
    res = []
    df = pd.read_csv(r'_internal/static/mail_list.csv')
    for x in (df.values):
        for y in x:
            res.append(y)
    unique_list = []
    for x in res:
        if x not in unique_list:
            unique_list.append(x)

    return render_template("mailID.html", sata_chk='{}'.format(stat1), resource='{}'.format(unique_list))


@app.route('/cred')
def cred():
    file = open("_internal/static/usnm.txt", "r")
    usnm_c = file.read()
    file.close()
    file = open("_internal/static/psw.txt", "r")
    psw_c = file.read()

    file.close()
    return render_template('cred.html', usnm_d='{}'.format(usnm_c), psw_d='{}'.format(psw_c))


@app.route('/utils2', methods=['POST'])
def change_psw():
    USNM = request.form['usnm']
    file = open("_internal/static/usnm.txt", "w")
    file.write(USNM)
    file.close()
    PSW = request.form['psw']
    file = open("_internal/static/psw.txt", "w")
    file.write(PSW)
    file.close()
    stat1 = 1
    # forgot_request = request.form['forgor']
    # if forgot_request==1:
    #     print(forgot_request)
    #     stat1=0
    #     print(stat1)
    #     file = open("_internal/static/assets/usnm.txt", "r")
    #     usnm_c = file.read()
    #     file.close()
    #     file = open("_internal/static/assets/psw.txt", "r")
    #     psw_c = file.read()
    #     file.close()
    #     return render_template('utils2.html', sata_chk='{}'.format(stat1),usnm_d='{}'.format(usnm_c),psw_d='{}'.format(psw_c))
    return render_template('utils2.html', sata_chk='{}'.format(stat1))


# @app.route('/utils2',methods=['POST'])
# def view_cred():
#     forgot_request = request.form['forgor']
#     stat1=0
#     file = open("_internal/static/assets/usnm.txt", "r")
#     usnm_c = file.read()
#     file.close()
#     file = open("_internal/static/assets/psw.txt", "r")
#     psw_c = file.read()
#     file.close()
#     return render_template('utils2.html', sata_chk='{}'.format(stat1),usnm_d='{}'.format(usnm_c),psw_d='{}'.format(psw_c))


@app.route('/utils', methods=['POST'])
def clear2():
    val = str(request.form['clear'])
    if val == "1":
        r = ['Name']
        with open("_internal/static/res.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()
        with open("_internal/static/resViceCaptain.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()
        with open("_internal/static/resSportsCaptain.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()
        with open("_internal/static/trial.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()
        with open("_internal/static/DeputyHeadGirl.csv", 'w') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(r)
            f_object.close()

    stat1 = 1
    return render_template('utils.html', sata_chk='{}'.format(stat1))


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == '__main__':
    # Individual System Setting
    app.run(debug=True)

    # Server System Setting
    # open_browser()
    # app.run(host='0.0.0.0',debug=True)

# gvsztdjgenggeiur