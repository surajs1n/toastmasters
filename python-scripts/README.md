The `python-scripts` package contains the following scripts.

- *meeting_feedback.py*: It pulls out all the good and improvement points of the meeting from the second voting link.
- *prepared_speakers_feedback.py*: It fetches and organizes the feedback of all the speakers. This script also fetched the details of the guest who joined in the meeting.


Pre-requisites before you run the script
---

- Make sure *python 3* _(not to be confused with python 2)_ is installed on your laptop: https://www.python.org/downloads/
- You have the access to download voting results from both the links: http://bit.ly/hsrtm-v1, http://bit.ly/hsrtm-v2
- Important one: Apart from two scripts and README.md files, no other files or folders should be present inside `python-scripts` folder. In case there are any, please delete those.

---

*How to fetch meeting feedback?*
-----

- Go to http://bit.ly/hsrtm-v2
- Click on a pencil icon present on the bottom right of the page. (You need admin access to the page)
- Click on the `Responses` tab.
- Click on the `:` icon present on the top right of the page, and click on `Download responses (.csv)`.
- Once the file is downloaded, extract and place it under `python-scripts` folder containing both of these scripts.
- For Linux/macOS open the terminal on the `python-scripts` folder, and an open command prompt on windows on the `python-scripts` folder. You can follow this video for further help: https://youtu.be/6G_y0L8VhSM
- Run command: `python3 meeting_feedback.py HSR\ Toastmasters\ -\ Roles.csv > meeting_feedback.txt`. This command will create a new text file:`meeting_feedback.txt` containing the details.
- Open file: `meeting_feedback.txt` copy and paste the content on the group.
- Delete both the files from the folder: `meeting_feedback.txt` and `HSR Toastmasters - Roles.csv`

---

*How to fetch prepared speaker's feedback and meeting details?*
----

- Go to http://bit.ly/hsrtm-v1
- Click on a pencil icon present on the bottom right of the page. (You need admin access to the page)
- Click on the `Responses` tab.
- Click on the `:` icon present on the top right of the page, and click on `Download responses (.csv)`.
- Once the file is downloaded, extract and place it under `python-scripts` folder containing both of these scripts.
- For Linux/macOS open the terminal on the `python-scripts` folder, and an open command prompt on windows on the `python-scripts` folder. You can follow this video for further help: https://youtu.be/6G_y0L8VhSM
- Run command: ` python3 prepared_speakers_feeback.py HSR\ Toastmasters\ -\ Speakers.csv 4 > prepared_speakers_feedback.txt`
- Open file: `prepared_speakers_feedback.txt` copy and share the individual feedback with the speakers.
- Delete both the files from the folder: `prepared_speakers_feedback.txt`



 
