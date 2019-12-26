Problem Statement:
Read the Apache Log File, Extract all the Valid IP Addresses and get the count of it. Generate the Email for the result.


Steps:

1. Take email address from the user for sending the mail using ArgParse Module.
2. Create Logging Configuration object for saving the Log Events.
3. Parse the Configuration file for fetching gmail_user and gmail_password
4. Use regular Expression, to find all the valid ip adresses and return the result in a dictionary.
5. Created a Function for sending the mail using SMTPLIB Module and displaying the result.



Help File:

(venv) C:\Users\admin\PycharmProjects\ApacheLogParser>python apachelog_parser.py -h
usage: apachelog_parser.py [-h] -e EMAIL_ID [EMAIL_ID ...]

optional arguments:
  -h, --help            show this help message and exit

Required Named arguments:
  -e EMAIL_ID [EMAIL_ID ...], --email EMAIL_ID [EMAIL_ID ...]  



Execution:
(venv) C:\Users\admin\PycharmProjects\ApacheLogParser>python apachelog_parser.py -e ***
26-Dec-19 12:33:18 - IP Count: {'45.242.88.10': 1, '64.242.88.10': 451, '213.181.81.4': 1, '213.54.168.132': 12, '200.160.249.68': 2
, '128.227.88.79': 14, '61.9.4.61': 3, '212.92.37.62': 14, '219.95.17.51': 1, '10.0.0.153': 270, '66.213.206.2': 1, '64.246.94.152':
 1, '195.246.13.119': 12, '195.230.181.122': 1, '207.195.59.160': 20, '80.58.35.111': 1, '200.222.33.33': 1, '203.147.138.233': 13,
'212.21.228.26': 1, '80.58.14.235': 4, '142.27.64.35': 7, '64.246.94.141': 1, '194.151.73.43': 4, '208.247.148.12': 4, '4.37.97.186'
: 1, '12.22.207.235': 1, '195.11.231.210': 1, '80.58.33.42': 3, '145.253.208.9': 7, '61.165.64.6': 4, '67.131.107.5': 3, '216.139.18
5.45': 1}
26-Dec-19 12:33:18 - Message Body         <html>
            <head></head>
            <body>
                <p>Hey ***,<br>
                <br>
                Following is the Log Message Count:<br>                <b>45.242.88.10 -> 1<br></b><b>64.242.88.10 -> 451<br></b><b>
213.181.81.4 -> 1<br></b><b>213.54.168.132 -> 12<br></b><b>200.160.249.68 -> 2<br></b><b>128.227.88.79 -> 14<br></b><b>61.9.4.61 ->
3<br></b><b>212.92.37.62 -> 14<br></b><b>219.95.17.51 -> 1<br></b><b>10.0.0.153 -> 270<br></b><b>66.213.206.2 -> 1<br></b><b>64.246.
94.152 -> 1<br></b><b>195.246.13.119 -> 12<br></b><b>195.230.181.122 -> 1<br></b><b>207.195.59.160 -> 20<br></b><b>80.58.35.111 -> 1
<br></b><b>200.222.33.33 -> 1<br></b><b>203.147.138.233 -> 13<br></b><b>212.21.228.26 -> 1<br></b><b>80.58.14.235 -> 4<br></b><b>142
.27.64.35 -> 7<br></b><b>64.246.94.141 -> 1<br></b><b>194.151.73.43 -> 4<br></b><b>208.247.148.12 -> 4<br></b><b>4.37.97.186 -> 1<br
></b><b>12.22.207.235 -> 1<br></b><b>195.11.231.210 -> 1<br></b><b>80.58.33.42 -> 3<br></b><b>145.253.208.9 -> 7<br></b><b>61.165.64
.6 -> 4<br></b><b>67.131.107.5 -> 3<br></b><b>216.139.185.45 -> 1<br></b>            </p>
            </body>
            </html>

26-Dec-19 12:33:25 - Email Sent!!
